/**
Script: Slideshow.Fold.js
	Slideshow.Fold - Flash extension for Slideshow.

License:
	MIT-style license.

Copyright:
	Copyright (c) 2008 [Aeron Glemann](http://www.electricprism.com/aeron/).

Dependencies:
	Slideshow.
*/
Slideshow.Fold=new Class({Extends:Slideshow,_show:function(b){if(!this.image.retrieve("tween")){var c=(this.options.overlap)?{duration:this.options.duration}:{duration:this.options.duration/2};$$(this.a,this.b).set("tween",Object.merge(c,{link:"chain",onStart:this._start.bind(this),onComplete:this._complete.bind(this),property:"clip",transition:this.options.transition}))}var a=(this.counter%2)?this.a:this.b,e=this._rect(this.image),f=Math.ceil(e.top+(e.bottom-e.top)/2);if(b){a.get("tween").cancel().set("rect(0, 0, 0, 0)");this.image.get("tween").cancel().set("rect(auto, auto, auto, auto)")}else{if(this.options.overlap){a.get("tween").set("rect(auto, auto, auto, auto)");this.image.get("tween").set(e.top+" "+e.left+" "+f+" "+e.left).start(e.top+" "+e.right+" "+f+" "+e.left).start(e.top+" "+e.right+" "+e.bottom+" "+e.left)}else{var d=function(g){this.image.get("tween").set(g.top+" "+g.left+" "+f+" "+g.left).start(g.top+" "+g.right+" "+f+" "+g.left).start(g.top+" "+g.right+" "+g.bottom+" "+g.left)}.pass(e,this);if(this.firstrun){return d()}e=this._rect(a);a.get("tween").set(e.top+" "+e.right+" "+e.bottom+" "+e.left).start(e.top+" "+e.right+" "+f+" "+e.left).start(e.top+" "+e.left+" "+f+" "+e.left).chain(d)}}},_rect:function(a){var b=a.getCoordinates(this.el.retrieve("images"));b.left=(b.left<0)?Math.abs(b.left):0;b.top=(b.top<0)?Math.abs(b.top):0;b.right=(b.right>this.width)?b.left+this.width:b.width;b.bottom=(b.bottom>this.height)?b.top+this.height:b.height;return b}});