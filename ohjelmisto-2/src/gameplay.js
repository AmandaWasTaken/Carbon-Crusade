function open_info(){
  const infoPopup = document.getElementById('info-popup');
  const overlay = document.getElementById('overlay');
  infoPopup.style.display = 'block';
  overlay.style.display = 'block';
}

function close_info(){
  const infoPopup = document.getElementById('info-popup');
  const overlay = document.getElementById('overlay');
  infoPopup.style.display = 'none';
  overlay.style.display = 'none';
}
