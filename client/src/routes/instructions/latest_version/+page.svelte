<script>
	import RBCorner from "$/routes/RBCorner.svelte";
	import TimeCorner from "$/routes/TimeCorner.svelte";

	export let data;
</script>

<svelte:head>
	<title>Warehouse Overview</title>
	<meta name="description" content="Warehouse Overview" />
</svelte:head>

<div class="main">
	<div class="cell2">
		<RBCorner />
	</div>

<!--	<div class="cell2">-->
<!--			<div class="title-box">-->
<!--&lt;!&ndash;				<p class="channel-name">{data.channel_code.split("_").join(" ")}</p>&ndash;&gt;-->
<!--				&lt;!&ndash;{#each data.info.statuses as info, index}&ndash;&gt;-->
<!--				&lt;!&ndash;	<h2 class="status-item">{info.status} - {info.count}</h2>&ndash;&gt;-->
<!--				&lt;!&ndash;{/each}&ndash;&gt;-->
<!--			</div>-->
<!--	</div>-->

	<div class="cell3">
		<TimeCorner />
	</div>

	<div class="cell1 rb-info-box">
		<div class="cell-spacer">
<!--			<div class="status-box">-->
				<p class="channel-name">Latest App Version: V1.3.1 - Duplicate Collections</p>
<!--			<h1 class="channel-name">{data.info.channel_name}</h1>-->
<!--				<h2 class="status-item">{data.total} Total Orders</h2>-->

<!--				{#each data.info.statuses as info, index}-->
<!--					<h2 class="status-item">{info.status} - {info.count}</h2>-->
<!--				{/each}-->
<!--			</div>-->
		</div>
	</div>

	<div class="cell4">
		<div class="cell-fill"></div>
	</div>
<!--	<div class="cell5">-->
<!--		<div class="cell-fill"></div>-->
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
		background: black;
		grid-template-columns: 1fr 2fr 1fr;
		grid-template-rows: 1fr 3fr 1fr;
		grid-column-gap: 0px;
		grid-row-gap: 0px;
	}

	.cell1 { grid-area: 2 / 1 / 3 / 4; }
	.cell2 { grid-area: 3 / 1 / 4 / 2; }
	.cell3 { grid-area: 3 / 3 / 4 / 4; }
	.cell4 { grid-area: 1 / 1 / 2 / 4; }

	/*.side-box {*/
	/*	align-items: center;*/
	/*	justify-content: center;*/
	/*}*/
	/*.status-box {*/
	/*	background: black;*/
	/*	!*align-items: stretch;*!*/
	/*	!*justify-content: stretch;*!*/
	/*	!*width: 100%;*!*/
	/*	height: 100%;*/
    /*    !*height: 19%;*!*/
	/*	border-radius: 25px;*/
	/*}*/
	/*.title-box {*/
	/*	background: black;*/
	/*	align-items: center;*/
	/*	justify-content: center;*/
	/*	display: flex;*/
    /*    position: fixed;*/
	/*	top: 0;*/
    /*    height: 15%;*/
    /*    width: 50%;*/
	/*	border-bottom-right-radius: 25px;*/
	/*	border-bottom-left-radius: 25px;*/
	/*}*/
	.rb-info-box {
		background: black;
	}
	/*.channel-box {*/
	/*	height: 20vh;*/
	/*}*/
	.channel-name {
		color: white;
		font-weight: bold;
		font-size: 20rem;
		text-align: center;
		padding-left: 5%;
		padding-right: 5%;
		margin: 0;
	}
	.cell-spacer {
		background: black;
		/*width: 100%;*/
		/*height: 100%;*/
		padding: 5px;
	}
	.cell-fill {
		background: black;
		width: 100%;
		height: 100%;
		/*padding: 5px;*/
	}
	/*.status-item {*/
	/*	color: white;*/
	/*	font-weight: bold;*/
	/*	font-size: 2rem;*/
	/*	text-align: center;*/
	/*}*/
</style>
