// metrika
//(function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
//   m[i].l=1*new Date();k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)})
//   (window, document, "script", "https://mc.yandex.ru/metrika/tag.js", "ym");
//
//   ym(69855739, "init", {
//        clickmap:true,
//        trackLinks:true,
//        accurateTrackBounce:true,
//        trackHash:true
//   });

// LiveInternet
new Image().src = "https://counter.yadro.ru/hit?r"+
escape(document.referrer)+((typeof(screen)=="undefined")?"":
";s"+screen.width+"*"+screen.height+"*"+(screen.colorDepth?
screen.colorDepth:screen.pixelDepth))+";u"+escape(document.URL)+
";h"+escape(document.title.substring(0,150))+
";"+Math.random();
