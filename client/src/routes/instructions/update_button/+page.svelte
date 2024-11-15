<script>
	import RBCorner from "$/routes/RBCorner.svelte";
	import TimeCorner from "$/routes/TimeCorner.svelte";
	import instruction from '$lib/images/update_button.webp';
</script>

<svelte:head>
	<title>Warehouse Overview</title>
	<meta name="description" content="Warehouse Overview" />
</svelte:head>

<div class="main">
	<div class="cell2">
		<RBCorner />
	</div>

	<div class="cell3">
		<TimeCorner />
	</div>

	<div class="cell1 rb-info-box">
		<div class="cell-spacer">
			<p class="channel-name">How to update the app?</p>
			<p class="channel-name">Press the home button, then the update button</p>
			<div class="logo">
            	<img src={instruction} alt="RexBrown Innovations" />
			</div>
		</div>
	</div>

	<div class="cell4">
<!--		<div class="cell-fill"></div>-->
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
    .logo > img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        height: auto;
        width: 50%;
        /*flex: 1;*/
        /*padding: 10%;*/
        /*padding-top: 25px;*/
        /*padding-bottom: 25px;*/
        /*padding-right: 10px;*/
        /*padding-left: 25px;*/
    }
    .logo {
        height: 100%;
        width: 100%;
        /*margin-top: 20px;*/
        /*margin-bottom: 20px;*/
        /*padding-top: 1rem;*/
    }
	.rb-info-box {
		background: black;
	}
	.channel-name {
		color: white;
		font-weight: bold;
		font-size: 10rem;
		text-align: center;
		padding-left: 2.5%;
		padding-right: 2.5%;
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
</style>
