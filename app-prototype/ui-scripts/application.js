/**
 * Created by Mensur Đogić on 11.08.14..
 * Enter your magic here!
 */

window.onload = function() {
  var ngui = require("nw.gui");
    var nwin =ngui.Window.get();
/* Enabling developer tools, comment if you don't need it! */    
var nwin_dev = ngui.Window.get().showDevTools();
    nwin.show();
    nwin_dev.show();


}
