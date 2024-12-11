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



async function button_click(answer_number){
  console.log(gameData)
  const player_answer = answer_number - 1
  const countries = gameData.all_country_options
  const correct_answer = gameData.current_country
  const response = await fetch('/compare_answer', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({ player_answer, countries, correct_answer })
  });
  const data = await response.json();
  console.log("done")
  console.log(data)
}

let country_data
let gameData

async function get_new_question(){
  const response = await fetch('/get_new_countries');
  const data = await response.json();

  const countries = data['all_country_options']
  for (let i = 0; i < countries.length; i++){
    const btn = "button" + (i+1)
    document.getElementById(btn).innerHTML = countries[i]
  }
  // document.getElementById('data1').innerHTML = countries
  return data
}

document.addEventListener('DOMContentLoaded', async function() {
    gameData = await get_new_question();
    console.log("Stored game data:", gameData);
    // someOtherFunction();
});

