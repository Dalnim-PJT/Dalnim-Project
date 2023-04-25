// menu
const menuBtn = document.getElementById("menuBtn");
const menu = document.getElementById("menu");

menuBtn.addEventListener("click", () => {
  if (menu.style.maxHeight) {
  menu.style.maxHeight = null;
  } else {
  menu.style.maxHeight = menu.scrollHeight + "px";
  }
});


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
