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
				<p class="channel-name">{data.info.channel_name}</p>
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
<!--		<div class="cell-spacer">-->
			{#each data.info.statuses.slice(0, 4) as info, index}
				<div class="status-spacer column is-full">
<!--					<div class="triangle-left"></div>-->
					<div class="status-box columns">
						<div class="column is-two-thirds status-item">
							{info.status}
						</div>
						<div class="column is-one-third status-item">
							{info.count}
						</div>
					</div>
<!--					<div class="triangle-right"></div>-->
				</div>
			{/each}
<!--		</div>-->
	</div>

	<div class="cell5 rb-info-box columns is-multiline">
<!--		<div class="cell-spacer">-->
			{#each data.info.statuses.slice(4) as info, index}
				<div class="status-spacer column is-full">
<!--					<div class="triangle-left"></div>-->
					<div class="status-box columns">
						<div class="column is-two-thirds status-item">
							{info.status}
						</div>
						<div class="column is-one-third status-item">
							{info.count}
						</div>
					</div>
<!--					<div class="triangle-right"></div>-->
				</div>
			{/each}
		</div>
<!--	</div>-->
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
		padding: 0;
	}
	.cell5 {
		grid-area: 1 / 3 / 2 / 5;
		height: 100%;
		margin: 0;
		padding: 0;
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
	/*.channel-box {*/
	/*	height: 20vh;*/
	/*}*/
	.channel-name {
		color: white;
		font-weight: bold;
		font-size: 12rem;
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
		padding: 0.75rem 1rem;
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
		/*border-radius: 25px;*/
		/*width: 200px;*/
		aspect-ratio: 1.732 / 1; /* Correct hexagon ratio */
		clip-path: polygon(
			15% 0%, 85% 0%, /* Top points */
			100% 50%, /* Right point */
			85% 100%, 15% 100%, /* Bottom points */
			0% 50% /* Left point */
		);
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
	/*.triangle-left {*/
	/*	width: 0;*/
	/*	height: 0;*/
	/*	border-top: 25px solid transparent;*/
	/*	border-right: 50px solid white;*/
	/*	border-bottom: 25px solid transparent;*/
	/*	!*background: white;*!*/
	/*}*/
	/*.triangle-right {*/
	/*	width: 0;*/
	/*	height: 0;*/
	/*	border-top: 25px solid transparent;*/
	/*	border-left: 50px solid white;*/
	/*	border-bottom: 25px solid transparent;*/
	/*	!*background: white;*!*/
	/*}*/
	/*.status-item-right {*/
	/*	color: black;*/
	/*	font-weight: bold;*/
	/*	font-size: 10rem;*/
	/*	margin: 0;*/
	/*	right: 0;*/
	/*	!*text-align: center;*!*/
	/*}*/
</style>
