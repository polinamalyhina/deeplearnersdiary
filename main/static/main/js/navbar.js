// // When the user scrolls the page, execute myFunction
// window.onscroll = function() {myFunction()};
//
// // Get the navbar
// var navbar = document.getElementById("navbar");
//
// // Get the offset position of the navbar
// var sticky = navbar.offsetTop;
//
// // Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
// function myFunction() {
//   if (window.pageYOffset >= sticky) {
//     navbar.classList.add("sticky")
//   } else {
//     navbar.classList.remove("sticky");
//   }
// }

window.onscroll = function(){
var scrolled = window.pageYOffset || document.documentElement.scrollTop;
var o=document.getElementById('sticky');
if (scrolled > 320) o.setAttribute('class','fix');
else o.setAttribute('class','not_fix');
}