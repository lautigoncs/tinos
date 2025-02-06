let height = 0;
let i = 0;
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

function triggerResBars() {
    const menu = document.getElementById('menuToggle');
    const bars = Array.from(menu.getElementsByTagName("div"));
    if (i==0) {
        bars.forEach(bar => {
            console.log(i);
            if(i==1) {
                bar.style.opacity = "0";
                i++;
            } else if (i==2) {
                bar.style.transform = "rotate(45deg)";
                bar.style.top = "-8px"
                i++;
            } else {
                bar.style.transform = "rotate(-45deg)";
                bar.style.top = "8px";
                i++;
            }
        }) 
    } else {
        bars.forEach(bar => {
                bar.style.opacity = "1";
                bar.style.transform = "rotate(0deg)";
                bar.style.top = "0px"
        })
        i=0;
    }
    document.getElementsByClassName("headerNav")[0].classList.toggle("headerNavActive");
}
