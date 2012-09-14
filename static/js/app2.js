var C = {};
C.loaded = false;

var Fx = {};

Fx.showLoading = function() {
    $("#loading").fadeIn(200);
    return true;
};

Fx.hideLoading = function() {
    $("#loading").fadeOut(200);
};


var IO = {};

IO.load = function(url) {
    var _url = url.replace("#!", "");
    Fx.showLoading();
    $.ajax({
        url: _url,
        data: {'ajax':'true'},
        success: function(data){
            //alert(data);
            $("#container").html(data);
            IO.attach();
            window.scrollTo(0, 0);
            Fx.hideLoading();
        }
    });
};


/**
 * All links will redirect
 */
IO.attach = function(){
    $("a[ajax='true']").each(function(index, element){
        if(!element["_hashed"]) {
            element["_hashed"] = true;
            $(element).click(function(){
                var href = $(this).attr("href");
                App.log("Attach = " + href);
                window.location = "#!" + href;
                IO.load(href);
                return false;
            });
        }
    });
};




var App = {};

App.log = function(msg) {
    if (window["console"]) {
        console.log(msg);
    }
};

App.fixTop = function(){

};

App.init = function() {
    Fx.hideLoading();

    /**
     * Hide the navigation bar
     *
     * http://davidwalsh.name/hide-address-bar
     * http://24ways.org/2011/raising-the-bar-on-mobile
     * http://stackoverflow.com/questions/6011223/how-to-completely-hide-the-navigation-bar-in-iphone-html-5
     */
    window.addEventListener("load",function() {
        // Set a timeout...
        setTimeout(function(){
            // Hide the address bar!
            window.scrollTo(0, 0);
        }, 0);
        //IO.load(window.location.hash);
    });

    /**
     * Listen to the hashchange event
     */
    window.addEventListener("hashchange", function(){
        App.log("hahs = " + window.location.hash);
        //IO.load(window.location.hash);
    });

    // detect if it exists
    /*
     if ("onhashchange" in window) {
     alert("The browser supports the hashchange event!");
     }*/

    //IO.attach();
};

//Auto init of this script
App.init();
