$(function(){
    $('.item-content').click(function(){
        var $under=$(this).find('.under');
        if($under.hasClass('open')){
            $under.removeClass('open');
            $under.slideUp();
            $(this).find('span').text('+')
        }else{
            $under.addClass('open');
            $under.slideDown();
            $(this).find('span').text('-')
        }
    });
    $('.list-item').hover(function(){
        var $underlist=$(this).find('.list-under');
        if($underlist.hasClass('openlist')){
            $underlist.removeClass('openlist');
            $underlist.slideUp();
        }else{
            $underlist.addClass('openlist');
            $underlist.slideDown();
        }
    });
});
