(function ($, undefined) {
	$(document).ready(function(){
		// $('#id_username').on('blur', function(evt){
		// 	checkUsernameAjax($('#id_username'));
		// });
		// $('#id_email').on('blur', function(evt){
		// 	emailCheckAjax($('#id_email'));
		// });
		$('#create_user_submit').on('click', function(evt){	
			if(emailCheck($('#id_email')) == false){
				evt.preventDefault();
			}
			// if(checkUsername($('#id_username')) == false){
			// 	evt.preventDefault();
			// }
		});
		$("#create_account").submit(function(e) {
            e.preventDefault();
            var form = this;
            var username = $('#id_username');
            var email = $('#id_email');
            $.ajax({
                url: '/homePage/create_user_ajax/' + 'username' + '/' + username.val() + '/' + 'email' + '/' + email.val(),
	        	success: function(result){callback(result, form)},
	         	error: function(err){
	         		alert('the ajax call to check the username is not working')
	         	},//erro
                cache: false,
                //complete : function(result){callback(result, form)}
            });     
        });
		var callback = function(result, form){
		  if(result.users != 'no users' ){
		  	alert('Username already taken');
		  }
		  else if(result.email != 'no email'){
		  	alert('Email already in use')
		  }
		  else{
		    form.submit();
		  }
		};
	})

	function checkPasswords(pass1, pass2){
		if(pass1.val() !== pass2.val()){
			alert('passwords do not match')
			return false;
		}else if(pass1.val() == ''){
			alert('Please Enter a Password')
			return false;
		}
	}
	// function checkUsername(username){
	// 	if(/\s/g.test(username.val()) == true){
	// 		alert('please remove spaces from the username')
	// 		return false;
	// 	}
	// 	if(username.val() == ''){
	// 		alert('Please enter a username')
	// 		return false;
	// 	}
	// }
	// function checkUsernameAjax(username){
	// 	$.ajax({
	//         url: '/homePage/create_user_ajax/' + 'username' + '/' + username.val(),
	//         success: handleData,
	//          error: function(err){
	//          	alert('the ajax call to check the username is not working')
	//          }//error
	//     });
	// }
	// function handleData(data){
	// 	if(data.users != 'no users'){
	// 		alert('Username already taken');
	// 		submit_form = false;
	// 		return false;
	// 	}
	// }
	// function handleDataEmail(data){
	// 	if(data.userdata != 'no email'){
	// 		alert('Email already taken');
	// 		submit_form = false;
	// 		return false;
	// 	}
	// 	else{
	// 		console.log(data)
	// 		console.log('looking good with the email')
	// 	}

	// }
	function validateEmail(email){
		var re = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
	    return re.test(email);
	}
	function emailCheck(emailStr) {
		if (emailStr.val() == '') {
			alert('Please Enter an Email');
			return false;
		}
		if(validateEmail(emailStr.val()) == false){
			alert('The email you entered does not look like an email address')
			return false;
		}
		if(checkPasswords($('#id_password'), $('#id_retypepassword')) == false){
			return false;
		}
		return true;
	}
	// function emailCheckAjax(emailStr) {
	// 	$.ajax({
	//         url: '/homePage/create_user_ajax/' + 'email' + '/' + emailStr.val(),
	//         success: handleDataEmail,
	//          error: function(err){
	//          	alert('the ajax call to check the username is not working')
	//          }//error
	//     });
	// }
}(jQuery));