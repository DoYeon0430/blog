// 페이지가 로드되었을 때 실행되는 함수
window.addEventListener("load", function() {
// 클릭 이벤트를 body 요소에 추가
var body = document.querySelector("body");
body.addEventListener("click", handleBodyClick);
});

// body 클릭 이벤트 핸들러
function handleBodyClick(event) {
var target = event.target;
var body = document.querySelector("body");
var menu = document.querySelector(".menu");

// 클릭된 요소가 메뉴 토글 버튼이 아니고, 메뉴 영역 내부에 속하지 않는 경우 메뉴를 닫음
if (!target.classList.contains("navbar-burger") && !menu.contains(target)) {
    body.classList.remove("open");
    menu.style.transform = "translateX(100%)";
}
}

// 메뉴 토글 함수
function toggleMenu() {
var body = document.querySelector("body");
var menu = document.querySelector(".menu");

body.classList.toggle("open");

if (body.classList.contains("open")) {
    menu.style.transform = "translateX(0)";
} else {
    menu.style.transform = "translateX(100%)";
}
}

// 스크롤 자바스크립트
window.addEventListener('scroll', function() {
// 현재 스크롤 위치
    var scrollPosition = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0;

// 스크롤이 1px 이상 내려갔을 때
    if (scrollPosition > 0) {
    // 링크 보이기
    document.getElementById("scrollTopLink").style.display = "block";
} else {
    // 링크 숨기기
    document.getElementById("scrollTopLink").style.display = "none";
}
});