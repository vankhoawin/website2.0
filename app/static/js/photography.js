$(document).ready(function() {


    $.ajax({
         type: "GET",
         url: "https://api.flickr.com/services/rest/?&method=flickr.photosets.getList&api_key=aa97f39fc7ff944178ebd92711b9ab35&user_id=126052905@N03",
         async: false,
         cache: true,
         beforeSend: function(x) {
          if(x && x.overrideMimeType) {
           x.overrideMimeType("application/j-son;charset=UTF-8");
          }
     },
     dataType: "xml",
     success: function(data){
         var result = data.getElementsByTagName("rsp")[0].getElementsByTagName("photoset");


         var picture_sidebar = "<li><a href='#'>Handpicked</a></li>";
         for (i=0; i<result.length; ++i) {
             var title = result[i].getElementsByTagName("title")[0].textContent;

             console.log(title + ", " + result[i].id);
             picture_sidebar += "<li><a href='#'>" + title + "</a></li>"
         }

         $('#picture-sidebar').html(picture_sidebar);
     }



    });



});