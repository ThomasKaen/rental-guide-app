# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/)
and this project adheres to [Semantic Versioning](https://semver.org/).

---

## [0.1.0] - 2025-11-29
### Added
- Project initialization with core folder structure (`backend/`, `frontend/`, `infra/`).
- FastAPI backend bootstrapped with:
  - Basic app configuration (`Settings` via pydantic-settings)
  - Health check endpoint (`/health`)
  - Static files mount (`/static`)
  - Jinja2 template engine setup
- Phase 1 in-memory guide system:
  - `Guide` and `LocalRecommendation` schemas
  - Hardcoded example property (`company-flat-1`)
  - Basic guide service for retrieving data
- First guest-facing guide page:
  - `/guide/{slug}` route
  - Responsive template with SaaS-style structure
  - Sections: Wi-Fi, Check-in/Out, House Rules, Appliances, Local Area, Emergency Info
- Initial CSS styling:
  - Modern SaaS design (cards, pills, sticky navigation, footer)
  - Mobile-first responsive layout

### Notes
- This version represents **Phase 1 foundation**: single-property, static data, template-driven guest page.
- No admin UI, database, or multi-property system yet — will come in v0.2.0+.

---

## [Unreleased]
### Planned
- Admin dashboard for editing guide content
- Persistent database (SQLite → PostgreSQL)
- Multiple property support
- Per-guest unique guide links (tokens)
- Media uploads (images / icons)
- QR code generator
