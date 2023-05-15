$(document).ready(function() {
    // 페이지 이동 시 상단으로 스크롤 방지
    $(".pagination a").on("click", function(event) {
        event.preventDefault();
        var url = $(this).attr("href");
        $.ajax({
            url: url,
            type: "GET",
            success: function(response) {
                // 페이지 이동
                $("#pagination-div").html(response);
            }
        });
    });
});