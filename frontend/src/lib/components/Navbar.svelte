<script lang="ts">
	import { page } from '$app/state';
	import { slide } from 'svelte/transition';
	import { quintOut } from 'svelte/easing';
	import { get, writable } from 'svelte/store';

	let isOpen = writable(false);

	const toggleMenu = () => {
		isOpen.update((v) => !v);
	};

	// Navigation links
	let navLinks = [
		{ href: '/', label: 'Home' },
		{ href: '/blogs', label: 'Blogs' },
		{ href: '/login', label: 'Login' }
	];
	// Action links (like Logout)
	const logout = () => {
		console.log('User logged out');
		localStorage.clear();
	};

	let actionLinks = [{ label: 'Logout', action: logout }];

	let activePath = page.url.pathname;
</script>

<header class="sticky top-0 z-50 border-b border-gray-100 bg-white/80 shadow-sm backdrop-blur-md">
	<div class="container mx-auto px-4 sm:px-6 lg:px-8">
		<div class="flex h-16 items-center justify-between">
			<!-- Logo -->
			<div class="flex flex-shrink-0 items-center">
				<a href="/" class="flex items-center">
					<span
						class="bg-gradient-to-r from-indigo-600 to-purple-600 bg-clip-text text-2xl font-bold text-transparent"
					>
						Fast Blog
					</span>
				</a>
			</div>

			<!-- Desktop Nav -->
			<div class="hidden items-center space-x-8 md:flex">
				{#each navLinks as { href, label }}
					<a
						{href}
						class="group relative text-sm font-medium transition-colors duration-200
              {activePath === href ? 'text-indigo-600' : 'text-gray-700'}"
					>
						{label}
						<span
							class="absolute -bottom-1 left-0 h-0.5 bg-indigo-600 transition-all duration-200
                {activePath === href ? 'w-full' : 'w-0'} group-hover:w-full"
						></span>
					</a>
				{/each}

				<!-- Action Links (Logout) -->
				{#each actionLinks as { label, action }}
					<button
						on:click={action}
						class="rounded-full bg-red-600 px-4 py-2 text-sm font-medium text-white transition-all duration-200 hover:bg-red-700"
					>
						{label}
					</button>
				{/each}
			</div>

			<!-- Mobile menu button -->
			<div class="flex items-center md:hidden">
				<button
					on:click={toggleMenu}
					class="inline-flex items-center justify-center rounded-md p-2 text-gray-700 hover:text-indigo-600 focus:outline-none"
					aria-expanded={get(isOpen)}
				>
					<span class="sr-only">Open main menu</span>
					{#if get(isOpen)}
						<svg
							class="block h-6 w-6"
							xmlns="http://www.w3.org/2000/svg"
							fill="none"
							viewBox="0 0 24 24"
							stroke="currentColor"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M6 18L18 6M6 6l12 12"
							/>
						</svg>
					{:else}
						<svg
							class="block h-6 w-6"
							xmlns="http://www.w3.org/2000/svg"
							fill="none"
							viewBox="0 0 24 24"
							stroke="currentColor"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M4 6h16M4 12h16m-7 6h7"
							/>
						</svg>
					{/if}
				</button>
			</div>
		</div>
	</div>

	<!-- Mobile menu -->
	{#if get(isOpen)}
		<div
			transition:slide={{ duration: 300, easing: quintOut }}
			class="rounded-b-lg bg-white shadow-lg md:hidden"
		>
			<div class="space-y-1 px-2 pt-2 pb-3 sm:px-3">
				{#each navLinks as { href, label }}
					<a
						{href}
						class="block rounded-md px-3 py-2 text-base font-medium transition-colors duration-200
              {activePath === href ? 'bg-indigo-600 text-white' : 'text-gray-700 hover:bg-gray-50'}"
					>
						{label}
					</a>
				{/each}

				<!-- Action Links (Logout) -->
				{#each actionLinks as { label, action }}
					<button
						on:click={action}
						class="block w-full rounded-md bg-red-600 px-4 py-2 text-base font-medium text-white transition-all duration-200 hover:bg-red-700"
					>
						{label}
					</button>
				{/each}
			</div>
		</div>
	{/if}
</header>
