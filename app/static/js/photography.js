$(document).ready(function() {


    $.ajax({
        type: "GET",
        url: "https://api.flickr.com/services/rest/?method=flickr.photosets.getList&api_key=55ce2a1b84747661aef66370d520bfdf&user_id=126052905%40N03&format=json&nojsoncallback=1&auth_token=72157645975684012-4b2ff1d6584f1228&api_sig=9c8d65a922776ae61d830ea222fe0380",
        cache: true,
        beforeSend: function(x) {
          if(x && x.overrideMimeType) {
            x.overrideMimeType("application/j-son;charset=UTF-8");
          }
    },
    dataType: "json",
    success: function(data){
        console.log(data);
        var result = data['photosets']['photoset'];

        var picture_sidebar = "<li><a href='#'>Handpicked</a></li>";
        for (i=0; i<result.length; ++i) {
            var title = result[i]['title']['_content'];

//            console.log(title + ", " + result[i].id);
            picture_sidebar += "<li><a href='#'>" + title + "</a></li>"
        }

        $('#picture-sidebar').html(picture_sidebar);
    }}),

    $.ajax({
        type: "GET",
        url: "https://api.flickr.com/services/rest/?method=flickr.photosets.getPhotos&api_key=55ce2a1b84747661aef66370d520bfdf&photoset_id=72157645615204052+&format=json&nojsoncallback=1&auth_token=72157645975684012-4b2ff1d6584f1228&api_sig=de1d9c72df552f42feb1d85fa1da7e97",
        cache: true,

    dataType: "json",
    success: function(data){
        var result = data['photoset']['photo'];
        var picture_body = "";

        for (i=0; i<result.length; ++i) {
            var photo = result[i]['id'];

            $.ajax({
                type: "GET",
                url: "https://api.flickr.com/services/rest/?method=flickr.photos.getSizes&api_key=55ce2a1b84747661aef66370d520bfdf&photo_id=" + photo + "&format=json&nojsoncallback=1",
                async: false,
                cache: true,

            dataType: "json",
            success: function(photoJSON){
                var photo_jpg = photoJSON['sizes']['size'][5]['source'];
                picture_body += "<img src=" + photo_jpg + ">";
            }});

        $('#picture-body').html(picture_body);
        }
    }});
});