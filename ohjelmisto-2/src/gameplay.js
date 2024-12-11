const infoButton = document.getElementById('info');
const infoPopup = document.getElementById('info-popup');
const closePopup = document.getElementById('close-popup');
const overlay = document.getElementById('overlay');

infoButton.addEventListener('click', () => {
  infoPopup.style.display = 'block';
  overlay.style.display = 'block';
});

closePopup.addEventListener('click', () => {
  infoPopup.style.display = 'none';
  overlay.style.display = 'none';
});

overlay.addEventListener('click', () => {
  infoPopup.style.display = 'none';
  overlay.style.display = 'none';
});