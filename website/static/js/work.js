document.querySelectorAll(".carousel").forEach(carousel => {

  const track = carousel.querySelector(".track");
  const prevBtn = carousel.querySelector(".prev");
  const nextBtn = carousel.querySelector(".next");

  let position = 0;

  nextBtn.addEventListener("click", () => {
    const slideWidth = track.querySelector(".slide").offsetWidth + 20;
    position -= slideWidth;
    track.style.transform = `translateX(${position}px)`;
    
  });

  prevBtn.addEventListener("click", () => {
    const slideWidth = track.querySelector(".slide").offsetWidth + 20;
    position += slideWidth;
    if(position > 0) position = 0;
    track.style.transform = `translateX(${position}px)`;
  });

});