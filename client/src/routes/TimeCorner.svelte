<script>
	import logo from '$lib/images/logo@2x.png';
	import { onMount } from 'svelte';

	let time = new Date();

	// these automatically update when `time`
	// changes, because of the `$:` prefix
	$: hours = time.getHours();
	$: minutes = time.getMinutes();
	$: seconds = time.getSeconds();
	// $: timeNow = time.toDateString();
	// $: day = time.getDay();
	$: date = time.toDateString();

    // Function to pad single digit numbers with a leading zero
    function padToTwoDigits(number) {
      return number.toString().padStart(2, '0');
    }

	onMount(() => {
		const interval = setInterval(() => {
			time = new Date();
		}, 1000);

		return () => {
			clearInterval(interval);
		};
	});
</script>

<div class="rb-corner">
    <div class="logo">
        <p class="time-text">{padToTwoDigits(hours)}:{padToTwoDigits(minutes)}:{padToTwoDigits(seconds)}</p>
        <p class="time-text">{date}</p>
    </div>
</div>


<style>
    .rb-corner {
        position: fixed;
        top: 0;
        right: 0;
        background: var(--rb-primary);
        border-bottom-left-radius: 25px;
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
        height: auto;
        width: 90%;
	}
</style>