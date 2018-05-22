$(function () {
    //点赞功能
    $('.recommend').click(function () {
        pressTimes = $(this).children('b').text();
        pressTimes++ ;
        $(this).children('b').text(pressTimes);
    });

    //评论功能
    var isShow = true;
    $('.discuss').click(function () {

        //评论次数
        commentTimes = $(this).children('b').text();

        //增加评论区域
        // $('<div class="comments-box-packup"></div>').insertAfter($(this).parent());

        if(isShow){
            $(this).parent()
        }




    })















});