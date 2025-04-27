
async function dropShowClass(e){
    if (!e || (e && !e.type) || (e && e.type && e.type !== "click")){
        return false;
      }
     const showElements = document.querySelectorAll(".show");
     if (showElements.length === 0) {
        return false;
     }
     for (let i = 0; i < showElements.length; i++) {
        if (showElements[i].classList.contains("show")) {
            showElements[i].classList.remove("show");
            return true;
        }
    }
}
document.addEventListener("DOMContentLoaded", () => {
  const navbarAll = document.querySelectorAll(".navbar");
  if (navbarAll.length === 0){
    console.log("Somenfing what frong!");
  }
  for (let i = 0; i < navbarAll.length; i++) {
    navbarAll[i].addEventListener("click", function(e){
      dropShowClass(e);
      if (!e || (e && !e.type) || (e && e.type && e.type !== "click")){
        return false;
      }

//      e.preventDefault();
      const res = [];

      Array.from(e.target.classList).forEach((item) => {
        const arr = ["dropdown-toggle", "dropdown"];

        if (item === "dropdown"){
//            e.target.classList.remove("show");
            e.target.classList.add("show");

        } else if (item === "dropdown-toggle") {
//            e.target.parentElement.classList.remove("show");
            e.target.parentElement.classList.add("show");
        }

      });
    });
  }
});
