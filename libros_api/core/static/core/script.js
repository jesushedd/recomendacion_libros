function toggleMenu() {
    const menu = document.getElementById("dropdown");
    menu.style.display = menu.style.display === "block" ? "none" : "block";
  }
  
  document.addEventListener("click", function(event) {
    const dropdown = document.getElementById("dropdown");
    const icon = document.querySelector(".menu-icon");
    if (!dropdown.contains(event.target) && !icon.contains(event.target)) {
      dropdown.style.display = "none";
    }
  });  