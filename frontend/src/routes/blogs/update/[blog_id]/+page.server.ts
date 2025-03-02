// src/routes/blogs/[blog_id]/+server.ts
import { error } from '@sveltejs/kit';
import axios from 'axios';

export async function load({ params }) {
  const { blog_id } = params;
  try {
    const response = await axios.get(`http://localhost:8000/blogs/${blog_id}`);

    console.log(response.data)
    return { blogData: response.data };
  } catch (err) {
    if (axios.isAxiosError(err)) {
      console.error('Error Status Code:', err.response?.status);
    } else {
      console.error('Error:', err);
    }

    throw error(500, `Unable to fetch blog data for blog ID: ${blog_id}.`);
  }
}
