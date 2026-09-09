#!/usr/bin/env python3
"""Regenerate or verify all parsed artifacts against their committed samples."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from analyze_eml import analyze as analyze_eml
from analyze_url_sample import analyze as analyze_url_sample


ROOT = Path(__file__).resolve().parents[1]
CASES = {
    ROOT / "artifacts" / "001-credential-phishing-parsed.json": lambda: analyze_eml(
        ROOT / "samples" / "001-credential-phishing-simulated.eml"
    ),
    ROOT / "artifacts" / "002-suspicious-link-parsed.json": lambda: analyze_url_sample(
        ROOT / "samples" / "002-suspicious-link-simulated.txt"
    ),
    ROOT / "artifacts" / "003-bec-parsed.json": lambda: analyze_eml(
        ROOT / "samples" / "003-bec-executive-impersonation-simulated.eml"
    ),
}


def serialize(value: dict[str, object]) -> str:
    return json.dumps(value, indent=2, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--write", action="store_true", help="regenerate committed artifacts")
    group.add_argument("--check", action="store_true", help="verify committed artifacts")
    args = parser.parse_args()

    stale: list[str] = []
    for artifact, producer in CASES.items():
        generated = serialize(producer())
        if args.write:
            artifact.write_text(generated, encoding="utf-8")
            print(f"wrote {artifact.relative_to(ROOT)}")
        elif not artifact.exists() or artifact.read_text(encoding="utf-8") != generated:
            stale.append(str(artifact.relative_to(ROOT)))
        else:
            print(f"verified {artifact.relative_to(ROOT)}")

    if stale:
        print("missing or stale artifacts: " + ", ".join(stale), file=sys.stderr)
        return 1
    if not args.write:
        print("3/3 synthetic case artifacts match their committed samples")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

