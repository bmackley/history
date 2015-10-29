$(function(){
	$(".active").hover(function (){
        $('.underline').css("text-decoration", "underline");
    },function(){
    	$('.underline').css("text-decoration", "none")
    });
});
