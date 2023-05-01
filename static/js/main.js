// news carousel
var slideIndex = 0;
showSlides();

function showSlides() {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}    
  slides[slideIndex-1].style.display = "block";  
  setTimeout(showSlides, 3000);
}

// melon carousel
var index = 0;
var slides = document.querySelectorAll('.slide1, .slide2');
slideShow();

function slideShow() {
  for (var i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  index++;
  if (index > slides.length) {
    index = 1;
  }
  slides[index-1].style.display = "block";
  setTimeout(slideShow, 4000);
}

// movie
var emblaNode = document.querySelector(".embla");
  var options = { loop: false };
  var plugins = [EmblaCarouselAutoplay()]; // Plugins

  var embla = EmblaCarousel(emblaNode, options, plugins);

  var posters = document.querySelectorAll('.poster');

  posters.forEach(function(poster) {
    poster.addEventListener('mouseover', function() {
      var btnWrap = poster.querySelector('.movieChart_btn_wrap');
      btnWrap.style.display = 'block';
    });

    poster.addEventListener('mouseout', function() {
      var btnWrap = poster.querySelector('.movieChart_btn_wrap');
      btnWrap.style.display = 'none';
    });
  });

// webtoon
document.addEventListener('DOMContentLoaded', function () {
  const carousel = document.querySelector('#webtoon-carousel.webtoon--container');
  let scrollInterval;

  function scrollWebtoon() {
    clearInterval(scrollInterval);
    scrollInterval = setInterval(() => {
      carousel.scrollLeft += 1;
      if (carousel.scrollLeft >= carousel.scrollWidth - carousel.clientWidth) {
        carousel.scrollLeft = 0;
      }
    }, 20);
  }

  scrollWebtoon();

  carousel.addEventListener('mouseover', () => {
    clearInterval(scrollInterval);
  });

  carousel.addEventListener('mouseout', () => {
    scrollWebtoon();
  });
});