# IOC Documentation

This directory contains **sanitized indicators of compromise (IOCs)** extracted from the controlled training samples.

Possible indicator types include:

- Sender domains
- Reply-to domains
- URLs
- Hostnames
- IP addresses when relevant and safe to publish
- File hashes from benign training artifacts

## Safety Rules

- Do not publish active malicious links as clickable URLs.
- Defang potentially harmful indicators when needed, for example `hxxps://example[.]invalid`.
- Do not publish real user email addresses, credentials, tokens, or unrelated personal data.
- Indicators are added only when they are part of a completed controlled investigation.
