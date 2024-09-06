<script>
	import spinner from '$lib/images/loading2.gif';
	export let showModal; // boolean

	let dialog; // HTMLDialogElement

	$: if (dialog) {
        showModal ? dialog.showModal() : dialog.close();
    }
</script>

<dialog
	bind:this={dialog}
	on:close={() => (showModal = false)}>
<!--	on:click|self={() => dialog.close()}>-->
    <div class="modal-content">
          <p>Loading, please wait...</p>
          <img src="{spinner}" alt="Loading">
    </div>
</dialog>


<style>
	dialog {
		max-width: 32em;
		border-radius: 25px;
		border: none;
		padding: 0;
        background: black;
	}
    .modal-content {
        margin: auto;
    }
    .modal-content > p {
        font-size: 2rem;
		color: white;
		font-weight: bold;
        text-align: center;
    }
	dialog::backdrop {
		background: rgba(0, 0, 0, 0.4);
	}
	dialog > div {
		padding: 1em;
	}
	dialog[open] {
		animation: zoom 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
	}
	@keyframes zoom {
		from {
			transform: scale(0.95);
		}
		to {
			transform: scale(1);
		}
	}
	dialog[open]::backdrop {
		animation: fade 0.2s ease-out;
	}
	@keyframes fade {
		from {
			opacity: 0;
		}
		to {
			opacity: 1;
		}
	}
</style>