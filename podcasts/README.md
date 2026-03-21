# CISA Podcast Scripts

This directory contains the markdown scripts for all 16 podcast episodes. Each script is used by `generate_audio.py` to produce the corresponding MP3 file in the `audio/` directory.

## Episodes

### Domain 1 — Auditing the Information Systems Process
| File | Topic |
|------|-------|
| `domain1_ep1_overview_auditing.md` | Overview of IS Auditing |
| `domain1_ep2_audit_planning.md` | Audit Planning & Execution |
| `domain1_ep3_evidence_sampling.md` | Evidence Collection & Sampling |

### Domain 2 — Governance & Management of IT
| File | Topic |
|------|-------|
| `domain2_ep1_governance_frameworks.md` | IT Governance Frameworks |
| `domain2_ep2_risk_compliance.md` | Risk Management & Compliance |

### Domain 3 — IS Acquisition, Development & Implementation
| File | Topic |
|------|-------|
| `domain3_ep1_sdlc.md` | Software Development Life Cycle |
| `domain3_ep2_change_management.md` | Change Management |
| `domain3_ep3_project_management.md` | Project Management |

### Domain 4 — IS Operations & Business Resilience
| File | Topic |
|------|-------|
| `domain4_ep1_service_management.md` | IT Service Management |
| `domain4_ep2_bcp_dr.md` | Business Continuity & Disaster Recovery |
| `domain4_ep3_database_network.md` | Database & Network Operations |

### Domain 5 — Protection of Information Assets
| File | Topic |
|------|-------|
| `domain5_ep1_security_frameworks.md` | Security Frameworks & Standards |
| `domain5_ep2_access_control.md` | Access Control & Authentication |
| `domain5_ep3_cryptography_pki.md` | Cryptography & PKI |
| `domain5_ep4_network_security.md` | Network Security |
| `domain5_ep5_incident_response.md` | Incident Response & Management |

## Generating Audio

From the project root:

```bash
pip install edge-tts
python generate_audio.py          # All episodes
python generate_audio.py 5.3      # Single episode (e.g., Domain 5, Episode 3)
```

Output MP3 files are saved to `audio/`.
