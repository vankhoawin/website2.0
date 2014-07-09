$(document).ready(function() {
  $('.slider').click(function(){
    if ($(this).hasClass("active")) {
      $(this).removeClass('active');
    }else {
      $(this).addClass("active");
      $(this).siblings('div').removeClass('active');
    }
  });
/*
  $('#resume-languages-icons img').hover(function(){
      $(this).siblings('div').removeClass('active');
    }
  });

    -webkit-filter: blur(5px);
    */


    var languages = [('Python - Proficient'), ('C++ - Proficient'), ('Java - Familiar'), ('SQL - Familiar'),
                 ('HTML5 - Proficient'), ('CSS3 - Proficient'), ('Javascript - Familiar'), ('PHP - Rudimentary')];

  $('.language-hover').mouseover(function(){
    var source = $(this).attr('id');
    var index = source.charAt(4);
//    console.log($('#language-header').html());
    $('#language-header').html(languages[index]);
  });

});