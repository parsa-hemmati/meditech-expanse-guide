# Changelog

## v5.1 - Self-Contained Files (2026-03-27)

### Fixed
- **Embedded scenarios data** directly in HTML to fix `fetch()` errors with `file://` URLs
- Clinical guide now works when opened directly from file system
- No web server required

### Changed
- `clinical-guide-enhanced.html` now contains embedded scenario data (299 KB, up from 67 KB)
- `scenarios-data.json` kept as reference/source file for editing
- Added `embed_scenarios.py` utility script for re-embedding data after edits

### Technical Details
- Replaced `fetch('scenarios-data.json')` with embedded `const SCENARIOS_DATA`
- All 235,129 characters of JSON data embedded as JavaScript variable
- Template rendering system unchanged - still uses same client-side rendering

## v5.0 - Template-Based Architecture (2026-03-27)

### Added
- Template-based rendering system for all 45 scenarios
- Separated data (JSON) from presentation (HTML template)
- Single JavaScript template function renders all scenarios

### Improved
- **85% code reduction** - from 7,266 lines to 1,063 lines
- Much easier to maintain - update template once, affects all scenarios
- Better developer experience

### Created
- `scenarios-data.json` - All 45 scenarios as structured data
- `build_template_version.py` - Build script for template version
- `extract_to_json_v2.py` - Extraction script from HTML to JSON

## v4.0 - Complete Configuration Tables (2026-03-27)

### Added
- Complete configuration tables for all 45 scenarios
- Full detail level matching original millbrook_expanse_v3.html
- 10+ configuration rows per scenario
- Failure modes and compensation strategies

### Improved
- From 4-6 row simplified tables to 15-20 row complete tables
- +5,920 insertions to clinical guide

## v3.0 - Interactive Configurator (2026-03-26)

### Added
- Interactive service configuration tool
- Real-time routing visualization
- Path A vs Path B comparison with user data
- System vs Real Consultant data quality gap visualization
- Print-ready configuration output

## v2.0 - Enhanced Clinical Guide (2026-03-25)

### Added
- Vertical left sidebar navigation
- Enhanced table styling and formatting
- Link between clinical guide and configurator

### Improved
- Better user experience with persistent navigation
- Collapsible level sections

## v1.0 - Initial Release (2026-03-24)

### Added
- 45 scenario-based learning guide
- Path A vs Path B configuration comparison
- 5 maturity levels
- Essential education section
- Glossary and technical reference
