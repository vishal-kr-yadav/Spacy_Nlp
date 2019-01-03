$(function(){
	$('button').click(function(){
		var options = $('#options').val();
		var search = $('#search').val();
		$.ajax({
			url: '/',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
				var result=JSON.stringify(JSON.parse(response),null,2);
				alert(result)
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});

