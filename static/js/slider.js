function updateValue(val) {
  document.getElementById('valueDisplay').textContent = val;
}

document.addEventListener("DOMContentLoaded", function() {
  const slider = document.getElementById("id_rating");
  if (slider){
    updateValue(slider.value);
    slider.addEventListener("input", function() {
        updateValue(this.value);
  });
  }
});