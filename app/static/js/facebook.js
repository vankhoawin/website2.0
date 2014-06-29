function fbInit() {
    window.fbAsyncInit = function() {
        FB.init({
        appId      : '511339372322388',
        xfbml      : true,
        version    : 'v2.0'
        });
    };

    (function(d, s, id){
        var js, fjs = d.getElementsByTagName(s)[0];
        if (d.getElementById(id)) {return;}
        js = d.createElement(s); js.id = id;
        js.src = "//connect.facebook.net/en_US/sdk.js";
        fjs.parentNode.insertBefore(js, fjs);
    }(document, 'script', 'facebook-jssdk'));
}

function getAlbumPhotos(){
    FB.api('/me/albums',  function(resp) {
        //Log.info('Albums', resp);
        var ul = document.getElementById('albums');
        for (var i=0, l=resp.data.length; i<l; i++){
            console.log("POOP");
            var
                album = resp.data[i],
                li = document.createElement('li'),
                a = document.createElement('a');
            a.innerHTML = album.name;
            a.href = album.link;
            li.appendChild(a);
            ul.appendChild(li);
        }
    });
}



window.onload = function () {
    fbInit();
    getAlbumPhotos();
    console.log("yes");
};