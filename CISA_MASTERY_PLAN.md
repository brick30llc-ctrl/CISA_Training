# CISA Mastery Platform — Project Build Plan
> **For Claude Code / Developer Use**
> Zero-budget deployment · Proxmox DEV → Public internet
> Last updated: 2026-03-20

---

## Project Overview

Build a full-stack, password-protected CISA exam preparation web application with five user profiles, an AI-powered adaptive tutor, a podcast-style audiobook player, interactive performance charts, and a complete Domain 5 podcast episode script. The application is designed for zero-budget infrastructure using a Proxmox home lab environment before being carried over to a public-facing static site.

**A cold-start spin-up delay of up to 30 seconds is explicitly acceptable** — the platform runs on a free-tier or self-hosted backend to eliminate hosting costs.

---

## Infrastructure & Deployment Architecture

### Environment 1 — Proxmox DEV (initial build & testing)

- **Hypervisor:** Proxmox VE (existing environment)
- **VM spec:** Create a lightweight Ubuntu 24.04 LTS VM or LXC container
  - Minimum: 1 vCPU, 512MB RAM, 8GB disk
  - Recommended: 2 vCPU, 1GB RAM, 20GB disk
- **Web server:** Nginx (free, lightweight)
- **Application type:** Static HTML/CSS/JS — single file, no Node.js or build step required
- **Local access:** `http://<proxmox-vm-ip>` on the local network
- **DNS (optional):** Assign a local hostname via Proxmox or local DNS (e.g. `cisa.local`)

### Proxmox VM Setup Commands

```bash
# On Proxmox host — create LXC container (Ubuntu 24.04)
pct create 200 local:vztmpl/ubuntu-24.04-standard_24.04-1_amd64.tar.zst \
  --hostname cisa-mastery \
  --memory 512 \
  --cores 1 \
  --rootfs local-lvm:8 \
  --net0 name=eth0,bridge=vmbr0,ip=dhcp \
  --start 1

# Inside the container
apt update && apt install -y nginx

# Create app directory
mkdir -p /var/www/cisa
# Place cisa_mastery.html here (see deliverable below)
cp cisa_mastery.html /var/www/cisa/index.html

# Configure Nginx
cat > /etc/nginx/sites-available/cisa << 'EOF'
server {
    listen 80;
    server_name _;
    root /var/www/cisa;
    index index.html;
    location / {
        try_files $uri $uri/ =404;
    }
}
EOF

ln -s /etc/nginx/sites-available/cisa /etc/nginx/sites-enabled/
nginx -t && systemctl reload nginx
```

### Environment 2 — Public Internet (production)

**Zero-budget options (choose one):**

| Option | Platform | Cold-start delay | Notes |
|--------|----------|-----------------|-------|
| **Primary** | Cloudflare Pages | None (static) | Best option — free, global CDN, custom domain |
| **Alt 1** | GitHub Pages | None (static) | Free, requires public repo or GitHub Pro for private |
| **Alt 2** | Render (free tier) | ~30 seconds | Acceptable per project spec — spins down when idle |
| **Alt 3** | Netlify free | None (static) | 100GB bandwidth/month free |
| **Alt 4** | Vercel free | None (static) | Hobby tier, generous limits |

**Recommended path:** Cloudflare Pages — zero cost, no spin-up delay, supports custom domain, automatic HTTPS. Since the app is a single static HTML file, this is the ideal fit.

#### Cloudflare Pages Deployment

```bash
# Option A — drag and drop via Cloudflare dashboard
# 1. Log into dash.cloudflare.com
# 2. Pages → Create a project → Direct Upload
# 3. Upload cisa_mastery.html (rename to index.html)
# 4. Deploy — get a *.pages.dev subdomain instantly
# 5. Add custom domain if desired (free)

# Option B — CLI deploy
npm install -g wrangler
wrangler pages deploy ./dist --project-name=cisa-mastery
```

#### Render Free Tier (if dynamic features added later)

```bash
# render.yaml — place in repo root
services:
  - type: web
    name: cisa-mastery
    env: static
    buildCommand: echo "No build needed"
    staticPublishPath: ./
    # Free tier spins down after 15 min inactivity
    # ~30 second cold start on first request — ACCEPTABLE per spec
```

---

## Application Architecture

- **Type:** Single-file static web application
- **File:** `cisa_mastery.html` (all HTML, CSS, JS in one file)
- **Dependencies:** Chart.js 4.4.1 via CDN (cdnjs.cloudflare.com) — no npm, no bundler
- **State:** In-memory JavaScript (no database, no backend, no cookies required)
- **Auth:** Client-side password gate — password: `Team`
- **Profiles:** Five in-memory user profiles (User 1 – User 5)

> **Note for Claude Code:** The entire application must be delivered as a single `cisa_mastery.html` file. Do not create separate CSS or JS files. All styles go in a `<style>` block, all scripts in `<script>` blocks, all within one HTML document.

---

## Complete Feature Specification

### 1. Password Gate

**Behavior:**
- Application loads to a login screen — all platform content is hidden
- Single team password: `Team` (case-sensitive)
- Wrong password: shake animation on input field, error message displayed for 2.5 seconds, input cleared
- Correct password: login screen hides, main application renders
- "Sign out" button in nav bar returns user to login screen
- No session persistence required (in-memory only)

**Login screen elements:**
- Shield/lock icon (SVG, inline)
- Title: "Welcome back"
- Subtitle: "Enter your team password to access the CISA study platform."
- Password input field with keyboard submit (Enter key)
- "Sign in" button
- Footer hint: "Contact your study group admin if you need access."
- Error state: red border on input, error text below

---

### 2. Navigation

Five tabs rendered in a horizontal nav bar:
1. Dashboard
2. Focus Settings
3. Audiobook
4. AI Tutor
5. Profiles
6. Sign out (right-aligned)

Active tab: blue background (`#185FA5`), white text.
Inactive tabs: transparent background, border, muted text.

---

### 3. User Profile System

**Five profiles — User 1 through User 5:**

| Profile | Avatar color | Initial scores (D1–D5) | Questions | Streak | Default focus |
|---------|-------------|------------------------|-----------|--------|---------------|
| User 1 | Blue | 81, 65, 70, 58, 77 | 148 | 6 days | [2,2,2,3,2] |
| User 2 | Green | 55, 72, 68, 80, 60 | 92 | 3 days | [3,2,2,1,3] |
| User 3 | Purple | 90, 88, 75, 82, 91 | 210 | 12 days | [1,1,2,1,1] |
| User 4 | Amber | 40, 50, 45, 38, 55 | 44 | 1 day | [3,3,3,4,3] |
| User 5 | Pink | 70, 68, 72, 74, 69 | 130 | 8 days | [2,2,2,2,2] |

Focus values: 0 = Skip, 1 = Low, 2 = Medium, 3 = High, 4 = Critical

**Profile switcher:** Displayed as pill buttons above all tabs. Switching profile updates all data across every tab instantly.

---

### 4. Dashboard Tab

**Stats row (3 metric cards):**
- Average domain score (%)
- Total questions completed
- Current day streak

**Performance chart (Chart.js 4.4.1):**

Three selectable chart modes via tab buttons above the chart:

**Mode 1 — Skill radar:**
- Type: `radar`
- Labels: Domain short names (Auditing, Governance, Dev & Acq, Operations, Protection)
- Dataset: active profile's 5 domain scores
- Color: `#185FA5` border, `rgba(24,95,165,0.08)` fill
- Scale: 0–100, step 25
- Legend: "Domain score %" with blue square

**Mode 2 — Domain scores:**
- Type: `bar`
- Color-coded bars by performance tier:
  - 80%+ → `#3B6D11` (green)
  - 65–79% → `#185FA5` (blue)
  - 50–64% → `#854F0B` (amber)
  - Below 50% → `#A32D2D` (red)
- Legend: four color squares with tier labels

**Mode 3 — Focus vs score:**
- Type: `bar` (grouped)
- Two datasets: Score (blue, 70% opacity) and Focus weight (red, 50% opacity)
- Focus weight = `focus_level × 25` (converts 0–4 scale to 0–100)
- Legend: Score and Focus weight squares

Chart height: 260px wrapper div. `responsive: true`, `maintainAspectRatio: false`. Destroy and rebuild chart on tab switch or profile switch to avoid canvas conflicts.

**Domain progress rows:**
- One row per domain
- Shows: domain icon, domain name, score %, focus badge, color-coded progress bar
- Focus badge colors:
  - Skip: gray (`#F1EFE8` bg, `#5F5E5A` text)
  - Low: green (`#EAF3DE` bg, `#3B6D11` text)
  - Medium: amber (`#FAEEDA` bg, `#854F0B` text)
  - High: red-light (`#FCEBEB` bg, `#A32D2D` text)
  - Critical: solid red (`#E24B4A` bg, `#fff` text)
- Progress bar color matches focus badge color

**Action buttons:**
- "Adjust focus levels" → switches to Focus tab
- "Full mock exam ↗" → `sendPrompt()` with 50-question CISA mock exam request

---

### 5. Focus Settings Tab

**Two modes:**

**Manual mode (default):**
- Label: "Drag each slider to set focus level (0 = skip, 4 = critical priority)"
- One row per domain containing: icon, name, score %, live focus badge, slider (range 0–4, step 1)
- Slider label endpoints: "Skip" (left) and "Critical" (right)
- Badge and bar color update live on drag via `oninput` handler
- Sliders are enabled

**Smart AI mode:**
- Derives focus from scores automatically:
  - Score ≥ 80 → Low (1)
  - Score 70–79 → Medium (2)
  - Score 55–69 → High (3)
  - Score < 55 → Critical (4)
- Displays insight card: identifies weakest and strongest domains by name, explains the weighting rationale
- Sliders rendered but `disabled`
- "Apply AI recommendation" button applies and saves

**Buttons:**
- "Save focus settings" → updates dashboard, playlist, charts; fires `sendPrompt()` with focus summary
- "Apply AI recommendation" (smart mode only)
- "Reset to balanced" → sets all focus values to 2 (Medium)

---

### 6. Audiobook Tab

**Quality settings panel (always visible):**

Display a settings card at the top of the tab with the following locked configuration:

| Setting | Value |
|---------|-------|
| Language level | Advanced professional |
| Accuracy standard | CISA exam-verified |
| Narration style | Expert practitioner |
| Content depth | Comprehensive + examples |
| Quality badge | "Very high quality" (green badge) |

This panel is informational — it confirms the quality standard applied to all generated podcast scripts.

**Audio player:**
- Now-playing domain label
- Episode title
- Controls: previous track, skip back 10s, play/pause, skip forward 10s, next track
- Scrub timeline (range input, accent color `#185FA5`)
- Current time / total duration display
- Speed control cycling: 1x → 1.25x → 1.5x → 2x

**Playlist (16 episodes):**

Episodes auto-sorted by active user's focus level (highest first). Each item shows: number, title, domain, duration, focus badge.

Full episode list:

| # | Domain | Title | Duration |
|---|--------|-------|----------|
| 1 | 1 | 1.1 — Overview of IS Auditing & CISA Exam Structure | 37:55 |
| 2 | 1 | 1.2 — Audit Planning & Risk Assessment | 42:10 |
| 3 | 1 | 1.3 — Audit Evidence, Sampling & Documentation | 31:22 |
| 4 | 2 | 2.1 — IT Governance Frameworks (COBIT, ITIL) | 45:00 |
| 5 | 2 | 2.2 — IT Risk Management & Compliance | 38:45 |
| 6 | 3 | 3.1 — Systems Development Life Cycle (SDLC) | 41:30 |
| 7 | 3 | 3.2 — Change Management & Quality Assurance | 29:50 |
| 8 | 3 | 3.3 — Project Management for IS | 33:15 |
| 9 | 4 | 4.1 — IT Service Management & Operations | 36:40 |
| 10 | 4 | 4.2 — Business Continuity & Disaster Recovery | 40:22 |
| 11 | 4 | 4.3 — Database & Network Management | 28:55 |
| 12 | 5 | 5.1 — Information Security Frameworks | 44:10 |
| 13 | 5 | 5.2 — Access Control & Identity Management | 39:30 |
| 14 | 5 | 5.3 — Cryptography & PKI | 35:18 |
| 15 | 5 | 5.4 — Network Security & Firewalls | 32:44 |
| 16 | 5 | 5.5 — Incident Response & Forensics | 37:05 |

**Buttons:**
- "Generate podcast episode ↗" → fires detailed `sendPrompt()` targeting the user's highest-focus domain with full quality specification (see prompt template below)
- "Generate full series ↗" → fires `sendPrompt()` requesting all 16 scripts

**Podcast generation prompt template (use this exact language in the button):**

```
Generate a full, publication-ready CISA audiobook podcast episode script for Domain [N]: "[Domain Name]" at a very high quality language level. Requirements:

LANGUAGE & TONE: Use advanced, professional language befitting a senior IT audit practitioner or governance executive. Employ precise technical terminology drawn directly from the ISACA CISA Review Manual. Avoid simplistic phrasing — narrate as a subject-matter expert addressing fellow professionals preparing for the CISA examination.

ACCURACY STANDARD: All content must be factually verified against current ISACA CISA exam objectives and the CISA Review Manual (most recent edition). Cite specific frameworks where applicable (COBIT 2019, ISO/IEC 27001, NIST, ITIL 4, ISO 31000). Distinguish clearly between concepts that are frequently confused on the exam.

STRUCTURE:
- Episode introduction with domain overview and exam weighting (~200 words)
- Key concept deep-dives with real-world enterprise examples (one per major subtopic)
- Common exam traps and how to navigate them
- Mnemonics and structured memory aids for high-density content
- Practice scenario walkthrough with auditor reasoning explained
- Episode summary with critical takeaways
- Transition to next episode

TARGET AUDIENCE: Working IT audit professionals, CISAs-in-training, governance and risk practitioners.
```

---

### 7. AI Tutor Tab

**Info banner:**
- Purple left border
- Text: "Adaptive tutor — focus-weighted. Questions are drawn from your highest-focus domains more frequently. Difficulty adapts to your score trends."

**Question card:**
- Domain tag (blue pill)
- Focus level tag (red pill, e.g. "Critical focus")
- Question text (bold, 14px)
- Four answer buttons (A, B, C, D)
- On answer selection:
  - Correct: button turns green (`#EAF3DE` bg, `#3B6D11` border/text)
  - Incorrect: button turns red; correct answer auto-highlighted green
  - All buttons disabled after selection
  - Feedback box appears with explanation
  - "Next question" button appears

**Feedback language standard:** Advanced professional level. Must cite ISACA audit principle or relevant framework. Example:

> *"Correct. The IS auditor's primary mandate within any BCP evaluation is objective assessment — not implementation, not recommendation of operational changes, but rigorous evaluation of whether the plan achieves its formally stated recovery objectives. This aligns with ISACA's audit independence principle."*

**Buttons:**
- "Start adaptive session ↗" → `sendPrompt()` requesting 5 focus-weighted scenario questions at advanced professional language level with framework citations
- "Deep explain ↗" → `sendPrompt()` requesting expert-level concept breakdown with frameworks, mnemonics, and exam traps

---

### 8. Profiles Tab

**Leaderboard:**
- All 5 users ranked by average domain score (descending)
- Each row: rank, name, question count, streak, average score %, "Top" badge for #1
- Left border color-coded per user (blue, green, purple, amber, pink)

**All-profiles radar chart (Chart.js):**
- Type: `radar`
- Five datasets, one per user, each a different color
- Same domain labels as dashboard radar
- Scale: 0–100
- Legend: colored dots with user name and average score
- Height: 220px wrapper

**Button:**
- "Generate study plan ↗" → `sendPrompt()` for personalized 4-week plan, time weighted by focus level (Critical = 40%, High = 25%, Medium = 20%, Low = 10%, Skip = 5%)

---

## Domain 5 Podcast Episode — Required Build Output

**This is a priority deliverable.** The Domain 5 podcast script must be generated and saved as `domain5_podcast.md` alongside the main application file.

### Domain 5: Protection of Information Assets

**Exam weighting:** 13% of the CISA examination (approximately 26 questions out of 200)

**Sub-episodes to cover (5 episodes, ~35–45 minutes each):**

#### Episode 5.1 — Information Security Frameworks

Key content requirements:
- ISACA's definition of information security governance vs. management
- ISO/IEC 27001:2022 — Information Security Management System (ISMS) structure, Annex A controls, certification process
- NIST Cybersecurity Framework (CSF) 2.0 — Govern, Identify, Protect, Detect, Respond, Recover functions
- COBIT 2019 — APO13 (Managed Security), DSS05 (Managed Security Services)
- Defense-in-depth strategy: people, process, technology layers
- Security policy hierarchy: policy → standard → procedure → guideline
- Exam trap: distinguishing between a security policy (what) vs. a standard (how much) vs. a procedure (how)
- Mnemonic for NIST CSF 2.0 functions: **"Governments Identify Protective Detectives Responding Resourcefully"**
- Real-world example: Enterprise ISMS implementation at a financial institution

#### Episode 5.2 — Access Control & Identity Management

Key content requirements:
- Access control models: DAC (Discretionary), MAC (Mandatory), RBAC (Role-Based), ABAC (Attribute-Based)
- Principle of least privilege and need-to-know
- Identity and Access Management (IAM) lifecycle: provisioning, review, de-provisioning
- Privileged Access Management (PAM) — separation of duties for admin accounts
- Single Sign-On (SSO), Multi-Factor Authentication (MFA), federated identity
- Access control review (recertification) — frequency, responsibility, auditor's role
- Logical access controls vs. physical access controls
- Exam trap: "segregation of duties" controls responsibility for a function; "dual control" requires two people simultaneously
- Mnemonic for access control types: **"Don't Make Rules About Behaviour"** (DAC, MAC, RBAC, ABAC, Bell-LaPadula)
- Real-world scenario: Privileged user access review at a healthcare organization

#### Episode 5.3 — Cryptography & PKI

Key content requirements:
- Symmetric encryption: AES-256, DES (deprecated), 3DES — key distribution problem
- Asymmetric encryption: RSA, ECC — public/private key pairs
- Hashing: SHA-256, SHA-3 — integrity, not confidentiality; collision resistance
- Digital signatures: authentication + non-repudiation + integrity
- Public Key Infrastructure (PKI): CA hierarchy (root CA, intermediate CA, end-entity), certificate lifecycle, CRL vs. OCSP
- TLS/SSL — transport security, certificate validation, cipher suites
- Key management lifecycle: generation, distribution, storage, rotation, destruction
- Exam trap: encryption provides confidentiality; hashing provides integrity; digital signatures provide both authentication and non-repudiation
- Mnemonic: **"CIA + NR"** — Confidentiality (encryption), Integrity (hashing), Availability, + Non-Repudiation (digital signature)
- Real-world example: PKI deployment for e-government services

#### Episode 5.4 — Network Security & Firewalls

Key content requirements:
- Network segmentation: DMZ architecture, VLANs, micro-segmentation
- Firewall types: packet filtering, stateful inspection, application-layer (WAF), next-generation (NGFW)
- Intrusion Detection Systems (IDS) vs. Intrusion Prevention Systems (IPS) — detection vs. active blocking
- VPN types: site-to-site vs. remote access; IPSec vs. SSL/TLS VPN
- Zero Trust Architecture (ZTA) — never trust, always verify; identity-centric perimeter
- Network monitoring: SIEM, NetFlow analysis, log aggregation
- Wireless security: WPA3, 802.1X, rogue access point detection
- Exam trap: IDS is passive (alerts only); IPS is active (blocks traffic) — auditors must verify both are tuned to minimize false positives/negatives
- Mnemonic for firewall types: **"Pretty Smart Applications Never Fail"** (Packet, Stateful, Application, Next-gen, Fail-safe defaults)
- Real-world example: Zero Trust implementation at a multinational enterprise post-breach

#### Episode 5.5 — Incident Response & Digital Forensics

Key content requirements:
- Incident response lifecycle (NIST SP 800-61 Rev. 2): Preparation → Detection & Analysis → Containment → Eradication → Recovery → Post-Incident Activity
- IS auditor's role during incident response: independent reviewer, NOT first responder
- Digital forensics principles: chain of custody, order of volatility (registers → RAM → disk → logs → archives)
- Evidence preservation: write blockers, forensic imaging (dd, FTK Imager), hash verification (MD5/SHA-256)
- Business continuity vs. disaster recovery: BC = keeping operations running; DR = restoring IT systems
- RTO (Recovery Time Objective), RPO (Recovery Point Objective), MTD (Maximum Tolerable Downtime) — definitions and relationships
- Post-incident review: lessons learned, control improvement, regulatory reporting obligations
- Exam trap: the auditor reviews the incident response process; they do not conduct the forensic investigation themselves
- Mnemonic for IR phases: **"Pretty Detectives Catch Every Rabbit Post-haste"** (Preparation, Detection, Containment, Eradication, Recovery, Post-incident)
- Real-world scenario: Ransomware incident at a regional bank — auditor's post-incident review process

**Script quality requirements (non-negotiable):**
- Language: Advanced professional, suitable for senior IT audit practitioners
- Accuracy: Every factual claim must be traceable to ISACA CISA Review Manual (current edition), NIST publications, or ISO standards
- Narration voice: Expert practitioner speaking to peers, not an instructor speaking to students
- Depth: Each sub-episode should be substantive enough for 35–45 minutes of narration
- Format: Full narration script with [SECTION BREAK] markers, not bullet points
- Include: Introduction, transitions between concepts, summary, and bridge to next episode

---

## Color System & Design Tokens

### Focus level colors

| Level | Value | Background | Text | Progress bar |
|-------|-------|-----------|------|-------------|
| Skip | 0 | `#F1EFE8` | `#5F5E5A` | `#D3D1C7` |
| Low | 1 | `#EAF3DE` | `#3B6D11` | `#97C459` |
| Medium | 2 | `#FAEEDA` | `#854F0B` | `#EF9F27` |
| High | 3 | `#FCEBEB` | `#A32D2D` | `#F09595` |
| Critical | 4 | `#E24B4A` | `#ffffff` | `#E24B4A` |

### Profile colors

| Profile | Border/accent | Avatar bg | Avatar text |
|---------|--------------|-----------|-------------|
| User 1 | `#185FA5` | `#E6F1FB` | `#185FA5` |
| User 2 | `#0F6E56` | `#E1F5EE` | `#0F6E56` |
| User 3 | `#534AB7` | `#EEEDFE` | `#534AB7` |
| User 4 | `#854F0B` | `#FAEEDA` | `#854F0B` |
| User 5 | `#993556` | `#FBEAF0` | `#993556` |

### Chart.js colors (hardcoded — canvas cannot use CSS variables)

- Primary blue: `#185FA5`
- Radar fill: `rgba(24, 95, 165, 0.08)`
- Grid lines: `rgba(136, 135, 128, 0.2)`
- Tick labels: `#888780` / `#5F5E5A`

---

## Final Deliverables Checklist

| File | Description | Required |
|------|-------------|----------|
| `cisa_mastery.html` | Complete single-file web application | ✅ Yes |
| `domain5_podcast.md` | Full narration script, Domain 5 all 5 episodes | ✅ Yes |
| `nginx.conf` | Nginx config for Proxmox deployment | Optional |

---

## Deployment Checklist

### Proxmox DEV

- [ ] Create Ubuntu 24.04 LXC container (200MB RAM minimum)
- [ ] Install Nginx
- [ ] Copy `cisa_mastery.html` → `/var/www/cisa/index.html`
- [ ] Configure Nginx virtual host
- [ ] Test at `http://<container-ip>`
- [ ] Verify Chart.js loads from CDN (requires outbound internet on container)
- [ ] Test all 5 profile switches
- [ ] Test login gate (password: `Team`)
- [ ] Test all 3 chart modes
- [ ] Test focus slider functionality
- [ ] Test Smart AI focus mode
- [ ] Test podcast generation button fires correct prompt
- [ ] Verify Domain 5 playlist episodes display correctly

### Public Deployment (Cloudflare Pages — recommended)

- [ ] Create Cloudflare account (free)
- [ ] Go to Pages → Create project → Direct Upload
- [ ] Upload `index.html` (rename from `cisa_mastery.html`)
- [ ] Verify deployment at `*.pages.dev` URL
- [ ] (Optional) Add custom domain
- [ ] (Optional) Enable Cloudflare Access for additional password protection at the network layer
- [ ] Share URL with study group

---

## Notes for Claude Code

1. **Single file only.** Do not create separate `.css` or `.js` files. Everything must be self-contained in `cisa_mastery.html`.

2. **Chart destruction.** When switching tabs or profiles, always call `chart.destroy()` before creating a new Chart.js instance on the same canvas. Use `let mainChart = null` and check before destroying.

3. **No localStorage.** All state is in-memory JavaScript objects. Refreshing the page resets to defaults — this is acceptable and by design.

4. **CDN only.** The only external resource is Chart.js from `cdnjs.cloudflare.com`. No other CDN calls. Load order: `<script src="cdnjs...chart.umd.js">` first, then a plain `<script>` block that uses `window.Chart`.

5. **Cold start.** The 30-second cold-start delay is a Render/backend concern. For static deployments (Cloudflare Pages, Nginx), there is no cold start. If a dynamic backend is ever added (e.g., for persistent user data), Render free tier is acceptable.

6. **Domain 5 podcast.** Generate `domain5_podcast.md` as a separate deliverable. It is a full narration script, not embedded in the app. It should be publication-ready — suitable for text-to-speech production via ElevenLabs, Play.ht, or similar tools.

7. **Password:** `Team` — case-sensitive, checked with strict equality (`===`).

8. **Profile data is not persisted.** If persistence is desired in a future iteration, consider localStorage or a lightweight backend (SQLite on Render free tier). For this phase, in-memory only.

9. **Mobile responsiveness.** Use `repeat(auto-fit, minmax(...))` grid layouts. The application should be usable on tablet-sized screens and above. Full mobile optimization is stretch goal, not required.

10. **Podcast quality is enforced via the prompt template.** The app does not generate audio directly — it fires a precisely engineered `sendPrompt()` call to Claude that specifies the exact quality requirements. Do not simplify this prompt.

---

*End of plan. Build `cisa_mastery.html` and `domain5_podcast.md` per the above specification.*
