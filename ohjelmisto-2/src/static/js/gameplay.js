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
  // jos button on valitsematon vastaus niin suorita tämä:
  if (answer_number >= 1 && answer_number <= 6){
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

    // jos vastausvaihtoehto on väärin niin poistetaan button käytöstä, sekä toinen random button
    if (data.success === false){
      document.getElementById('button' + answer_number).classList = "button-disabled"
      document.getElementById('button' + answer_number).setAttribute("onclick", "")
      // luodaan lista että mitkä vaihtoehdot ovat vielä käytettävissä
      const remaining_list = []
      for (let i = 1; i < 7; i++){
        if (document.getElementById('button'+i).className === "button"){
          remaining_list.push(i)
        } else {
          remaining_list.push(0)
        }
      }
      // haetaan random väärä vastaus joka poistetaan käytöstä
      const response = await fetch('/remove_random_answers', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          remaining_country_indexes: remaining_list,
          correct_country_index: countries.indexOf(correct_answer) })
        });
      const data2 = await response.json();

      document.getElementById('button' + data2.selection).classList = "button-disabled"
      document.getElementById('button' + data2.selection).setAttribute("onclick", "")

      // vähennetään pelaajalta yksi "elämä"
      if (document.getElementById('heart1').className === "heart"){
        document.getElementById('heart1').classList = "no-heart"
        document.getElementById('heart1').setAttribute("src", "../static/Images/heart_empty.svg")
      } else if (document.getElementById('heart2').className === "heart"){
        document.getElementById('heart2').classList = "no-heart"
        document.getElementById('heart2').setAttribute("src", "../static/Images/heart_empty.svg")
      // jos kolmas väärä vastaus niin aloitetaan uusi kysymys
      } else if (document.getElementById('heart2').className === "no-heart"){
        document.getElementById('random-event').innerHTML = "Unfortunately you answered wrong and didn't gain any points"
        open_event()
        // resetoidaan sydämmet ja buttonit
        reset_buttons()
        reset_hearts()
        reduce_turns()
        gameData = await get_new_question();
      }
    }


    // jos vastaus oli oikein
    if (data.success === true){
      document.getElementById('random-event').innerHTML = "Correct!<br>Now choose where you want to fly."
      document.getElementById('button' + answer_number).classList = "button-disabled"
      document.getElementById('button' + answer_number).setAttribute("onclick", "")
      for (let i = 1; i < 7; i++){
        if (document.getElementById('button'+i).className === "button"){
          const button_content = i+6
          document.getElementById('button'+i).setAttribute("onclick", "button_click("+button_content+")")
        }
      }
      open_event()
    }
  // "lennetään" pelaajan valitsemaan maahan
  } else if (answer_number >= 7 && answer_number <= 12){
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
    // jos tapahtui random event niin suoritetaan tämä
    if (data.did_event_happen === true){
      const content = "You decided to fly to " + gameData.all_country_options[answer_number-7] + "!"
      document.getElementById('random-event').innerHTML = content
      open_event()
      reset_buttons()
      reset_hearts()
      reduce_turns()
      gameData = await get_new_question();
    }
    // jos ei tullut random eventtiä niin suoritetaan tämä
    if (data.did_event_happen === false){
      const content = "You decided to fly to " + gameData.all_country_options[answer_number-7] + "!"
      document.getElementById('random-event').innerHTML = content
      open_event()
      reset_buttons()
      reset_hearts()
      reduce_turns()
      gameData = await get_new_question();
    }
  }
}
// }

function reset_buttons(){
  for (let i = 1; i < 7; i++){
    document.getElementById('button' + i).classList = "button"
    document.getElementById('button' + i).setAttribute("onclick", "button_click("+i+")")
  }
}

function reset_hearts(){
  document.getElementById('heart1').classList = "heart"
  document.getElementById('heart1').setAttribute("src", "../static/Images/heart_full.svg")
  document.getElementById('heart2').classList = "heart"
  document.getElementById('heart2').setAttribute("src", "../static/Images/heart_full.svg")
  document.getElementById('heart3').classList = "heart"
  document.getElementById('heart3').setAttribute("src", "../static/Images/heart_full.svg")
}

function reduce_turns(){
  document.getElementById('turns').innerHTML = parseInt(document.getElementById('turns').innerHTML) - 1
}


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
});
