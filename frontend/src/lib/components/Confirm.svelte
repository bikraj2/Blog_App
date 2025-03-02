<!-- src/lib/components/ConfirmModal.svelte -->
<script lang="ts">
	export let isOpen = false;
	export let onConfirm: () => void;
	export let onCancel: () => void;
	export let message = 'Are you sure you want to proceed?';
</script>

{#if isOpen}
	<!-- Soft Overlay (Blur instead of full black) -->
	<div
		class="bg-opacity-30 fixed inset-0 flex items-center justify-center bg-gray-900 backdrop-blur-sm"
	>
		<div class="w-96 rounded-lg bg-white p-6 shadow-lg">
			<h2 class="text-lg font-semibold text-gray-800">Confirm Action</h2>
			<p class="mt-2 text-gray-600">{message}</p>

			<div class="mt-4 flex justify-end gap-3">
				<button
					class="rounded-md bg-gray-300 px-4 py-2 text-gray-700 transition hover:bg-gray-400"
					on:click={onCancel}
				>
					Cancel
				</button>
				<button
					class="rounded-md bg-red-600 px-4 py-2 text-white transition hover:bg-red-700"
					on:click={onConfirm}
				>
					Delete
				</button>
			</div>
		</div>
	</div>
{/if}
