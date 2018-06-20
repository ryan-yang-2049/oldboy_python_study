/**
 * Created by ryan on 2018/6/19.
 */


$(function () {
    var a = 0;
    $('#btn').click(function () {
        a++;
        if(a%4===1){
            $('#h4').css('color','green')
        }else if(a%4===2) {
            $('#h4').css('color','yellow')
        }else if (a%4===3){
            $('#h4').css('color','blue')
        }else{
            $('#h4').css('color','red')
        }
    })
});
