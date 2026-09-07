# Parsed Artifacts

These JSON files were produced from the committed synthetic `.eml` samples with [`tools/analyze_eml.py`](../tools/analyze_eml.py). They make the header and URL extraction reproducible; they do not convert the synthetic messages into real incident evidence.

Recreate them from the repository root:

```bash
python3 tools/analyze_eml.py samples/001-credential-phishing-simulated.eml
python3 tools/analyze_eml.py samples/003-bec-executive-impersonation-simulated.eml
```

The BEC artifact intentionally records that the sample declares `dkim=pass` in `Authentication-Results` but contains no `DKIM-Signature` header. The declared result is scenario data and cannot be cryptographically verified from the committed file.
