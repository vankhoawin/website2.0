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
    var index = source.charAt(12);

    $('#language-header').css("opacity", "100").html(languages[index]);

  }).mouseout(function(){
    $('#language-header').css("opacity", "0");
  });


  var softwares = [('Flask'), ('Eclipse'), ('PyCharm'), ('Git'),
                 ('Adobe Photoshop'), ('Adobe Lightroom'), ('Windows'), ('Ubuntu')];

  $('.software-hover').mouseover(function(){
    var source = $(this).attr('id');
    var index = source.charAt(12);

    $('#software-header').css("opacity", "100").html(softwares[index]);

  }).mouseout(function(){
    $('#software-header').css("opacity", "0");
  });

});