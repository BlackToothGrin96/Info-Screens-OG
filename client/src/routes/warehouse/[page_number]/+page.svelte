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
	</div>

	<div class="cell2">
			<div class="title-box">
				<p class="channel-name">All Channels {data.page_number}/6</p>
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
		<div class="status-spacer column is-full">
			<div class="status-box-title columns">
				<div class="column is-half title-title">
					Channel
				</div>
				<div class="column is-half title-item">
					Open Orders
				</div>
			</div>
		</div>
		<!--{#if data.page_number === "1"}-->
			{#each data.info.slice(0, 6) as info, index}
				<div class="status-spacer column is-full">
					{#if info.open_count === 0}
						<div class="status-box columns done">
							{#if info.channel_code.length >= 25}
								<div class="column is-three-fifths status-title-done" style="font-size: 4rem">
									{info.channel_code}
								</div>
							{:else if info.channel_code.length >= 22}
								<div class="column is-three-fifths status-title-done" style="font-size: 4.5rem">
									{info.channel_code}
								</div>
							{:else if info.channel_code.length >= 18}
								<div class="column is-three-fifths status-title-done" style="font-size: 5rem">
									{info.channel_code}
								</div>
							{:else if info.channel_code.length >= 15}
								<div class="column is-three-fifths status-title-done" style="font-size: 5.5rem">
									{info.channel_code}
								</div>
							{:else}
								<div class="column is-three-fifths status-title-done">
									{info.channel_code}
								</div>
							{/if}
							<div class="column is-two-fifths status-item-done">
								{info.open_count}
							</div>
						</div>
					{:else}
						<div class="status-box columns">
							{#if info.channel_code.length >= 25}
								<div class="column is-three-fifths status-title" style="font-size: 4rem">
									{info.channel_code}
								</div>
							{:else if info.channel_code.length >= 22}
								<div class="column is-three-fifths status-title" style="font-size: 4.5rem">
									{info.channel_code}
								</div>
							{:else if info.channel_code.length >= 18}
								<div class="column is-three-fifths status-title" style="font-size: 5rem">
									{info.channel_code}
								</div>
							{:else if info.channel_code.length >= 15}
								<div class="column is-three-fifths status-title" style="font-size: 5.5rem">
									{info.channel_code}
								</div>
							{:else}
								<div class="column is-three-fifths status-title">
									{info.channel_code}
								</div>
							{/if}
							<div class="column is-two-fifths status-item">
								{info.open_count}
							</div>
						</div>
					{/if}
				</div>
			{/each}
		<!--{:else}-->
		<!--	{#each data.info.slice(13, 19) as info, index}-->
		<!--		<div class="status-spacer column is-full">-->
		<!--			{#if info.open_count === 0}-->
		<!--				<div class="status-box columns done">-->
		<!--					<div class="column is-three-fifths status-title-done">-->
		<!--						{info.channel_code}-->
		<!--					</div>-->
		<!--					<div class="column is-two-fifths status-item-done">-->
		<!--						{info.open_count}-->
		<!--					</div>-->
		<!--				</div>-->
		<!--			{:else}-->
		<!--				<div class="status-box columns">-->
		<!--					<div class="column is-three-fifths status-title">-->
		<!--						{info.channel_code}-->
		<!--					</div>-->
		<!--					<div class="column is-two-fifths status-item">-->
		<!--						{info.open_count}-->
		<!--					</div>-->
		<!--				</div>-->
		<!--			{/if}-->
		<!--		</div>-->
		<!--	{/each}-->
		<!--{/if}-->
	</div>

	<div class="cell5 rb-info-box columns is-multiline">
		<!--{#if data.page_number === "1"}-->
			{#each data.info.slice(6, 13) as info, index}
				<div class="status-spacer column is-full">
					{#if info.open_count === 0}
						<div class="status-box columns done">
							{#if info.channel_code.length >= 25}
								<div class="column is-three-fifths status-title-done" style="font-size: 4rem">
									{info.channel_code}
								</div>
							{:else if info.channel_code.length >= 22}
								<div class="column is-three-fifths status-title-done" style="font-size: 4.5rem">
									{info.channel_code}
								</div>
							{:else if info.channel_code.length >= 18}
								<div class="column is-three-fifths status-title-done" style="font-size: 5rem">
									{info.channel_code}
								</div>
							{:else if info.channel_code.length >= 15}
								<div class="column is-three-fifths status-title-done" style="font-size: 5.5rem">
									{info.channel_code}
								</div>
							{:else}
								<div class="column is-three-fifths status-title-done">
									{info.channel_code}
								</div>
							{/if}
							<div class="column is-two-fifths status-item-done">
								{info.open_count}
							</div>
						</div>
					{:else}
						<div class="status-box columns">
							{#if info.channel_code.length >= 25}
								<div class="column is-three-fifths status-title" style="font-size: 4rem">
									{info.channel_code}
								</div>
							{:else if info.channel_code.length >= 22}
								<div class="column is-three-fifths status-title" style="font-size: 4.5rem">
									{info.channel_code}
								</div>
							{:else if info.channel_code.length >= 18}
								<div class="column is-three-fifths status-title" style="font-size: 5rem">
									{info.channel_code}
								</div>
							{:else if info.channel_code.length >= 15}
								<div class="column is-three-fifths status-title" style="font-size: 5.5rem">
									{info.channel_code}
								</div>
							{:else}
								<div class="column is-three-fifths status-title">
									{info.channel_code}
								</div>
							{/if}
							<div class="column is-two-fifths status-item">
								{info.open_count}
							</div>
						</div>
					{/if}
				</div>
			{/each}
<!--		{:else}-->
<!--			{#each data.info.slice(19) as info, index}-->
<!--				<div class="status-spacer column is-full">-->
<!--					{#if info.open_count === 0}-->
<!--						<div class="status-box columns done">-->
<!--							<div class="column is-three-fifths status-title-done">-->
<!--								{info.channel_code}-->
<!--							</div>-->
<!--							<div class="column is-two-fifths status-item-done">-->
<!--								{info.open_count}-->
<!--							</div>-->
<!--						</div>-->
<!--					{:else}-->
<!--						<div class="status-box columns">-->
<!--							<div class="column is-three-fifths status-title">-->
<!--								{info.channel_code}-->
<!--							</div>-->
<!--							<div class="column is-two-fifths status-item">-->
<!--								{info.open_count}-->
<!--							</div>-->
<!--						</div>-->
<!--					{/if}-->
<!--				</div>-->
<!--			{/each}-->
<!--&lt;!&ndash;			<div class="cell-spacer">&ndash;&gt;-->
<!--&lt;!&ndash;				<p class="info-text">More Channels Will Appear Here As They Are Added To The System</p>&ndash;&gt;-->
<!--&lt;!&ndash;			</div>&ndash;&gt;-->
<!--		{/if}-->
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
		padding: 2rem 0 0 1rem;
	}
	.cell5 {
		grid-area: 1 / 3 / 2 / 5;
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
		font-size: 8rem;
		text-align: center;
		padding: 0;
		margin: 0;
	}
	.info-text {
		color: white;
		font-weight: bold;
		font-size: 6rem;
		text-align: center;
		padding: 2%;
		margin: 0;
	}
	.status-spacer {
		align-items: center;
		justify-content: center;
		display: flex;
		background: black;
		width: 100%;
		height: calc(100%/7.25);
		padding: 0.5rem;
		margin: 0;
	}
	.cell-spacer {
		align-items: center;
		justify-content: center;
		display: flex;
		background: black;
		width: 100%;
		height: 85%;
		padding: 0.5rem;
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
	.status-box-title {
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
	.status-title {
		white-space: nowrap;
		color: black;
		font-weight: bold;
		font-size: calc(1.75vw + 1.75vh + .75vmin);
		margin: 0;
		padding: 0 0 0 2%;
		/*left: 0;*/
		text-align: start;
	}
	.status-item {
		white-space: nowrap;
		color: black;
		font-weight: bold;
		font-size: calc(1.75vw + 1.75vh + .75vmin);
		margin: 0;
		padding: 0 2% 0 0;
		/*left: 0;*/
		text-align: end;
	}
	.title-title {
		white-space: nowrap;
		color: white;
		font-weight: bold;
		font-size: calc(1.75vw + 1.75vh + .75vmin);
		margin: 0;
		padding: 0 0 0 2%;
		/*left: 0;*/
		text-align: start;
	}
	.title-item {
		white-space: nowrap;
		color: white;
		font-weight: bold;
		font-size: calc(1.75vw + 1.75vh + .75vmin);
		margin: 0;
		padding: 0 2% 0 0;
		/*left: 0;*/
		text-align: end;
	}
	.done {
		background: green;
	}
	.status-title-done {
		white-space: nowrap;
		color: white;
		font-weight: bold;
		font-size: calc(1.75vw + 1.75vh + .75vmin);
		margin: 0;
		padding: 0 0 0 2%;
		/*left: 0;*/
		text-align: start;
	}
	.status-item-done {
		white-space: nowrap;
		color: white;
		font-weight: bold;
		font-size: calc(1.75vw + 1.75vh + .75vmin);
		margin: 0;
		padding: 0 2% 0 0;
		/*left: 0;*/
		text-align: end;
	}
	.cell-spacer {
		background: black;
		/*width: 100%;*/
		/*height: 100%;*/
		padding: 5px;
	}
</style>
