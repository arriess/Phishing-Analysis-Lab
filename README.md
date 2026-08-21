# Phishing Analysis & Incident Response Lab

Hands-on SOC portfolio project focused on **phishing triage, email-header analysis, IOC extraction, URL/domain investigation, threat assessment, MITRE ATT&CK mapping, and incident-response documentation**.

> **Current status:** Investigations 001 and 002 completed using controlled training simulations. Investigation 003 remains planned.

## Objective

The goal of this project is to demonstrate a repeatable SOC workflow for investigating suspicious emails from initial user report through technical analysis, classification, IOC handling, response recommendations, and sanitized analyst documentation.

## Skills Demonstrated

- Phishing Analysis
- Email Header Analysis
- IOC Analysis
- Incident Response
- Threat Intelligence Fundamentals
- MITRE ATT&CK Mapping
- URL and Domain Analysis
- DNS Analysis
- SOC Triage
- Security Documentation

## Investigations

| Investigation | Focus | Status |
|---|---|---|
| **001 — Credential Phishing Analysis** | Header review, sender validation, suspicious-link triage, IOC extraction, analyst verdict | ✅ Completed |
| **002 — Suspicious Link Analysis** | URL structure, redirect context, domain/DNS analysis, risk assessment | ✅ Completed |
| **003 — Business Email Compromise Scenario** | Display-name spoofing, social-engineering indicators, payment-request triage | 🟡 Planned |

## Investigation 001 Highlights

The first investigation analyzed a deliberately constructed Microsoft 365 credential-phishing simulation. The analyst workflow identified sender/reply-path mismatches, simulated SPF/DMARC failures, missing DKIM, urgency and account-loss language, and a Microsoft-themed verification URL using reserved lab infrastructure.

**Final classification:** Credential Phishing — Simulated / Authorized Lab  
**Severity:** Medium  
**MITRE ATT&CK:** T1566.002 — Phishing: Spearphishing Link

Documentation:

- [`investigations/001-credential-phishing-analysis.md`](investigations/001-credential-phishing-analysis.md)
- [`iocs/001-credential-phishing-iocs.md`](iocs/001-credential-phishing-iocs.md)
- [`samples/001-credential-phishing-simulated.eml`](samples/001-credential-phishing-simulated.eml)

## Investigation 002 Highlights

The second investigation analyzed a deliberately constructed suspicious authentication link with an encoded redirect, a staged Microsoft 365-themed destination, user-specific query parameters, and simulated DNS mappings using documentation-only IP addresses.

**Final classification:** Suspicious / Credential-Phishing Link Simulation  
**Severity:** Medium  
**MITRE ATT&CK:** T1566.002 — Phishing: Spearphishing Link

Documentation:

- [`investigations/002-suspicious-link-analysis.md`](investigations/002-suspicious-link-analysis.md)
- [`iocs/002-suspicious-link-iocs.md`](iocs/002-suspicious-link-iocs.md)
- [`samples/002-suspicious-link-simulated.txt`](samples/002-suspicious-link-simulated.txt)

## End-to-End Analyst Workflow

```text
Reported suspicious email
        ↓
Initial triage
        ↓
Header / sender analysis
        ↓
URL / domain analysis
        ↓
IOC extraction
        ↓
Threat assessment
        ↓
MITRE ATT&CK mapping when relevant
        ↓
Analyst verdict
        ↓
Containment / response recommendations
        ↓
Sanitized portfolio documentation
```

## Repository Structure

```text
Phishing-Analysis-Lab/
├── README.md
├── investigations/
│   ├── 001-credential-phishing-analysis.md
│   ├── 002-suspicious-link-analysis.md
│   └── 003-business-email-compromise.md
├── iocs/
│   ├── README.md
│   ├── 001-credential-phishing-iocs.md
│   └── 002-suspicious-link-iocs.md
├── playbooks/
│   └── phishing-response-playbook.md
├── samples/
│   ├── README.md
│   ├── 001-credential-phishing-simulated.eml
│   └── 002-suspicious-link-simulated.txt
└── screenshots/
    └── README.md
```

## Evidence Standard

Each completed investigation documents:

1. Initial alert or user-report context
2. Email metadata and authentication observations
3. Suspicious indicators and extracted IOCs
4. URL/domain/DNS observations when applicable
5. Analyst reasoning and false-positive considerations
6. MITRE ATT&CK mapping where behavior supports it
7. Final classification and severity
8. Containment and remediation recommendations
9. Sanitized screenshots or evidence when useful

## Ethics & Safety

All exercises in this repository use **simulated, benign, or deliberately constructed training samples**. No real credentials are collected, no malicious payloads are executed, no live phishing infrastructure is operated, and no third-party systems or users are targeted.

Public evidence is sanitized before publication. Real personal email addresses, authentication tokens, account identifiers, private infrastructure details, and unrelated user data are excluded or redacted.

## Related Project

My complementary SIEM and detection-engineering portfolio is available here:

- [SOC Analyst Lab — Splunk, Microsoft Sentinel, Windows Security & Wireshark](https://github.com/arriess/SOC-Analyst-Lab)

## Author

**Hicham Essafi**  
Cybersecurity | Junior SOC Analyst / Security Operations

- GitHub: https://github.com/arriess
- LinkedIn: https://www.linkedin.com/in/hicham-essafi/
