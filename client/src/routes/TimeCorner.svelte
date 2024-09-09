<script>
	import logo from '$lib/images/logo@2x.png';
	import { onDestroy } from 'svelte';

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

<div class="rb-corner">
    <div class="logo">
        <p class="time-text">{padToTwoDigits(hours)}:{padToTwoDigits(minutes)}:{padToTwoDigits(seconds)}</p>
        <p class="time-text">{date}</p>
<!--        {#if mounted}-->
<!--            &lt;!&ndash; Display the time and date after hydration &ndash;&gt;-->
<!--            <p class="time-text">{padToTwoDigits(hours)}:{padToTwoDigits(minutes)}:{padToTwoDigits(seconds)}</p>-->
<!--            <p class="time-text">{date}</p>-->
<!--        {:else}-->
<!--            &lt;!&ndash; Placeholder before the component is fully mounted &ndash;&gt;-->
<!--            <p></p>-->
<!--        {/if}-->
    </div>
</div>


<style>
    .rb-corner {
        position: fixed;
        bottom: 0;
        right: 0;
        background: var(--rb-primary);
        border-top-left-radius: 25px;
        width: 24%;
        height: 15%;
        display: flex;
        /*padding-bottom: 5px;*/
        /*padding-right: 5px;*/
    }

    .logo {
        height: 100%;
        width: 100%;
        align-items: center;
        justify-content: center;
        /*margin-top: 20px;*/
        /*margin-bottom: 20px;*/
        /*padding-top: 1rem;*/
    }

    /*.columns {*/
    /*    !*display: flex;*!*/
    /*    !*align-items: center;*!*/
    /*    !*justify-content: center;*!*/
    /*    width: 100%;*/
    /*    height: 100%;*/
    /*}*/

    /*.column {*/
    /*    display: flex;*/
    /*    align-items: center;*/
    /*    justify-content: center;*/
    /*}*/

    /*.time-container {*/
    /*    height: 30%;*/
    /*}*/

	.time-text {
		color: white;
		font-weight: bold;
		font-size: 5rem;
		text-align: center;
		margin: 0;
        display: block;
        height: 50%;
        width: 100%;
        align-items: center;
        justify-content: center;
	}
</style>