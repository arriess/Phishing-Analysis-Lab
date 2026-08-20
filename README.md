# Phishing Analysis & Incident Response Lab

Hands-on SOC portfolio project focused on **phishing triage, email-header analysis, IOC extraction, URL/domain investigation, threat assessment, MITRE ATT&CK mapping, and incident-response documentation**.

> **Current status:** Lab structure initialized. Investigations remain planned until controlled analysis is completed and validated.

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

## Planned Investigations

| Investigation | Focus | Status |
|---|---|---|
| **001 — Credential Phishing Analysis** | Header review, sender validation, suspicious-link triage, IOC extraction, analyst verdict | 🟡 Planned |
| **002 — Suspicious Link Analysis** | URL structure, redirect context, domain/DNS analysis, risk assessment | 🟡 Planned |
| **003 — Business Email Compromise Scenario** | Display-name spoofing, social-engineering indicators, payment-request triage | 🟡 Planned |

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
│   └── README.md
├── playbooks/
│   └── phishing-response-playbook.md
├── samples/
│   └── README.md
└── screenshots/
    └── README.md
```

## Evidence Standard

Each completed investigation will document:

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
