let slideIndex = 0;
showSlides();

function showSlides() {
  let i;
  const slides = document.getElementById("slider").getElementsByTagName("img");

  // 이미지를 왼쪽으로 이동하고, 첫 번째 이미지가 보이도록 함
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) {
    slideIndex = 1;
  }
  slides[slideIndex - 1].style.display = "block";

  // 1초마다 이미지를 슬라이드로 이동
  setTimeout(showSlides, 3000);
}