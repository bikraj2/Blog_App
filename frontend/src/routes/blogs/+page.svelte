<script lang="ts">
	import { onMount } from 'svelte';
	import { page } from '$app/state';
	import api from '$lib/api/api';

	// Reactive state variables
	let blogsData = $state<any[]>([]);
	let currentPage = $state(1);
	let totalPages = $state(1);
	let limit = $state(9); // Number of blogs per page
	let isLoading = $state(false);

	// Fetch paginated blogs
	async function fetchBlogs(pageNumber: number) {
		isLoading = true;
		try {
			const offset = (pageNumber - 1) * limit;
			const response = await api.get(`http://localhost:8000/blogs?offset=${offset}&limit=${limit}`);

			// Get total count from headers
			console.log(response.data);
			const totalCount = Number(response.data.total_count || 0);
			totalPages = Math.ceil(totalCount / limit);
			blogsData = response.data.data;
			console.log(blogsData);
			currentPage = pageNumber;
		} catch (error) {
			console.error('Error fetching blogs:', error);
		} finally {
			isLoading = false;
		}
	}

	// Navigate to a specific page
	function goToPage(pageNumber: number) {
		if (pageNumber >= 1 && pageNumber <= totalPages) {
			fetchBlogs(pageNumber);
		}
	}

	// Fetch blogs on mount
	onMount(() => {
		fetchBlogs(currentPage);
	});
</script>

<div class="min-h-screen bg-gray-50">
	<!-- Blog List -->

	<div class="mt-6 mb-6 flex justify-center">
		<a
			href="/blogs/create"
			class="ml-4 rounded-lg bg-green-600 px-4 py-2 text-white hover:bg-green-700"
		>
			Create Blog
		</a>
	</div>

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
								<div>
									<div class="text-sm text-gray-500">
										{new Date(blog.created_at).toLocaleDateString()} <br />
										{blog.read_time} min read
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

		<div class="mt-8 flex justify-center space-x-2">
			<!-- Previous Button -->
			<button
				class="rounded-lg bg-gray-600 px-4 py-2 text-white hover:bg-gray-700 disabled:opacity-50"
				onclick={() => goToPage(currentPage - 1)}
				disabled={currentPage === 1}
			>
				Previous
			</button>

			<!-- Page Numbers -->
			{#each Array(totalPages) as _, index}
				<button
					class="rounded-lg px-4 py-2 font-semibold text-white
				{currentPage === index + 1 ? 'bg-indigo-600' : 'bg-gray-500 hover:bg-gray-700'}"
					onclick={() => goToPage(index + 1)}
					disabled={currentPage === index + 1}
				>
					{index + 1}
				</button>
			{/each}

			<!-- Next Button -->
			<button
				class="rounded-lg bg-indigo-600 px-4 py-2 text-white hover:bg-indigo-700 disabled:opacity-50"
				onclick={() => goToPage(currentPage + 1)}
				disabled={currentPage === totalPages}
			>
				Next
			</button>
		</div>
	</main>
</div>
