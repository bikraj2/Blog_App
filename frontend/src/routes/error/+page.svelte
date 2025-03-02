<script lang="ts">
	export let status: number = 500;
	export let message: string = 'Something went wrong.';
</script>

<div class="flex min-h-screen flex-col items-center justify-center bg-gray-50 px-4 text-center">
	<h1 class="text-6xl font-bold text-red-600">{status}</h1>
	<p class="mt-2 text-xl text-gray-800">{message}</p>

	<a
		href="/"
		class="mt-6 rounded-lg bg-indigo-600 px-6 py-2 text-white transition hover:bg-indigo-700"
	>
		Go Home
	</a>
</div>
