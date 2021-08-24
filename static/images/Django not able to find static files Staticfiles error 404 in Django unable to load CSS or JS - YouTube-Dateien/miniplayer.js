(function(g){var window=this;'use strict';var A6=function(a){g.V.call(this,{D:"div",K:"ytp-miniplayer-ui"});this.hg=!1;this.player=a;this.N(a,"minimized",this.rg);this.N(a,"onStateChange",this.gF)},B6=function(a){g.pN.call(this,a);
this.i=new A6(this.player);this.i.hide();g.eN(this.player,this.i.element,4);a.Fe()&&(this.load(),g.N(a.getRootNode(),"ytp-player-minimized",!0))};
g.w(A6,g.V);g.k=A6.prototype;
g.k.pD=function(){this.tooltip=new g.MQ(this.player,this);g.J(this,this.tooltip);g.eN(this.player,this.tooltip.element,4);this.tooltip.scale=.6;this.qc=new g.kO(this.player);g.J(this,this.qc);this.Ag=new g.V({D:"div",K:"ytp-miniplayer-scrim"});g.J(this,this.Ag);this.Ag.Ba(this.element);this.N(this.Ag.element,"click",this.gz);var a=new g.V({D:"button",Fa:["ytp-miniplayer-close-button","ytp-button"],V:{"aria-label":"Schlie\u00dfen"},S:[g.pL()]});g.J(this,a);a.Ba(this.Ag.element);this.N(a.element,"click",
this.Ci);a=new g.W1(this.player,this);g.J(this,a);a.Ba(this.Ag.element);this.Xo=new g.V({D:"div",K:"ytp-miniplayer-controls"});g.J(this,this.Xo);this.Xo.Ba(this.Ag.element);this.N(this.Xo.element,"click",this.gz);var b=new g.V({D:"div",K:"ytp-miniplayer-button-container"});g.J(this,b);b.Ba(this.Xo.element);a=new g.V({D:"div",K:"ytp-miniplayer-play-button-container"});g.J(this,a);a.Ba(this.Xo.element);var c=new g.V({D:"div",K:"ytp-miniplayer-button-container"});g.J(this,c);c.Ba(this.Xo.element);this.zL=
new g.IP(this.player,this,!1);g.J(this,this.zL);this.zL.Ba(b.element);b=new g.FP(this.player,this);g.J(this,b);b.Ba(a.element);this.nextButton=new g.IP(this.player,this,!0);g.J(this,this.nextButton);this.nextButton.Ba(c.element);this.Dg=new g.zQ(this.player,this);g.J(this,this.Dg);this.Dg.Ba(this.Ag.element);this.Mc=new g.NP(this.player,this);g.J(this,this.Mc);g.eN(this.player,this.Mc.element,4);this.Sy=new g.V({D:"div",K:"ytp-miniplayer-buttons"});g.J(this,this.Sy);g.eN(this.player,this.Sy.element,
4);a=new g.V({D:"button",Fa:["ytp-miniplayer-close-button","ytp-button"],V:{"aria-label":"Schlie\u00dfen"},S:[g.pL()]});g.J(this,a);a.Ba(this.Sy.element);this.N(a.element,"click",this.Ci);a=new g.V({D:"button",Fa:["ytp-miniplayer-replay-button","ytp-button"],V:{"aria-label":"Schlie\u00dfen"},S:[g.uL()]});g.J(this,a);a.Ba(this.Sy.element);this.N(a.element,"click",this.lU);this.N(this.player,"presentingplayerstatechange",this.Lc);this.N(this.player,"appresize",this.xb);this.N(this.player,"fullscreentoggled",
this.xb);this.xb()};
g.k.show=function(){this.Bd=new g.Cq(this.Op,null,this);this.Bd.start();this.hg||(this.pD(),this.hg=!0);0!==this.player.getPlayerState()&&g.V.prototype.show.call(this);this.Mc.show();this.player.unloadModule("annotations_module")};
g.k.hide=function(){this.Bd&&(this.Bd.dispose(),this.Bd=void 0);g.V.prototype.hide.call(this);this.player.Fe()||(this.hg&&this.Mc.hide(),this.player.loadModule("annotations_module"))};
g.k.va=function(){this.Bd&&(this.Bd.dispose(),this.Bd=void 0);g.V.prototype.va.call(this)};
g.k.Ci=function(){this.player.stopVideo();this.player.Na("onCloseMiniplayer")};
g.k.lU=function(){this.player.playVideo()};
g.k.gz=function(a){if(a.target===this.Ag.element||a.target===this.Xo.element)g.T(this.player.T().experiments,"kevlar_miniplayer_play_pause_on_scrim")?g.sK(this.player.vb())?this.player.pauseVideo():this.player.playVideo():this.player.Na("onExpandMiniplayer")};
g.k.rg=function(){g.N(this.player.getRootNode(),"ytp-player-minimized",this.player.Fe())};
g.k.kd=function(){this.Mc.Tb();this.Dg.Tb()};
g.k.Op=function(){this.kd();this.Bd&&this.Bd.start()};
g.k.Lc=function(a){g.U(a.state,32)&&this.tooltip.hide()};
g.k.xb=function(){g.ZP(this.Mc,0,this.player.Za().getPlayerSize().width,!1);g.QP(this.Mc)};
g.k.gF=function(a){this.player.Fe()&&(0===a?this.hide():this.show())};
g.k.hc=function(){return this.tooltip};
g.k.Pe=function(){return!1};
g.k.nf=function(){return!1};
g.k.ri=function(){return!1};
g.k.Oz=function(){};
g.k.Pm=function(){};
g.k.yr=function(){};
g.k.jn=function(){return null};
g.k.ij=function(){return new g.nl(0,0,0,0)};
g.k.handleGlobalKeyDown=function(){return!1};
g.k.handleGlobalKeyUp=function(){return!1};
g.k.Wp=function(a,b,c,d,e){var f=0,h=d=0,l=g.Jl(a);if(b){c=g.Mq(b,"ytp-prev-button")||g.Mq(b,"ytp-next-button");var m=g.Mq(b,"ytp-play-button"),n=g.Mq(b,"ytp-miniplayer-expand-watch-page-button");c?f=h=12:m?(b=g.Hl(b,this.element),h=b.x,f=b.y-12):n&&(h=g.Mq(b,"ytp-miniplayer-button-top-left"),f=g.Hl(b,this.element),b=g.Jl(b),h?(h=8,f=f.y+40):(h=f.x-l.width+b.width,f=f.y-20))}else h=c-l.width/2,d=25+(e||0);b=this.player.Za().getPlayerSize().width;e=f+(e||0);l=g.Of(h,0,b-l.width);e?(a.style.top=e+"px",
a.style.bottom=""):(a.style.top="",a.style.bottom=d+"px");a.style.left=l+"px"};
g.k.showControls=function(){};
g.k.Vk=function(){};
g.k.yk=function(){return!1};g.w(B6,g.pN);B6.prototype.create=function(){};
B6.prototype.Mi=function(){return!1};
B6.prototype.load=function(){this.player.hideControls();this.i.show()};
B6.prototype.unload=function(){this.player.showControls();this.i.hide()};g.AN.miniplayer=B6;})(_yt_player);
