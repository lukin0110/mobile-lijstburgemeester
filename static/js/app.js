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
