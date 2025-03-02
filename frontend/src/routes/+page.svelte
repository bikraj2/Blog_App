<!-- src/lib/components/Hero.svelte -->
<script lang="ts">
	export let title: string = 'Welcome to the Blog';
	export let subtitle: string = 'Discover insightful articles and stories curated just for you.';
</script>

<div
	class="relative flex min-h-[50vh] flex-col items-center justify-center bg-gradient-to-r from-indigo-500 to-purple-600 px-6 text-center text-white"
>
	<h1 class="text-4xl font-extrabold sm:text-5xl">{title}</h1>
	<p class="mt-4 max-w-2xl text-lg text-white/90 sm:text-xl">{subtitle}</p>

	<a
		href="/blogs"
		class="mt-6 rounded-lg bg-white px-6 py-3 font-semibold text-indigo-600 shadow-lg transition-all hover:bg-gray-100"
	>
		Explore Blogs
	</a>
</div>
