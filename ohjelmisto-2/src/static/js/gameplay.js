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
  // console.log(country_data)
}

let gameData;

async function get_new_question() {
    const response = await fetch('/get_new_countries');
    const data = await response.json();

    const countries = data.all_country_options;
    const currentCountryName = data.current_country[1];
    const airportCode = data.current_country[0];
    const continent = data.current_country[2];

    const wrongCountriesData = data.wrong_countries[0];

    for (let i = 0; i < countries.length; i++) {
        const btn = "button" + (i + 1);
        const button = document.getElementById(btn);
        if (button) {
            button.innerHTML = countries[i];
        }
    }

    return data;
}


document.addEventListener('DOMContentLoaded', async function() {
    gameData = await get_new_question();
    console.log("Stored game data:", gameData);
    someOtherFunction();
});


function someOtherFunction() {
  console.log("Current country is:", gameData.current_country[1]);
}
