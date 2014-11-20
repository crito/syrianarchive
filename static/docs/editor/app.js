(function($){
jQuery(document).ready(function() {

  /*

$('.editable').hallo({
  plugins: {
    'halloformat': {'formattings': {"bold": true, "italic": true, "strikethrough": true, "underline": true},},
    'halloheadings': {'headings': [1,2,3,4,5],},
    'hallolists': {},
    'halloreundo': {},
    'hallolink': {},
    'halloimage': {
        'searchUrl' : '/find/images',
    },
  },

});

$('.pagetitle').hallo({
  plugins: {

  },

});




*/



  var options = {
    editor: document.getElementById('documenteditor'),
    debug: true,
    class: 'pen',
    textarea: '<textarea name="content"></textarea>',
    list: [
      'blockquote', 'h2', 'h3', 'p', 'insertorderedlist', 'insertunorderedlist', 'inserthorizontalrule',
      'indent', 'outdent', 'bold', 'italic', 'underline', 'createlink', 'insertimage'
    ],
    stay: true

  };

  // create editor
  var pen = new Pen(options);

var form = $("#documentform");
var form2 = $("#uploadform");


function isInArray(value, array) {
  return array.indexOf(value) > -1;
}


  var savedocument = function(){

      var mddescription = markdownize($('#documenteditor').html());

      $("#documentform #id_name").attr('value',  $('#pagetitle').html());
      $("#id_description").html(mddescription);
      $("#id_comment").attr('value', $("#tempvalue").val());

      var selectgroupchoices = $("#selectgroups").select2('val');

      $('#selectgroups option').each(function(){
        console.log($(this).attr('value'));
        if(isInArray($(this).attr('value'), selectgroupchoices)){
          $(this).attr('selected', true);
        }else{
          $(this).attr('selected', false);
        }
      });

      $("#selectgroups").select2('val', $("#selectgroups").select2('val'));
      console.log($("#selectgroups").select2('val'));



      $("#id_groups").html($("#selectgroups").html());

      //start ajax
      $.ajax({
          url:form.attr('action'),
          type:'post',
          data: form.serializeArray(),
          success: function(responseText, responseStatus) {
              // After ajax success, make the form submittable again

              // After adding the entry via ajax, select and focus the 'task' field again
              console.log(form.html());
              $('.bottom-right').notify({
                message: { text: 'Saved!' }
              }).show(); 

              pen.rebuild();

          },
          error: function(responseText, responseStatus){
            $('.bottom-right').notify({
                message: { text: 'Somethin GOOFED' + responseText, type:'bs-callout-danger' }
              }).show(); 
          }
      });
      // end ajax
  }





  var markdownize = function(content) {
    var html = content.split("\n").map($.trim).filter(function(line) { 
      return line != "";
    }).join("\n");

    html = $.trim(html).replace(/\s*[\r\n]+\s*/g, '\n').replace(/(<[^\/][^>]*>)\s*/g, '$1').replace(/\s*(<\/[^>]+>)/g, '$1');

    return toMarkdown(html);
  };



  var converter = new Showdown.converter();
  var htmlize = function(content) {
    return converter.makeHtml(content);
  };





$('.documentcontent').html(htmlize($('.documentcontent').html()));



$('.savedocument').click(function(e){
  savedocument();
  e.preventDefault(); 
});





$('.uploadfile').click(function(e){
  $("#uploadmodal").modal("show");
  e.preventDefault(); 
});


$('#uploaddoc').click(function(e){

            console.log(form2.serializeArray());

            var daaata = new FormData(form2[0]);
            
            console.log(daaata);
  $.ajax({
          url:form2.attr('action'),
          type:'post',
          processData: false, 
          contentType: false,
          enctype: "multipart/form-data",
          data: daaata,
          success: function(responseText, responseStatus) {
              // After ajax success, make the form submittable again

              // After adding the entry via ajax, select and focus the 'task' field again

              $('.bottom-right').notify({
                message: { text: 'Added New file!' }
              }).show(); 

              $("#uploadmodal").modal("hide");

              $("#attachedfiles").load($("#attachedfiles").attr('data-load-url'));


          },
          error: function(responseText, responseStatus){

            $('.bottom-right').notify({
                message: { text: 'Somethin GOOFED', type:'bs-callout-danger' }
              }).show(); 
          }
      });


  e.preventDefault(); 
});









});
}(jQuery));