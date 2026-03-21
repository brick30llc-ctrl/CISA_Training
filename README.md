# CISA Mastery Platform

A comprehensive, zero-budget CISA exam preparation web application featuring adaptive study tools, interactive quizzes, performance analytics, and a full podcast series covering all five ISACA CISA domains.

## Live Demo

**https://brick30llc-ctrl.github.io/CISA_Training/**

## Features

- **5 User Profiles** — Track progress independently for multiple learners
- **Adaptive AI Tutor** — Personalized study recommendations based on performance
- **Interactive Quizzes** — Domain-specific practice questions with detailed explanations
- **Performance Charts** — Visual analytics powered by Chart.js to track progress over time
- **Podcast Series** — 16 audio episodes covering all 5 CISA domains with an HTML5 player
- **TTS Playback** — Text-to-speech with download capability for offline listening
- **Password Protected** — Simple login screen for access control
- **Fully Static** — No backend required; runs on GitHub Pages or any static host

## CISA Domains Covered

| Domain | Episodes | Topics |
|--------|----------|--------|
| **1 — Auditing IS Process** | 3 | Overview & Auditing, Audit Planning, Evidence & Sampling |
| **2 — Governance & Management** | 2 | Governance Frameworks, Risk & Compliance |
| **3 — IS Acquisition, Development & Implementation** | 3 | SDLC, Change Management, Project Management |
| **4 — IS Operations & Business Resilience** | 3 | Service Management, BCP/DR, Database & Network |
| **5 — Protection of Information Assets** | 5 | Security Frameworks, Access Control, Cryptography & PKI, Network Security, Incident Response |

## Project Structure

```
CISA_Training/
├── index.html            # Main landing page (GitHub Pages entry point)
├── cisa_mastery.html     # Full CISA Mastery Platform application
├── generate_audio.py     # TTS script using Edge TTS (Microsoft Neural Voices)
├── CISA_MASTERY_PLAN.md  # Detailed project build plan
├── audio/                # 16 MP3 podcast episodes
│   ├── ep1_1_overview_auditing.mp3
│   ├── ep1_2_audit_planning.mp3
│   └── ... (16 episodes total)
└── podcasts/             # Markdown scripts for each podcast episode
    ├── domain1_ep1_overview_auditing.md
    ├── domain1_ep2_audit_planning.md
    └── ... (16 scripts total)
```

## Getting Started

### Option 1 — GitHub Pages (recommended)

The site is deployed automatically via GitHub Pages. Just visit the [live demo](https://brick30llc-ctrl.github.io/CISA_Training/).

### Option 2 — Local

Open `index.html` or `cisa_mastery.html` directly in a browser. No build step or server required.

### Option 3 — Self-Hosted (Proxmox / Nginx)

See [CISA_MASTERY_PLAN.md](CISA_MASTERY_PLAN.md) for detailed Proxmox LXC container and Nginx setup instructions.

## Generating Podcast Audio

The podcast MP3 files are generated from markdown scripts using Microsoft Edge TTS:

```bash
pip install edge-tts
python generate_audio.py          # Generate all episodes
python generate_audio.py 1.1      # Generate a specific episode
```

**Voice:** `en-US-AndrewMultilingualNeural` — warm, confident delivery tuned for educational content.

## Tech Stack

- **Frontend:** Vanilla HTML, CSS, JavaScript (single-file architecture)
- **Charts:** Chart.js 4.4
- **Audio:** HTML5 `<audio>` player + Edge TTS for generation
- **Hosting:** GitHub Pages (zero cost)

## License

This project is for personal educational use in preparing for the ISACA CISA certification exam.
