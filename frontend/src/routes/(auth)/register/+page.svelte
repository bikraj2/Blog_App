<script lang="ts">
	import axios from 'axios';
	import { goto } from '$app/navigation';

	// Reactive state variables
	let username = $state('');
	let email = $state('');
	let full_name = $state('');
	let password = $state('');
	let confirmPassword = $state('');
	let server_error: string = $state('');
	let errors = $state({
		username: '',
		email: '',
		full_name: '',
		password: '',
		confirmPassword: ''
	});

	// Strong password regex: 8+ chars, 1 uppercase, 1 lowercase, 1 number, 1 special character
	const strongPasswordRegex =
		/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;

	// Validation function
	const validateForm = () => {
		let isValid = true;
		errors = { username: '', email: '', full_name: '', password: '', confirmPassword: '' };

		if (!username.trim()) {
			errors.username = 'Username cannot be empty.';
			isValid = false;
		}

		if (!email.trim() || !/^\S+@\S+\.\S+$/.test(email)) {
			errors.email = 'Please enter a valid email address.';
			isValid = false;
		}

		if (!full_name.trim()) {
			errors.full_name = 'Full name cannot be empty.';
			isValid = false;
		}

		if (!password.trim() || !strongPasswordRegex.test(password)) {
			errors.password =
				'Password must be at least 8 characters long and contain an uppercase letter, a lowercase letter, a number, and a special character.';
			isValid = false;
		}

		if (password !== confirmPassword) {
			errors.confirmPassword = 'Passwords do not match.';
			isValid = false;
		}

		return isValid;
	};

	// Form submission function
	const submitForm = async (event: Event) => {
		event.preventDefault();

		if (!validateForm()) return; // Stop submission if validation fails

		const data = { username, email, full_name, password };

		try {
			const response = await axios.post('http://localhost:8000/users/register', data);
			goto('/login'); // Redirect to login page after successful registration
		} catch (error: any) {
			if (error.response) {
				const result = error.response.data;
				server_error = result.detail;
			}
		}
	};
</script>

<main class="mx-auto max-w-md px-4 py-12 sm:px-6 lg:px-8">
	<h1 class="mb-4 text-3xl font-bold">Register</h1>
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

		<!-- Email Field -->
		<div>
			<label for="email" class="block text-sm font-medium text-gray-700">Email</label>
			<input
				id="email"
				type="email"
				bind:value={email}
				class="mt-1 block w-full rounded-md border-gray-300 px-3 py-2 {errors.email
					? 'border-red-500'
					: ''}"
			/>
			{#if errors.email}
				<p class="mt-1 text-xs text-red-500">{errors.email}</p>
			{/if}
		</div>

		<!-- Full Name Field -->
		<div>
			<label for="full_name" class="block text-sm font-medium text-gray-700">Full Name</label>
			<input
				id="full_name"
				type="text"
				bind:value={full_name}
				class="mt-1 block w-full rounded-md border-gray-300 px-3 py-2 {errors.full_name
					? 'border-red-500'
					: ''}"
			/>
			{#if errors.full_name}
				<p class="mt-1 text-xs text-red-500">{errors.full_name}</p>
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

		<!-- Confirm Password Field -->
		<div>
			<label for="confirmPassword" class="block text-sm font-medium text-gray-700"
				>Confirm Password</label
			>
			<input
				id="confirmPassword"
				type="password"
				bind:value={confirmPassword}
				class="mt-1 block w-full rounded-md border-gray-300 px-3 py-2 {errors.confirmPassword
					? 'border-red-500'
					: ''}"
			/>
			{#if errors.confirmPassword}
				<p class="mt-1 text-xs text-red-500">{errors.confirmPassword}</p>
			{/if}
		</div>

		<!-- Submit Button -->
		<button
			type="submit"
			class="w-full rounded-lg bg-indigo-600 px-4 py-2 text-white hover:bg-indigo-700"
		>
			Register
		</button>
	</form>
</main>
