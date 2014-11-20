(function($){
/*
Tracktime.JS
This file deals with all of the ajax functions for the main
timetracker page.  Adding entries, removing entries, dragging 
entries, and so forth.
*/

// a function to add an entry via ajax.  takes the form
//that is usually posted to /time/add, and posts it via
//ajax.  also refreshes the #entries div which pulls from
// the entries list page

      // set the variables, list of timetracher entries and the form var
      var entriesurl = '/time/entries_list.html';
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

                  //adds the entry on success, will have to change when more things are added
                  $.ajax({
                    url: entriesurl,
                    success: function(data) {
                      $('#entries').html(data);
                    }
                  });
              },
              error: function(responseText, responseStatus){
                $('.bottom-right').notify({
                    message: { text: 'Something went wrong!' + responseText, type:'error' }
                  }).show(); 
              }
          });
          // end ajax

          e.preventDefault(); 

          // SERIOUSLY the form should always be submittable
          $("#sendbutton").attr('disabled', false)
      });
      // end ajax submit function

// a function which ajax deletes items.
      $('#entries').on("click",".removebutton", function(e){
        e.preventDefault();

        //second guess clause, because the backend will just delete
        $(this).html("you sure?").click(function(){
          $.ajax({
            // it is going to the url that deletes the item, so
            url: $(this).attr('href'),
            success: function() {
              $.ajax({
                url: entriesurl,
                success: function(data) {
                  // refresh the entries list
                  $('#entries').html(data);
                }
              });
            }
          });
        });
      });

/*
STUFF FOR THE DATE PICKER  CODE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
==============================================================
==============================================================
*/

  $(document).ready(function(){

      $('#realdate').datepicker({
          format: 'yyyy-mm-dd',
      });

      $('#fakedate').datepicker({
          format: 'dd, MM DD yyyy',
          autoclose : true,
          todayBtn: true,
          closeBtn: true,
          weekStart: 1,
      })
      .on('changeDate', function(e){
         $('#realdate').datepicker('update', $('#fakedate').datepicker('getDate'));
      });

      $('#fakedate').datepicker('update', 'Today');
      $('#realdate').datepicker('update', $('#fakedate').datepicker('getDate'));
      $taskfield.focus();
      $taskfield.select();

  });




}(jQuery));