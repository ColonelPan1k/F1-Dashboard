//https://www.youtube.com/watch?v=kTWJypbcSLI
import React, {useEffect, useState } from 'react';
import Header from './header';
import { Countdown } from './Countdown.js';
import { ScheduleTable } from './ScheduleTable.js'
import './App.css';


function App() {
		const [raceInfo, setRaceInfo] = useState([])
		const [eventName, setEventName] = useState([])
		const [eventDate, setEventDate] = useState([])
		const [eventTimeInfo, setEventTimeInfo] = useState([])

		useEffect(() => {
				fetch('http://localhost:8000/upcoming')
						.then(res => res.json())
						.then(data => {
								setEventTimeInfo(data.events);
								setRaceInfo(data.race);
								setEventName(Object.keys(data.events.next)[0].toString());

								const eventDate = new Date(Object.values(data.events.next)[0]);
								setEventDate(eventDate)
						})
		},[])

		return <div>
							 <Header/>
							 <div className="logo">
							 </div>
							 <div className="raceHeader">
									 <h1>{raceInfo.year} {raceInfo.race} - {eventName}</h1>
							 </div>

							 <div className="countdown-timer">
									 <Countdown date={eventDate} />
							 </div>
							 <div className="eventInfo">
									 <h2>{eventDate.toLocaleString()}</h2>
							 </div>
					 </div>;
}

export default App;
