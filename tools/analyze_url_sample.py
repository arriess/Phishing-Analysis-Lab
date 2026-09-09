#!/usr/bin/env python3
"""Parse the repository's synthetic suspicious-link training sample."""

from __future__ import annotations

import argparse
import ipaddress
import json
import re
from pathlib import Path
from urllib.parse import parse_qs, urlparse


DOCUMENTATION_NETWORKS = {
    "TEST-NET-1": ipaddress.ip_network("192.0.2.0/24"),
    "TEST-NET-2": ipaddress.ip_network("198.51.100.0/24"),
    "TEST-NET-3": ipaddress.ip_network("203.0.113.0/24"),
}


def value_after_label(text: str, label: str) -> str:
    match = re.search(rf"^{re.escape(label)}:\s*\n([^\n]+)$", text, flags=re.MULTILINE)
    if not match:
        raise ValueError(f"missing sample field: {label}")
    return match.group(1).strip()


def parse_url(value: str) -> dict[str, object]:
    parsed = urlparse(value)
    return {
        "url": value,
        "scheme": parsed.scheme,
        "hostname": parsed.hostname or "",
        "path": parsed.path,
        "query_parameters": {
            key: values if len(values) > 1 else values[0]
            for key, values in sorted(parse_qs(parsed.query, keep_blank_values=True).items())
        },
    }


def documentation_range(address: str) -> str | None:
    ip = ipaddress.ip_address(address)
    for name, network in DOCUMENTATION_NETWORKS.items():
        if ip in network:
            return name
    return None


def analyze(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    initial = parse_url(value_after_label(text, "Initial URL"))
    redirect = parse_url(value_after_label(text, "Simulated redirect destination"))

    dns_entries = []
    for hostname, address in re.findall(
        r"^([A-Za-z0-9.-]+)\s+->\s+([0-9.]+)$", text, flags=re.MULTILINE
    ):
        dns_entries.append(
            {
                "hostname": hostname,
                "address": address,
                "documentation_range": documentation_range(address),
            }
        )

    initial_redirect = initial["query_parameters"].get("redirect")
    warnings: list[str] = []
    if initial_redirect != redirect["url"].split("?", 1)[0]:
        warnings.append(
            "The initial redirect parameter and the supplied simulated destination base URL differ."
        )
    if not all(str(item["hostname"]).endswith(".example") for item in dns_entries):
        warnings.append("At least one supplied hostname is outside the reserved .example namespace.")
    if not all(item["documentation_range"] for item in dns_entries):
        warnings.append("At least one supplied address is outside TEST-NET documentation ranges.")

    return {
        "source_file": path.name,
        "initial_url": initial,
        "simulated_redirect_destination": redirect,
        "provided_dns_context": dns_entries,
        "safety_checks": {
            "all_dns_hostnames_use_example": all(
                str(item["hostname"]).endswith(".example") for item in dns_entries
            ),
            "all_addresses_use_test_net": all(
                bool(item["documentation_range"]) for item in dns_entries
            ),
        },
        "warnings": warnings,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sample_file", type=Path, help="Path to the simulated URL text sample")
    args = parser.parse_args()
    print(json.dumps(analyze(args.sample_file), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

