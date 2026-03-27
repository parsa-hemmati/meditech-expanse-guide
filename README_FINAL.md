# MEDITECH Expanse Configuration Guide - Final Version

## Template-Based Architecture v5.0

This directory contains the **production-ready** version of the MEDITECH Expanse Imaging Results Configuration Guide with a clean, maintainable template-based architecture.

---

## 📁 Files Included

### Core Application Files

| File | Purpose | Size |
|------|---------|------|
| `index.html` | Landing page with navigation to both apps | 6 KB |
| `clinical-guide-enhanced.html` | Main clinical guide (self-contained with embedded data) | 299 KB |
| `scenarios-data.json` | Scenario data (reference only - embedded in HTML) | 233 KB |
| `clinical-styles-enhanced.css` | Styles for clinical guide | 24 KB |
| `interactive-configurator.html` | Interactive configuration tool (self-contained) | 44 KB |
| `README.md` | Original project documentation | 9 KB |

**Total:** 615 KB (self-contained, no server required)

---

## 🚀 Quick Start

**No server required! All files work directly from the file system.**

1. **Open `index.html`** in a web browser (double-click or drag to browser)
2. Choose your tool:
   - **Clinical Guide** - For learning and reference
   - **Interactive Configurator** - For building your service configuration

### Or direct access:
- Open `clinical-guide-enhanced.html` directly for the full guide
- Open `interactive-configurator.html` directly for the configurator

### ✅ Self-Contained Files
- `clinical-guide-enhanced.html` has all scenario data **embedded** - works offline
- `interactive-configurator.html` has all styles **inline** - single file
- `scenarios-data.json` is for reference only (data is embedded in HTML)

---

## 🎯 What's New in v5.0

### Template-Based Architecture

**Before (v4.0):**
- 7,266 lines of HTML
- 45 scenarios with duplicated markup
- ~6,300 lines of repeated code
- Hard to maintain

**After (v5.0):**
- 1,063 lines of HTML (85% reduction!)
- Single JavaScript template for all scenarios
- Data separated from presentation
- Easy to maintain

### How It Works

```
scenarios-data.json          ← Source data (for editing/reference)
        ↓
    embedded into
        ↓
clinical-guide-enhanced.html ← Template + embedded data + JavaScript renderer
        ↓
Dynamically rendered scenarios on page load
        ↓
Works offline, no server needed!
```

**Note:** The scenario data is **embedded directly** in the HTML file as a JavaScript variable. This allows the file to work when opened directly from the file system (no `fetch()` issues with `file://` URLs).

---

## 📚 Architecture Details

### Scenario Data Structure

Each scenario in `scenarios-data.json` contains:

```json
{
  "number": 1,
  "title": "Scenario title",
  "level": 1,
  "service": "Service name",
  "mechanisms": "Active mechanisms",
  "schemaFilter": "Q&A filter",
  "clinicalContext": "Clinical description",
  "tables": {
    "configuration": "HTML table content",
    "outcome": "HTML table content",
    "failures": "HTML table content",
    "compensation": "HTML table content"
  },
  "asNote": "Application Specialist note",
  "keyLearning": "Key learning point"
}
```

### Template Rendering

Single JavaScript template function renders all 45 scenarios:

```javascript
function renderScenario(scenario) {
  return `
    <div class="scenario-card">
      <div class="scenario-header">
        <span class="scenario-number">S${scenario.number}</span>
        <h4>${scenario.title}</h4>
        <span class="badge-level-${scenario.level}">Level ${scenario.level}</span>
      </div>
      <div class="scenario-body">
        ${scenario.tables.configuration}
        ${scenario.tables.outcome}
        ${scenario.tables.failures}
        ${scenario.tables.compensation}
      </div>
    </div>
  `;
}
```

---

## ✨ Features

### Clinical Guide
- **45 complete scenarios** across 5 maturity levels
- **Path A vs Path B** configuration comparison
- **4 detailed tables per scenario:**
  - Configuration (10+ rows)
  - Outcome comparison
  - Failure modes
  - Compensation strategies
- **Collapsible levels** for easy navigation
- **Vertical sidebar** with quick links
- **Template-based** - update once, affects all scenarios

### Interactive Configurator
- **Real-time routing visualization**
- **Enter your service details** and see results instantly
- **Path A vs Path B comparison** with your data
- **System vs Real Consultant** data quality gap visualization
- **Print-ready output** for AS meetings
- **Self-contained** - all styles inline, no dependencies

---

## 🛠️ Maintenance

### To Update Scenario Content

1. Edit `scenarios-data.json` (the source data file)
2. Run `python embed_scenarios.py` to embed updated data into HTML
3. Open `clinical-guide-enhanced.html` - changes appear

**Or** edit the embedded data directly in `clinical-guide-enhanced.html` (search for `const SCENARIOS_DATA`)

### To Update Table Structure

1. Edit the template function in `clinical-guide-enhanced.html` (search for `renderScenario`)
2. Refresh the browser - all 45 scenarios update automatically

### To Add New Scenarios

1. Add new scenario object to `scenarios-data.json`
2. Run `python embed_scenarios.py` to re-embed
3. Open `clinical-guide-enhanced.html` - automatically rendered with correct level grouping

### Re-embedding Data

If you update `scenarios-data.json`:
```bash
python embed_scenarios.py
```
This replaces the embedded data in the HTML file.

---

## 📊 Technical Specifications

- **Browser Requirements:** Modern browser with JavaScript enabled (Chrome, Firefox, Edge, Safari)
- **No Server Required:** Pure client-side rendering (HTML + CSS + JavaScript)
- **Data Format:** JSON for scenario data, HTML for rich text formatting
- **Rendering:** Fetch API + Template literals
- **Styles:** External CSS + inline styles for configurator

---

## 🎓 Use Cases

### For Clinical Leads
1. Start with `index.html`
2. Read the Clinical Guide scenarios (Level 1-3)
3. Use Interactive Configurator to test your service configuration
4. Print configuration for AS meeting

### For Application Specialists
1. Reference complete scenario configuration tables
2. Use AS NOTES for Expanse navigation guidance
3. Cross-reference schema questions (Q1-Q7)
4. Validate configuration against failure modes

### For Training
1. Use Clinical Guide as teaching material
2. Work through levels progressively (1 → 5)
3. Interactive Configurator for hands-on practice
4. Failure modes as case studies

---

## 📝 Version History

- **v5.0** - Template-based architecture refactor (85% code reduction)
- **v4.0** - Complete 45-scenario coverage with full configuration tables
- **v3.0** - Interactive configurator integration
- **v2.0** - Enhanced clinical guide with vertical navigation
- **v1.0** - Initial scenario-based guide

---

## 🏥 Credits

**Mid Cheshire NHS Foundation Trust**
MEDITECH Expanse PP64 Build
Results Notification Configuration Project

---

## 📞 Support

For questions or updates:
1. Refer to original `README.md` for project context
2. Check scenario AS NOTES for specific guidance
3. Use Interactive Configurator to test configuration changes

---

**Built with template-based architecture for maximum maintainability** ✨
