<script lang="ts">
	import axios from 'axios';
	import { goto } from '$app/navigation';

	// Reactive state variables
	let username = $state('');
	let password = $state('');
	let server_error: string = $state('');
	let errors = $state({ username: '', password: '' });

	// Validation function
	const validateForm = () => {
		let isValid = true;
		errors = { username: '', password: '' };

		if (!username.trim()) {
			errors.username = 'Username cannot be empty.';
			isValid = false;
		}

		if (!password.trim()) {
			errors.password = 'Password cannot be empty.';
			isValid = false;
		}

		return isValid;
	};

	// Form submission function
	const submitForm = async (event: Event) => {
		event.preventDefault();

		if (!validateForm()) return; // Stop submission if validation fails

		const data = new URLSearchParams();
		data.append('username', username);
		data.append('password', password);

		try {
			const response = await axios.post('http://localhost:8000/users/token', data, {
				headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
			});

			const token = response.data.access_token;
			localStorage.setItem('token', token); // Store token in localStorage

			// Redirect to home or dashboard
			goto('/');
		} catch (error: any) {
			if (error.response) {
				server_error = error.response.data.detail || 'Login failed.';
			} else {
				server_error = 'An unexpected error occurred.';
			}
		}
	};
</script>

<main class="mx-auto max-w-md px-4 py-12 sm:px-6 lg:px-8">
	<h1 class="mb-4 text-3xl font-bold">Login</h1>
	<div>
		{#if server_error}
			<p class="text-xs text-red-500">{server_error}</p>
		{/if}
	</div>

	<form onsubmit={submitForm} class="space-y-4">
		<!-- Username Field -->
		<div>
			<label for="username" class="block text-sm font-medium text-gray-700">Username</label>
			<input
				id="username"
				type="text"
				bind:value={username}
				class="mt-1 block w-full rounded-md border-gray-300 px-3 py-2 {errors.username
					? 'border-red-500'
					: ''}"
			/>
			{#if errors.username}
				<p class="mt-1 text-xs text-red-500">{errors.username}</p>
			{/if}
		</div>

		<!-- Password Field -->
		<div>
			<label for="password" class="block text-sm font-medium text-gray-700">Password</label>
			<input
				id="password"
				type="password"
				bind:value={password}
				class="mt-1 block w-full rounded-md border-gray-300 px-3 py-2 {errors.password
					? 'border-red-500'
					: ''}"
			/>
			{#if errors.password}
				<p class="mt-1 text-xs text-red-500">{errors.password}</p>
			{/if}
		</div>

		<a href="/register"> Register</a>
		<!-- Submit Button -->
		<button
			type="submit"
			class="w-full rounded-lg bg-indigo-600 px-4 py-2 text-white hover:bg-indigo-700"
		>
			Login
		</button>
	</form>
</main>
