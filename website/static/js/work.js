
function initMobileSlider() {
  if (window.innerWidth > 768) return;

  document.querySelectorAll('.card').forEach(card => {
    const slider = card.querySelector('.slider');
    const left = card.querySelector('.arrow.left');
    const right = card.querySelector('.arrow.right');

    right.onclick = () => slider.scrollLeft += slider.clientWidth;
    left.onclick = () => slider.scrollLeft -= slider.clientWidth;
  });
}

initMobileSlider();
window.addEventListener('resize', initMobileSlider);