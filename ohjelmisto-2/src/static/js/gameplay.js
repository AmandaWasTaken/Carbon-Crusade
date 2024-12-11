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



function button_click(answer_number){
  const jotai = 0
}

async function get_new_question(){
  const response = await fetch('/get_new_countries');
  const data = await response.json();
  // console.log(data)
  // console.log(data['all_country_options'])
  // console.log("hello world")
  const countries = data['all_country_options']
  for (let i = 0; i < countries.length; i++){
    // console.log(countries[i])
    const btn = "button" + (i+1)
    // console.log(btn)
    document.getElementById(btn).innerHTML = countries[i]
  }

}
