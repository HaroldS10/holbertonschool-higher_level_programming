//change color hader on click
const header_div = document.querySelector("#red_header")

header_div.addEventListener("click", uploadColor)

function uploadColor() {
    const header = document.querySelector("header")
    header.style.color = "#FF0000"
}