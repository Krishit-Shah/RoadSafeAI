window.addEventListener("DOMContentLoaded", () => {
    alert("Welcome Admin 👩‍💻 – Dashboard Loaded!");

    const now = new Date();
    const timestamp = document.getElementById("timestamp");
    if (timestamp) {
        timestamp.innerText = "Page generated at: " + now.toLocaleString();
    }

    const regionFilter = document.getElementById("regionFilter");
    if (regionFilter) {
        regionFilter.addEventListener("change", function () {
            const selected = this.value;
            alert("You selected: " + selected + " region (feature coming soon)");
        });
    }

    const cards = document.querySelectorAll(".card");
    cards.forEach(card => {
        card.addEventListener("mouseover", () => {
            card.style.boxShadow = "0 4px 16px rgba(0, 0, 0, 0.2)";
            card.style.transform = "scale(1.05)";
            card.style.transition = "all 0.3s ease-in-out";
        });
        card.addEventListener("mouseout", () => {
            card.style.boxShadow = "";
            card.style.transform = "scale(1)";
        });
    });

})
    .catch(err => {
        console.error("Failed to load dashboard.html:", err);
        document.getElementById("content").innerHTML =
            "<p style='color:red'>⚠️ Failed to load dashboard content.</p>";
    });
