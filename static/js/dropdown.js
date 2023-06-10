var dropdown = document.querySelector(".dropdown_bar");
var dropdownContent = document.querySelector(".dropdown-content");
var dropdown_toggle = document.querySelector(".dropdown_toggle");
var dropdown_toggleContent = document.querySelector(".dropdown_main");

dropdown.addEventListener("click", function() {
    if (dropdownContent.style.display === "block") {
        dropdownContent.style.display = "none";
    } else {
        dropdownContent.style.display = "block";
    }
});

dropdown_toggle.addEventListener("click", function() {
    if (dropdown_toggleContent.style.display === "block") {
      dropdown_toggleContent.style.display = "none";
    } else {
      dropdown_toggleContent.style.display = "block";
    }
});