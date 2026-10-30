# Form Field Hesitation & Abandonment Telemetry Snippet

> Discover the exact form field that makes your visitors abandon. Drop in a 1KB, privacy-safe JavaScript telemetry snippet.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Format: CLI_SCRIPT](https://img.shields.io/badge/Format-CLI--SCRIPT-green.svg)](#)
[![Tier: 2](https://img.shields.io/badge/Tier-2-orange.svg)](#)
[![Region: MENA](https://img.shields.io/badge/Region-Egypt%20%7C%20GCC%20%7C%20Saudi-purple.svg)](#)
[![Tests: Passing](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)](#)
[![Owner: mahmoudabdelnaby1](https://img.shields.io/badge/Owner-mahmoudabdelnaby1-blue.svg)](https://github.com/mahmoudabdelnaby1)

---

## 📌 Problem Statement & Target Persona

### Target Persona
**PRO** operating in high-growth e-commerce, digital publishing, and direct-response marketing across Saudi Arabia, UAE, and Egypt.

### Core Problem
Develop a lightweight, privacy-safe form hesitation tracking library (`form_telemetry.js`): 1) Tracks time spent per field (focus to blur), correction count (backspaces), and last-interacted field upon abandonment, 2) Does not record keystroke text by design; field timing and correction-count events still require appropriate consent, minimization, and disclosure, 3) Pushes structured `form_friction` events to `dataLayer`, 4) Includes GTM container JSON and GA4 exploration guide.

---

## 🛠️ Repository Architecture & Deliverables

This repository provides self-contained, documented implementations and specifications:

- `docs/ga4-exploration-setup.md`
- `examples/sample_form_events.json`
- `gtm/form-telemetry-gtm-recipe.json`
- `LICENSE`
- `README.md`
- `reports/hesitation_heatmap.html`
- `src/aggregate_hesitation.py`
- `src/form_telemetry.js`
- `src/form_telemetry.min.js`
- `src/hesitation_tracker.js`
- `tests/telemetry.test.js`
- `tests/test_hesitation.py`


---

## 🚀 Quick Start & How to Run Locally

### Run Test Suite Locally
```bash
# Ensure no bytecode generation
export PYTHONDONTWRITEBYTECODE=1  # Linux / macOS
$env:PYTHONDONTWRITEBYTECODE="1"  # Windows PowerShell

# Run Python unittest discovery
python -m unittest discover -s tests
```

### Run Native JavaScript Tests (Zero NPM Dependencies)
```bash
# Uses Node.js v20+ built-in test runner
node --test tests/*.test.js
```

### Run CLI Script
```bash
python src/aggregate_hesitation.py --help
```

### Interactive Browser Tool
Open `reports/hesitation_heatmap.html` directly in your web browser (Chrome, Edge, Safari) to use the local interactive calculator or dashboard. Operates 100% client-side with zero external network calls.

---

## 📊 Sample Input & Output Fixtures

> **Data Disclosure:** Any included sample data is illustrative and may be synthetic; it is not a measured customer result or market benchmark unless a source and collection method are stated alongside it. These files run offline with standard libraries and require no paid third-party API credentials.

```json
{
  "domain": "cro",
  "repository": "form-field-hesitation-telemetry-kit",
  "status": "READY_FOR_LOCAL_REVIEW",
  "license": "MIT"
}
```

---

## ⚠️ Known Technical & Domain Constraints

- **Performance Impact:** Event listeners for focus, blur, and keystroke timing must use passive listeners and debounce routines to prevent input lag.
- **PII Data Isolation:** Field value contents are never logged or transmitted; telemetry captures field names, character counts, and hesitation milliseconds only.
- **Bilingual Field Identification:** Normalizes Arabic input labels (e.g. 'رقم الجوال') to standard telemetry keys (e.g. 'phone_input').

---

## 📚 Primary Documentation & Verifiable References

- [Baymard Institute: Form Usability & User Hesitation Studies](https://baymard.com/) - Research on form abandonment, field confusion, and input error recovery.
- [W3C User Timing API Specification](https://www.w3.org/TR/user-timing/) - High-precision client-side performance and latency measurement standard.
- [Google Analytics 4 Custom Metric Configuration](https://developers.google.com/analytics/devguides/collection/ga4/events) - Logging high-resolution user timing telemetry in analytics.

---


## 👤 Maintainer & License

- **Author & Maintainer:** [Mahmoud Abdelnaby](https://github.com/mahmoudabdelnaby1) (`@mahmoudabdelnaby1`)
- **License:** [MIT License](LICENSE) - Open-source, auditable, and freely adaptable for internal enterprise or commercial use.
