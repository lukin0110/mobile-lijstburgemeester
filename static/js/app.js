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


var App = {};

App.init = function() {
    Fx.hideLoading();
};

//Auto init of this script
App.init();


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
});




/**
 * Deep linking, and invoking ajax
 */
$.address.state("/").init(function(event)
{
    console.log("init");
    $("a").address();

}).change(function(event)
{
    console.log("change = " + event.value + ", " + window.location.pathname);

    if(C.loaded) {
        Fx.showLoading();
        $.get(event.value, {'ajax':'true'}, function(data){
            $('#container').html(data);
            Fx.hideLoading();
        }, "html");
    } else {
        C.loaded = true;
    }
});



/*
 $.address.change(function(event){

 console.log("Hello buddy = " + event.value + ", " + event.path);
 });
 */

/*
 $.address.state('/jquery/address/samples/express').init(function(event) {

 // Initializes the plugin
 $('.nav a').address();

 }).change(function(event) {

 var value = $.address.state().replace(/^\/$/, '') + event.value;

 // Selects the proper navigation link
 $('.nav a').each(function() {
 if ($(this).attr('href') == value) {
 $(this).addClass('selected').focus();
 } else {
 $(this).removeClass('selected');
 }
 });

 if (state && init) {

 init = false;

 } else {

 // Loads and populates the page data
 $.ajax({
 cache: false,
 complete: handler,
 url: value
 });
 }
                */