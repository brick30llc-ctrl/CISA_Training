# CISA Podcast Audio Files

This directory contains 16 MP3 podcast episodes generated from the markdown scripts in `podcasts/` using Microsoft Edge TTS.

## Episodes

| File | Domain | Topic |
|------|--------|-------|
| `ep1_1_overview_auditing.mp3` | 1 | Overview of IS Auditing |
| `ep1_2_audit_planning.mp3` | 1 | Audit Planning & Execution |
| `ep1_3_evidence_sampling.mp3` | 1 | Evidence Collection & Sampling |
| `ep2_1_governance_frameworks.mp3` | 2 | IT Governance Frameworks |
| `ep2_2_risk_compliance.mp3` | 2 | Risk Management & Compliance |
| `ep3_1_sdlc.mp3` | 3 | Software Development Life Cycle |
| `ep3_2_change_management.mp3` | 3 | Change Management |
| `ep3_3_project_management.mp3` | 3 | Project Management |
| `ep4_1_service_management.mp3` | 4 | IT Service Management |
| `ep4_2_bcp_dr.mp3` | 4 | Business Continuity & Disaster Recovery |
| `ep4_3_database_network.mp3` | 4 | Database & Network Operations |
| `ep5_1_security_frameworks.mp3` | 5 | Security Frameworks & Standards |
| `ep5_2_access_control.mp3` | 5 | Access Control & Authentication |
| `ep5_3_cryptography_pki.mp3` | 5 | Cryptography & PKI |
| `ep5_4_network_security.mp3` | 5 | Network Security |
| `ep5_5_incident_response.mp3` | 5 | Incident Response & Management |

## Regenerating

```bash
python generate_audio.py          # All episodes
python generate_audio.py 2.1      # Single episode
```

**Voice:** `en-US-AndrewMultilingualNeural` | **Rate:** +8% | **Pitch:** -2Hz
