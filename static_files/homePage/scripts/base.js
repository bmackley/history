
$(function(){
	
	$('.products').off('click').on('click', function(){
		$(this).css('background-color', "#d3d3d3")
	});
	$('.products').off('mouseout').on('mouseout', function(){
		$(this).css('background-color', none)
	});
	$('.products').css('font-family', "Times-New Roman")
});



