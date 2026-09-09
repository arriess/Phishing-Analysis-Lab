#!/usr/bin/env python3
"""Extract reviewable headers and URLs from an RFC 5322 email file."""

from __future__ import annotations

import argparse
import json
import re
from email import policy
from email.message import Message
from email.parser import BytesParser
from pathlib import Path


URL_PATTERN = re.compile(r"https?://[^\s<>\"']+")
REVIEW_HEADERS = (
    "From",
    "Reply-To",
    "Return-Path",
    "To",
    "Date",
    "Message-ID",
    "Subject",
)


def extract_text(message: Message) -> str:
    parts: list[str] = []
    for part in message.walk():
        if part.is_multipart():
            continue
        if part.get_content_type() not in {"text/plain", "text/html"}:
            continue
        try:
            content = part.get_content()
        except (LookupError, UnicodeDecodeError):
            payload = part.get_payload(decode=True) or b""
            content = payload.decode("utf-8", errors="replace")
        if isinstance(content, str):
            parts.append(content)
    return "\n".join(parts)


def analyze(path: Path) -> dict[str, object]:
    with path.open("rb") as source:
        message = BytesParser(policy=policy.default).parse(source)

    authentication_results = [str(value) for value in message.get_all("Authentication-Results", [])]
    dkim_signature_present = bool(message.get_all("DKIM-Signature", []))
    warnings: list[str] = []

    if any("dkim=pass" in value.lower() for value in authentication_results) and not dkim_signature_present:
        warnings.append(
            "Authentication-Results declares dkim=pass, but this sample contains no "
            "DKIM-Signature header; the result cannot be independently verified from the file."
        )

    return {
        "source_file": path.name,
        "headers": {header: str(message.get(header, "")) for header in REVIEW_HEADERS},
        "authentication_results": authentication_results,
        "dkim_signature_present": dkim_signature_present,
        "urls": sorted(set(URL_PATTERN.findall(extract_text(message)))),
        "warnings": warnings,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("eml_file", type=Path, help="Path to an .eml file")
    args = parser.parse_args()
    print(json.dumps(analyze(args.eml_file), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
