<script>
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';
  import Clock from "$/routes/Clock.svelte";
  import RBCorner from "$/routes/RBCorner.svelte";
  import TimeCorner from "$/routes/TimeCorner.svelte";

  // onMount(() => {
  //   const timer = setTimeout(() => {
  //     goto('/KITANDKIN'); // Replace '/target-page' with the actual path you want to navigate to
  //   }, 1000); // 500 = 5s
  //
  //   // Cleanup timeout if the component is destroyed before the timeout
  //   return () => clearTimeout(timer);
  // });

	export let data;
</script>

<svelte:head>
	<title>Warehouse Overview</title>
	<meta name="description" content="Warehouse Overview" />
</svelte:head>

<div class="main">
	<div class="cell1">
		<RBCorner />
		<div class="title-box">
			<p class="channel-name">Today's Goods-Out</p>
		</div>
		<TimeCorner />
	</div>

	<div class="cell2 rb-info-box columns is-multiline">
		<div class="status-spacer column is-full" style="height: 13%">
			<div class="status-box-title columns">
				<div class="column is-full status-title" style="font-size: 7rem">
					Courier Group
				</div>
			</div>
		</div>
		{#each data.orders as info, index}
			<div class="status-spacer column is-full" style="height: calc(86%/{data.orders.length})">
				<div class="status-box columns">
					{#if info.name.length > 25}
						<div class="column is-full status-title" style="font-size: 4rem">
							{info.name}
						</div>
					{:else if info.name.length > 20}
						<div class="column is-full status-title" style="font-size: 5rem">
							{info.name}
						</div>
					{:else if info.name.length > 16}
						<div class="column is-full status-title" style="font-size: 6rem">
							{info.name}
						</div>
					{:else}
						<div class="column is-full status-title" style="font-size: 7rem">
							{info.name}
						</div>
					{/if}
				</div>
			</div>
		{/each}
	</div>

	<div class="cell3 rb-info-box columns is-multiline">
		<div class="status-spacer column is-full" style="height: 13%">
			<div class="status-box columns">
				<div class="column is-half title-title" style="font-size: 5rem">
					Order Scans
				</div>
				<div class="column is-half title-title">
					Pallets
				</div>
			</div>
		</div>
		{#each data.pallets as info, index}
			<div class="status-spacer column is-full" style="height: calc(87%/{data.pallets.length})">
				<div class="status-box-title columns">
					<div class="column is-half title-item">
						{data.orders[index].count}
					</div>
					<div class="column is-half title-item">
						{info.count}
					</div>
				</div>
			</div>
		{/each}
	</div>

	<div class="cell4 rb-info-box columns is-multiline">
		<div class="status-spacer column is-full" style="height: 13%">
			<div class="status-box-title columns">
				<div class="column is-half title-title" style="font-size: 5rem">
					Pallet Scans
				</div>
				<div class="column is-half title-title">
					Trucks
				</div>
			</div>
		</div>
		{#each data.pallet_scans as info, index}
			<div class="status-spacer column is-full" style="height: calc(87%/{data.pallets.length})">
				<div class="status-box columns">
					<div class="column is-half title-item">
						{info.count}
					</div>
					<div class="column is-half title-item">
						{data.trucks[index].count}
					</div>
				</div>
			</div>
		{/each}
	</div>
</div>


<style>
	.main {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		grid-template-rows: 1fr 15%;
		grid-column-gap: 0px;
		grid-row-gap: 0px;
		height: 100vh;
		width: 100vw;
		align-items: center;
		justify-content: center;
		margin: auto;
		background: black;
	}

	.cell1 {
		grid-area: 2 / 1 / 3 / 4;
		padding: 0;
		margin: 0;
	}
	.cell2 {
		grid-area: 1 / 1 / 2 / 2;
		height: 100%;
		margin: 0;
		padding: 2rem 0 0 1rem;
	}
	.cell3 {
		grid-area: 1 / 2 / 2 / 3;
		height: 100%;
		margin: 0;
		padding: 2rem 1rem 0 1rem;
	}
	.cell4 {
		grid-area: 1 / 3 / 2 / 4;
		height: 100%;
		margin: 0;
		padding: 2rem 1rem 0 0;
	}

	.title-box {
		background: var(--rb-byzantium);
		align-items: center;
		justify-content: center;
		display: flex;
        position: fixed;
		margin: 0 auto;
		bottom: 0;
		left: 25%;
		right: 25%;
        height: 12%;
        width: 50%;
		border-top-right-radius: 25px;
		border-top-left-radius: 25px;
	}
	.rb-info-box {
		background: black;
		height: 100%;
		width: 100%;
		/*padding: 5%;*/
		top: 0;
		align-items: center;
		justify-content: center;
	}
	.channel-name {
		white-space: nowrap;
		color: white;
		font-weight: bold;
		font-size: 8rem;
		text-align: center;
		padding: 0;
		margin: 0;
	}
	.status-spacer {
		align-items: center;
		justify-content: center;
		display: flex;
		background: black;
		width: 100%;
		/*height: calc(100%/7.25);*/
		padding: 0.5rem;
		margin: 0;
	}
	.status-box {
		background: var(--rb-primary);
		align-items: center;
		justify-content: center;
		/*padding-left: 10px;*/
		/*padding-right: 10px;*/
		margin: 0;
		padding: 0;
		width: 100%;
		height: 100%;
        /*height: 19%;*/
		border-radius: 25px;
	}
	.status-box-title {
		background: var(--rb-byzantium);
		align-items: center;
		justify-content: center;
		/*padding-left: 10px;*/
		/*padding-right: 10px;*/
		margin: 0;
		padding: 0;
		width: 100%;
		height: 100%;
        /*height: 19%;*/
		border-radius: 25px;
	}
	.status-title {
		white-space: nowrap;
		color: white;
		font-weight: bold;
		/*font-size: 4rem;*/
		margin: 0;
		padding: 0 0 0 2%;
		/*left: 0;*/
		text-align: center;
	}
	.status-item {
		white-space: nowrap;
		color: white;
		font-weight: bold;
		/*font-size: calc(1.75vw + 1.75vh + .75vmin);*/
		font-size: 7rem;
		margin: 0;
		padding: 0 2% 0 0;
		/*left: 0;*/
		text-align: center;
	}
	.title-title {
		white-space: nowrap;
		color: white;
		font-weight: bold;
		font-size: 6rem;
		margin: 0;
		padding: 0 0 0 2%;
		/*left: 0;*/
		text-align: center;
	}
	.title-item {
		white-space: nowrap;
		color: white;
		font-weight: bold;
		font-size: calc(1.75vw + 1.75vh + .75vmin);
		margin: 0;
		padding: 0 2% 0 0;
		/*left: 0;*/
		text-align: center;
	}
</style>
