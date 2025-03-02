<script lang="ts">
	import '../app.css';
	import Footer from '$lib/components/Footer.svelte';
	import Navbar from '$lib/components/Navbar.svelte';
	let { children } = $props();
</script>

<div class="flex min-h-screen flex-col">
	<Navbar />

	<!-- Main Content: Uses flex-grow to fill available space -->
	<main class="flex-grow">
		{@render children()}
	</main>

	<Footer />
</div>
