/**
 * Form Field Hesitation & Dwell Telemetry Tracker
 */
document.querySelectorAll('input, select, textarea').forEach(field => {
  let focusTime = 0;
  field.addEventListener('focus', () => { focusTime = Date.now(); });
  field.addEventListener('blur', () => {
    const dwell = Date.now() - focusTime;
    if (dwell > 3000) { // Over 3s hesitation
      console.log(`Hesitation detected on field: ${field.name || field.id} (${dwell}ms)`);
    }
  });
});
