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