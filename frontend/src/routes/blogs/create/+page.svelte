<script lang="ts">
	import axios from 'axios';
	let title: string = $state('');
	let content: string = $state('');
	let date: string = $state(new Date().toISOString().split('T')[0]);
	let category: string = $state('');
	let readTime: string = $state('');
	let countErrors: number = $state(0);
	let errors: { [key: string]: any } = $state({
		title: '',
		content: '',
		date: '',
		category: ''
	});
	async function handleSubmit() {}
	let categories = ['Tech', 'Education', 'Business', 'Lifestyle', 'Entertainment'];
	let selectedCategory = $state(''); // Variable to hold the selected category
	const submitForm = async (event: Event) => {
		event.preventDefault();
		const data = {
			title: title,
			content: content,
			read_time: readTime,
			category: selectedCategory
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

		// Validate read_time (must be a positive integer)
		if (
			!data.read_time ||
			!Number.isInteger(Number(data.read_time)) ||
			Number(data.read_time) <= 0
		) {
			errors.read_time = 'Read time must be a positive integer.';
			countErrors += 1;
		}

		// If there are errors, don't submit the form
		if (countErrors > 0) {
			return;
		}

		try {
			const response = await axios.post('http://localhost:8000/blogs', data);

			// Handle success response
			const blog = response.data;

			// Redirect to the blog detail page using the result.id
			window.location.href = `/blogs/${blog.id}`;
		} catch (error: any) {
			if (error.response) {
				// The request was made and the server responded with an error
				const result = error.response.data;
				console.log(result);
			} else {
				// Something went wrong while setting up the request
				console.error('Error occurred:', error.message);
			}
		}
	};
</script>

<main class="mx-auto max-w-4xl px-4 py-12 sm:px-6 lg:px-8">
	<h1 class="mb-4 text-3xl font-bold">Create Blog</h1>
	<form onsubmit={submitForm}>
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
				class="mt-1 block w-full rounded-md border-gray-300 {errors.title ? 'border-red-500' : ''}"
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
				class="mt-1 block h-48 w-full rounded-md border-gray-300 {errors.content
					? 'border-red-500'
					: ''}"
			></textarea>
		</div>

		<div>
			{#if errors.date}
				<p class="text-xs text-red-500">{errors.date}</p>
			{/if}
		</div>

		<div class="mb-4">
			<label for="date" class="block text-sm font-medium text-gray-700">Date</label>
			<input
				id="date"
				type="date"
				bind:value={date}
				class="mt-1 block w-full rounded-md border-gray-300 {errors.date ? 'border-red-500' : ''}"
			/>
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
				bind:value={selectedCategory}
				class="mt-1 block w-full rounded-md border-gray-300 {errors.category
					? 'border-red-500'
					: ''}"
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
				class="mt-1 block w-full rounded-md border-gray-300 {errors.read_time
					? 'border-red-500'
					: ''}"
			/>
		</div>

		<button type="submit" class="rounded-lg bg-indigo-600 px-4 py-2 text-white">Create Blog</button>
	</form>
</main>
