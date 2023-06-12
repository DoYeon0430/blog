const btn_search = document.getElementById("btn_search");
btn_search.addEventListener('click', function() {
    document.getElementById('kw').value = document.getElementById('search_kw').value;
    document.getElementById('page').value = 1;  // 검색버튼을 클릭할 경우 1페이지부터 조회한다.
    document.getElementById('searchForm').submit();
    document.getElementById('search_kw').value = "";  // 검색 버튼을 클릭한 후 input 값 초기화 
});

document.getElementById("search_kw").addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {  // Enter 키의 keyCode는 13입니다.
        event.preventDefault();
        document.getElementById("btn_search").click();  // 검색 버튼 클릭 이벤트 실행
    }
});
var input = document.getElementById("search_kw");
input.value = null;

function dropdownForm(tag) {
    document.getElementById("kw").value = '';
    document.getElementById("page").value = '1';
    document.getElementById('tag').value = tag;
    document.getElementById('searchForm').submit();
}

function pageForm(page) {
    var urlParams = new URLSearchParams(window.location.search);
    document.getElementById('page').value = page;
    document.getElementById('kw').value = urlParams.get('kw');
    document.getElementById('tag').value = urlParams.get('tag');
    document.getElementById('searchForm').submit();
}