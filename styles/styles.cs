@import url("https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&family=Montserrat:wght@500&display=swap");
header {
  min-height: 100px;
  width: 100%;
  background-color: rgba(0, 0, 0, 0.474);
  position: fixed;
  display: grid;
  grid-template: "logo nav";
  grid-template-columns: 2fr 1fr;
  justify-content: space-between;
  padding: 0 2%;
  align-items: center;
  transition: height 0.2s;
}

.headerNav {
  grid-area: nav;
  transition: max-height 0.3s, padding 0.3s;
}
.headerNav ul {
  display: flex;
  justify-content: space-around;
  width: 100%;
  list-style: none;
}
.headerNav ul li a {
  text-decoration: none;
  color: white;
  font-size: 1.2rem;
  transition: color 0.2s;
}
.headerNav ul li a:hover {
  color: rgba(255, 255, 255, 0.5);
}

.logoNav {
  grid-area: logo;
  height: 80px;
  display: flex;
  align-items: center;
}

.mini {
  display: none;
  opacity: 0;
  height: 50%;
}

.full {
  opacity: 100;
  height: 100%;
}

#menuToggle {
  z-index: 999;
  display: none;
  background-color: transparent;
  grid-area: burger;
  border: none;
  padding: 5px;
  transition: background-color 0.3s;
}
#menuToggle:focus {
  outline: none;
}
#menuToggle div {
  width: 30px;
  height: 3px;
  background-color: white;
  margin: 5px 0;
  position: relative;
  transition: opacity 0.3s, transform 0.3s, top 0.3s;
}

.headerNavActive {
  max-height: 130px !important;
  display: block !important;
  padding: 3%;
}

.headerMini {
  min-height: 50px;
}
.headerMini .headerMini {
  height: 20px;
}
.headerMini .mini {
  display: block;
  opacity: 100%;
}
.headerMini .full {
  display: none;
}

@media (max-width: 1200px) {
  header {
    grid-template-columns: 1fr 1fr;
  }
}
@media (max-width: 680px) {
  header {
    grid-template-columns: 1fr;
    grid-template: "logo burger" "nav nav";
    padding: 0 5%;
  }
  header .headerNav {
    max-height: 0px;
    overflow: hidden;
  }
  header .headerNav ul {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  header .headerNav ul li {
    padding-bottom: 2%;
  }
  header .headerNav ul li:last-of-type {
    padding-bottom: 0;
  }
  header #menuToggle {
    display: block;
  }
  header .logoNav {
    justify-self: center;
  }
}
main {
  height: 100vh;
}

section {
  height: 100%;
  width: 100%;
  background-color: rgb(198, 198, 198);
}
section:last-of-type {
  background-color: rgb(95, 95, 95) !important;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  height: 100vh;
}

p, a, h1, h2, h3, h4, h5, h6 {
  font-family: "Montserrat", serif;
}

/*# sourceMappingURL=styles.cs.map */
