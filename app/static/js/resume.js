$(document).ready(function() {
  $('.col-sm-4').click(function(){
    if ($(this).hasClass("active")) {
      $(this).removeClass('active');
    }else {
      $(this).addClass("active");
      $(this).siblings('div').removeClass('active');
    }
  });
});