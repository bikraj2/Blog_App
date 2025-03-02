<script lang="ts">
	import SingleBlog from '$lib/components/Single_blog.svelte';
	export let data: { blogData: any }; // Define the type of `data`

	// Convert the data
	let blogPost = JSON.parse(JSON.stringify(data.blogData)); // Convert the string back to JSON

	// Format created_at into a human-readable format
	let formattedDate = new Date(blogPost.created_at).toLocaleDateString('en-US', {
		weekday: 'long',
		year: 'numeric',
		month: 'long',
		day: 'numeric'
	});
</script>

<!-- Render the data using SingleBlog component -->

<SingleBlog
	title={blogPost.title}
	content={blogPost.content}
	id={blogPost.id}
	date={formattedDate}
	author={blogPost.author}
	read_time={blogPost.read_time}
	category={blogPost.category}
/>
