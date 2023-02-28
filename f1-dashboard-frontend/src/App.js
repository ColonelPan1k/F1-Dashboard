//https://www.youtube.com/watch?v=kTWJypbcSLI
import React, {useEffect, useState, useRef, useMemo} from 'react';
import logo from './logo.svg';
import {Countdown} from './Countdown.js'
import './App.css';

function App() {
		const [raceInfo, setRaceInfo] = useState([])
		const [eventName, setEventName] = useState([])
		const [eventDate, setEventDate] = useState([])

		useEffect(() => {
				fetch('http://localhost:8000/upcoming')
						.then(res => res.json())
						.then(data => {
								setRaceInfo(data.event)

								const event_name = Object.keys(data.next_event)[0].split("_")[0].toUpperCase()
								setEventName(event_name)

								const eventDate = new Date(Object.values(data.next_event)[0]);
								setEventDate(eventDate)
						})
		},[])

		return <div>
							 <h1>{raceInfo.year} {raceInfo.race} - Round {raceInfo.round}</h1>
							 <Countdown date={eventDate} />
							 <h2>{eventName}: {eventDate.toLocaleString()}</h2>
					 </div>;
}

export default App;
