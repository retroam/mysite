
window.log=function(){log.history=log.history||[];log.history.push(arguments);arguments.callee=arguments.callee.caller;if(this.console)console.log(Array.prototype.slice.call(arguments));};(function(b){function c(){}for(var d="assert,count,debug,dir,dirxml,error,exception,group,groupCollapsed,groupEnd,info,log,markTimeline,profile,profileEnd,time,timeEnd,trace,warn".split(","),a;a=d.pop();)b[a]=b[a]||c})(window.console=window.console||{});!function(){var MIN_WORD=6;var tag_blacklist={'code':true,'pre':true,'abbr':true}
function justify_my_love(el){var nodes=el.childNodes;for(var i=0;i<nodes.length;i++){var node=nodes[i];switch(node.nodeType){case 3:node.nodeValue=break_dance(node.nodeValue);break;case 1:if(!tag_blacklist[node.nodeName.toLowerCase()]&&node.className.indexOf('justice-denied')===-1){justify_my_love(node);}
break;}}}
var whitespace=/[ \s\n\r\v\t]+/;function break_dance(text){var words=text.split(whitespace);for(var i=0;i<words.length;i++){if(breakable(words[i])){words[i]=break_word_en(words[i]);}}
return words.join(' ');}
function breakable(word){return(/\w{6,}/.test(word))&&(!/^[0-9\&]|@|\-|\u00AD/.test(word));}
var vowels='aeiouyAEIOUY'+'ẚÁáÀàĂăẮắẰằẴẵẲẳÂâẤấẦầẪẫẨẩǍǎÅåǺǻÄäǞǟÃãȦȧǠǡĄąĀāẢảȀȁȂȃẠạẶặẬậḀḁȺⱥ'+'ǼǽǢǣÉƏƎǝéÈèĔĕÊêẾếỀềỄễỂểĚěËëẼẽĖėȨȩḜḝĘęĒēḖḗḔḕẺẻȄȅȆȇẸẹỆệḘḙḚḛɆɇɚɝÍíÌìĬĭÎîǏǐÏ'+'ïḮḯĨĩİiĮįĪīỈỉȈȉȊȋỊịḬḭIıƗɨÓóÒòŎŏÔôỐốỒồỖỗỔổǑǒÖöȪȫŐőÕõṌṍṎṏȬȭȮȯȰȱØøǾǿǪǫǬǭŌōṒṓ'+'ṐṑỎỏȌȍȎȏƠơỚớỜờỠỡỞởỢợỌọỘộƟɵÚúÙùŬŭÛûǓǔŮůÜüǗǘǛǜǙǚǕǖŰűŨũṸṹŲųŪūṺṻỦủȔȕȖȗƯưỨứỪừ'+'ỮữỬửỰựỤụṲṳṶṷṴṵɄʉÝýỲỳŶŷY̊ẙŸÿỸỹẎẏȲȳỶỷỴỵʏɎɏƳƴ';var c='[^'+vowels+']';var v='['+vowels+']';var vccv=new RegExp('('+v+c+')('+c+v+')','g');var simple=new RegExp('(.{2,4}'+v+')'+'('+c+')','g');var dumb=/\u00AD(.?)|$\u00AD(.{0,2}\w+)$/;function break_word_default(word){return word.replace(vccv,'$1\u00AD$2').replace(simple,'$1\u00AD$2').replace(dumb,'$1');}
var presuf=/^(\W*)(anti|auto|ab|an|ax|al|as|bi|bet|be|contra|cat|cath|cir|cum|cog|col|com|con|cor|could|co|desk|de|dis|did|dif|di|eas|every|ever|extra|ex|end|en|em|epi|evi|func|fund|fin|hyst|hy|han|il|in|im|ir|just|jus|loc|lig|lit|li|mech|manu|man|mal|mis|mid|mono|multi|mem|micro|non|nano|ob|oc|of|opt|op|over|para|per|post|pre|peo|pro|retro|rea|re|rhy|should|some|semi|sen|sol|sub|suc|suf|super|sup|sur|sus|syn|sym|syl|tech|trans|tri|typo|type|uni|un|van|vert|with|would|won)?(.*?)(weens?|widths?|icals?|ables?|ings?|tions?|ions?|ies|isms?|ists?|ful|ness|ments?|ly|ify|ize|ise|ity|en|ers?|ences?|tures?|ples?|als?|phy|puts?|phies|ry|ries|cy|cies|mums?|ous|cents?)?(\W*)$/i;function break_word_en(word){var parts=presuf.exec(word);var ret=[];if(parts[2]){ret.push(parts[2]);}
if(parts[3]){ret.push(parts[3].replace(vccv,'$1\u00AD$2'));}
if(parts[4]){ret.push(parts[4]);}
return(parts[1]||'')+ret.join('\u00AD')+(parts[5]||'');}
function copy_protect(e){var body=document.getElementsByTagName('body')[0];var shyphen=/(?:\u00AD|\&#173;|\&shy;)/g;var shadow=document.createElement('div');shadow.style.overflow='hidden';shadow.style.position='absolute';shadow.style.top='-5000px';shadow.style.height='1px';body.appendChild(shadow);if(typeof window.getSelection!=='undefined'){sel=window.getSelection();var range=sel.getRangeAt(0);shadow.appendChild(range.cloneContents());shadow.innerHTML=shadow.innerHTML.replace(shyphen,'');sel.selectAllChildren(shadow);window.setTimeout(function(){shadow.parentNode.removeChild(shadow);if(typeof window.getSelection().setBaseAndExtent!=='undefined'){sel.setBaseAndExtent(range.startContainer,range.startOffset,range.endContainer,range.endOffset);}},0);}else{sel=document.selection;var range=sel.createRange();shadow.innerHTML=range.htmlText.replace(shyphen,'');var range2=body.createTextRange();range2.moveToElementText(shadow);range2.select();window.setTimeout(function(){shadow.parentNode.removeChild(shadow);if(range.text!==''){range.select();}},0);}
return;}
function sweet_justice_jq(){jQuery('.sweet-justice, .sweet-hyphens').each(function(idx,el){justify_my_love(el);});jQuery('body').bind('copy',copy_protect);}
function sweet_justice_yui(Y){Y.all('.sweet-justice, .sweet-hyphens').each(function(el){justify_my_love(Y.Node.getDOMNode(el));});Y.Node.DOM_EVENTS.copy=1;Y.one('body').on('copy',copy_protect);}
try{var style=document.createElement('style');style.type='text/css';var css='.sweet-justice {text-align:justify;text-justify:distribute} '+'.justice-denied {text-align:left;text-justify:normal}';if(!!(window.attachEvent&&!window.opera)){style.styleSheet.cssText=css;}else{style.appendChild(document.createTextNode(css));}
document.getElementsByTagName('head')[0].appendChild(style);}catch(e){}
if(window.jQuery){jQuery(window).load(sweet_justice_jq);}else if(window.YUI){YUI().use('node',function(Y){sweet_justice_yui(Y);});}}();(function($){$.timeago=function(timestamp){if(timestamp instanceof Date){return inWords(timestamp);}else if(typeof timestamp==="string"){return inWords($.timeago.parse(timestamp));}else{return inWords($.timeago.datetime(timestamp));}};var $t=$.timeago;$.extend($.timeago,{settings:{refreshMillis:60000,allowFuture:false,strings:{prefixAgo:null,prefixFromNow:null,suffixAgo:"ago",suffixFromNow:"from now",seconds:"less than a minute",minute:"about a minute",minutes:"%d minutes",hour:"about an hour",hours:"about %d hours",day:"a day",days:"%d days",month:"about a month",months:"%d months",year:"about a year",years:"%d years",numbers:[]}},inWords:function(distanceMillis){var $l=this.settings.strings;var prefix=$l.prefixAgo;var suffix=$l.suffixAgo;if(this.settings.allowFuture){if(distanceMillis<0){prefix=$l.prefixFromNow;suffix=$l.suffixFromNow;}
distanceMillis=Math.abs(distanceMillis);}
var seconds=distanceMillis/1000;var minutes=seconds/60;var hours=minutes/60;var days=hours/24;var years=days/365;function substitute(stringOrFunction,number){var string=$.isFunction(stringOrFunction)?stringOrFunction(number,distanceMillis):stringOrFunction;var value=($l.numbers&&$l.numbers[number])||number;return string.replace(/%d/i,value);}
var words=seconds<45&&substitute($l.seconds,Math.round(seconds))||seconds<90&&substitute($l.minute,1)||minutes<45&&substitute($l.minutes,Math.round(minutes))||minutes<90&&substitute($l.hour,1)||hours<24&&substitute($l.hours,Math.round(hours))||hours<48&&substitute($l.day,1)||days<30&&substitute($l.days,Math.floor(days))||days<60&&substitute($l.month,1)||days<365&&substitute($l.months,Math.floor(days/30))||years<2&&substitute($l.year,1)||substitute($l.years,Math.floor(years));return $.trim([prefix,words,suffix].join(" "));},parse:function(iso8601){var s=$.trim(iso8601);s=s.replace(/\.\d\d\d+/,"");s=s.replace(/-/,"/").replace(/-/,"/");s=s.replace(/T/," ").replace(/Z/," UTC");s=s.replace(/([\+\-]\d\d)\:?(\d\d)/," $1$2");return new Date(s);},datetime:function(elem){var isTime=$(elem).get(0).tagName.toLowerCase()==="time";var iso8601=isTime?$(elem).attr("datetime"):$(elem).attr("title");return $t.parse(iso8601);}});$.fn.timeago=function(){var self=this;self.each(refresh);var $s=$t.settings;if($s.refreshMillis>0){setInterval(function(){self.each(refresh);},$s.refreshMillis);}
return self;};function refresh(){var data=prepareData(this);if(!isNaN(data.datetime)){$(this).text(inWords(data.datetime));}
return this;}
function prepareData(element){element=$(element);if(!element.data("timeago")){element.data("timeago",{datetime:$t.datetime(element)});var text=$.trim(element.text());if(text.length>0){element.attr("title",text);}}
return element.data("timeago");}
function inWords(date){return $t.inWords(distance(date));}
function distance(date){return(new Date().getTime()-date.getTime());}
document.createElement("abbr");document.createElement("time");}(jQuery));