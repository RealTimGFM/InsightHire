# INSIGHT HIRE

INSIGHT HIRE is a polished Flask product preview for an AI-powered career intelligence platform built for software engineering candidates. It combines a dark startup-style interface, working authentication, structured company research, and a clear subscription model.

This is a product preview, not a production recruiting platform. Login and signup are real. Company intelligence, employee insights, interview questions, referral matching, AI summaries, resume tips, and job fit scores are simulated with structured mock data.

## Product Positioning

INSIGHT HIRE is designed to make three things clear:

1. The idea is useful.
2. The UI looks professional.
3. The business model makes sense.

## Features

- Public landing page with strong hero, feature sections, premium teaser, and pricing preview
- Working signup, login, logout, password hashing, and session auth with SQLite
- Instant access button that logs into the main job seeker preview account
- Role-based dashboards for job seekers and the verified employee preview account
- Search across Google, Microsoft, Nvidia, and Apple
- Rich company detail pages with:
  - overview
  - company culture
  - verified employee insight cards
  - interview question cards with insider tips
  - skill gap analysis
  - referral matching with unlocked and premium cards
  - fake AI summary
  - resume tips based on a built-in sample resume
  - fake job fit score
- Pricing page with Free, Premium, and Enterprise / School plans
- Roadmap page for future product direction
- Custom dark-mode UI with polished cards, hover states, sticky nav, toasts, and modal interactions

## Tech Stack

- Python
- Flask
- Jinja templates
- SQLite for authentication only
- Custom CSS
- Lightweight vanilla JavaScript
- Structured Python data files for all mock content

## Folder Structure

```text
InsightHire/
  app.py
  requirements.txt
  README.md
  .gitignore
  /data
    __init__.py
    companies.py
    demo_resume.py
    pricing.py
    site_content.py
  /templates
    base.html
    landing.html
    login.html
    signup.html
    dashboard.html
    verified_dashboard.html
    search.html
    company_detail.html
    pricing.html
    roadmap.html
    preview_verified.html
    404.html
  /static
    /css
      style.css
    /js
      app.js
  /instance
    users.db
  /utils
    __init__.py
    auth.py
    helpers.py
    seed.py
```

## How To Run

### 1. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the app

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

## First-Run Behavior

- The SQLite database is created automatically in `instance/users.db` if it does not exist.
- Preview accounts are seeded automatically on startup if they are missing.
- New signups are stored as normal job seeker accounts.

## Default Preview Accounts

Job seeker preview account:

- Email: `demo@insighthire.com`
- Password: `demo123`

Verified employee preview account:

- Email: `verified@insighthire.com`
- Password: `demo123`

## What Is Real vs Simulated

Real:

- Login
- Signup
- Logout
- Duplicate email prevention
- Password hashing
- Session-based auth
- Role-based dashboard routing

Simulated:

- AI summary
- Resume tips
- Job fit score
- Employee insights
- Interview questions
- Referral matching
- Resume upload

The resume upload interaction is intentionally simulated and always uses the built-in sample resume for `Alex Chen`.

## Data Notes

- Only four companies are included: Google, Microsoft, Nvidia, and Apple
- All company insights are tailored for the `Software Engineer` role only
- All employee names, comments, questions, and referral matches are simulated preview content
- Some referral cards are intentionally locked to make the Premium tier feel believable

## Suggested Walkthrough

Use this flow for the clearest product walkthrough:

1. Show the landing page hero and explain the value proposition.
2. Click `Instant Access`.
3. Land on the job seeker dashboard and point out the focused, startup-style layout.
4. Use the search bar or open a recommended company.
5. On the company page, highlight:
   - verified employee insights
   - interview questions with insider tips
   - referral matching
   - job fit score
6. Open the pricing page and explain why Premium and school partnerships make sense.
7. Log out and log in with the verified employee preview account.
8. Show the verified employee dashboard and preview page briefly.

## Product Notes

- The most impressive sections are the verified employee insights, referral matching, and interview preparation cards.
- Instant Access is the fastest route if you want a reliable live walkthrough.
- The product is desktop-first and optimized for a polished, focused experience.

## Development Notes

This implementation prioritizes clarity, maintainability, and ease of setup. It uses simple Flask architecture, readable files, and structured mock data so the platform preview is easy to understand, run, and extend.
