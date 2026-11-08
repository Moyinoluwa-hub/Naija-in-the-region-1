const searchBox = document.getElementById("search");
const cards = document.querySelectorAll(".card");

searchBox.addEventListener("input", function () {
    const term = searchBox.value.toLowerCase();

    cards.forEach(function (card) {
        const text = card.textContent.toLowerCase();
        card.style.display = text.includes(term) ? "" : "none";
    });
});
