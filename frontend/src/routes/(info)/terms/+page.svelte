<!-- src/routes/terms/+page.svelte -->
<script lang="ts">
	import { onMount } from 'svelte';

	let currentSection = $state('introduction');

	const sections = [
		{ id: 'introduction', title: 'Introduction' },
		{ id: 'acceptance', title: 'Acceptance of Terms' },
		{ id: 'services', title: 'Services Description' },
		{ id: 'eligibility', title: 'Eligibility' },
		{ id: 'accounts', title: 'Accounts & Registration' },
		{ id: 'content', title: 'User Content' },
		{ id: 'license', title: 'License Grant' },
		{ id: 'rules', title: 'Rules of Conduct' },
		{ id: 'payments', title: 'Payments & Billing' },
		{ id: 'termination', title: 'Termination' },
		{ id: 'warranty', title: 'Disclaimer of Warranty' },
		{ id: 'liability', title: 'Limitation of Liability' },
		{ id: 'disputes', title: 'Dispute Resolution' },
		{ id: 'changes', title: 'Changes to Terms' },
		{ id: 'contact', title: 'Contact Information' }
	];

	const lastUpdated = 'March 1, 2025';

	function scrollToSection(id) {
		const element = document.getElementById(id);
		if (element) {
			element.scrollIntoView({ behavior: 'smooth' });
			currentSection = id;
		}
	}

	onMount(() => {
		const observer = new IntersectionObserver(
			(entries) => {
				entries.forEach((entry) => {
					if (entry.isIntersecting) {
						currentSection = entry.target.id;
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
	<title>Terms of Service | Brand</title>
	<meta name="description" content="Terms of Service for Brand's products and services" />
</svelte:head>

<div class="bg-gray-50">
	<div class="container mx-auto px-4 py-16 sm:px-6 lg:px-8">
		<div class="mx-auto max-w-3xl">
			<h1 class="mb-6 text-4xl font-bold text-gray-900">Terms of Service</h1>
			<p class="mb-8 text-sm text-gray-500">Last Updated: {lastUpdated}</p>

			<div class="prose prose-indigo mb-12 max-w-none">
				<p class="lead">
					Welcome to Brand. Please read these Terms of Service carefully before using our platform.
					By accessing or using our services, you agree to be bound by these terms.
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

				<!-- Terms Content -->
				<div class="lg:col-span-3">
					<div class="prose prose-indigo max-w-none">
						<section id="introduction" class="mb-12">
							<h2>1. Introduction</h2>
							<p>
								These Terms of Service ("Terms") govern your access to and use of Brand's website,
								products, and services ("Services"). These Terms constitute a legally binding
								agreement between you and Brand, Inc. ("Brand," "we," "us," or "our").
							</p>
							<p>
								By accessing or using our Services, you acknowledge that you have read, understood,
								and agree to be bound by these Terms. If you do not agree to these Terms, you must
								not access or use our Services.
							</p>
						</section>

						<section id="acceptance" class="mb-12">
							<h2>2. Acceptance of Terms</h2>
							<p>You accept these Terms by:</p>
							<ul>
								<li>
									Clicking to accept or agree to the Terms where this option is made available to
									you;
								</li>
								<li>Creating an account or signing up for our Services;</li>
								<li>
									Using or accessing our Services in any manner, even if you have not created an
									account; or
								</li>
								<li>Continuing to use our Services after we have posted updates to these Terms.</li>
							</ul>
							<p>
								If you are using our Services on behalf of a company, organization, or other entity,
								you represent and warrant that you have the authority to bind that entity to these
								Terms, in which case "you" will refer to that entity.
							</p>
						</section>

						<section id="services" class="mb-12">
							<h2>3. Services Description</h2>
							<p>
								Brand provides a platform that allows users to [brief description of your services].
								Our Services include any new features, tools, or functionality that we may add to
								the platform.
							</p>
							<p>
								We reserve the right to modify, suspend, or discontinue our Services, temporarily or
								permanently, at any time, with or without notice. You agree that we will not be
								liable to you or any third party for any modification, suspension, or
								discontinuation of our Services.
							</p>
						</section>

						<section id="eligibility" class="mb-12">
							<h2>4. Eligibility</h2>
							<p>To use our Services, you must:</p>
							<ul>
								<li>
									Be at least 18 years old, or the age of legal majority in your jurisdiction,
									whichever is greater;
								</li>
								<li>Have the legal capacity to enter into these Terms;</li>
								<li>Complete the registration process, if applicable;</li>
								<li>Agree to these Terms; and</li>
								<li>Comply with all applicable laws and regulations.</li>
							</ul>
							<p>
								If you are using our Services on behalf of a business, you represent and warrant
								that you have the authority to bind that business to these Terms.
							</p>
						</section>

						<section id="accounts" class="mb-12">
							<h2>5. Accounts & Registration</h2>
							<p>
								To access certain features of our Services, you may need to create an account. When
								you create an account, you must provide accurate, current, and complete information.
								You are responsible for maintaining the confidentiality of your account credentials
								and for all activities that occur under your account.
							</p>
							<p>You agree to:</p>
							<ul>
								<li>
									Immediately notify us of any unauthorized use of your account or any other breach
									of security;
								</li>
								<li>Not share your account credentials with any third party;</li>
								<li>Not transfer, sell, or assign your account to anyone else; and</li>
								<li>
									Log out from your account at the end of each session when using a shared computer.
								</li>
							</ul>
							<p>
								We reserve the right to disable any account, at any time, if we believe that you
								have violated these Terms.
							</p>
						</section>

						<section id="content" class="mb-12">
							<h2>6. User Content</h2>
							<p>
								Our Services may allow you to create, upload, post, send, receive, store, share, and
								otherwise make available content, including but not limited to text, images, audio,
								video, and other materials ("User Content").
							</p>
							<p>
								You retain all ownership rights to your User Content. However, by submitting User
								Content to our platform, you grant us a worldwide, non-exclusive, royalty-free,
								sublicensable, and transferable license to use, reproduce, distribute, prepare
								derivative works of, display, and perform your User Content in connection with our
								Services.
							</p>
							<p>You represent and warrant that:</p>
							<ul>
								<li>You own or have the necessary rights to your User Content;</li>
								<li>
									Your User Content does not violate the rights of any third party, including
									intellectual property rights and privacy rights; and
								</li>
								<li>
									Your User Content complies with these Terms and all applicable laws and
									regulations.
								</li>
							</ul>
						</section>

						<section id="license" class="mb-12">
							<h2>7. License Grant</h2>
							<p>
								Subject to your compliance with these Terms, we grant you a limited, non-exclusive,
								non-transferable, non-sublicensable license to access and use our Services for your
								personal or internal business purposes.
							</p>
							<p>This license does not include the right to:</p>
							<ul>
								<li>Modify, reverse engineer, decompile, or disassemble our Services;</li>
								<li>
									Rent, lease, loan, sell, sublicense, distribute, or otherwise transfer the license
									to any third party;
								</li>
								<li>
									Copy, reproduce, distribute, publicly display, or publicly perform our Services;
								</li>
								<li>Remove, alter, or obscure any proprietary notices on our Services; or</li>
								<li>
									Use our Services in any way that violates these Terms or applicable laws and
									regulations.
								</li>
							</ul>
						</section>

						<section id="rules" class="mb-12">
							<h2>8. Rules of Conduct</h2>
							<p>While using our Services, you agree not to:</p>
							<ul>
								<li>Violate any applicable laws, regulations, or third-party rights;</li>
								<li>
									Use our Services for any illegal, harmful, fraudulent, or malicious purpose;
								</li>
								<li>
									Post, upload, or share any content that is illegal, harmful, threatening, abusive,
									harassing, defamatory, vulgar, obscene, invasive of privacy, or otherwise
									objectionable;
								</li>
								<li>
									Impersonate any person or entity, or falsely state or otherwise misrepresent your
									affiliation with a person or entity;
								</li>
								<li>
									Interfere with or disrupt our Services or servers or networks connected to our
									Services;
								</li>
								<li>
									Attempt to gain unauthorized access to our Services, user accounts, or computer
									systems;
								</li>
								<li>Collect or store personal data about other users without their consent;</li>
								<li>
									Use automated means, including spiders, robots, crawlers, data mining tools, or
									similar methods to access our Services;
								</li>
								<li>
									Transmit any viruses, worms, defects, Trojans, or other items of a destructive
									nature; or
								</li>
								<li>
									Engage in any activity that would constitute a criminal offense or give rise to
									civil liability.
								</li>
							</ul>
						</section>

						<section id="payments" class="mb-12">
							<h2>9. Payments & Billing</h2>
							<p>
								Certain aspects of our Services may require payment. You agree to provide accurate
								and complete billing information and to keep this information updated.
							</p>
							<p>For subscription-based services:</p>
							<ul>
								<li>
									Your subscription will automatically renew unless you cancel it at least 24 hours
									before the end of the current billing period;
								</li>
								<li>
									You authorize us to charge your payment method for the subscription fees at the
									beginning of each billing period;
								</li>
								<li>
									If your payment cannot be completed, we may suspend or terminate your access to
									our Services;
								</li>
								<li>
									We reserve the right to change our subscription fees at any time with reasonable
									notice; and
								</li>
								<li>Refunds are provided in accordance with our Refund Policy.</li>
							</ul>
						</section>

						<section id="termination" class="mb-12">
							<h2>10. Termination</h2>
							<p>
								We may terminate or suspend your access to our Services, including your account, at
								any time and for any reason, without prior notice or liability, if you violate these
								Terms.
							</p>
							<p>
								You may terminate your account at any time by following the instructions on our
								platform. Upon termination:
							</p>
							<ul>
								<li>Your right to use our Services will immediately cease;</li>
								<li>
									We may delete your account and all associated data, unless we are required to
									retain it by law;
								</li>
								<li>Any outstanding payments will become immediately due; and</li>
								<li>
									All provisions of these Terms that by their nature should survive termination
									shall survive termination.
								</li>
							</ul>
						</section>

						<section id="warranty" class="mb-12">
							<h2>11. Disclaimer of Warranty</h2>
							<p>
								OUR SERVICES ARE PROVIDED "AS IS" AND "AS AVAILABLE," WITHOUT WARRANTY OF ANY KIND,
								EITHER EXPRESS OR IMPLIED. WE EXPRESSLY DISCLAIM ALL WARRANTIES, INCLUDING BUT NOT
								LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
								PURPOSE, AND NON-INFRINGEMENT.
							</p>
							<p>We do not warrant that:</p>
							<ul>
								<li>Our Services will meet your requirements;</li>
								<li>Our Services will be uninterrupted, timely, secure, or error-free;</li>
								<li>
									The results that may be obtained from the use of our Services will be accurate or
									reliable;
								</li>
								<li>
									The quality of any products, services, information, or other material purchased or
									obtained through our Services will meet your expectations; or
								</li>
								<li>Any errors in our Services will be corrected.</li>
							</ul>
						</section>

						<section id="liability" class="mb-12">
							<h2>12. Limitation of Liability</h2>
							<p>
								TO THE MAXIMUM EXTENT PERMITTED BY APPLICABLE LAW, IN NO EVENT SHALL BRAND, ITS
								AFFILIATES, DIRECTORS, EMPLOYEES, AGENTS, OR LICENSORS BE LIABLE FOR ANY INDIRECT,
								PUNITIVE, INCIDENTAL, SPECIAL, CONSEQUENTIAL, OR EXEMPLARY DAMAGES, INCLUDING
								WITHOUT LIMITATION DAMAGES FOR LOSS OF PROFITS, GOODWILL, USE, DATA, OR OTHER
								INTANGIBLE LOSSES, ARISING OUT OF OR RELATING TO YOUR USE OF OR INABILITY TO USE OUR
								SERVICES.
							</p>
							<p>
								In jurisdictions that do not allow the exclusion or limitation of liability for
								consequential or incidental damages, our liability shall be limited to the maximum
								extent permitted by law.
							</p>
						</section>

						<section id="disputes" class="mb-12">
							<h2>13. Dispute Resolution</h2>
							<p>
								Any dispute arising from these Terms or your use of our Services shall be resolved
								through:
							</p>
							<ol>
								<li>
									<strong>Informal Resolution:</strong> We encourage you to contact us first to try to
									resolve any disputes informally.
								</li>
								<li>
									<strong>Binding Arbitration:</strong> If informal resolution is unsuccessful, any dispute
									shall be resolved through binding arbitration administered by [Arbitration Organization],
									in accordance with its rules.
								</li>
								<li>
									<strong>Class Action Waiver:</strong> You agree to resolve any disputes on an individual
									basis and waive any right to participate in a class action lawsuit.
								</li>
								<li>
									<strong>Governing Law:</strong> These Terms shall be governed by and construed in accordance
									with the laws of [Your Jurisdiction], without regard to its conflict of law provisions.
								</li>
							</ol>
						</section>

						<section id="changes" class="mb-12">
							<h2>14. Changes to Terms</h2>
							<p>
								We reserve the right to modify these Terms at any time. We will provide notice of
								any material changes by:
							</p>
							<ul>
								<li>Posting the updated Terms on our platform;</li>
								<li>Sending you an email notification; or</li>
								<li>Displaying a prominent notice on our Services.</li>
							</ul>
							<p>
								Your continued use of our Services after such modifications constitutes your
								acceptance of the updated Terms. If you do not agree to the updated Terms, you must
								stop using our Services.
							</p>
						</section>

						<section id="contact" class="mb-12">
							<h2>15. Contact Information</h2>
							<p>If you have any questions about these Terms, please contact us at:</p>
							<ul>
								<li>Email: legal@brand.com</li>
								<li>Address: 123 Main Street, City, State 12345</li>
								<li>Phone: (123) 456-7890</li>
							</ul>
						</section>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>
