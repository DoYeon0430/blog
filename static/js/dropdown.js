var dropdown = document.querySelector(".dropdown_bar");
var dropdownContent = document.querySelector(".dropdown-content");
var dropdown_toggle = document.querySelector(".dropdown_toggle");
var dropdown_toggleContent = document.querySelector(".dropdown_main");
var drop_icon1 = document.querySelector(".drop_icon1");
var drop_icon2 = document.querySelector(".drop_icon2");

dropdown.addEventListener("click", function() {
  if (dropdownContent.style.display === "block") {
      dropdownContent.style.display = "none";
      drop_icon1.style.display = "inline-flex";
      drop_icon2.style.display = "none";
  } else {
      dropdownContent.style.display = "block";
      drop_icon1.style.display = "none";
      drop_icon2.style.display = "inline-flex";
  }
});


dropdown_toggle.addEventListener("click", function() {
    if (dropdown_toggleContent.style.display === "block") {
      dropdown_toggleContent.style.display = "none";
    } else {
      dropdown_toggleContent.style.display = "block";
    }
});