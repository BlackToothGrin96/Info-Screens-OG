<script>
	// import {goto, replaceState} from '$app/navigation';
	// import trolley from '$lib/images/trolleytrans.png';
	import Loading from '$lib/components/Loading.svelte';
	/** @type {import('./$types').PageData} */

	export let data;

	// let container;
	// let barcode = "";

	// async function fetchContainer(barcode) {
	// 	// goto(`/${barcode}`, {replaceState: true});
	// 	showModal = true;
	// 	const response = await fetch('http://192.168.1.194:8000/staging/fetch_container?container_barcode=' + barcode);
	// 	let res = await response.json();
	// 	container = res;
	// 	console.log(container);
	// 	showModal = false;
	// }
</script>

<svelte:head>
	<title>Container {data.barcode}</title>
	<meta name="description" content="Container {data.barcode}" />
</svelte:head>

<div class="main pure-g">
	<div class="side-bar pure-u-1-5">
		<div class="side-box">
			<h1>Container {data.barcode}</h1>
		</div>
	</div>
	<div class="content pure-u-4-5"></div>
</div>


<style>
	.main {
		/*height: 100vh;*/
		width: 100vw;
		align-items: center;
		margin: auto;
	}
	.side-bar {
		height: 60vh;
		/*width: auto;*/
		/*padding-top: 20rem;*/
		/*background-color: var(--rb-mindaro);*/
	}
	.content {
		/*background-color: var(--rb-atomic-tangerine);*/
		font-weight: bold;
		height: 85vh;
		/*width: auto;*/
	}
</style>
