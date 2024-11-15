<script>
  import RBCorner from "$/routes/RBCorner.svelte";
  import TimeCorner from "$/routes/TimeCorner.svelte";

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
				{#if data.channel_name.length > 20}
					<p class="channel-name" style="font-size: 8rem">{data.channel_name}</p>
				{:else if data.channel_name.length > 16}
					<p class="channel-name" style="font-size: 10rem">{data.channel_name}</p>
				{:else}
					<p class="channel-name" style="font-size: 12rem">{data.channel_name}</p>
				{/if}
			</div>
	</div>

	<div class="cell3">
		<TimeCorner />
	</div>

<!--	<div class="cell5">-->
<!--		<div class="cell-spacer"></div>-->
<!--	</div>-->

	<div class="cell4 rb-info-box columns is-multiline">
		<!--{#each data.info.statuses.slice(0, 4) as info, index}-->
			<div class="status-spacer column is-full">
				<div class="status-box columns">
					<div class="column is-two-thirds status-item">
						New Today
					</div>
					<div class="column is-one-third status-item">
						{data.new}
					</div>
				</div>
			</div>
			<div class="status-spacer column is-full">
				<div class="status-box columns">
					<div class="column is-three-quarters oldest-title">
						Oldest Open Order
					</div>
					<div class="column is-one-quarter oldest-item">
						{data.oldest}
					</div>
				</div>
			</div>
			<div class="status-spacer column is-full">
				<div class="status-box columns">
					<div class="column is-three-quarters oldest-title">
						Ready for Packing
					</div>
					<div class="column is-one-quarter status-item">
						{data.other.statuses[1].count}
					</div>
				</div>
			</div>
			<div class="status-spacer column is-full">
				<div class="status-box columns">
					<div class="column is-two-thirds status-item">
						Recalled
					</div>
					<div class="column is-one-third status-item">
						{data.cancelled}
					</div>
				</div>
			</div>
		<!--{/each}-->
	</div>

	<div class="cell5 rb-info-box columns is-multiline">
		<!--{#each data.info.statuses.slice(4) as info, index}-->
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
						{data.other.statuses[0].status}
					</div>
					<div class="column is-one-third status-item">
						{data.other.statuses[0].count}
					</div>
				</div>
			</div>
			<div class="status-spacer column is-full">
				<div class="status-box columns">
					<div class="column is-two-thirds status-item">
						Priority
					</div>
					<div class="column is-one-third status-item">
						{data.priority}
					</div>
				</div>
			</div>
			<div class="status-spacer column is-full">
				<div class="status-box columns">
					<div class="column is-two-thirds status-item">
						Out of Stock
					</div>
					<div class="column is-one-third status-item">
						{data.other.statuses[2].count}
					</div>
				</div>
			</div>
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
		padding: 1rem 0 0 1rem;
	}
	.cell5 {
		grid-area: 1 / 3 / 2 / 5;
		height: 100%;
		margin: 0;
		padding: 1rem 1rem 0 0;
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
	/*.channel-box {*/
	/*	height: 20vh;*/
	/*}*/
	.channel-name {
		white-space: nowrap;
		color: white;
		font-weight: bold;
		/*font-size: 12rem;*/
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
		padding: 1rem;
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
	}
	.status-item {
		color: black;
		font-weight: bold;
		font-size: 9rem;
		margin: 0;
		padding: 0;
		/*left: 0;*/
		text-align: center;
	}
	.oldest-item {
		color: black;
		font-weight: bold;
		font-size: 7rem;
		margin: 0;
		padding: 0;
		/*left: 0;*/
		text-align: center;
	}
	.oldest-title {
		color: black;
		font-weight: bold;
		font-size: 7rem;
		margin: 0;
		padding: 0;
		/*left: 0;*/
		text-align: center;
	}
</style>
