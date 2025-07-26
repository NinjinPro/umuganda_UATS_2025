document.addEventListener("DOMContentLoaded", () => {
  const slides = document.querySelectorAll(".slide");
  let currentSlide = 0;
  const prevBtn = document.getElementById("prevBtn");
  const nextBtn = document.getElementById("nextBtn");
  const submitBtn = document.getElementById("submitBtn");

  function showNextSlide(index) {
    slides.forEach((slide, i) => {
      slide.classList.toggle("active", i === index);
    });
    prevBtn.disabled = index === 0;
    if (index === slides.length - 1) {
      nextBtn.classList.add("hidden");
      submitBtn.classList.remove("hidden");
    } else {
      nextBtn.classList.remove("hidden");
      submitBtn.classList.add("hidden");
    }
  }

  nextBtn.addEventListener("click", () => {
    if (currentSlide < slides.length - 1) {
      currentSlide++;
      showNextSlide(currentSlide);
    }
  });

  prevBtn.addEventListener("click", () => {
    if (currentSlide > 0) {
      currentSlide--;
      showNextSlide(currentSlide);
    }
  });

  document.getElementById("togglePassword").addEventListener("change", function () {
    ["password", "confirm"].forEach(id => {
      const field = document.getElementById(id);
      if (field) field.type = this.checked ? "text" : "password";
    });
  });

  document.querySelectorAll('input[name="is_local"]').forEach(radio => {
    radio.addEventListener("change", () => {
      const countryInput = document.querySelector(".country-input");
      countryInput.classList.toggle("hidden", radio.value === "yes");
    });
  });

  showNextSlide(currentSlide);
});
