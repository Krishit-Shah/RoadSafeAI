document.getElementById("accidentForm").addEventListener("submit", function (e) {
  const vehicleChecks = document.querySelectorAll('input[name="vehicle_type"]:checked');
  const terms = document.querySelector('input[name="terms"]');

  if (vehicleChecks.length === 0) {
    alert("Please select at least one vehicle type.");
    e.preventDefault(); // Stop form from submitting
    return;
  }

  if (!terms.checked) {
    alert("Please accept the terms to submit.");
    e.preventDefault();
    return;
  }

  alert("✅ Accident report submitted (for now it's just a test)");
});
