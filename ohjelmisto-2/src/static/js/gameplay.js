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



function button_click(answer_number){
  const jotai = 0
  // console.log(country_data)
}

async function get_new_question(){
  const response = await fetch('/get_new_countries');
  const data = await response.json();

  const countries = data['all_country_options']
  for (let i = 0; i < countries.length; i++){
    const btn = "button" + (i+1)
    document.getElementById(btn).innerHTML = countries[i]
  }
  // return [data['all_country_options'], data['current_country'], data['wrong_countries']]
  // console.log(data['all_country_options'])
  return data['all_country_options']
}
let country_data = get_new_question()
console.log(get_new_question())

