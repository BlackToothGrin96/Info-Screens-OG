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
				<p class="channel-name">{data.channel_name}</p>
				<!--{#each data.info.statuses as info, index}-->
				<!--	<h2 class="status-item">{info.status} - {info.count}</h2>-->
				<!--{/each}-->
			</div>
	</div>

	<div class="cell3">
		<TimeCorner />
	</div>

<!--	<div class="cell5">-->
<!--		<div class="cell-spacer"></div>-->
<!--	</div>-->

	<div class="cell4 rb-info-box columns is-multiline">
		<div class="overview-spacer">
			<div class="overview-box columns is-multiline">
				<div class="column is-full status-item">
					Channel Codes
				</div>
				{#if data.channel_codes.length > 7}
					{#each data.channel_codes as code, index}
						{#if index % 2 === 0}
							<hr class="line-divider">
						{/if}
<!--						<hr class="line-divider">-->
						<div class="column is-half overview-item-small">
							{code}
						</div>
					{/each}
				{:else}
					{#each data.channel_codes as code, index}
						<hr class="line-divider">
						<div class="column is-full overview-item">
							{code}
						</div>
					{/each}
				{/if}
			</div>
		</div>
	</div>

	<div class="cell5 rb-info-box columns is-multiline">
		<div class="overview-spacer">
			<div class="overview-box columns is-multiline">
				<div class="column is-full status-item">
					Picking Modules
				</div>
				{#each data.modules as module, index}
					{#if module.type === "PICKING"}
						<hr class="line-divider">
						<div class="column is-full overview-item">
							{module.name}
						</div>
					{/if}
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
		padding: 3rem 1rem 1rem 2rem;
	}
	.cell5 {
		grid-area: 1 / 3 / 2 / 5;
		height: 100%;
		margin: 0;
		padding: 3rem 2rem 1rem 1rem;
	}

	.title-box {
		background: var(--rb-byzantium);
		align-items: center;
		justify-content: center;
		display: flex;
        position: fixed;
		bottom: 0;
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
		color: white;
		font-weight: bold;
		font-size: 10rem;
		text-align: center;
		padding: 0;
		margin: 0;
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
	.overview-item-small {
		color: black;
		font-weight: bold;
		font-size: 4.5rem;
		margin: 0;
		padding: 0;
		/*left: 0;*/
		text-align: center;
	}
	hr.line-divider {
	  border-top: 8px solid #bbb;
	  border-radius: 5px;
	  width: 85%;
	}
</style>
