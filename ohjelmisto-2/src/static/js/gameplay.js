function set_random_event(){
	const popup = document.getElementById('random-event');
	const event_desc = "asdasdas";
	popup.innerHTML = event_desc;
}

function open_event(){
  const eventPopup = document.getElementById('event-popup');
  const overlay = document.getElementById('event-overlay');
  eventPopup.style.display = 'block';
  overlay.style.display = 'block';
}

function close_event(){
  const eventPopup = document.getElementById('event-popup');
  const overlay = document.getElementById('event-overlay');
  eventPopup.style.display = 'none';
  overlay.style.display = 'none';
}


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
  if (answer_number >= 1 && answer_number <= 6){
    // console.log(gameData)
    const player_answer = answer_number
    const countries = gameData.all_country_options
    const correct_answer = gameData.current_country[1];
    const response = await fetch('/compare_answer', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          player_answer: player_answer,
          country_options: countries,
          correct_country: correct_answer })
    });
    const data = await response.json();

    // console.log(data)
    // console.log("done")
    // console.log(data.success)
    if (data.success === false){
      document.getElementById('button' + answer_number).classList = "button-disabled"
      document.getElementById('button' + answer_number).setAttribute("onclick", "")
    }

    if (data.success === true){
      document.getElementById('random-event').innerHTML = "Correct!<br>Now choose where you want to fly."
      document.getElementById('button1').setAttribute("onclick", "button_click(7)")
      // console.log("asd")
      open_event()
    }
  } else if (answer_number >= 7 && answer_number <= 12){
    // console.log("APUA")
    console.log(answer_number-6, gameData.wrong_countries[0], document.getElementById('turns').innerHTML, gameData.current_country[1])
    console.log(gameData.all_country_options)
    console.log(gameData)
    const response = await fetch('/count_player_points', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          flight_destination: answer_number - 6,
          country_options: gameData.all_country_options,
          wrong_countries: gameData.wrong_countries[0],
          turns_left: document.getElementById('turns').innerHTML })
    });
    const data = await response.json();
    // console.log("toimi")
    console.log(data)
    if (data.did_event_happen === true){
      const content = "You decided to fly to " + gameData.all_country_options[answer_number-7] + "!"
      document.getElementById('random-event').innerHTML = content
      open_event()
      gameData = await get_new_question();
      for (let i = 1; i < 7; i++){
        // console.log("asd")
        document.getElementById('button' + i).classList = "button"
        document.getElementById('button' + i).setAttribute("onclick", "button_click("+i+")")
      }
    }
    if (data.did_event_happen === false){
      const content = "You decided to fly to " + gameData.all_country_options[answer_number-7] + "!"
      document.getElementById('random-event').innerHTML = content
      open_event()
      gameData = await get_new_question();
      for (let i = 1; i < 7; i++){
        // console.log("asd")
        document.getElementById('button' + i).classList = "button"
        document.getElementById('button' + i).setAttribute("onclick", "button_click("+i+")")
      }
    }
    //document.getElementById('random-event').innerHTML = ""
  }

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
  document.getElementById('airport').innerHTML = data.current_country[0]
  return data
}

document.addEventListener('DOMContentLoaded', async function() {
    gameData = await get_new_question();
    console.log("Stored game data:", gameData);
    // someOtherFunction();
});
