$(document).ready(function () {
  $(".owl-carousel").owlCarousel({
    items: 1,
    loop: true,
    autoplay: true,
    autoplayTimeout: 5000,
  });
});

Fancybox.bind("#gallery a", {
  groupAll: true,
  on: {
    ready: (fancybox) => {
      console.log(`fancybox #${fancybox.id} is ready!`);
    },
  },
});

let btn = document.querySelector(`.burger-btn`);

const burgerFunc = (menuClassName, showClassName) => {
  let menu = document.querySelector(`.${menuClassName}`);

  if (menu.className.includes(showClassName)) {
    menu.className = menuClassName;
  } else {
    menu.className += ` ${showClassName}`;
  }
};

btn.addEventListener("click", () => {
  burgerFunc("header__menu", "header__menu-show ");
});



let lol = 'lol';
console.log(lol)



document.querySelector('.modal_autorization_').addEventListener('click', openModal);

function openModal() {
  document.getElementById('overlay').style.display = 'block';
  document.getElementById('modal').style.display = 'block';
}

function closeModal() {
  document.getElementById('overlay').style.display = 'none';
  document.getElementById('modal').style.display='none';
}
