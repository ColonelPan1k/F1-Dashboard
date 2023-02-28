import React, {useState, useEffect} from "react";

export function Countdown(props){

		const [days, setDays] = useState(0)
		const [hours, setHours] = useState(0)
		const [minutes, setMinutes] = useState(0)
		const [seconds, setSeconds] = useState(0)

		useEffect(() => {
				const target = props.date

				const interval = setInterval(() =>{
						const now = new Date();
						const diff = target - now;

						const days = Math.floor(diff / (1000 * 60 * 60 * 24))
						setDays(days)

						const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60))
						setHours(hours)

						const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
						setMinutes(minutes)

						const s = Math.floor((diff % (1000 * 60)) / 1000);
						setSeconds(s);
				});

				return () => clearInterval(interval)
		});

		return ( <div><h1>{days}d {hours}h {minutes}m {seconds}s </h1></div>)
}
