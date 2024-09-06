<script>
	import {goto, replaceState} from '$app/navigation';
	import trolley from '$lib/images/trolleytrans.png';
	// import Loading from '$lib/components/Loading.svelte';

	let container;
	let barcode = "";
	// let showModal = false;
	// up = 38
	// down = 40
	// right = 39
	// left = 37
	function onKeyDown(e) {
		// console.log(e.key);
		if (e.key !== "Enter" && e.key !== "Shift") {
			if (barcode === "") {
				barcode = e.key;
			} else {
				barcode += e.key;
			}
		} else if (e.key === "Enter") {
			console.log("Fetching container: " + barcode);
			fetchContainer(barcode);
			barcode = "";
			// loadingModal();
			// window.location.pathname = "/staging/" + barcode + "/";
		}
	}

	async function fetchContainer(barcode) {
		goto(`/${barcode}`, {replaceState: true});
		// showModal = true;
		// const response = await fetch('http://192.168.1.194:8000/staging/fetch_container?container_barcode=' + barcode);
		// let res = await response.json();
		// container = res;
		// console.log(container);
		// showModal = false;
	}
</script>

<svelte:head>
	<title>Staging Home</title>
	<meta name="description" content="RexBrown Staging System Home Page" />
</svelte:head>

<section class="home-container columns is-centered is-multiline">
	<div class="rb-info-box column is-one-third">
		<h1>Please scan a trolley to begin</h1>
	</div>
	<img src={trolley} alt="Scan a trolley" class="column is-one-third" />
</section>

<svelte:window on:keydown|preventDefault={onKeyDown} />

<style>
	.home-container {
		/*justify-content: center;*/
		/*align-items: center;*/
		margin-top: auto;
		margin-bottom: 4rem;
		width: 100vw;
		/*height: 80vh;*/
	}
	.home-container > img {
		height: 60vh;
		object-fit: contain;
		/*margin: auto;*/
		/*width: 100vw;*/
		padding-top: 4rem;
	}
	.home-container > div > h1 {
		color: white;
		font-weight: bold;
		/*margin: auto;*/
		/*width: 100vw;*/
	}
</style>
