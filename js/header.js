let height = 0;
const header = document.querySelector("header");

function pageHeight(){
    height = window.scrollY;
    console.log(height);
    if (height >= 200) {
        header.classList.add("headerMini");
    } else {
        header.classList.remove("headerMini");
    }
}

window.addEventListener("scroll", pageHeight);