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


}(jQuery));