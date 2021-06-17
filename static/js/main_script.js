const sliders = document.querySelector('.swiper-container');
const slidersMain = document.querySelector('.swiper-container-main');
const slidersExrta = document.querySelector('.swiper-container-extra');

/* Swiper №1 */
var mySwiper = new Swiper(sliders, {
  speed: 400,
  slidesPerView: 1,
  spaceBetween: 10,
  setWrapperSize: true,
  preloadImages: false,
  lazy: true,
  pagination: {
    el: '.swiper-pagination',
    type: 'bullets',
    clickable: true,
    renderBullet: function (index, className) {
          return '<span class="' + className + '">' + (index + 1) + '</span>';
        },
  },
  lazy: {
    loadPrevNext: true,
  },
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  zoom: {
    maxRatio: 2,
  },
})

/* Swiper №2 */
var mySwiperMain = new Swiper(slidersMain, {
  loop: true,
  speed: 400,
  slidesPerView: 2,
  spaceBetween: 10,
  setWrapperSize: true,
  preloadImages: false,
  lazy: true,
  breakpoints: {
    640: {
      slidesPerView: 3,
      spaceBetween: 10
    }
  },
  pagination: {
    el: '.swiper-pagination',
    type: 'bullets',
    clickable: true,
    dynamicBullets: true,
    renderBullet: function (index, className) {
          return '<span class="' + className + '">' + (index + 1) + '</span>';
        },
  },
  lazy: {
    loadPrevNext: true,
  },
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
   autoplay: {
     delay: 3000,
     disableOnInteraction: false,
   },
})

/* Swiper №3 extra */
var mySwiper = new Swiper(slidersExrta, {
  speed: 400,
  slidesPerView: 1,
  spaceBetween: 10,
  setWrapperSize: true,
  preloadImages: false,
  lazy: true,
  pagination: {
    el: '.swiper-pagination',
    type: 'bullets',
    clickable: true,
    dynamicBullets: true,
    renderBullet: function (index, className) {
          return '<span class="' + className + '">' + (index + 1) + '</span>';
        },
  },
  lazy: {
    loadPrevNext: true,
  },
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  zoom: {
    maxRatio: 3,
  },
})

/* menu icon animations */

$(document).ready(function () {

  $('.first-button').on('click', function () {

    $('.animated-icon1').toggleClass('open');
  });
});


/* lazyloadImages */
document.addEventListener("DOMContentLoaded", function() {
  var lazyloadImages;    

  if ("IntersectionObserver" in window) {
    lazyloadImages = document.querySelectorAll(".lazy");
    var imageObserver = new IntersectionObserver(function(entries, observer) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          var image = entry.target;
          image.src = image.dataset.src;
          image.classList.remove("lazy");
          imageObserver.unobserve(image);
        }
      });
    });

    lazyloadImages.forEach(function(image) {
      imageObserver.observe(image);
    });
  } else {  
    var lazyloadThrottleTimeout;
    lazyloadImages = document.querySelectorAll(".lazy");
    
    function lazyload () {
      if(lazyloadThrottleTimeout) {
        clearTimeout(lazyloadThrottleTimeout);
      }    

      lazyloadThrottleTimeout = setTimeout(function() {
        var scrollTop = window.pageYOffset;
        lazyloadImages.forEach(function(img) {
            if(img.offsetTop < (window.innerHeight + scrollTop)) {
              img.src = img.dataset.src;
              img.classList.remove('lazy');
            }
        });
        if(lazyloadImages.length == 0) { 
          document.removeEventListener("scroll", lazyload);
          window.removeEventListener("resize", lazyload);
          window.removeEventListener("orientationChange", lazyload);
        }
      }, 20);
    }

    document.addEventListener("scroll", lazyload);
    window.addEventListener("resize", lazyload);
    window.addEventListener("orientationChange", lazyload);
  }
})


/* выделение активного dropdown-menu */
$('.navbar-nav a').each(function() {
  if ( (window.location.pathname.indexOf( $(this).attr('href') ) ) > -1) {
    $(this).removeClass("btn-dark-green");
    $(this).addClass("btn-amber dark-grey-text");
  }
});

$(document).ready(function(){
    $('.extremum-click').click(function () {
        $(this).siblings(".extremum-slide").toggleClass('visually-hidden');
        if($(this).text() == 'Подробнее'){
            $(this).text('Скрыть');
        } else {
            $(this).text('Подробнее');
        }
    });
});
