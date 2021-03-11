$(function() {
	$(".panel").css({"height":$(window).height()});
	$.scrollify({
		section:".panel",
		scrollbars: false,
	});
	

	$(".scroll").click(function(e) {
		e.preventDefault();
		$.scrollify("move",$(this).attr("href"));
	});
});