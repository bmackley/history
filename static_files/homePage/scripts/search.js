$(function(){
		$('.title').each(function(){
		$(this).append( 'Join Group');
	});
});

$(function(){
		$('.price').each(function(){
		$(this).css({'color': 'red'});
	});
});

$(function(){
		$('.thumbnail').mouseover(function(){
		$('.brand').css('fontWeight', '800');
	});
});
$(function(){
		$('.thumbnail').mouseout(function(){
		$('.brand').css('fontWeight', '200');
	});
});