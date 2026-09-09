# Phishing Analysis & Incident Response Lab

Three controlled phishing and Business Email Compromise (BEC) exercises built from deliberately constructed training samples. The repository demonstrates a documented triage method, IOC extraction, severity and confidence decisions, MITRE ATT&CK mapping, and response recommendations.

> **Evidence boundary:** These are synthetic scenario analyses, not production incidents. The committed `.eml` files, text sample, parsed JSON, and case reports are reviewable; the SVG files are visual summaries rather than independent evidence of tool use.

## Start Here

1. [Credential-phishing investigation](investigations/001-credential-phishing-analysis.md) and its [parsed email artifact](artifacts/001-credential-phishing-parsed.json).
2. [Suspicious-link investigation](investigations/002-suspicious-link-analysis.md) and its [parsed URL artifact](artifacts/002-suspicious-link-parsed.json).
3. [BEC investigation](investigations/003-business-email-compromise.md) and its [parsed email artifact](artifacts/003-bec-parsed.json).
4. [Phishing response playbook](playbooks/phishing-response-playbook.md).

## Case Coverage

| Case | Analyst focus | Final lab classification | Committed material |
|---|---|---|---|
| 001 — Credential phishing | Sender/Reply-To/Return-Path comparison, declared authentication results, URL extraction, urgency and brand impersonation | Credential phishing simulation, Medium | [Report](investigations/001-credential-phishing-analysis.md) · [Sample](samples/001-credential-phishing-simulated.eml) · [Parsed JSON](artifacts/001-credential-phishing-parsed.json) · [IOCs](iocs/001-credential-phishing-iocs.md) |
| 002 — Suspicious link | URL decomposition, encoded redirect, authentication-themed hostnames, and provided TEST-NET context | Credential-phishing link simulation, Medium | [Report](investigations/002-suspicious-link-analysis.md) · [Sample](samples/002-suspicious-link-simulated.txt) · [Parsed JSON](artifacts/002-suspicious-link-parsed.json) · [IOCs](iocs/002-suspicious-link-iocs.md) |
| 003 — BEC | Executive impersonation, Reply-To mismatch, payment urgency, verification-process bypass, and financial impact | BEC / executive-impersonation simulation, High | [Report](investigations/003-business-email-compromise.md) · [Sample](samples/003-bec-executive-impersonation-simulated.eml) · [Parsed JSON](artifacts/003-bec-parsed.json) · [IOCs](iocs/003-bec-executive-impersonation-iocs.md) |

## Reproducible Parsing

### Email samples

[`tools/analyze_eml.py`](tools/analyze_eml.py) uses Python's standard-library email parser to extract review headers, `Authentication-Results`, the presence of a `DKIM-Signature`, and URLs from a committed `.eml` file.

```bash
python3 tools/analyze_eml.py samples/001-credential-phishing-simulated.eml
python3 tools/analyze_eml.py samples/003-bec-executive-impersonation-simulated.eml
```

### Suspicious-link sample

[`tools/analyze_url_sample.py`](tools/analyze_url_sample.py) parses the initial and simulated redirect URLs, decodes query parameters, extracts the supplied DNS context, and confirms that the scenario uses `.example` hostnames and TEST-NET addresses.

```bash
python3 tools/analyze_url_sample.py samples/002-suspicious-link-simulated.txt
```

The checked-in outputs for all three cases are in [`artifacts/`](artifacts/README.md). Verify that every artifact still matches its source sample with:

```bash
python3 tools/verify_artifacts.py --check
```

GitHub Actions runs the same verification on every push and pull request.

### Authentication limitation in Case 003

The BEC sample deliberately declares `spf=pass`, `dkim=pass`, and `dmarc=pass` in its synthetic `Authentication-Results` header to support the scenario lesson that email authentication does not prove the claimed human identity. However, the file contains no `DKIM-Signature` header and uses reserved domains, so the declared DKIM result cannot be cryptographically verified from the sample. The parser exposes this limitation instead of presenting the value as independently validated.

## Analyst Workflow

```text
Preserve the message or training sample
        ↓
Compare sender identities and reply paths
        ↓
Review declared authentication results
        ↓
Extract and safely analyze URLs and indicators
        ↓
Assess user interaction and business impact
        ↓
Record verdict, severity, confidence, and false positives
        ↓
Recommend containment, recovery, and escalation
```

## Evidence and Scope Limitations

- All domains are reserved `.example` names and all published IP addresses use TEST-NET ranges.
- Case 002 contains a constructed redirect and provided DNS context; it is not evidence of a live redirect or DNS lookup.
- The SVG case cards summarize the written analyses. They are not screenshots from an email gateway, sandbox, SIEM, DNS tool, or threat-intelligence platform.
- No real sender reputation, domain age, passive DNS, sandbox verdict, mail-gateway telemetry, or user-click telemetry is available in these scenarios.
- No credentials were entered or collected, no malicious payload was executed, and no live phishing infrastructure was contacted.

## Repository Map

```text
Phishing-Analysis-Lab/
├── README.md
├── tools/
│   ├── analyze_eml.py
│   ├── analyze_url_sample.py
│   └── verify_artifacts.py
├── artifacts/
│   ├── README.md
│   ├── 001-credential-phishing-parsed.json
│   ├── 002-suspicious-link-parsed.json
│   └── 003-bec-parsed.json
├── investigations/
│   ├── 001-credential-phishing-analysis.md
│   ├── 002-suspicious-link-analysis.md
│   └── 003-business-email-compromise.md
├── iocs/
│   ├── 001-credential-phishing-iocs.md
│   ├── 002-suspicious-link-iocs.md
│   └── 003-bec-executive-impersonation-iocs.md
├── playbooks/
│   └── phishing-response-playbook.md
├── samples/
│   ├── 001-credential-phishing-simulated.eml
│   ├── 002-suspicious-link-simulated.txt
│   └── 003-bec-executive-impersonation-simulated.eml
└── screenshots/
    ├── 001-credential-phishing-evidence.svg
    ├── 002-suspicious-link-evidence.svg
    └── 003-bec-evidence.svg
```

## Privacy and Ethics

The scenarios use fictitious identities, reserved domains, documentation-only IP addresses, and non-functional payment details. No real company, executive, employee, bank account, credential, or third-party system is targeted.

## Related Project

- [SOC Analyst Lab — Windows, Splunk, Microsoft Sentinel, KQL, and Wireshark](https://github.com/arriess/SOC-Analyst-Lab)

## Author

**Hicham Essafi**  
Cybersecurity | Junior SOC Analyst / Security Operations

- [GitHub](https://github.com/arriess)
- [LinkedIn](https://www.linkedin.com/in/hicham-essafi/)
