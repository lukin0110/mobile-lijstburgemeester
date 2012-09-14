/**
 * Created with PyCharm.
 * User: maarten
 * Date: 9/10/12
 * Time: 11:24 PM
 * To change this template use File | Settings | File Templates.
 */

var Fx = {};

Fx.showLoading = function() {

};

Fx.hideLoading = function() {

};

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
/*
$.address.state("/").init(function(event){
    console.log("init");
    $("a").address();
}).change(function(event){
    console.log("change = " + event.value);
});
*/


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