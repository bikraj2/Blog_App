<script lang="ts">
	import SingleBlog from '$lib/components/Single_blog.svelte';
	import { onMount } from 'svelte';
	import { page } from '$app/state';
	import api from '$lib/api/api';
	import axios from 'axios';
	import { error } from '@sveltejs/kit';

	// Convert the data
	let blogPost: { [key: string]: string } = $state({});

	// Format created_at into a human-readable format
	let formattedDate = $state('');
	onMount(async () => {
		const { blog_id } = page.params;
		try {
			const response = await api.get(`http://localhost:8000/blogs/${blog_id}`);
			blogPost = response.data;

			formattedDate = new Date(blogPost.created_at).toLocaleDateString('en-US', {
				weekday: 'long',
				year: 'numeric',
				month: 'long',
				day: 'numeric'
			});
		} catch (err) {
			if (axios.isAxiosError(err)) {
				console.error('Error Status Code:', err.response?.status);
			} else {
				console.error('Error:', err);
			}
			window.location.pathname = '/blogs';
		}
	});
</script>

<!-- Render the data using SingleBlog component -->

<SingleBlog
	title={blogPost.title}
	content={blogPost.content}
	id={blogPost.id}
	date={formattedDate}
	author={blogPost.author_id}
	read_time={blogPost.read_time}
	category={blogPost.category}
/>
