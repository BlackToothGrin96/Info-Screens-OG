<script>
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';
  import RBCorner from "$/routes/RBCorner.svelte";
  import Clock from "$/routes/Clock.svelte";

  // onMount(() => {
  //   const timer = setTimeout(() => {
  //     goto('/warehouse'); // Replace '/target-page' with the actual path you want to navigate to
  //   }, 1000); // 500 = 5s
  //
  //   // Cleanup timeout if the component is destroyed before the timeout
  //   return () => clearTimeout(timer);
  // });

	export let data;
</script>

<svelte:head>
	<title>{data.channel_code} Info</title>
	<meta name="description" content="{data.channel_code}" />
</svelte:head>

<div class="main">
	<div class="cell1">
		<RBCorner />
	</div>

	<div class="cell2">
		<div class="cell-spacer">
			<div class="status-box">
				<p class="channel-name">{data.info.channel_name}</p>
				<!--{#each data.info.statuses as info, index}-->
				<!--	<h2 class="status-item">{info.status} - {info.count}</h2>-->
				<!--{/each}-->
			</div>
		</div>
	</div>

	<div class="cell3">
		<div class="cell-spacer">
			<Clock />
		</div>
	</div>

	<div class="cell4">
		<div class="cell-spacer"></div>
	</div>

	<div class="cell5">
		<div class="cell-spacer">
			<div class="status-box">
<!--			<h1 class="channel-name">{data.info.channel_name}</h1>-->
				<h2 class="status-item">{data.total} Total Orders</h2>

				{#each data.info.statuses as info, index}
					<h2 class="status-item">{info.status} - {info.count}</h2>
				{/each}
			</div>
		</div>
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
		grid-template-columns: 1fr 2fr 1fr;
		grid-template-rows: 1fr 3fr 1fr;
		grid-column-gap: 0px;
		grid-row-gap: 0px;
	}

	.cell1 { grid-area: 1 / 1 / 2 / 2; }
	.cell2 { grid-area: 1 / 2 / 2 / 3; }
	.cell3 { grid-area: 1 / 3 / 2 / 4; }
	.cell4 { grid-area: 2 / 2 / 4 / 4; }
	.cell5 { grid-area: 2 / 1 / 4 / 2; }

	/*.side-box {*/
	/*	align-items: center;*/
	/*	justify-content: center;*/
	/*}*/
	.status-box {
		background: black;
		/*align-items: stretch;*/
		/*justify-content: stretch;*/
		/*width: 100%;*/
		/*height: 100%;*/
		border-radius: 25px;
	}
	/*.channel-box {*/
	/*	height: 20vh;*/
	/*}*/
	.channel-name {
		color: white;
		font-weight: bold;
		font-size: 8rem;
		text-align: center;
		margin: 0;
	}
	.cell-spacer {
		background: white;
		/*width: 100%;*/
		/*height: 100%;*/
		padding: 5px;
	}
	.status-item {
		color: white;
		font-weight: bold;
		font-size: 2rem;
		text-align: center;
	}
</style>
