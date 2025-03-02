<script lang="ts">
	import { onMount } from 'svelte';

	// Declare the prop and initialize it
	let data = $props();

	let offset = $state(0); // Start from 0 to align with typical API conventions
	let limit = $state(10);
	let isLoading = $state(false);
	let allBlogsLoaded = $state(false);

	let blogsData = $state<any[]>([]);

	onMount(() => {
		blogsData = data.data.blogsData;
	});

	async function loadMore() {
		if (isLoading || allBlogsLoaded) return;

		isLoading = true;

		try {
			const response = await fetch(
				`http://localhost:8000/blogs?offset=${offset + limit}&limit=${limit}`
			);
			const newBlogs = await response.json();
			if (newBlogs.length === 0) {
				allBlogsLoaded = true;
			} else {
				blogsData = [...blogsData, ...newBlogs];
				offset += limit;
			}
		} catch (error) {
			console.error('Error loading more blogs:', error);
		} finally {
			isLoading = false;
		}
	}
</script>

<div class="min-h-screen bg-gray-50">
	<!-- Blog List -->
	<main class="mx-auto max-w-4xl px-4 py-12 sm:px-6 lg:px-8">
		<div class="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-3">
			{#each blogsData as blog}
				<div class="overflow-hidden rounded-lg bg-white shadow">
					<!-- Hero Image Placeholder -->
					<div class="relative h-48 w-full bg-gradient-to-r from-indigo-500 to-purple-600">
						<div class="absolute inset-0 flex items-center justify-center">
							<h1 class="px-4 text-center text-2xl font-bold text-white">{blog.title}</h1>
						</div>
					</div>

					<!-- Meta Info -->
					<div class="border-b border-gray-100 px-6 py-4">
						<div class="flex items-center justify-between">
							<div class="flex items-center space-x-4">
								<div class="flex h-10 w-10 items-center justify-center rounded-full bg-indigo-100">
									<span class="font-bold text-indigo-600">AC</span>
									<!-- Author Initials -->
								</div>
								<div>
									<div class="text-sm font-medium text-gray-900">Author Name</div>
									<div class="text-sm text-gray-500">
										{new Date(blog.created_at).toLocaleDateString()} · {blog.read_time} min read
									</div>
								</div>
							</div>
							<div>
								<span
									class="inline-flex items-center rounded-full bg-indigo-100 px-3 py-0.5 text-sm font-medium text-indigo-800"
								>
									{blog.category}
								</span>
							</div>
						</div>
					</div>

					<!-- Excerpt -->
					<div class="px-6 py-4">
						<p class="line-clamp-3 text-base text-gray-700">
							{@html blog.content.substring(0, 200)}...
						</p>
					</div>

					<!-- View More Link -->
					<div class="px-6 py-4">
						<a
							href={`/blogs/${blog.id}`}
							class="text-lg font-semibold text-indigo-600 hover:text-indigo-900"
						>
							Read More
						</a>
					</div>
				</div>
			{/each}
		</div>

		<!-- Load More Button -->
		<div class="mt-8 flex justify-center">
			<button
				class="rounded-lg bg-indigo-600 px-4 py-2 text-white hover:bg-indigo-700 disabled:opacity-50"
				onclick={loadMore}
				disabled={isLoading || allBlogsLoaded}
			>
				{#if isLoading}
					Loading...
				{:else}
					Load More
				{/if}
			</button>
		</div>
	</main>
</div>
