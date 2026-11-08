const searchBox = document.getElementById("search");
const cards = document.querySelectorAll(".card");

searchBox.addEventListener("input", function () {
    const term = searchBox.value.toLocaleLowerCase();

    cards.forEach(function (card){
        const text = card.textContent.toLocaleLowerCase();
        card.style.display = text.includes(term)?"" : "none";
    })
})
