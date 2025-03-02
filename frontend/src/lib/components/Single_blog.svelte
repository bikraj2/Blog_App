<script lang="ts">
	import axios from 'axios';
	import Confirm from './Confirm.svelte';
	import api from '$lib/api/api';
	import { onMount } from 'svelte';
	// Define the prop types
	export let title: string = '';
	export let id: string = '';
	export let content: string = '';
	export let date: string = '';
	export let author: string = '';
	export let read_time: string = '';
	export let category: string = '';

	export let isModalOpen = false;
	// Function to navigate to the Edit page
	let hasPermissions = false;
	let userData;
	const navigateToEdit = async () => {
		window.location.href = `/blogs/update/${id}`;
	};
	onMount(async () => {
		try {
			const user_info = await api.get('http://localhost:8000/users/');
			userData = user_info.data;
			console.log(userData);
			console.log(author);
			hasPermissions = userData.id == author;
		} catch (err) {}
	});

	const deleteBlog = async () => {
		// Logic for deleting the blog (for example, making an API call)
		try {
			const response = await api.delete(`http://localhost:8000/blogs/${id}`);
			// Handle success response

			console.log('Blog deleted:', response.data);
			// Optionally redirect after deleting
			// navigate to another page or show a success message
			window.location.pathname = '/blogs';
		} catch (error) {
			console.error('Error deleting blog:', error);
		}
	};
</script>

<div class="min-h-screen bg-gray-50">
	<!-- Navigation -->

	<!-- Blog Content -->
	<main class="mx-aublogto max-w-4xl px-4 py-12 sm:px-6 lg:px-8">
		<article class="overflow-hidden rounded-lg bg-white shadow">
			<!-- Hero Image -->
			<div class="relative h-64 w-full bg-gradient-to-r from-indigo-500 to-purple-600">
				<div class="absolute inset-0 flex items-center justify-center">
					<h1 class="px-4 text-center text-4xl font-bold text-white">{title}</h1>
				</div>
			</div>

			<!-- Meta Info -->
			<div class="border-b border-gray-100 px-6 py-4">
				<div class="flex items-center justify-between">
					<div class="flex items-center space-x-4">
						<div>
							<div class="text-sm font-medium text-gray-900">{author}</div>
							<div class="text-sm text-gray-500">{date} · {read_time} min</div>
						</div>
					</div>
					<div>
						<span
							class="inline-flex items-center rounded-full bg-indigo-100 px-3 py-0.5 text-sm font-medium text-indigo-800"
						>
							{category}
						</span>
					</div>
				</div>
			</div>

			<!-- Content -->
			<div class="prose lg:prose-lg max-w-none px-6 py-8">
				{@html content}
				<!-- Edit Button -->
				{#if hasPermissions}
					<div class="mt-6 flex justify-between">
						<!-- Delete Button -->
						<button
							class="inline-flex items-center rounded-lg bg-red-600 px-6 py-2 text-sm font-semibold text-white transition-all duration-200 hover:bg-red-700"
							onclick={() => (isModalOpen = true)}
						>
							<span>Delete</span>
						</button>

						<!-- Edit Button -->
						<button
							class="inline-flex items-center rounded-lg bg-indigo-600 px-6 py-2 text-sm font-semibold text-white transition-all duration-200 hover:bg-indigo-700"
							onclick={navigateToEdit}
						>
							<span>Edit</span>
						</button>
					</div>
				{/if}
			</div>
		</article>
		<Confirm
			isOpen={isModalOpen}
			onConfirm={() => {
				deleteBlog();
				isModalOpen = false;
			}}
			onCancel={() => (isModalOpen = false)}
			message="Are you sure you want to delete this blog? This action cannot be undone."
		/>
	</main>
</div>
