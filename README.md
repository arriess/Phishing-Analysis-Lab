# Phishing Analysis & Incident Response Lab

Hands-on SOC portfolio project focused on **phishing triage, email-header analysis, IOC extraction, URL/domain investigation, threat assessment, MITRE ATT&CK mapping, business email compromise analysis, and incident-response documentation**.

> **Current status:** Core portfolio complete — 3 controlled phishing/BEC investigations documented and validated using simulated training samples.

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
- Business Email Compromise (BEC) Analysis
- Executive Impersonation Triage
- SOC Triage
- Security Documentation

## Investigations

| Investigation | Focus | Status |
|---|---|---|
| **001 — Credential Phishing Analysis** | Header review, sender validation, suspicious-link triage, IOC extraction, analyst verdict | ✅ Completed |
| **002 — Suspicious Link Analysis** | URL structure, redirect context, domain/DNS analysis, risk assessment | ✅ Completed |
| **003 — Business Email Compromise Scenario** | Executive impersonation, Reply-To mismatch, urgent payment request, financial-risk triage | ✅ Completed |

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

## Investigation 003 Highlights

The third investigation analyzed a simulated Business Email Compromise scenario involving executive impersonation, a Reply-To domain mismatch, a confidential high-value payment request, changed bank details, and instructions to bypass normal supplier verification.

A key lesson is that **SPF, DKIM, and DMARC can all pass while a BEC message is still malicious in intent** when an attacker controls their own sending domain and impersonates a trusted person rather than spoofing that person's real domain.

**Final classification:** Business Email Compromise / Executive Impersonation — Simulated / Authorized Lab  
**Severity:** High  
**MITRE ATT&CK:** T1656 — Impersonation

Documentation:

- [`investigations/003-business-email-compromise.md`](investigations/003-business-email-compromise.md)
- [`iocs/003-bec-executive-impersonation-iocs.md`](iocs/003-bec-executive-impersonation-iocs.md)
- [`samples/003-bec-executive-impersonation-simulated.eml`](samples/003-bec-executive-impersonation-simulated.eml)

## End-to-End Analyst Workflow

```text
Reported suspicious email
        ↓
Initial triage
        ↓
Header / sender analysis
        ↓
URL / domain analysis when applicable
        ↓
IOC extraction
        ↓
Threat / business-impact assessment
        ↓
MITRE ATT&CK mapping when relevant
        ↓
Analyst verdict
        ↓
Containment / verification / response recommendations
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
│   ├── 002-suspicious-link-iocs.md
│   └── 003-bec-executive-impersonation-iocs.md
├── playbooks/
│   └── phishing-response-playbook.md
├── samples/
│   ├── README.md
│   ├── 001-credential-phishing-simulated.eml
│   ├── 002-suspicious-link-simulated.txt
│   └── 003-bec-executive-impersonation-simulated.eml
└── screenshots/
    └── README.md
```

## Evidence Standard

Each completed investigation documents initial context, email metadata, suspicious indicators, IOC extraction, URL/domain/DNS observations where applicable, analyst reasoning, false-positive considerations, MITRE ATT&CK mapping where supported, final classification, severity, and response recommendations.

## Ethics & Safety

All exercises in this repository use **simulated, benign, or deliberately constructed training samples**. No real credentials are collected, no malicious payloads are executed, no live phishing infrastructure is operated, and no third-party systems or users are targeted.

Public evidence is sanitized before publication. Real personal email addresses, authentication tokens, account identifiers, private infrastructure details, live bank details, and unrelated user data are excluded or redacted.

## Related Project

My complementary SIEM and detection-engineering portfolio is available here:

- [SOC Analyst Lab — Splunk, Microsoft Sentinel, Windows Security & Wireshark](https://github.com/arriess/SOC-Analyst-Lab)

## Author

**Hicham Essafi**  
Cybersecurity | Junior SOC Analyst / Security Operations

- GitHub: https://github.com/arriess
- LinkedIn: https://www.linkedin.com/in/hicham-essafi/
