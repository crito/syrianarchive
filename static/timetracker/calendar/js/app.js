(function($) {

	"use strict";

	var options = {
		events_source: '/time/api/calendar_list.json',
		view: 'month',
		tmpl_path: '/static/timetracker/calendar/tmpls/',
		tmpl_cache: false,
		day: 'now',
		onAfterEventsLoad: function(events) {
			if(!events) {
				return;
			}
			var list = $('#eventlist');
			list.html('');
			events.reverse();
			$.each(events, function(key, val) {
				var date = new Date(val.start*1000);
				$(document.createElement('li'))
					.html('<a href="' + val.url + '">' + val.title + '</a><span class="listdate">' + (date.toString()).substr(0,10) + "</span>")
					.appendTo(list);
			});
		},
		onAfterViewLoad: function(view) {
			$('.page-header h3').text(this.getTitle());
			$('.btn-group button').removeClass('active');
			$('button[data-calendar-view="' + view + '"]').addClass('active');


						$('.addentry a').click(function(e){
							e.preventDefault();
							e.stopPropagation();

							$('#entrymodal').on('shown.bs.modal', function () {
    							$("#id_name").focus();
								$("#id_name").select();
							})

							// prepare form
							$("#entrymodal").modal("show");

							$('#realdate input').attr('value', $(this).attr('data-date'));

						});


	
		},
		classes: {
			months: {
				general: 'label'
			}
		}
	};

	var calendar = $('#calendar').calendar(options);

	$('.btn-group button[data-calendar-nav]').each(function() {
		var $this = $(this);
		$this.click(function() {
			calendar.navigate($this.data('calendar-nav'));
		});
	});

	$('.btn-group button[data-calendar-view]').each(function() {
		var $this = $(this);
		$this.click(function() {
			calendar.view($this.data('calendar-view'));
		});
	});

	$('#first_day').change(function(){
		var value = $(this).val();
		value = value.length ? parseInt(value) : null;
		calendar.setOptions({first_day: value});
		calendar.view();
	});

	$('#language').change(function(){
		calendar.setLanguage($(this).val());
		calendar.view();
	});

	$('#events-in-modal').change(function(){
		var val = $(this).is(':checked') ? $(this).val() : null;
		calendar.setOptions({modal: val});
	});


	

	var form = $("#entryadd");
	var $taskfield = $("#id_name");

	form.submit(function(e) {

	  $("#sendbutton").attr('disabled', true)
	  //start ajax
	  $.ajax({
	      url:form.attr('action'),
	      type:'post',
	      data: form.serializeArray(),
	      success: function(responseText, responseStatus) {
	          // After ajax success, make the form submittable again
	          $("#sendbutton").attr('disabled', false)

	          // After adding the entry via ajax, select and focus the 'task' field again
	          
	          $taskfield.focus();
	          $taskfield.select();

	          $('.bottom-right').notify({
                    message: { text: 'Entry Successfully Added!' }
              }).show(); 

	          // window.location.reload();
	          options["day"] = $('#realdate input').attr('value');
	          calendar = $('#calendar').calendar(options);
	          $("#entrymodal").modal("hide");
	      },
	      error: function(responseText, responseStatus){
                $('.bottom-right').notify({
                    message: { text: 'Entry Successfully Added! ', type:'error' }
                  }).show();
          }
	  });
	  // end ajax

	  e.preventDefault(); 

	  // SERIOUSLY the form should always be submittable
	  $("#sendbutton").attr('disabled', false)
	});












}(jQuery));