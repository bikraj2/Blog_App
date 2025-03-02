<script lang="ts">
	import { onMount } from 'svelte';
	import { writable } from 'svelte/store'; // Import writable store

	// Initialize the store for currentSection
	const currentSection = writable('introduction');

	const sections = [
		{ id: 'introduction', title: 'Introduction' },
		{ id: 'collection', title: 'Information Collection' },
		{ id: 'usage', title: 'How We Use Information' },
		{ id: 'sharing', title: 'Information Sharing' },
		{ id: 'cookies', title: 'Cookies & Tracking' },
		{ id: 'security', title: 'Data Security' },
		{ id: 'children', title: "Children's Privacy" },
		{ id: 'international', title: 'International Transfers' },
		{ id: 'rights', title: 'Your Rights' },
		{ id: 'retention', title: 'Data Retention' },
		{ id: 'changes', title: 'Changes to Privacy Policy' },
		{ id: 'contact', title: 'Contact Information' }
	];

	const lastUpdated = 'March 1, 2025';

	function scrollToSection(id) {
		const element = document.getElementById(id);
		if (element) {
			element.scrollIntoView({ behavior: 'smooth' });
			currentSection.set(id); // Update the current section in the store
		}
	}

	onMount(() => {
		const observer = new IntersectionObserver(
			(entries) => {
				entries.forEach((entry) => {
					if (entry.isIntersecting) {
						currentSection.set(entry.target.id); // Update the current section in the store
					}
				});
			},
			{ threshold: 0.5 }
		);

		sections.forEach((section) => {
			const element = document.getElementById(section.id);
			if (element) observer.observe(element);
		});

		return () => {
			sections.forEach((section) => {
				const element = document.getElementById(section.id);
				if (element) observer.unobserve(element);
			});
		};
	});
</script>

<svelte:head>
	<title>Privacy Policy | Brand</title>
	<meta name="description" content="Privacy Policy for Brand's products and services" />
</svelte:head>

<div class="bg-gray-50">
	<div class="container mx-auto px-4 py-16 sm:px-6 lg:px-8">
		<div class="mx-auto max-w-3xl">
			<h1 class="mb-6 text-4xl font-bold text-gray-900">Privacy Policy</h1>
			<p class="mb-8 text-sm text-gray-500">Last Updated: {lastUpdated}</p>

			<div class="prose prose-indigo mb-12 max-w-none">
				<p class="lead">
					At Brand, we value your privacy and are committed to protecting your personal information.
					This Privacy Policy explains how we collect, use, and safeguard your information when you
					use our services.
				</p>
			</div>

			<div class="grid grid-cols-1 gap-8 lg:grid-cols-4">
				<!-- Table of Contents - Sticky on large screens -->
				<aside class="lg:col-span-1">
					<div class="sticky top-24 rounded-lg border border-gray-100 bg-white p-5 shadow-sm">
						<h2 class="mb-4 text-lg font-semibold">Contents</h2>
						<nav>
							<ul class="space-y-2">
								{#each sections as { id, title }}
									<li>
										<button
											on:click={() => scrollToSection(id)}
											class="w-full rounded px-2 py-1 text-left text-sm transition-colors duration-200"
											class:text-indigo-600={currentSection === id}
											class:bg-indigo-50={currentSection === id}
											class:font-medium={currentSection === id}
											class:text-gray-600={currentSection !== id}
											class:hover:text-indigo-500={currentSection !== id}
										>
											{title}
										</button>
									</li>
								{/each}
							</ul>
						</nav>
					</div>
				</aside>

				<!-- Privacy Policy Content -->
				<div class="lg:col-span-3">
					<div class="prose prose-indigo max-w-none">
						<section id="introduction" class="mb-12">
							<h2>1. Introduction</h2>
							<p>
								This Privacy Policy ("Policy") describes how Brand, Inc. ("Brand," "we," "us," or
								"our") collects, uses, and discloses information about you when you visit our
								website, use our mobile applications, or interact with our other services
								(collectively, the "Services").
							</p>
							<p>
								By using our Services, you agree to the collection, use, and disclosure of your
								information as described in this Policy. If you do not agree with our policies and
								practices, do not use our Services.
							</p>
							<p>This Policy applies to information we collect:</p>
							<ul>
								<li>On our website and mobile applications;</li>
								<li>
									Through email, text, and other electronic communications between you and us;
								</li>
								<li>
									When you interact with our advertising and content on third-party websites and
									services; and
								</li>
								<li>Offline or through any other means when you interact with us.</li>
							</ul>
						</section>

						<section id="collection" class="mb-12">
							<h2>2. Information Collection</h2>
							<p>We collect several types of information from and about users of our Services:</p>

							<h3>Information You Provide to Us</h3>
							<p>We collect information that you provide directly to us, such as:</p>
							<ul>
								<li>
									Account information: When you create an account, we collect your name, email
									address, password, and other registration information;
								</li>
								<li>
									Profile information: Information you add to your profile, such as a profile
									picture, biography, and preferences;
								</li>
								<li>
									Content you create: Any content you create, upload, or share through our Services;
								</li>
								<li>
									Communications: Information you provide when you contact us, respond to surveys,
									or communicate with other users;
								</li>
								<li>
									Transaction information: Details about purchases or transactions you make through
									our Services, including payment information; and
								</li>
								<li>
									Marketing preferences: Your preferences for receiving marketing communications
									from us.
								</li>
							</ul>

							<h3>Information We Collect Automatically</h3>
							<p>
								When you use our Services, we automatically collect certain information, such as:
							</p>
							<ul>
								<li>
									Device information: Information about your device, including IP address, device
									type, operating system, browser type, and device identifiers;
								</li>
								<li>
									Usage information: Information about how you use our Services, including the pages
									you visit, the features you use, and the time and duration of your visits;
								</li>
								<li>
									Location information: General location information (such as the city or country
									from which you access our Services);
								</li>
								<li>
									Log information: Information that your browser or device automatically sends when
									you use our Services, including server logs and error reports; and
								</li>
								<li>
									Cookies and similar technologies: Information collected through cookies, web
									beacons, and similar technologies (see the "Cookies & Tracking" section below).
								</li>
							</ul>

							<h3>Information We Receive From Other Sources</h3>
							<p>We may receive information about you from other sources, such as:</p>
							<ul>
								<li>
									Business partners: Information from our business partners, such as payment
									processors, analytics providers, and advertising partners;
								</li>
								<li>
									Social media platforms: Information from social media platforms when you connect
									your account to our Services or interact with us on social media; and
								</li>
								<li>
									Public sources: Information from publicly available sources, such as public social
									media profiles.
								</li>
							</ul>
						</section>

						<section id="usage" class="mb-12">
							<h2>3. How We Use Information</h2>
							<p>We use the information we collect for various purposes, including:</p>

							<h3>Providing and Improving Our Services</h3>
							<ul>
								<li>To provide, maintain, and improve our Services;</li>
								<li>To develop new products, services, and features;</li>
								<li>
									To personalize your experience and deliver content tailored to your interests;
								</li>
								<li>To process transactions and fulfill your requests;</li>
								<li>To respond to your inquiries and provide customer support; and</li>
								<li>To monitor and analyze usage patterns and trends.</li>
							</ul>

							<h3>Communications</h3>
							<ul>
								<li>To communicate with you about your account, transactions, or requests;</li>
								<li>
									To send you technical notices, updates, security alerts, and administrative
									messages;
								</li>
								<li>
									To send you marketing communications about our products, services, and promotions,
									if you have opted in to receive them; and
								</li>
								<li>To facilitate communications between users, where applicable.</li>
							</ul>

							<h3>Security and Protection</h3>
							<ul>
								<li>To protect the security and integrity of our Services;</li>
								<li>
									To detect, prevent, and address fraud, unauthorized access, and other potentially
									illegal activities;
								</li>
								<li>To enforce our Terms of Service and other policies; and</li>
								<li>
									To comply with legal obligations and protect our rights, privacy, safety, or
									property, and that of our users and the public.
								</li>
							</ul>

							<h3>Analytics and Research</h3>
							<ul>
								<li>To understand how users interact with our Services;</li>
								<li>To measure the effectiveness of our advertising and marketing;</li>
								<li>To improve our algorithms and recommendation systems; and</li>
								<li>To conduct research and develop new features and services.</li>
							</ul>
						</section>

						<section id="sharing" class="mb-12">
							<h2>4. Information Sharing</h2>
							<p>We may share your information in the following circumstances:</p>

							<h3>With Your Consent</h3>
							<p>We may share your information when you give us explicit consent to do so.</p>

							<h3>With Service Providers</h3>
							<p>
								We share information with third-party service providers who perform services on our
								behalf, such as:
							</p>
							<ul>
								<li>Hosting and infrastructure providers;</li>
								<li>Payment processors;</li>
								<li>Customer support providers;</li>
								<li>Analytics providers; and</li>
								<li>Advertising and marketing partners.</li>
							</ul>

							<h3>For Legal and Safety Purposes</h3>
							<p>
								We may share information when we believe it is necessary to comply with a legal
								obligation, enforce our policies, protect the rights, property, or safety of Brand,
								our users, or others, or in connection with a corporate transaction, such as a
								merger, sale, or acquisition.
							</p>

							<h3>With Affiliates</h3>
							<p>
								We may share information with our affiliated companies, but they will be bound by
								this Policy.
							</p>

							<h3>With Business Transfers</h3>
							<p>
								We may share or transfer your information in connection with a merger, sale, or
								other business transfer, as permitted by law.
							</p>
						</section>

						<section id="cookies" class="mb-12">
							<h2>5. Cookies & Tracking</h2>
							<p>
								We use cookies and similar tracking technologies to collect information about your
								interactions with our Services.
							</p>
						</section>

						<section id="security" class="mb-12">
							<h2>6. Data Security</h2>
							<p>
								We take reasonable measures to protect your data, but we cannot guarantee complete
								security.
							</p>
						</section>

						<section id="children" class="mb-12">
							<h2>7. Children's Privacy</h2>
							<p>We do not knowingly collect information from children under 13.</p>
						</section>

						<section id="international" class="mb-12">
							<h2>8. International Transfers</h2>
							<p>
								Your data may be transferred to, and maintained on, servers outside your state or
								country.
							</p>
						</section>

						<section id="rights" class="mb-12">
							<h2>9. Your Rights</h2>
							<p>You have rights to access, correct, and delete your personal data.</p>
						</section>

						<section id="retention" class="mb-12">
							<h2>10. Data Retention</h2>
							<p>
								We retain your data only for as long as necessary for the purposes outlined in this
								Privacy Policy.
							</p>
						</section>

						<section id="changes" class="mb-12">
							<h2>11. Changes to Privacy Policy</h2>
							<p>
								We may update this Privacy Policy from time to time. Please check for updates
								periodically.
							</p>
						</section>

						<section id="contact" class="mb-12">
							<h2>12. Contact Information</h2>
							<p>If you have questions, feel free to contact us at support@brand.com.</p>
						</section>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>
