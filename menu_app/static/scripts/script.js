document.addEventListener("DOMContentLoaded", () => {
  const navbarAll = document.querySelectorAll(".navbar");
  if (navbarAll.length === 0){
    console.log("Somenfing what frong!");
  }
  for (let i = 0; i < navbarAll.length; i++) {
    navbarAll[i].addEventListener("mousedown", function(e){
      if (!e || (e && !e.type) || (e && e.type && e.type !== "mousedown")){
        return false;
      }
      e.preventDefault();
      const res = [];

      Array.from(e.target.classList).forEach((item) => {
        const arr = ["dropdown-toggle", "dropdown"];

        if (item === "dropdown"){
            e.target.classList.remove("show");
            e.target.classList.add("show");

        } else if (item === "dropdown-toggle") {
            e.target.parentElement.classList.remove("show");
            e.target.parentElement.classList.add("show");
        }

      });
      res
      console.log(res)
    });
  }
});