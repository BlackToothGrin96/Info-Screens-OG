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
	<title>All Users Info</title>
	<meta name="description" content="" />
</svelte:head>

<div class="main">
	<div class="rb-info-box channel-box">
		<div class="side-box">
			<h1 class="channel-name">All Users</h1>
			<!--{#each data.info.statuses as info, index}-->
			<!--	<h2 class="status-item">{info.status} - {info.count}</h2>-->
			<!--{/each}-->
		</div>
	</div>
	<div class="rb-info-box status-box">
		<div class="side-box">
<!--			<h1 class="channel-name">{data.info.channel_name}</h1>-->
			<h2 class="status-item">Total Orders</h2>

			<!--{#each data.info.statuses as info, index}-->
			<!--	<h2 class="status-item">{info.status} - {info.count}</h2>-->
			<!--{/each}-->
		</div>
	</div>
</div>


<style>
	.main {
		height: 100vh;
		width: 100vw;
		align-items: center;
		margin: auto;
	}
	.side-box {
		align-items: center;
		justify-content: center;
	}
	.status-box {
		align-items: center;
		justify-content: center;
	}
	.channel-box {
		height: 20vh;
	}
	.channel-name {
		color: white;
		font-weight: bold;
		font-size: 7rem;
	}
	.rb-info-box {
	background: black;
	}
	.status-item {
		color: white;
		font-weight: bold;
		font-size: 2rem;
		text-align: center;
	}
</style>
