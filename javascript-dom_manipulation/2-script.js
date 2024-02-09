const redheader = document.getElementById("red_header")
redheader.addEventListener("click", addClass())

function addClass () {
    const header = document.querySelector("header")
    header.classList.add("red")
}