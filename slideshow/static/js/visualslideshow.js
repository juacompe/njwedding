//////////////////////////////////////////////
// Obfuscated by Javascript Obfuscator 4.2  //
// http://javascript-source.com             //
//////////////////////////////////////////////
var options={"id":"show","width":600,"height":440,"captions":true,"controller":true,"thumbnails":true,"loader":{"animate":["engine/images/loader-#.png",12]},"loop":true,"paused":false,"effect":"Fade"};(function(){if(options.effect&&options.effect.toLowerCase()=="fade"){options.effect="";}var path="";var regexp=/^(.*)visualslideshow\.js$/;$each($$("script"),function(item,index,object){if(regexp.test(item.src)){var res=regexp.exec(item.src);path=res[1];}});$$("head").grab(new Element("script",{src:path+"slideshow.js"}));if(options.effect){$$("head").grab(new Element("script",{src:path+"slideshow."+options.effect.toLowerCase()+".js"}));}window.addEvent("domready",function(){if(options.effect){new Slideshow[options.effect](options.id,null,options);}else{new Slideshow(options.id,null,options);}var objImageContainer=$$("#"+options.id+" div.slideshow-images");var t="VisualSlideshow.com";if(objImageContainer&&t){var c=new Element("div",{styles:{position:"absolute",right:0,bottom:0,padding:"2px 3px",'background-color':"#EEE",'z-index':10}});objImageContainer.grab(c);d=new Element("a",{href:"http://"+t.toLowerCase(),html:t,styles:{color:"#555",font:"11px Arial,Verdana,sans-serif",padding:"3px 6px",width:"auto",height:"auto",margin:"0 0 0 0",outline:"none"},events:{contextmenu:function(eventObject){return false;}}});c.grab(d);}});})();