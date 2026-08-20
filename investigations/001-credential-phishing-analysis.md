# Investigation 001 — Credential Phishing Analysis

**Status:** 🟠 In Progress  
**Scenario type:** Simulated / Benign Training Sample

## Objective

Investigate a simulated credential-phishing email using a repeatable SOC triage workflow. The final report will document sender/header observations, suspicious-link analysis, extracted indicators, analyst reasoning, MITRE ATT&CK mapping where justified, severity, and response recommendations.

## Sample

[`samples/001-credential-phishing-simulated.eml`](../samples/001-credential-phishing-simulated.eml)

The sample uses only reserved `.example` domains and TEST-NET addressing. It contains no live phishing infrastructure or real credentials.

## Initial Triage

### Visible message indicators

- Display name claims to be **Microsoft Security**.
- Sender domain is `microsoft-support.example`, which does not match an official Microsoft production domain and is intentionally synthetic for the lab.
- Reply-To points to a different domain: `account-check.example`.
- Subject uses urgency: **"URGENT: Your Microsoft 365 account will be suspended"**.
- Body threatens suspension within **30 minutes** and possible permanent loss of access.
- Call-to-action points to `login-microsoft.example`, which differs from both the visible sender and Reply-To domains.

### Authentication observations

The sample contains the following simulated authentication results:

- SPF: **fail**
- DKIM: **none**
- DMARC: **fail**

These results increase suspicion when combined with the domain mismatch and social-engineering language.

### Initial assessment

The message exhibits multiple classic credential-phishing indicators: impersonation of a trusted brand, urgency, account-loss pressure, mismatched sender/Reply-To/link domains, and failed email-authentication checks.

At this stage, the message should be treated as **suspicious / likely phishing** pending completion of URL and IOC analysis.

## Planned Next Analysis

- Inspect the suspicious URL structure safely
- Extract and document sanitized IOCs
- Assess social-engineering techniques
- Map supported behavior to MITRE ATT&CK
- Determine final severity and classification
- Recommend containment and user-response actions

## Evidence

Evidence will be added only after the controlled investigation is completed. Any public screenshot will be sanitized before publication.

## Analyst Verdict

**Provisional:** Likely credential phishing — final verdict pending URL/IOC analysis.

## Ethics

This investigation uses a deliberately constructed training sample. No real credentials, active phishing infrastructure, malicious payloads, or third-party targets are used.
