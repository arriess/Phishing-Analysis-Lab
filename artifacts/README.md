# Parsed Artifacts

These JSON files were produced from the committed synthetic samples with [`tools/analyze_eml.py`](../tools/analyze_eml.py) and [`tools/analyze_url_sample.py`](../tools/analyze_url_sample.py). They make the documented header, URL, redirect, and supplied DNS-context extraction reproducible; they do not convert the synthetic scenarios into real incident evidence.

Recreate them from the repository root:

```bash
python3 tools/verify_artifacts.py --write
```

Verify that all three committed artifacts match their source samples:

```bash
python3 tools/verify_artifacts.py --check
```

The BEC artifact intentionally records that the sample declares `dkim=pass` in `Authentication-Results` but contains no `DKIM-Signature` header. The declared result is scenario data and cannot be cryptographically verified from the committed file.
