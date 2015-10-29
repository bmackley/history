$(function() {
	$('#details img').hover(function(evt){
		$(evt.target).css("cursor", "pointer")
	
	});
	$('#details img').off('mouseover').on('mouseover', function(){
		$(this).css('border', '15px solid blue');
	});
	$('#details img').mouseout(function(evt){
		$(this).css('border', 'none');
	});


});