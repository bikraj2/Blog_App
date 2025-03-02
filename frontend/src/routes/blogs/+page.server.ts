import { json } from '@sveltejs/kit';

// Example of handling pagination in the server-side route
export async function load({ url }) {
  const offset = Number(url.searchParams.get('offset')) || 0;
  const limit = Number(url.searchParams.get('limit')) || 10;

  // Fetch the paginated data from your database or API (adjust as needed)
  const response = await fetch(`http://localhost:8000/blogs?offset=${offset}&limit=${limit}`);
  const data = await response.json();
  return {
    blogsData: data,  // Adjust this to match your response structure
  };
}
