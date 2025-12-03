# Feature Request: Smart Detection of Provider Changes

Request for fuzzy matching to detect channel renames and preserve mappings.

### Current Limitation

Provider renames channels ’ all mappings lost.

### Feature Request

Fuzzy matching to detect renames, preserve mappings automatically.

### Benefit

Survive provider changes without complete remapping. Detect that "ESPN HD" was renamed to "ESPN FHD" and preserve all configuration.

### Technical Challenge

Balancing false positives (matching wrong channels) with false negatives (missing obvious renames).

### Related Topics

- [Source Sync Breaking Layouts](../troubleshooting/02_source_sync_breaking_layouts.md)
- [Lost EPG Mappings After Renewal](../faq/10_lost_epg_mappings_after_renewal.md)
