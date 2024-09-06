<script>
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';

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
	<div class="rb-info-box channel-box">
		<div class="side-box">
			<h1 class="channel-name">{data.channel_code} Users</h1>
			<!--{#each data.info.statuses as info, index}-->
			<!--	<h2 class="status-item">{info.status} - {info.count}</h2>-->
			<!--{/each}-->
		</div>
	</div>
	<div class="rb-info-box status-box">
		<div class="side-box">
<!--			<h1 class="channel-name">{data.info.channel_name}</h1>-->
			<h2 class="status-item"> Total Orders</h2>

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
