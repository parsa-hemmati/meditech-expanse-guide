# MEDITECH Expanse Results Notification Configuration Guide
## Mid Cheshire NHS Foundation Trust | PP64 Build

Educational materials and interactive tools for configuring MEDITECH Expanse imaging results notification routing.

---

## 🎯 **NEW: Interactive Configuration Tool**

### [`interactive-configurator.html`](interactive-configurator.html) ⭐ **START HERE**

A dynamic web application for service leads to configure and visualize their results notification routing in real-time.

#### Features:
- **Real-time visualization** - See how results route as you type
- **Service-specific configuration** - For each department (Fracture Clinic, AMU, HASU, etc.)
- **Variable tracking** - Trust, Location, Department, Service, System Consultant, Patient, Requester, Report Authorised, Primary/Secondary Recipients
- **Path A vs Path B comparison** - Side-by-side visualization with actual clinician names
- **Flow diagram** - Report Authorised → MEDITECH Routing → Recipients
- **Print/PDF export** - Take your configuration to AS meetings
- **Educational** - Understand impact of Radio Button choice

#### Use Cases:
- Fracture clinic lead configures settings and sees routing in real-time
- Consultant visualizes how their service's results will be delivered
- Educational tool for demonstrating routing differences
- Printable configuration worksheet for Application Specialist meetings

#### How to Use:
1. Open `interactive-configurator.html` in any browser
2. Fill in your service details (Department, Service, Care Setting)
3. Select Radio Button choice and Workgroup configuration
4. Enter example scenario (Patient name, Consultants)
5. Watch the routing visualization update in real-time
6. Click "Print / Save as PDF" for your AS meeting

---

## 📚 **Clinical Lead's Guide**

### [`clinical-guide-enhanced.html`](clinical-guide-enhanced.html)

Comprehensive educational guide with scenario-based learning and detailed technical comparisons.

#### Features:
- **Vertical left sidebar navigation** - Easy section jumping
- **Complete 45-scenario coverage** - ALL scenarios from millbrook_expanse_v3.html now included
- **Detailed Path A vs Path B comparison tables** - Side-by-side configuration, failure modes, compensation
- **Visual key configuration concepts** - Radio Button, Workgroups, Task Generation, Priority Handling
- **Interactive collapsible learning levels** - Progressive complexity across 5 maturity levels
- **Glossary** - With corrected Item Triage definition
- **Governance & Technical Reference** - Access control, monitoring, AS translation guide

#### Structure:
1. **Quick Start** (5 min) - What you need to know
2. **Essential Education** (10 min) - Core concepts with visual cards
3. **Scenario-Based Learning** (20-30 min) - Progressive examples with ALL 45 scenarios
   - **Level 1:** Foundation (S1-S5) - Radio Button, first workgroup, critical priority
   - **Level 2:** Team Routing (S6-S14) - Workgroup delivery, pathway basics
   - **Level 3:** Pathway Intelligence (S15-S25, S30) - Multi-site, complex routing, stale Attending (S25)
   - **Level 4:** Governance Layer (S26-S29, S31-S35, S37) - Locum safety, surveillance rules, confidentiality, rotating clinics
   - **Level 5:** Resolution Failures (S36, S38-S45) - System limits, interface boundaries, full synthesis (S45)
4. **Glossary** - Key terms explained
5. **Technical Reference** - Clinical → AS translation
6. **Governance** - Access control & post-go-live monitoring
7. **Configuration Worksheet** - Your service requirements

---

## 📋 **Original Documentation**

### Source Materials:
- `millbrook_expanse_v3.html` - Original comprehensive guide (Google Docs export)
- `millbrook_expanse_v4.html` - Revised version with v4 corrections
- `V4_REVISION_SUMMARY.md` - Summary of v4 changes
- `V4_TECHNICAL_ERRATA.md` - Technical corrections in v4

### Previous Versions:
- `clinical-guide.html` - Earlier clinical guide
- `index.html`, `index-v2.html` - Previous index formats
- `*.css` - Supporting stylesheets

---

## 🚀 **Quick Start**

### For Service Leads:
1. **Open** [`interactive-configurator.html`](interactive-configurator.html)
2. **Fill in** your service details
3. **Watch** the routing visualization update
4. **Print** for your AS meeting

### For Clinical Leads Learning the System:
1. **Open** [`clinical-guide-enhanced.html`](clinical-guide-enhanced.html)
2. **Read** Quick Start (5 min)
3. **Work through** Essential Education (10 min)
4. **Explore** scenarios for your service
5. **Complete** Configuration Worksheet

### For Application Specialists:
1. **Review** clinical-guide-enhanced.html for full scenario details
2. **Use** interactive-configurator.html in service lead meetings
3. **Reference** detailed Path A vs Path B comparison tables
4. **Note** governance recommendations (S25, S37, access control)

---

## 🔧 **Technical Details**

### Key Configuration Variables:
| Variable | Description |
|----------|-------------|
| **Trust** | Your NHS Trust |
| **Location** | Hospital site |
| **Department** | Clinical department |
| **Service** | Specific service within department |
| **System Consultant** | Current Attending in MEDITECH |
| **Patient** | Example patient |
| **Requester** | Who ordered the imaging |
| **Report Authorised** | Trigger event from CRIS |
| **Primary Recipient** | Individual or workgroup (depends on Radio Button + Deliver To) |
| **Secondary Recipient** | Additional pathway routing (workgroups, specialist teams) |

### Radio Button Paths:
#### Path A (Attending)
- Results go to **current responsible consultant**
- **Requires:** Robust Attending field governance
- **Risk:** Stale Attending field (Consultant of Week syndrome - see S25)
- **NHS Reality:** Attending field rarely updated after admission

#### Path B (Requesting Clinician)
- Results go to **whoever ordered the scan**
- **Works well for:** Outpatients with stable consultants
- **Risk:** Junior rotation (unmanned inbox)
- **NHS Reality:** Juniors rotate every 4-6 months

### Item Triage Values (Confirmed PP64):
- **INPRESULT** - Inpatient workgroup routing
- **AMBRESULT** - Ambulatory/outpatient workgroup routing

**⚠️ CRITICAL:** Item Triage classifies **care setting** (inpatient vs ambulatory), NOT urgency. Do not confuse with OBR-5 (HL7 priority field).

---

## ⚠️ **Critical Corrections from V4**

1. **Item Triage Definition** - Corrected: classifies care setting (inpatient vs ambulatory), NOT urgency
2. **S36/S37 Numbering** - S37 now covers CRIS vetting gap (no conflict)
3. **Stale Attending Problem** - S25 fully documents Path A's scale failure mode
4. **Governance** - Access control recommendations added
5. **Trust Name** - Updated to Mid Cheshire NHS Foundation Trust
6. **Double-rendered annotation tags** - Fixed

---

## 🎯 **Who Should Use What?**

| Role | Primary Tool | Purpose |
|------|--------------|---------|
| **Service Lead** (e.g., Fracture Clinic) | `interactive-configurator.html` | Configure your service settings, visualize routing, print for AS meeting |
| **Clinical Lead** (Learning) | `clinical-guide-enhanced.html` | Understand system, work through scenarios, complete worksheet |
| **Consultant** (50s+) | `clinical-guide-enhanced.html` | Educational guide designed for consultants leading discussions with AS |
| **Application Specialist** | Both | Use configurator in meetings, reference guide for technical detail |
| **CCIO / Governance** | `clinical-guide-enhanced.html` | Governance section, S25 (Consultant of Week), S37 (CRIS gap), access control |

---

## 📁 **File Structure**

```
millbrook_expanse_v3/
├── interactive-configurator.html   # ⭐ NEW: Dynamic configuration tool
├── clinical-guide-enhanced.html    # ⭐ Enhanced clinical guide with left nav
├── clinical-styles-enhanced.css    # Styles for enhanced guide
│
├── millbrook_expanse_v3.html       # Original comprehensive guide
├── millbrook_expanse_v4.html       # V4 with corrections
│
├── clinical-guide.html             # Earlier clinical guide version
├── clinical-styles.css             # Styles for earlier guide
│
├── index.html                      # Previous index (v1)
├── index-v2.html                   # Previous index (v2)
├── styles.css, styles-v2.css       # Previous stylesheets
├── app.js, app-v2.js               # Previous JavaScript
│
├── README.md                       # This file
├── V4_REVISION_SUMMARY.md          # V4 changes summary
├── V4_TECHNICAL_ERRATA.md          # V4 technical corrections
└── WHICH_VERSION.md                # Version guide
```

---

## 🔒 **NHS Compliance**

- Follows NHS Digital guidelines
- Caldicott Guardian consultation prompts (S19, S20)
- Patient safety risk identification
- Confidentiality controls
- Governance recommendations for access control

---

## 🤝 **Support**

- **Scenarios:** Contact your Trust's Application Specialist
- **Governance:** Consult your CCIO or Caldicott Guardian
- **Technical:** Reference clinical-guide-enhanced.html Technical Reference section

---

## 📄 **License & Attribution**

Educational materials for MEDITECH Expanse configuration.
Mid Cheshire NHS Foundation Trust | PP64 Build

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>

---

**Version 4.0 Enhanced** | 45 Scenarios | Interactive Configuration Tool | Path A vs Path B Comparisons
