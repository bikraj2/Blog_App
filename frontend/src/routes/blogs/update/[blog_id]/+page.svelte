<script lang="ts">
	import { page } from '$app/state';
	import { error } from '@sveltejs/kit';
	import axios, { AxiosError, type AxiosPromise } from 'axios';
	let { data } = $props();
	let countErrors: number = $state(0);
	let errors: { [key: string]: any } = $state({
		title: '',
		content: '',
		category: ''
	});

	let title: string = $state(data.blogData.title);
	let content: string = $state(data.blogData.content);
	let readTime: string = $state(data.blogData.read_time);
	let category: string = $state(data.blogData.category);
	let version: string = $state(data.blogData.version);
	let id: string = $state(data.blogData.id);
	let server_error: string = $state('');
	// Assuming you already have the blog ID from the URL or passed as a prop
	let categories = ['Tech', 'Education', 'Business', 'Lifestyle', 'Entertainment'];

	const submitForm = async (event: Event) => {
		event.preventDefault();
		const data = {
			title: title,
			content: content,
			read_time: readTime,
			category: category,
			version: version
		};

		errors = {
			title: '',
			content: '',
			date: '',
			category: ''
		};

		countErrors = 0;
		if (!data.title || data.title.trim() === '') {
			errors.title = 'Title cannot be empty.';
			countErrors += 1;
		}

		// Validate content
		if (!data.content || data.content.trim() === '') {
			errors.content = 'Content cannot be empty.';
			countErrors += 1;
		}

		// Validate category
		if (!data.category || data.category.trim() === '') {
			errors.category = 'Please select a category';
			countErrors += 1;
		}

		if (
			!data.read_time ||
			!Number.isInteger(Number(data.read_time)) ||
			Number(data.read_time) <= 0
		) {
			errors.read_time = 'Read time must be a positive integer.';
			countErrors += 1;
		}

		if (countErrors > 0) {
			return;
		}

		// If validation passes, make the PUT request to update the blog
		try {
			const response = await axios.patch(`http://localhost:8000/blogs/${id}`, data);

			// Handle success response
			const blog = response.data;
			// Redirect to the blog's detail page
			window.location.href = `/blogs/${id}`;
		} catch (error: any) {
			if (error.response) {
				// The request was made and the server responded with an error

				const result = error.response.data;
				server_error = result.detail;
			} else {
				// Something went wrong while setting up the request
			}
		}
	};
</script>

<main class="mx-auto max-w-4xl px-4 py-12 sm:px-6 lg:px-8">
	<h1 class="mb-4 text-3xl font-bold">Edit Blog</h1>
	<form onsubmit={submitForm}>
		<div>
			{#if server_error}
				<p class="text-xs text-red-500">{server_error}</p>
			{/if}
		</div>

		<div>
			{#if errors.title}
				<p class="text-xs text-red-500">{errors.title}</p>
			{/if}
		</div>
		<div class="mb-4">
			<label for="title" class="block text-sm font-medium text-gray-700">Title</label>
			<input
				id="title"
				type="text"
				bind:value={title}
				class="mt-1 block w-full rounded-md border-gray-300"
			/>
		</div>

		<div>
			{#if errors.content}
				<p class="text-xs text-red-500">{errors.content}</p>
			{/if}
		</div>

		<div class="mb-4">
			<label for="content" class="block text-sm font-medium text-gray-700">Content</label>
			<textarea
				id="content"
				bind:value={content}
				class="mt-1 block h-48 w-full rounded-md border-gray-300"
			></textarea>
		</div>

		<div>
			{#if errors.category}
				<p class="text-xs text-red-500">{errors.category}</p>
			{/if}
		</div>
		<div class="mb-4">
			<label for="category" class="block text-sm font-medium text-gray-700">Category</label>
			<select
				id="category"
				bind:value={category}
				class="mt-1 block w-full rounded-md border-gray-300"
			>
				<option value="" disabled selected>Select a category</option>
				{#each categories as category}
					<option value={category}>{category}</option>
				{/each}
			</select>
		</div>

		<div>
			{#if errors.read_time}
				<p class="text-xs text-red-500">{errors.read_time}</p>
			{/if}
		</div>
		<div class="mb-4">
			<label for="readTime" class="block text-sm font-medium text-gray-700">Read Time (min)</label>
			<input
				id="readTime"
				type="text"
				bind:value={readTime}
				class="mt-1 block w-full rounded-md border-gray-300"
			/>
		</div>

		<button type="submit" class="rounded-lg bg-indigo-600 px-4 py-2 text-white">Update Blog</button>
	</form>
</main>
