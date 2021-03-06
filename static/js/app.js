var Fx = {};

Fx.showLoading = function() {
    $("#loading").fadeIn(200);
    return true;
};

Fx.hideLoading = function() {
    $("#loading").fadeOut(200);
};


var App = {};

App.log = function(msg) {
    if (window["console"]) {
        console.log(msg);
    }
};

App.history = function() {
    var hash = window.location.hash;
    var path = window.location.pathname;

    if(path === "/waarom"){
        if(hash){
            window.location = '/waarom';
        } else {
            window.location = "/";
        }
    } else if(path === "/wie/") {
        window.location = "/";
    } else {
        history.go(-1);
    }

    //App.log("1 = " + hash + ", " + window.location.pathname);
    //App.log("2 = " + (hash ? "rr" : "tt"));
    //history.go(-1);
};

/**
 * /s/img/persons/youth
 * /s/img/persons/poster
 *
 * @param base
 */
App.preload = function(base) {
    $(document).ready(function(){
        for(var i=0;i<31;i++){
            var tmp = new Image();
            tmp.src = base + "/" + (i+1) + ".jpg";
        }
    });
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


    $("a[loading='true']").each(function(index, element){
        if ($(element).attr("href").indexOf("#") === -1) {
            $(element).click(function(){
                Fx.showLoading();
                setTimeout(function(){Fx.hideLoading()}, 1000);
            });
        }
    });
};

//Auto init of this script
App.init();
