<script>
	import logo from '$lib/images/logo@2x.png';
	import { onDestroy } from 'svelte';
	import RBCorner from "$/routes/RBCorner.svelte";
	import TimeCorner from "$/routes/TimeCorner.svelte";

	// Helper function to get the current local time and date
	function getCurrentLocalTime() {
		const now = new Date();
        // now.setTime( now.getTime() - now.getTimezoneOffset()*60*1000 );
		const options = { hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: false };
		const timeString = new Intl.DateTimeFormat(undefined, options).format(now);
		const [hour, minute, second] = timeString.match(/\d{2}/g);
		return {
			hours: parseInt(hour),
			minutes: parseInt(minute),
			seconds: parseInt(second),
			date: now.toDateString(),
		};
	}

	// Initialize the time values with the correct local time
	let { hours, minutes, seconds, date } = getCurrentLocalTime();

	// Function to pad single digit numbers with a leading zero
	function padToTwoDigits(number) {
		return number.toString().padStart(2, '0');
	}

	// Start updating time immediately after the component mounts
	const interval = setInterval(() => {
		const { hours: newHours, minutes: newMinutes, seconds: newSeconds, date: newDate } = getCurrentLocalTime();
		hours = newHours;
		minutes = newMinutes;
		seconds = newSeconds;
		date = newDate;
	}, 500); // update every second

	// Cleanup when component is destroyed
	onDestroy(() => {
		clearInterval(interval);
	});
</script>

<svelte:head>
	<title>Channel Overview</title>
	<meta name="description" content="Channel Overview" />
</svelte:head>

<div class="main">
	<div class="cell2">
		<RBCorner />
	</div>

	<div class="cell3">
		<TimeCorner />
	</div>

	<div class="cell1 rb-info-box">
		<div class="cell-spacer">
			<p class="time-text">{padToTwoDigits(hours)}:{padToTwoDigits(minutes)}:{padToTwoDigits(seconds)}</p>
			<p class="date-text">{date}</p>
		</div>
	</div>

	<div class="cell4">
		<div class="cell-fill"></div>
	</div>
</div>


<style>
	.main {
		height: 100vh;
		width: 100vw;
		align-items: center;
		justify-content: center;
		margin: auto;
		display: grid;
		background: black;
		grid-template-columns: 1fr 2fr 1fr;
		grid-template-rows: 1fr 3fr 1fr;
		grid-column-gap: 0px;
		grid-row-gap: 0px;
	}

	.cell1 { grid-area: 2 / 1 / 3 / 4; }
	.cell2 { grid-area: 3 / 1 / 4 / 2; }
	.cell3 { grid-area: 3 / 3 / 4 / 4; }
	.cell4 { grid-area: 1 / 1 / 2 / 4; }

	.rb-info-box {
		background: black;
	}
	.time-text {
		color: white;
		font-weight: bold;
		font-size: 40rem;
		text-align: center;
		padding-left: 10%;
		padding-right: 10%;
		margin: 0;
	}
	.date-text {
		color: white;
		font-weight: bold;
		font-size: 20rem;
		text-align: center;
		padding-left: 5%;
		padding-right: 5%;
		margin: 0;
	}
	.cell-spacer {
		background: black;
		/*width: 100%;*/
		/*height: 100%;*/
		padding: 5px;
	}
	.cell-fill {
		background: black;
		width: 100%;
		height: 100%;
		/*padding: 5px;*/
	}
</style>
