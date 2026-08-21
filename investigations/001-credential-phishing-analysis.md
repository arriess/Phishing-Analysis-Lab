# Investigation 001 — Credential Phishing Analysis

**Status:** ✅ Completed  
**Scenario type:** Simulated / Benign Training Sample  
**Severity:** Medium  
**Final classification:** Credential Phishing — Simulated / Authorized Lab

## Objective

Investigate a simulated credential-phishing email using a repeatable SOC triage workflow and document sender/header observations, suspicious-link analysis, extracted indicators, analyst reasoning, MITRE ATT&CK mapping, severity, and response recommendations.

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

## URL Analysis

Suspicious training URL:

```text
https://login-microsoft.example/verify?session=TRAINING-001
```

The URL was analyzed structurally only; no live malicious content was accessed.

### Findings

- Hostname uses Microsoft-themed wording to imitate a trusted service.
- Link domain does not match the visible sender domain or Reply-To domain.
- `/verify` supports the account-verification pretext.
- `session=TRAINING-001` is a synthetic training parameter, not a real token.
- The `.example` namespace confirms that this is non-production lab infrastructure.

## IOC Extraction

The investigation produced a sanitized IOC set documented here:

[`iocs/001-credential-phishing-iocs.md`](../iocs/001-credential-phishing-iocs.md)

Key indicator categories include:

- Visible sender domain
- Reply-To domain
- Return-Path domain
- Link domain
- Synthetic sending host and TEST-NET source IP
- Authentication failures
- Verification-themed URL path and training parameter

## Social-Engineering Assessment

The message combines several common phishing techniques:

- Trusted-brand impersonation
- Urgency and time pressure
- Threat of account suspension
- Fear of losing access
- Credential-verification pretext
- Mismatched sender, reply-path, and link domains

The combination is designed to encourage rapid user action before the recipient verifies the message independently.

## MITRE ATT&CK Mapping

### T1566.002 — Phishing: Spearphishing Link

The simulated email delivers a link intended to direct the recipient toward a credential-verification flow. The project does **not** claim that credential theft occurred, because no credentials were entered or collected in this lab.

## Analyst Assessment

### Evidence supporting phishing classification

- Microsoft-themed impersonation
- Sender / Reply-To / Return-Path inconsistencies
- Link-domain mismatch
- SPF failure
- No DKIM signature
- DMARC failure
- Urgent account-suspension language
- Verification-themed call to action

### False-positive considerations

A legitimate security message can contain urgent language, and some legitimate senders can experience authentication or forwarding issues. However, the combined domain mismatches, failed authentication, brand impersonation, and verification link make a benign interpretation unlikely in this constructed scenario.

## Severity

**Medium**

Rationale: the message is designed to obtain account credentials and would require prompt containment in a real environment. No user interaction, credential submission, account compromise, or malware execution occurred in this controlled lab, so the investigation does not claim confirmed impact.

## Response Recommendations

For an equivalent real-world case, a SOC analyst should:

1. Quarantine or remove the message from affected mailboxes.
2. Block confirmed malicious sender, reply-to, and URL/domain indicators according to organizational policy.
3. Search the mail environment for additional recipients of the same campaign.
4. Determine whether any user clicked the link or submitted credentials.
5. If credentials may have been exposed, reset the password, revoke active sessions/tokens, and verify MFA status.
6. Review authentication logs for suspicious sign-ins after the email was delivered.
7. Notify affected users and document the incident.
8. Escalate if account compromise, lateral movement, or additional malicious activity is identified.

## Final Verdict

**Credential Phishing — Simulated / Authorized Lab**

The email is classified as phishing based on brand impersonation, authentication failures, sender/reply-path mismatches, a suspicious verification link, and strong urgency/account-loss social engineering.

No live malicious infrastructure was contacted and no credential compromise occurred.

## Ethics

This investigation uses a deliberately constructed training sample. No real credentials, active phishing infrastructure, malicious payloads, or third-party targets are used.
