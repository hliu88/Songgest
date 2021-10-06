$(function(){
	$('button').click(function(){
		var playlist = $('#text').val();
		// var pass = $('#inputPassword').val();
		$.ajax({
			url: '/processing',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});