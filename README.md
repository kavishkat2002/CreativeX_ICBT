# MedDoc — AI-Powered Digital Healthcare Platform

> **"Early Detection. Better Tomorrows."**  
> *A unified digital healthcare ecosystem combining dual-pathway hospital navigation, multi-cancer AI visual risk screening, medical report simplification, and the MedMind eCare emotional wellness companion.*

---

## 🏆 Submission Information

- **Competition:** [Innodata AI Catalyst '26](https://github.com/AI-Catalyst-Innodata) — University Track
- **Team Name:** CreativeX Technology
- **University / Institute:** ICBT Campus
- **Product Category:** Health Care & Services
- **Official Repository:** [https://github.com/kavishkat2002/CreativeX_ICBT](https://github.com/kavishkat2002/CreativeX_ICBT)
  

---

## 📂 Repository Structure

This repository strictly conforms to the **Innodata GitHub Repository Submission Guidelines — University Track**:

```
CreativeX_ICBT/
├── project/
│   ├── main.py                  # Main application entry point (FastAPI server)
│   └── requirements.txt         # Python dependencies required to run the project
├── README.md                    # Project overview, setup instructions & execution guide
├── docs/
│   ├── Proposal.docx            # Complete formal project proposal document
│   ├── Workflow.md              # System workflow, user journey & implementation steps
│   └── PROJECT_DETAILS.md       # Technical specs, architecture, database schemas & features
└── project-demo.mp4             # High-definition project demonstration video
```

---

## 💡 Problem Definition & Proposed Solution

### The Challenge
- **Delayed Intervention:** Patients often overlook early warning signs (such as persistent oral ulcers or evolving skin lesions) due to uncertainty over severity.
- **Fragmented Healthcare Journey:** Existing platforms isolate appointment scheduling from symptom assessment, leaving patients confused about which clinical specialist to consult.
- **Diagnostic Anxiety:** Waiting for hospital appointments or biopsy results causes severe emotional distress without structured guidance.
- **Scattered Health Data:** Medical records, prescriptions, and lab reports are dispersed across disparate clinics, preventing continuity of care.

### The MedDoc Solution
MedDoc bridges the gap between first symptoms and clinical treatment through a cohesive patient-centric platform:
1. **Dual Healthcare Pathways:** Choose between traditional doctor/hospital scheduling or interactive AI-assisted triage.
2. **Multi-Modal AI Screening:** Evaluates visible lesions (Oral, Skin, Breast, Eye) and summarizes complex pathology/lab reports into plain language.
3. **Smart Clinical Referral:** Automatically routes patients to verified specialists (e.g., Oral & Maxillofacial Surgeons, Dermatologists, Oncologists) based on clinical risk indicators.
4. **MedMind eCare:** An AI-powered mental wellness companion offering stress management, cognitive reframing, and calming exercises during anxious waiting periods.
5. **Personal Health Intelligence Profile:** A unified, encrypted digital health record keeping history, prescriptions, and follow-up reminders accessible at all times.

---

## 🛠️ Technology Stack

| Layer | Technologies |
|---|---|
| **Backend API** | FastAPI (Python 3.11+), Uvicorn ASGI, Pydantic v2 |
| **Frontend UI** | React 18, TypeScript, Tailwind CSS, shadcn/ui, Framer Motion |
| **AI & Computer Vision** | PyTorch, MONAI, OpenCV, Hugging Face Transformers |
| **Conversational AI** | Google Gemini Live API, Medical NLP Parsers |
| **Database & Auth** | PostgreSQL, Supabase Authentication & Object Storage |
| **Containerization** | Docker, Docker Compose |

---

## 🚀 Setup & Execution Guide

### Prerequisites
- Python 3.10+ (Python 3.11 recommended)
- `pip` or virtual environment manager
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/kavishkat2002/CreativeX_ICBT.git
cd CreativeX_ICBT
```

### 2. Set Up a Virtual Environment
```bash
# Create virtual environment
python3 -m venv venv

# Activate on macOS / Linux:
source venv/bin/activate

# Activate on Windows:
# .\venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r project/requirements.txt
```

### 4. Run the Application Entry Point
```bash
# Option A: Run directly via Python entrypoint
cd project
python main.py

# Option B: Run via Uvicorn CLI
uvicorn project.main:app --host 0.0.0.0 --port 8000 --reload
```

The server will launch at: `http://127.0.0.1:8000`

---

## 📖 Interactive API Documentation

Once running, explore and test all live endpoints via the interactive Swagger UI:
- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
- **System Health Check:** [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health)

### Quick Testing with cURL

#### 1. AI Symptom Triage (`POST /api/v1/triage/chat`)
```bash
curl -X POST "http://127.0.0.1:8000/api/v1/triage/chat" \
     -H "Content-Type: application/json" \
     -d '{
       "symptoms_description": "I have a painless white ulcer on my inner cheek that has not healed for 3 weeks.",
       "duration_days": 21,
       "severity_scale": 4,
       "lifestyle_factors": ["Tobacco/Betel chew history"]
     }'
```

#### 2. Multi-Cancer Visual Image Analysis (`POST /api/v1/ai/analyze-image`)
```bash
curl -X POST "http://127.0.0.1:8000/api/v1/ai/analyze-image" \
     -H "Content-Type: application/json" \
     -d '{
       "category": "skin",
       "image_base64_or_url": "https://storage.meddoc.health/samples/skin_sample.jpg",
       "lesion_location": "Forehead near hairline",
       "reported_changes": "Gradually enlarging nodular spot"
     }'
```

#### 3. Medical Report Simplification (`POST /api/v1/ai/analyze-report`)
```bash
curl -X POST "http://127.0.0.1:8000/api/v1/ai/analyze-report" \
     -H "Content-Type: application/json" \
     -d '{
       "report_title": "Histopathology Biopsy Report",
       "report_text": "Biopsy specimen: Mild epithelial dysplasia identified on lateral tongue border. Hemoglobin: 11.2 g/dL."
     }'
```

#### 4. MedMind eCare Emotional Wellness Companion (`POST /api/v1/medmind/chat`)
```bash
curl -X POST "http://127.0.0.1:8000/api/v1/medmind/chat" \
     -H "Content-Type: application/json" \
     -d '{
       "persona": "Dr. Nuwan (Senior Psychological Counselor)",
       "user_message": "I received an elevated risk alert and I am feeling very anxious about my appointment."
     }'
```

---

## 📑 Detailed Documentation Links

- 📄 [Proposal Document (Proposal.docx)](docs/Proposal.docx): Complete formal proposal covering problem analysis, solution architecture, business model canvas, and growth roadmap.
- 🔄 [System Workflow (Workflow.md)](docs/Workflow.md): Detailed end-to-end user journeys, computer vision pipelines, report NLP architecture, and sequence diagrams.
- 📋 [Project Details (PROJECT_DETAILS.md)](docs/PROJECT_DETAILS.md): Comprehensive functional specifications, entity-relationship database schemas, and AI models.
- 🎥 [Project Demo Video (project-demo.mp4)](project-demo.mp4): Full walkthrough of the MedDoc web interface, AI assistant voice & text triage, image analysis, and report parser.

---

## 👥 Team Information — CreativeX Technology

- **Institution:** ICBT Campus
- **Competition Track:** Innodata AI Catalyst '26 (University Track)
- **Product:** MedDoc (Health Care & Services)
- **Repository URL:** `https://github.com/kavishkat2002/CreativeX_ICBT.git`

---

## ⚖️ Ethical & Clinical Disclaimer
MedDoc is designed exclusively as an **AI-assisted clinical decision support and healthcare navigation system**. All outputs, risk scores, and recommendations are intended to guide users toward qualified medical specialists and **do not replace licensed professional medical diagnosis or treatment**.
