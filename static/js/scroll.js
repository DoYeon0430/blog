// 스크롤 이벤트 리스너 추가
window.addEventListener('scroll', function () {
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