Phase 0 – Framing & Scope (1–2 sessions of thinking, not coding)

Decide:

Is this just for your flats, or also something you might sell to other hosts later?

Tech stack:

Backend: FastAPI (fits your style, easy to Dockerise).

Frontend: React or simple server-rendered templates first (you can upgrade later).

DB: SQLite → PostgreSQL when needed.

Output of this phase:

One short doc:

“Core use case”: Host sends link to guest, guest sees everything needed with zero friction.

“Non-goals for v1”: No PMS integration, no crazy automation, no analytics dashboard yet.

Phase 1 – Tiny MVP: Single Property, Static Content

Goal: Have something you can give to a guest as a URL or QR code.

Features:

Public, mobile-friendly page with sections:

Welcome

Check-in / Check-out

Wi-Fi

House rules

Appliances & how-tos

Local recommendations

Emergency contacts

Content stored in a simple JSON or a single DB table.

No login, no admin panel yet — just seeded data.

Tech:

FastAPI (or Flask) endpoint: GET /guide/{slug} → render HTML.

Simple templating (Jinja2) or minimal React SPA calling a /api/guide/{slug} endpoint.

Ship at end of Phase 1:

https://yourdomain.com/guide/my-flat that you’d be happy to share with a real guest.

A printable QR code pointing to that URL.

Phase 2 – Multi-Property + Basic Admin

Goal: Support multiple flats + be able to edit content without touching code.

Features:

Data model:

Property (flat)

GuidePageSection (or a JSON blob per property)

Simple admin login (even just one user for now).

Admin UI:

List properties

Create / Edit property info

Upload images (logo, room photos, etc.)

Each property has its own slug: /guide/{property_slug}

Tech:

DB migration to proper schema (SQLite is fine).

Admin front-end (could be: simple React/Next.js admin, or server-rendered forms).

Auth: very simple session-based or JWT with one admin user.

Ship at end of Phase 2:

You can manage multiple flats from a dashboard and generate a unique guide URL per flat.

Phase 3 – Per-Guest / Per-Booking Links

Goal: Move from “static guide per flat” → “personalised guide per booking.”

Features:

Booking / GuestGuide entity:

property_id

guest_name (optional)

checkin_date, checkout_date

unique_token or slug

Guest-facing URL: /g/{token} that:

Loads the property guide

Optionally shows: “Welcome, [Name]! Your stay: 12–15 March.”

Auto-expires or hides after checkout date (optional).

Extra nice bits:

QR generation per booking (store URL, show QR preview in admin).

“Copy link” button in admin.

Ship at end of Phase 3:

From your admin:

Create booking → get unique link → send to guest.

Each guest sees a personalised header and the right property.

Phase 4 – UX Polish & Content Power-Ups

Goal: Make it feel better than a generic tool like Touch Stay.

Guest-side improvements:

Clean responsive layout (big tap targets, clear sections).

Sticky bottom nav or top tabs:
Home · Check-in · House Rules · Appliances · Local Area · Emergency

Embedded Google Map with pins for:

Property

Key local spots (shops, restaurants, bus/metro).

Optional video sections:

“How to use the heating”

“How the lockbox works”

Offline-friendly behaviour (basic: encourage screenshot / save to home screen; advanced: PWA).

Host-side improvements:

Reusable templates:

Standard house rules

Standard emergency info

Standard welcome message
So when you add a new flat, you just override specifics.

Ship at end of Phase 4:

Guests genuinely feel, “Wow this is slick and easy,” not just “PDF online.”

Phase 5 – Automation & Integrations (Optional but Powerful)

Goal: Reduce manual work around sending the guide & add “smart” features.

Ideas:

Integrate with wherever you pull booking info from (Airbnb API is messy, but you can start with manual input or CSV import).

Email sending:

When you create a booking, system can send a ready-made email:

“Hi [Name], here is your digital guide for [Property].”

Optional webhooks or API:

/api/create_guide → used by other tools later.

Smart extras:

Simple analytics:

last_opened_at

open_count

Most-viewed sections

Guest feedback form at bottom:

“Was anything unclear?”

“Any suggestions for this guide?”

Ship at end of Phase 5:

You barely have to think about sharing the guide; it fits into your flow.

You have some data to improve copy & instructions over time.

Phase 6 – Productise (If You Want to Sell It to Other Hosts Later)

If you ever want to turn it into a micro-SaaS or something you offer local hosts:

Multi-tenant model:

Account / Host

Each host only sees their own properties and bookings.

Billing layer (Stripe) with:

Free tier: 1 property.

Paid plans for more properties or extra features (analytics, custom branding, etc.).

Branding:

White-label subdomains like host-name.yourapp.com or custom domain support.

This can be future-you territory; you don’t need it for your own flats.