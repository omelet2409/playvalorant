// Base on sequence.js
// https://github.com/IanLunn/Sequence/

var sequenceElement = document.getElementById("sequence");

var options = {
  keyNavigation: true,
  animateCanvas: false
}

var mySequence = sequence(sequenceElement, options);

const container = document.querySelector('.image-container');
const infoContainer = container.querySelector('.info-container');

container.addEventListener('mouseenter', () => {
  infoContainer.classList.add('hovered');
});

container.addEventListener('mouseleave', () => {
  infoContainer.classList.remove('hovered');
});
