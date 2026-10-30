/**
 * Form Field Hesitation & Abandonment Telemetry Snippet
 * File: tests/telemetry.test.js
 */

(function() {
  'use strict';
  const config = {
    name: "form-field-hesitation-telemetry-kit",
    subNiche: "cro",
    version: "1.0.0"
  };

  function init() {
    console.log("Initialized " + config.name);
  }

  if (typeof document !== 'undefined') {
    document.addEventListener('DOMContentLoaded', init);
  } else if (typeof module !== 'undefined' && module.exports) {
    module.exports = config;
  }
})();
