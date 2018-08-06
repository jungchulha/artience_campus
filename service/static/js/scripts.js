
let doapply = $(".applyevent");

doapply.on('click', function() {
    let item = $(this);
    let data = {};
    data["post_id"] = item.attr("postid");
    let url = "/unapply/"
    let like = item.hasClass("apply");
    let target = $(item.attr("notapply"));
    console.log(item.attr("target"));

    if(like) {
        url = "/apply/";
    }

    $.ajax({
        type: "POST",
        data: data,
        url: url,
        success: function(e) {
            console.log(e);
            item.toggleClass("apply");
            item.toggleClass("notapply");
            if (url=="/apply/"){item.text("강의 취소")} else {item.text("강의 신청")}


            target.html(e.likes_count);
        }
    });
});
