# Investigation 003 — Business Email Compromise Scenario

**Status:** ✅ Completed  
**Scenario type:** Simulated / Benign Training Sample

## Objective

Investigate a simulated business email compromise (BEC) scenario focused on executive impersonation, payment-request social engineering, email identity analysis, financial-risk assessment, and SOC escalation decisions.

## Sample

[`samples/003-bec-executive-impersonation-simulated.eml`](../samples/003-bec-executive-impersonation-simulated.eml)

The sample uses fictitious identities, reserved `.example` domains, TEST-NET infrastructure, and non-functional payment details.

## Initial Triage

### Identity observations

- Display name claims to be **Martin Keller — CEO** of a fictitious company.
- Visible sender uses `executive-mail.example`.
- Reply-To uses a different domain: `consultant-mail.example`.
- The message is addressed to Accounts Payable and requests a direct financial action.

### Email authentication

The synthetic sample reports:

- SPF: **pass**
- DKIM: **pass**
- DMARC: **pass**

These results show that the sender controls the sending domain, but they do **not** prove that the sender is the executive being impersonated. This is an important BEC triage lesson: successful authentication does not make a socially engineered message trustworthy.

## Social-Engineering Indicators

The message contains several high-risk BEC behaviors:

- Executive / CEO impersonation
- Urgent same-day payment deadline
- High-value transfer request: **EUR 48,750**
- New beneficiary / changed bank-details pretext
- Confidentiality pressure
- Instruction not to contact the supplier
- Request to bypass normal verification channels
- Request to reply directly after initiating payment

These indicators are consistent with attempted financial fraud through identity deception and process bypass.

## IOC Summary

Full IOC documentation:

[`iocs/003-bec-executive-impersonation-iocs.md`](../iocs/003-bec-executive-impersonation-iocs.md)

Key synthetic indicators include:

- `executive-mail.example`
- `consultant-mail.example`
- `mail.executive-mail.example`
- `203.0.113.90`
- Fictitious payment amount and transaction reference

## Risk Assessment

**Primary risk:** Business Email Compromise / attempted financial fraud  
**User interaction:** No payment performed in the lab  
**Severity:** **High**  
**Confidence:** **High**

The severity is High because a successful real-world version of this scenario could cause immediate financial loss, despite the absence of malware or credential theft.

## MITRE ATT&CK Mapping

**T1656 — Impersonation**

The scenario relies on impersonating a trusted executive identity to influence a finance employee into performing an unauthorized payment action. The mapping is used for the social-engineering behavior demonstrated by the lab scenario; no actual account compromise is claimed.

## False-Positive Considerations

Legitimate executives can make urgent payment requests, and external domains may sometimes be valid. Therefore, the analyst should not classify a message as BEC based on urgency alone.

The combination of executive impersonation, Reply-To mismatch, changed-bank-details pretext, confidentiality pressure, instruction to avoid supplier verification, and a high-value transfer request substantially increases confidence.

## Recommended Response

1. Do **not** initiate the payment.
2. Verify the request using a trusted out-of-band channel such as a known corporate phone number or internal collaboration platform.
3. Contact the supplier through previously established contact details to confirm any bank-account change.
4. Escalate the message to the SOC / security team and finance leadership.
5. Search the mail environment for similar sender, Reply-To, subject, and wording patterns.
6. Block or quarantine confirmed malicious sender infrastructure according to organizational policy.
7. If a payment was already initiated, immediately engage finance, the receiving bank, legal/fraud teams, and incident response procedures.
8. Preserve the original message and headers for investigation.

## Analyst Verdict

**Final classification:** Business Email Compromise / Executive Impersonation — Simulated / Authorized Lab  
**Severity:** High  
**Confidence:** High

The message is classified as a BEC simulation because it combines trusted-executive impersonation with financial urgency and explicit attempts to bypass normal verification procedures.

## Ethics

This investigation uses only fictitious identities, organizations, payment details, reserved domains, and documentation-only IP addressing. No real executive, company, bank account, employee, or third-party system is targeted.
