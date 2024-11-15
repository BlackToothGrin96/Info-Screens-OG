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
	<title>Channel Overview</title>
	<meta name="description" content="Channel Overview" />
</svelte:head>

<div class="main">
	<div class="cell1">
		<RBCorner />
	</div>

	<div class="cell2">
			<div class="title-box">
				{#if data.channel_name.length > 16}
					<p class="channel-name" style="font-size: 10rem">{data.channel_name}</p>
				{:else}
					<p class="channel-name" style="font-size: 12rem">{data.channel_name}</p>
				{/if}
			</div>
	</div>

	<div class="cell3">
		<TimeCorner />
	</div>

	<div class="cell4 rb-info-box">
			<div class="overview-spacer">
				<div class="overview-box columns is-multiline">
					{#if data.open !== 0}
						<div class="column is-full status-item">
							Orders by Courier
						</div>
						{#each data.couriers as courier, index}
							<hr class="line-divider">
							{#if courier.open_count === 0}
								<div class="column is-10 courier-name" style="color: green">
									{courier.name}
								</div>
								<div class="column is-2 overview-item" style="color: green">
									{courier.open_count}
								</div>
							{:else}
								<div class="column is-10 courier-name">
									{courier.name}
								</div>
								<div class="column is-2 overview-item">
									{courier.open_count}
								</div>
							{/if}
						{/each}
					{:else }
						<div class="column is-full title-item">
							Top 5 Couriers (14 Days)
						</div>
						{#each data.couriers.slice(0, 5) as courier, index}
							<hr class="line-divider">
							<div class="column is-10 courier-name">
								{courier.name}
							</div>
							<div class="column is-2 overview-item">
								{courier.total_count}
							</div>
						{/each}
					{/if}
				</div>
			</div>
	</div>

	<div class="cell5 rb-info-box columns is-multiline">
		<div class="status-spacer column is-full">
			{#if data.oldest !== "N/A"}
				<div class="status-box columns">
					<div class="column is-two-thirds oldest-item">
						Oldest Open Order
					</div>
					<div class="column is-one-third status-item">
						{data.oldest}
					</div>
				</div>
			{:else }
				<div class="finished-box columns">
					<div class="column finished-item">
						Orders Finished
					</div>
				</div>
			{/if}
		</div>

		<div class="status-spacer column is-full">
			<div class="status-box columns">
				<div class="column is-two-thirds status-item">
					Open
				</div>
				<div class="column is-one-third status-item">
					{data.open}
				</div>
			</div>
		</div>

		<div class="status-spacer column is-full">
			<div class="status-box columns">
				<div class="column is-two-thirds status-item">
					Processing
				</div>
				<div class="column is-one-third status-item">
					{data.other.statuses[0].count}
				</div>
			</div>
		</div>

		<div class="status-spacer column is-full">
			<div class="status-box columns">
				<div class="column is-two-thirds status-item">
					Out of Stock
				</div>
				<div class="column is-one-third status-item">
					{data.other.statuses[1].count}
				</div>
			</div>
		</div>

			<!--{#each data.info.statuses as info, index}-->
			<!--	<div class="status-spacer column is-full">-->
			<!--		<div class="status-box columns">-->
			<!--			<div class="column is-two-thirds status-item">-->
			<!--				{info.status}-->
			<!--			</div>-->
			<!--			<div class="column is-one-third status-item">-->
			<!--				{info.count}-->
			<!--			</div>-->
			<!--		</div>-->
			<!--	</div>-->
			<!--{/each}-->
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
		grid-template-columns: repeat(4, 1fr);
		grid-template-rows: 1fr 15%;
		grid-column-gap: 0px;
		grid-row-gap: 0px;
		background: black;
	}

	.cell1 { grid-area: 2 / 1 / 3 / 2; }
	.cell2 { grid-area: 2 / 2 / 3 / 4; }
	.cell3 { grid-area: 2 / 4 / 3 / 5; }
	.cell4 {
		grid-area: 1 / 1 / 2 / 3;
		height: 100%;
		margin: 0;
		padding: 3rem 0 1rem 2rem;
	}
	.cell5 {
		grid-area: 1 / 3 / 2 / 5;
		height: 100%;
		margin: 0;
		/*padding: 0;*/
		padding: 3rem 0 1rem 2rem;
	}

	/*.side-box {*/
	/*	align-items: center;*/
	/*	justify-content: center;*/
	/*}*/
	.title-box {
		background: var(--rb-byzantium);
		align-items: center;
		justify-content: center;
		display: flex;
        position: fixed;
		bottom: 0;
		margin: 0;
		padding: 0;
        height: 12%;
        width: 50%;
		border-top-right-radius: 25px;
		border-top-left-radius: 25px;
	}
	.title-item {
		color: black;
		font-weight: bold;
		font-size: 8rem;
		margin: 0;
		padding: 0;
		/*left: 0;*/
		text-align: center;
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
	/*.channel-box {*/
	/*	height: 20vh;*/
	/*}*/
	.channel-name {
		white-space: nowrap;
		color: white;
		font-weight: bold;
		/*font-size: 12rem;*/
		/*font-size: 100%;*/
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
		height: 25%;
		padding: 3rem 2rem 3rem 2rem;
		margin: 0;
	}
	.status-box {
		background: white;
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
		/*width: 200px;*/
		/*aspect-ratio: 1.732 / 1; !* Correct hexagon ratio *!*/
		/*clip-path: polygon(*/
		/*	15% 0%, 85% 0%, !* Top points *!*/
		/*	100% 50%, !* Right point *!*/
		/*	85% 100%, 15% 100%, !* Bottom points *!*/
		/*	0% 50% !* Left point *!*/
		/*);*/
	}
	.status-item {
		color: black;
		font-weight: bold;
		font-size: 10rem;
		margin: 0;
		padding: 0;
		/*left: 0;*/
		text-align: center;
	}

	.overview-spacer {
		align-items: center;
		justify-content: center;
		display: flex;
		background: black;
		width: 100%;
		height: 100%;
		/*padding: 5px;*/
		margin: 0;
	}
	.overview-box {
		background: white;
		align-items: center;
		justify-content: center;
		align-content: start;
		/*padding-left: 10px;*/
		/*padding-right: 10px;*/
		margin: 0;
		padding: 0;
		width: 100%;
		height: 100%;
        /*height: 19%;*/
		border-radius: 25px;
		/*width: 200px;*/
		/*aspect-ratio: 1.732 / 1; !* Correct hexagon ratio *!*/
		/*clip-path: polygon(*/
		/*	15% 0%, 85% 0%, !* Top points *!*/
		/*	100% 50%, !* Right point *!*/
		/*	85% 100%, 15% 100%, !* Bottom points *!*/
		/*	0% 50% !* Left point *!*/
		/*);*/
	}
	.overview-item {
		color: black;
		font-weight: bold;
		font-size: 6rem;
		margin: 0;
		padding: 0;
		/*left: 0;*/
		text-align: center;
	}
	.courier-name {
		white-space: nowrap;
		color: black;
		font-weight: bold;
		font-size: calc(1vw + 1vh + 0.5vmin);
		margin: 0;
		padding: 0;
		/*left: 0;*/
		text-align: center;
	}
	.oldest-item {
		color: black;
		font-weight: bold;
		font-size: 9rem;
		margin: 0;
		padding: 0;
		/*left: 0;*/
		text-align: center;
	}
	.finished-box {
		background: var(--rb-primary);
		align-items: center;
		justify-content: center;
		margin: 0;
		padding: 0;
		width: 100%;
		height: 100%;
		border-radius: 25px;
	}
	.finished-item {
		color: white;
		font-weight: bold;
		font-size: 10rem;
		margin: 0;
		padding: 0;
		text-align: center;
	}
	hr.line-divider {
	  border-top: 8px solid #bbb;
	  border-radius: 5px;
	  width: 85%;
	  margin: 0;
	  padding: 0;
	}
</style>
