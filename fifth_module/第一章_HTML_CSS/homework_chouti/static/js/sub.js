$(function () {
    //点赞功能
    $('.recommend').click(function () {
        pressTimes = $(this).children('b').text();
        pressTimes++ ;
        $(this).children('b').text(pressTimes);
    });

    //展开评论功能
    var isShow = true;
    $('.discuss').click(function () {

        commentTimes = $(this).parent().siblings('.comments-box-packup').children('ul').children().length;
        $(this).parent().siblings('.comments-box-packup').children('.count-times').html(commentTimes);

        $(this).children('b').html(commentTimes);

        //评论次数
        // commentTimes = $(this).children('b').text();

        //创建评论框
        // var $commentText = $('<textarea class="comment-reply" maxLength="150"></textarea>');
        // var $commentSubmit = $('<a class="comment-submit"></a>');
        // $commentSubmit.html('评论');
        //
        //
        // $commentText.insertAfter($(this).parent().siblings('.comments-box-packup').children('ul'));
        // $commentSubmit.insertAfter($(this).parent().siblings('.comments-box-packup').children('ul'));
        // console.log($(this).parent().siblings('.comments-box-packup').children('ul'));
        if(isShow){
            $(this).parent().siblings($('.comments-box-packup')).show('normal',function () {
                isShow = false;
            });

        }else {
            $('.comments-box-packup').hide('fast',function () {
                isShow = true;
            })

        }




    });
    
    //书写评论
    $('.comment-submit').click(function () {
        //获取textarea里面的值
        var commtenText = $('.comment-reply').val();
        //创建li标签
        var $createLi = $('<li></li>');
        if(commtenText){
            $createLi.html(commtenText);
            // console.log(commtenText)
            $(this).siblings('ul').append($createLi);
            $('.comment-reply').val('');
            //更新评论功能
            commentTimes = $(this).siblings('ul').children('li').length;
            $(this).siblings('.count-times').html(commentTimes);
            $(this).parent().siblings('.part2').children('.discuss').children('b').html(commentTimes)

        }else {
            return false;
        }
    });


    //登录 注册

    $('.login_register').on('click','a',function () {
        $('.login-register').css('display','block');
        var $ChooseLi = $('.cd-switcher').children('li');
        var $ChooseDiv = $('.cd-user-modal-container').children('div');
        $('.cd-switcher').on('click','li',function () {
            $(this).addClass('active').siblings('li').removeClass('active');
            index = $(this).index($ChooseLi);
            $ChooseDiv.eq(index).show().siblings('div').hide();


        })
    });

    $('.cd-user-modal-container').click(function () {
        return false
    });
    $('.cd-user-modal').click(function () {
        return false
    });
    
    $('.login-register').click(function () {
        $('.login-register').css('display','none');
    })
















});