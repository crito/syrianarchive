// The Javascript code for site wite hooks, triggers, starts.
// Things to do with menus and forms and whatnot.

//REQUIREMENTS:  the following must be loaded before this file for it to work

//select2.js

(function($){

	//Sitewide javascript variable


	//Functions


	//document ready
	$(document).ready(function(){


		function format_opt(item) {
    		var originalOption = item.element;
			var originalText = item.text;
    		return '<span style="' +$(originalOption).attr('style')+ '">' + originalText + ' '   + '</span>';
    	}

    	function select2Focus() {
		    var select2 = $(this).data('select2');
		    setTimeout(function() {
		        if (!select2.opened()) {
		            select2.open();
		        }
		    }, 0);  
		}

		//initialise a basic select box for all available.  i love this plugin.
		$("select").select2({
			placeholder:'type here',
			formatResult: format_opt,
    		formatSelection: format_opt,
    		escapeMarkup: function(m) { return m; }
		}).one('select2-focus', select2Focus).on("select2-blur", function () {
    		$(this).one('select2-focus', select2Focus)
		});


	});


	//window load
	$(window).load(function(){

	});

	// CSRF token for ajaxed forms et al ! 
	//Code from here: https://gist.github.com/broinjc/db6e0ac214c355c887e5
	// This function gets cookie with a given name
	function getCookie(name) {
	    var cookieValue = null;
	    if (document.cookie && document.cookie != '') {
	        var cookies = document.cookie.split(';');
	        for (var i = 0; i < cookies.length; i++) {
	            var cookie = jQuery.trim(cookies[i]);
	            // Does this cookie string begin with the name we want?
	            if (cookie.substring(0, name.length + 1) == (name + '=')) {
	                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
	                break;
	            }
	        }
	    }
	    return cookieValue;
	}
	var csrftoken = getCookie('csrftoken');
	 
	/*
	The functions below will create a header with csrftoken
	*/
	 
	function csrfSafeMethod(method) {
	    // these HTTP methods do not require CSRF protection
	    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}
	function sameOrigin(url) {
	    // test that a given url is a same-origin URL
	    // url could be relative or scheme relative or absolute
	    var host = document.location.host; // host + port
	    var protocol = document.location.protocol;
	    var sr_origin = '//' + host;
	    var origin = protocol + sr_origin;
	    // Allow absolute or scheme relative URLs to same origin
	    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
	        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
	        // or any other URL that isn't scheme relative or absolute i.e relative.
	        !(/^(\/\/|http:|https:).*/.test(url));
	}
	 
	$.ajaxSetup({
	    beforeSend: function(xhr, settings) {
	        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
	            // Send the token to same-origin, relative URLs only.
	            // Send the token only if the method warrants CSRF protection
	            // Using the CSRFToken value acquired earlier
	            xhr.setRequestHeader("X-CSRFToken", csrftoken);
	        }
	    }
	});

	console.log("in here");

	// form helper


	// AJAX for posting
	function create_post() {
    		console.log("create post is working!") // sanity check
    		console.log($('#post-text').val())
	};

	// Submit post on submit
	$('#post-form').on('submit', function(event){
	    event.preventDefault();
	    console.log("form submitted!")  // sanity check
	    create_post();
	});



}(jQuery));