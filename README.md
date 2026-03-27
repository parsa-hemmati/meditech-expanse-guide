# MEDITECH Expanse Configuration Guide

[![Live Demo](https://img.shields.io/badge/Live-Demo-blue?style=for-the-badge)](https://parsa-hemmati.github.io/meditech-expanse-guide/)
[![GitHub](https://img.shields.io/badge/GitHub-Repo-181717?style=for-the-badge&logo=github)](https://github.com/parsa-hemmati/meditech-expanse-guide)

**Template-Based Clinical Guide & Interactive Configurator for MEDITECH Expanse PP64 Imaging Results Notification**

---

## 🌐 Live Demo

**Access the guide online:**
### **[https://parsa-hemmati.github.io/meditech-expanse-guide/](https://parsa-hemmati.github.io/meditech-expanse-guide/)**

Or download and use offline - no server required!

---

## 📚 What's Inside

### 1. Clinical Guide
Comprehensive scenario-based learning guide for clinical leads and application specialists.

- **45 complete scenarios** across 5 maturity levels
- **Path A vs Path B** configuration comparison
- **Complete configuration tables** (10+ rows per scenario)
- **Failure modes** and compensation strategies
- **Template-based architecture** - 85% code reduction

### 2. Interactive Configurator
Real-time service configuration tool with live routing visualization.

- Enter your service details and see routing instantly
- Visual Path A vs Path B comparison with your data
- System vs Real Consultant data quality gap visualization
- Print-ready configuration output

---

## 🚀 Quick Start

### Online Access
Visit **[https://parsa-hemmati.github.io/meditech-expanse-guide/](https://parsa-hemmati.github.io/meditech-expanse-guide/)**

### Offline Use
1. Download this repository
2. Open `index.html` in any modern browser
3. All files work offline - no server needed!

**Or direct access:**
- `clinical-guide-enhanced.html` - Full clinical guide
- `interactive-configurator.html` - Interactive tool

---

## 📊 Features

### Clinical Guide Features
- 5 maturity levels (Foundation → Master)
- Radio Button & RESULTTASK configuration
- Workgroup Dictionary & Task Generation
- Coverage Schedule & User Override
- Surveillance Rules & Ancillary Mapping
- Collapsible sections with vertical navigation
- AS NOTES for Expanse navigation guidance

### Interactive Configurator Features
- Real-time routing calculation
- Path A/B comparison with your clinician names
- Data quality gap visualization (System vs Real)
- OOH coverage configuration
- Workgroup setup
- Task generation rules
- Print-friendly output

---

## 🏗️ Technical Architecture

### Template-Based Design
```
scenarios-data.json          ← Source data (for editing)
        ↓
    embedded into
        ↓
clinical-guide-enhanced.html ← Template + embedded data
        ↓
JavaScript dynamic rendering
        ↓
45 scenarios rendered on page load
```

### Key Benefits
- **85% code reduction** (7,266 → 1,063 lines)
- **Single template** renders all 45 scenarios
- **Embedded data** - no fetch() issues
- **Self-contained** - works offline
- **Easy maintenance** - update template once, affects all

---

## 📁 Files

| File | Size | Purpose |
|------|------|---------|
| `index.html` | 6 KB | Landing page |
| `clinical-guide-enhanced.html` | 299 KB | Self-contained clinical guide |
| `interactive-configurator.html` | 44 KB | Self-contained configurator |
| `clinical-styles-enhanced.css` | 24 KB | Styles for guide |
| `scenarios-data.json` | 233 KB | Source data (reference) |
| `embed_scenarios.py` | 2 KB | Re-embedding utility |

**Total:** 640 KB

---

## 🛠️ Maintenance

### To Update Scenario Content

1. Edit `scenarios-data.json`
2. Run `python embed_scenarios.py` to re-embed into HTML
3. Commit and push changes

### To Update Template Structure

1. Edit the `renderScenario()` function in `clinical-guide-enhanced.html`
2. Refresh browser - all 45 scenarios update automatically

### Re-embedding Data

After editing `scenarios-data.json`:
```bash
python embed_scenarios.py
git add clinical-guide-enhanced.html scenarios-data.json
git commit -m "Update scenario data"
git push
```

GitHub Pages will automatically deploy the updates.

---

## 📖 Scenario Coverage

### Level 1: Foundation (S1-S5)
- Radio Button & RESULTTASK rows
- Primary recipient routing
- Workgroup patterns
- Rotation problems

### Level 2: Pathway Routing (S6-S15)
- Result Task Generation
- Pathway-based routing
- OOH coverage schedules
- Ward transfer scenarios

### Level 3: Advanced Mechanisms (S16-S25)
- User Override
- Surveillance Rules
- Specialty-specific patterns
- Multiple mechanism interaction

### Level 4: Edge Cases (S26-S35)
- Complex interactions
- Performance optimization
- Unusual clinical workflows
- Multiple conditions firing

### Level 5: Master Level (S36-S45)
- System boundaries
- Inter-trust transfers
- Comprehensive synthesis
- Advanced troubleshooting

---

## 🎯 Use Cases

### For Clinical Leads
1. Understand configuration options (Path A vs Path B)
2. Learn through real scenarios from your Trust
3. Use Interactive Configurator to test your service
4. Print configuration for AS meetings

### For Application Specialists
1. Reference complete configuration tables
2. Use AS NOTES for Expanse navigation
3. Cross-reference schema questions (Q1-Q7)
4. Validate against failure modes

### For Training
1. Progressive learning (Level 1 → 5)
2. Hands-on practice with configurator
3. Failure modes as case studies
4. Print for training materials

---

## 🏥 Project Context

**Built for:** Mid Cheshire NHS Foundation Trust
**System:** MEDITECH Expanse PP64 Build
**Module:** Imaging Results Notification
**Purpose:** Clinical lead education and configuration planning

---

## 📜 Version History

- **v5.1** (2026-03-27) - Self-contained files with embedded data
- **v5.0** (2026-03-27) - Template-based architecture (85% reduction)
- **v4.0** (2026-03-27) - Complete configuration tables for all scenarios
- **v3.0** (2026-03-26) - Interactive configurator integration
- **v2.0** (2026-03-25) - Enhanced navigation and styling
- **v1.0** (2026-03-24) - Initial scenario-based guide

See [CHANGELOG.md](CHANGELOG.md) for detailed version history.

---

## 🔧 Browser Requirements

- Modern browser with JavaScript enabled
- Chrome, Firefox, Edge, Safari (latest versions)
- Works offline (no server required)
- No plugins or extensions needed

---

## 📄 License

This guide is for educational and configuration planning purposes for NHS Trusts implementing MEDITECH Expanse.

---

## 🤝 Contributing

To suggest improvements or report issues:
1. Open an issue on [GitHub](https://github.com/parsa-hemmati/meditech-expanse-guide/issues)
2. Submit a pull request with improvements
3. Share feedback with your Application Specialist

---

## 🌟 Acknowledgments

Built with template-based architecture for maximum maintainability and ease of use.

**Live Demo:** [https://parsa-hemmati.github.io/meditech-expanse-guide/](https://parsa-hemmati.github.io/meditech-expanse-guide/)

---

**🤖 Built with Claude Code** | Template-Based Architecture | Self-Contained | Offline-Ready
