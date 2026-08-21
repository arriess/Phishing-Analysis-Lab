# Investigation 002 — Suspicious Link Analysis

**Status:** ✅ Completed  
**Scenario type:** Simulated / Benign Training Sample  
**Severity:** Medium

## Objective

Analyze a simulated suspicious URL from a SOC perspective using safe, non-interactive methods. The investigation focuses on URL structure, domain context, redirect behavior, DNS observations, IOC extraction, analyst risk assessment, and response recommendations.

## Sample

[`samples/002-suspicious-link-simulated.txt`](../samples/002-suspicious-link-simulated.txt)

The sample uses only reserved `.example` domains and TEST-NET IP address ranges. No live malicious infrastructure is contacted.

## Initial URL

```text
https://secure-sharepoint-login.example/auth?redirect=https%3A%2F%2Fm365-session-check.example%2Fsignin&user=employee%40soc-lab.example
```

## URL Structure Analysis

### Scheme

- `https`
- HTTPS alone does **not** make a link trustworthy; it only indicates encrypted transport.

### Hostname

- `secure-sharepoint-login.example`
- The hostname includes trust-inducing words such as `secure`, `sharepoint`, and `login`.
- This naming pattern attempts to resemble a legitimate Microsoft/SharePoint authentication destination in the simulated scenario.

### Path

- `/auth`
- Authentication-themed paths can be legitimate, but here they reinforce the credential-verification pretext when combined with the lookalike hostname and redirect behavior.

### Query Parameters

- `redirect=` contains an encoded second destination.
- `user=employee@soc-lab.example` embeds a synthetic target identity.

The encoded redirect parameter makes the next destination less obvious to a casual user and increases suspicion.

## Simulated Redirect Analysis

The initial link redirects to:

```text
https://m365-session-check.example/signin?continue=%2Faccount%2Fverify&case=TRAINING-002
```

Indicators observed:

- A second Microsoft 365-themed hostname is introduced.
- The path changes to `/signin`.
- The `continue` parameter points to `/account/verify`.
- The navigation sequence repeatedly uses authentication and verification language.

This is consistent with a simulated credential-harvesting flow designed to keep the user inside a convincing login narrative.

## DNS Context

The lab uses documentation-only IP addresses:

| Host | Simulated IP | Context |
|---|---|---|
| `secure-sharepoint-login.example` | `198.51.100.44` | TEST-NET-2 |
| `m365-session-check.example` | `203.0.113.25` | TEST-NET-3 |

These are not real attack hosts and are safe to publish as part of the training scenario.

## Extracted IOCs

The full IOC set is documented in:

[`iocs/002-suspicious-link-iocs.md`](../iocs/002-suspicious-link-iocs.md)

Key indicators include:

- `secure-sharepoint-login.example`
- `m365-session-check.example`
- encoded redirect behavior
- `/auth`, `/signin`, and `/account/verify` paths
- synthetic user-targeting parameter
- TEST-NET IP addresses associated with the training hosts

## Risk Assessment

### Suspicious factors

- Brand-themed lookalike hostnames
- Authentication and verification wording
- Encoded redirect parameter
- Multiple staged destinations
- User-specific query parameter
- Sign-in / verification flow consistent with credential collection pretext

### Factors preventing a higher severity

- This is a controlled synthetic sample.
- No real user clicked a live malicious link.
- No credentials were submitted.
- No endpoint compromise or malware execution occurred.

**Severity: Medium**

In a production environment, severity should be increased if telemetry confirms user interaction, credential submission, account compromise, malicious payload delivery, or broader campaign activity.

## MITRE ATT&CK Mapping

### T1566.002 — Phishing: Spearphishing Link

The simulated lure uses a link intended to direct a target toward a staged authentication flow. This behavior is consistent with **Spearphishing Link**.

The mapping is limited to the behavior demonstrated by the lab and does not imply a real-world threat actor or campaign.

## Analyst Verdict

**Classification:** Suspicious / Credential-Phishing Link Simulation  
**Confidence:** High  
**Severity:** Medium

The link structure, lookalike naming, encoded redirect, staged authentication path, and user-targeting parameter collectively support a phishing assessment in this controlled scenario.

## Recommended Response Actions

If equivalent indicators were observed in a real environment, the analyst should:

1. Quarantine or remove the suspicious email/message.
2. Block confirmed malicious domains and URLs at appropriate security controls.
3. Search email and proxy/SIEM telemetry for other recipients or clicks.
4. Determine whether any user submitted credentials.
5. If credentials may have been exposed, reset the password and revoke active sessions/tokens.
6. Review authentication logs for suspicious sign-ins or MFA changes.
7. Notify affected users and document the incident timeline.
8. Preserve relevant evidence for further investigation.

## False-Positive Considerations

Legitimate services can use redirects, encoded URLs, SSO parameters, and authentication-themed paths. Analysts should therefore avoid classifying a URL based on one feature alone and instead correlate hostname reputation, sender context, authentication results, user behavior, destination ownership, and surrounding telemetry.

## Ethics

No active malicious URL was visited. The entire redirect chain, DNS context, hostnames, identities, and IP addresses were deliberately constructed for safe portfolio training.
