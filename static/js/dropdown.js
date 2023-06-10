var dropdown = document.querySelector(".dropdown_bar");
var dropdownContent = document.querySelector(".dropdown-content");
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