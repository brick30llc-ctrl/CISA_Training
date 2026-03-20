#!/usr/bin/env python3
"""
CISA Podcast Audio Generator
Uses Edge TTS (Microsoft Neural Voices) to convert markdown scripts to MP3.
Voice: en-US-AndrewMultilingualNeural (Warm, Confident, Authentic)
"""

import asyncio
import re
import sys
import os
import edge_tts

VOICE = "en-US-AndrewMultilingualNeural"
RATE = "+8%"       # Slightly faster, tighter pacing
PITCH = "-2Hz"     # Slightly deeper for authority
VOLUME = "+0%"

EPISODE_FILES = {
    "1.1": "podcasts/domain1_ep1_overview_auditing.md",
    "1.2": "podcasts/domain1_ep2_audit_planning.md",
    "1.3": "podcasts/domain1_ep3_evidence_sampling.md",
    "2.1": "podcasts/domain2_ep1_governance_frameworks.md",
    "2.2": "podcasts/domain2_ep2_risk_compliance.md",
    "3.1": "podcasts/domain3_ep1_sdlc.md",
    "3.2": "podcasts/domain3_ep2_change_management.md",
    "3.3": "podcasts/domain3_ep3_project_management.md",
    "4.1": "podcasts/domain4_ep1_service_management.md",
    "4.2": "podcasts/domain4_ep2_bcp_dr.md",
    "4.3": "podcasts/domain4_ep3_database_network.md",
    "5.1": "podcasts/domain5_ep1_security_frameworks.md",
    "5.2": "podcasts/domain5_ep2_access_control.md",
    "5.3": "podcasts/domain5_ep3_cryptography_pki.md",
    "5.4": "podcasts/domain5_ep4_network_security.md",
    "5.5": "podcasts/domain5_ep5_incident_response.md",
}

OUTPUT_MAP = {
    "1.1": "audio/ep1_1_overview_auditing.mp3",
    "1.2": "audio/ep1_2_audit_planning.mp3",
    "1.3": "audio/ep1_3_evidence_sampling.mp3",
    "2.1": "audio/ep2_1_governance_frameworks.mp3",
    "2.2": "audio/ep2_2_risk_compliance.mp3",
    "3.1": "audio/ep3_1_sdlc.mp3",
    "3.2": "audio/ep3_2_change_management.mp3",
    "3.3": "audio/ep3_3_project_management.mp3",
    "4.1": "audio/ep4_1_service_management.mp3",
    "4.2": "audio/ep4_2_bcp_dr.mp3",
    "4.3": "audio/ep4_3_database_network.mp3",
    "5.1": "audio/ep5_1_security_frameworks.mp3",
    "5.2": "audio/ep5_2_access_control.mp3",
    "5.3": "audio/ep5_3_cryptography_pki.mp3",
    "5.4": "audio/ep5_4_network_security.mp3",
    "5.5": "audio/ep5_5_incident_response.mp3",
}


def preprocess_script(text: str) -> str:
    """
    Convert markdown podcast script into clean narration text
    optimized for natural TTS output.
    """
    # Remove metadata header (everything before first ## or first paragraph after ---)
    # Keep content after the metadata block
    lines = text.split("\n")
    content_lines = []
    past_header = False
    for line in lines:
        # Skip the YAML-style metadata at top
        if not past_header:
            if line.startswith("## ") or (line.startswith("Welcome") or line.startswith("Let")):
                past_header = True
                # For ## headers, we'll process them below
                content_lines.append(line)
            continue
        content_lines.append(line)

    text = "\n".join(content_lines)

    # Remove reference footer (italic text at end starting with *)
    text = re.sub(r'\n---\n\*.*$', '', text, flags=re.DOTALL)

    # Convert [SECTION BREAK] to brief pause
    text = text.replace("[SECTION BREAK]", "\n")

    # Convert ## HEADERS to spoken section transitions
    def header_to_speech(match):
        title = match.group(1).strip()
        # Remove timestamp markers like (0:00–2:30)
        title = re.sub(r'\s*\(\d+:\d+[–-]\d+:\d+\)\s*', '', title)
        # Clean up all-caps to title case for more natural reading
        if title.isupper():
            title = title.title()
        return f"\n\n{title}.\n\n"

    text = re.sub(r'^##\s+(.+)$', header_to_speech, text, flags=re.MULTILINE)
    text = re.sub(r'^#\s+(.+)$', header_to_speech, text, flags=re.MULTILINE)

    # Remove markdown bold **text** — keep the text
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)

    # Remove markdown italic *text* — keep the text
    text = re.sub(r'\*([^*]+)\*', r'\1', text)

    # Remove markdown tables
    text = re.sub(r'^\|.*\|$', '', text, flags=re.MULTILINE)

    # Remove code blocks
    text = re.sub(r'```[\s\S]*?```', '', text)

    # Remove horizontal rules
    text = re.sub(r'^-{3,}$', '', text, flags=re.MULTILINE)

    # Remove bullet point markers but keep content
    text = re.sub(r'^[\s]*[-•]\s+', '', text, flags=re.MULTILINE)

    # Convert em dashes to spoken pauses (comma works well for TTS)
    text = text.replace(" — ", ", ")
    text = text.replace("—", ", ")

    # Expand common abbreviations for more natural speech
    text = text.replace("e.g.", "for example")
    text = text.replace("i.e.", "that is")
    text = text.replace("vs.", "versus")
    text = text.replace("etc.", "et cetera")

    # Clean up excessive whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'  +', ' ', text)

    # Trim
    text = text.strip()

    return text


async def generate_episode(episode_num: str, base_dir: str) -> str:
    """Generate MP3 for a single episode. Returns output path."""
    src = os.path.join(base_dir, EPISODE_FILES[episode_num])
    dst = os.path.join(base_dir, OUTPUT_MAP[episode_num])

    os.makedirs(os.path.dirname(dst), exist_ok=True)

    print(f"[{episode_num}] Reading script: {src}")
    with open(src, "r", encoding="utf-8") as f:
        raw = f.read()

    text = preprocess_script(raw)
    word_count = len(text.split())
    print(f"[{episode_num}] Preprocessed: {word_count} words")

    print(f"[{episode_num}] Generating audio with {VOICE}...")
    communicate = edge_tts.Communicate(
        text,
        VOICE,
        rate=RATE,
        pitch=PITCH,
        volume=VOLUME,
    )
    await communicate.save(dst)

    size_mb = os.path.getsize(dst) / (1024 * 1024)
    print(f"[{episode_num}] Done: {dst} ({size_mb:.1f} MB)")
    return dst


async def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    if len(sys.argv) > 1:
        episodes = sys.argv[1:]
    else:
        episodes = sorted(EPISODE_FILES.keys(), key=lambda x: float(x))

    for ep in episodes:
        if ep not in EPISODE_FILES:
            print(f"Unknown episode: {ep}")
            print(f"Available: {', '.join(sorted(EPISODE_FILES.keys(), key=lambda x: float(x)))}")
            sys.exit(1)

    print(f"Generating {len(episodes)} episode(s): {', '.join(episodes)}")
    print(f"Voice: {VOICE} | Rate: {RATE} | Pitch: {PITCH}")
    print()

    for ep in episodes:
        await generate_episode(ep, base_dir)
        print()

    print("All done!")


if __name__ == "__main__":
    asyncio.run(main())
