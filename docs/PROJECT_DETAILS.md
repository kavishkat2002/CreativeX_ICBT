# MedDoc — Comprehensive Project Details & Technical Specifications

**Project Name:** MedDoc  
**Tagline:** Early Detection. Better Tomorrows.  
**Team Name:** CreativeX Technology  
**University:** ICBT Campus  
**Category:** Health Care & Services  
**Competition:** Innodata AI Catalyst '26 — University Track  
**GitHub Repository:** `https://github.com/kavishkat2002/CreativeX_ICBT.git`  
**Document:** `docs/PROJECT_DETAILS.md`  

---

## 1. Project Abstract & Vision

**MedDoc** is an AI-powered digital healthcare platform engineered to bridge the critical gap between early symptom discovery, clinical risk assessment, and specialist healthcare intervention. In many regions, patients delay seeking professional consultation because they are uncertain of symptom severity, intimidated by medical jargon, or unable to identify the appropriate clinical specialist. These delays frequently result in late diagnoses for treatable conditions, particularly visible and accessible carcinomas such as oral, skin, breast, and eye abnormalities.

MedDoc solves this through a unified healthcare ecosystem combining:
1. **Intelligent Dual-Pathway Navigation:** Seamless choice between direct appointment booking and conversational AI-driven triage.
2. **Multi-Modal AI Clinical Screening:** Computer Vision lesion analysis and Medical NLP report summarization.
3. **Specialist & Hospital Routing:** Geo-aware and availability-aware routing to verified specialists.
4. **MedMind eCare:** An integrated AI emotional wellness companion that addresses pre-diagnostic anxiety.
5. **Personal Health Intelligence Profile:** A continuous, patient-owned health timeline.

---

## 2. Core Project Objectives

- **Democratize Early Assessment:** Provide accessible, non-diagnostic AI screening tools that help users recognize potential warning signs early.
- **De-escalate Clinical Anxiety:** Support patients emotionally during uncertain waiting periods with MedMind eCare.
- **Streamline Healthcare Discovery:** Match patients intelligently to the correct medical specialty (e.g., distinguishing between general dental needs and maxillofacial oncological concerns).
- **Bridge the Digital Divide:** Provide a fast, responsive, and mobile-friendly application usable in bandwidth-constrained environments.
- **Facilitate Doctor-Patient Communication:** Generate structured, pre-consultation clinical briefing notes from patient-uploaded images and documents to optimize physical consultation time.

---

## 3. Comprehensive Feature & Functionality Breakdown

### 3.1 Dual-Pathway Intake
- **Traditional Pathway:**
  - Searchable directory of verified hospitals, specialist clinics, and registered medical consultants.
  - Multi-parameter filtering: specialty, hospital affiliation, consultation fee, patient reviews, and next available slot.
  - One-click booking for in-person consultations or encrypted telemedicine video sessions.
- **AI-Guided Pathway:**
  - Natural conversation interface supporting text and voice inputs.
  - Guided clinical dialogue prompting for symptom duration, evolution, severity, and lifestyle risk factors.

### 3.2 Multi-Cancer Visual Risk Assessment Engine
- **Supported Anatomical Categories:**
  - **Oral Health:** Screening mucosal lesions, persistent ulcers, leukoplakia, and erythroplakia.
  - **Dermatology / Skin:** Evaluation of suspicious moles and lesions against ABCDE melanoma criteria and Basal Cell Carcinoma (BCC) patterns.
  - **Breast Health:** Visual analysis of superficial skin changes, erythema, and asymmetry.
  - **Ophthalmology / Eye:** Detection of scleral jaundice, conjunctival irregularities, and visible pupillary abnormalities.
- **Explainability & Output Metrics:**
  - **Confidence Score (%):** Statistical certainty of the visual classifier.
  - **Risk Stratification:** Categorization into *Low Risk (Monitor)*, *Moderate Risk (Consultation Recommended)*, or *Elevated Risk (Prompt Specialist Referral Needed)*.
  - **Grad-CAM Attention Heatmap:** Highlights key pixel regions influencing the model's output.
  - **Mandatory Clinical Disclaimer:** Clear statement that AI output is not a diagnosis.

### 3.3 Medical Report Summarizer & NLP Engine
- Upload engine for laboratory tests (Full Blood Count, Lipid Panels, Liver Function Tests) and biopsy pathology reports.
- Automated entity recognition identifying out-of-range clinical biomarkers.
- Dual summary generation:
  - **Patient View:** Plain-language explanation avoiding jargon to eliminate undue fear.
  - **Doctor View:** Concise tabular summary of abnormal parameters formatted for clinical review.

### 3.4 MedMind eCare — Mental Wellness Companion
- Safe, non-judgmental environment to discuss health anxieties, test result fears, and hospital apprehensions.
- Choice of companion personalities:
  - *Dr. Nuwan (Senior Psychological Counselor):* Structured cognitive reframing, breathing exercises, and emotional regulation.
  - *Friendly Companion:* Casual, comforting dialogue to alleviate loneliness and tension.
- Integrated safety protocols for distress keyword detection with escalation to emergency support resources.

### 3.5 Personal Health Intelligence Profile & Timeline
- Unified chronological repository for prescriptions, test results, doctor notes, and AI screening records.
- Longitudinal health pattern detection and automated follow-up reminders.

---

## 4. Technical Architecture & Technology Stack

```
┌─────────────────────────────────────────────────────────────┐
│                 PRESENTATION LAYER (CLIENT)                 │
│  React 18 + TypeScript | Tailwind CSS | shadcn/ui | Framer   │
└──────────────────────────────┬──────────────────────────────┘
                               │ HTTPS / JSON REST
┌──────────────────────────────▼──────────────────────────────┐
│                  APPLICATION LAYER (BACKEND)                │
│  FastAPI (Python 3.11+) | Uvicorn ASGI | Pydantic Schemas   │
│  ├── Auth & RBAC (JWT & Supabase Integration)               │
│  ├── Triage & Conversational Router                         │
│  ├── Computer Vision Inference Service                      │
│  ├── Medical NLP Parser Service                             │
│  ├── Recommendation & Hospital Booking Engine               │
│  └── MedMind eCare Dialogue Manager                         │
└──────────────────────────────┬──────────────────────────────┘
                               │
       ┌───────────────────────┴───────────────────────┐
       ▼                                               ▼
┌─────────────────────────────┐         ┌─────────────────────────────┐
│     AI & ML FOUNDATION      │         │     PERSISTENCE & DATA      │
│  PyTorch | MONAI | OpenCV   │         │  PostgreSQL Relational DB   │
│  Hugging Face Transformers  │         │  Supabase Auth & Storage    │
│  Google Gemini API          │         │  Dockerized Deployments     │
└─────────────────────────────┘         └─────────────────────────────┘
```

### 4.1 Frontend Stack
- **Framework:** React 18 with TypeScript for type-safe UI components.
- **Styling:** Tailwind CSS with shadcn/ui accessible component primitives.
- **Animation:** Framer Motion for micro-interactions and smooth page transitions.
- **State Management:** React Query / TanStack Query for efficient server-state caching.

### 4.2 Backend Stack
- **Framework:** FastAPI with asynchronous request handling via Uvicorn.
- **Data Validation:** Pydantic v2 schemas enforcing strict request/response contracts.
- **Authentication:** JWT tokens integrated with Supabase Auth for role-based access.

### 4.3 AI & ML Technologies
- **Computer Vision:** PyTorch, torchvision, and MONAI for medical image processing.
- **Medical NLP:** Hugging Face Transformers and spaCy for biomedical entity extraction.
- **Conversational Intelligence:** Google Gemini API for natural conversation and multimodal context.

---

## 5. Database Schema & Data Modeling

### Core Entities:
1. **Users (`users`):** `id`, `email`, `role` (patient, doctor, admin), `full_name`, `phone`, `created_at`.
2. **Patient Profiles (`patient_profiles`):** `user_id`, `dob`, `gender`, `blood_group`, `emergency_contact`, `allergies`, `medical_history`.
3. **Doctors (`doctors`):** `id`, `user_id`, `specialty`, `license_no`, `hospital_id`, `consultation_fee`, `rating`, `bio`.
4. **Hospitals (`hospitals`):** `id`, `name`, `city`, `address`, `contact_number`, `latitude`, `longitude`, `emergency_ready`.
5. **Appointments (`appointments`):** `id`, `patient_id`, `doctor_id`, `hospital_id`, `appointment_time`, `status`, `type` (in-person, telemedicine).
6. **AI Assessments (`ai_assessments`):** `id`, `patient_id`, `category` (oral, skin, breast, eye), `image_url`, `risk_tier`, `confidence_score`, `findings_summary`, `recommended_specialty`, `created_at`.
7. **Medical Documents (`medical_documents`):** `id`, `patient_id`, `file_name`, `file_url`, `extracted_summary`, `abnormal_flags`, `uploaded_at`.

---

## 6. Security, Compliance & Ethical AI Principles

- **Non-Diagnostic Stance:** Clear clinical disclaimers present across all AI outputs explicitly stating that MedDoc provides risk stratification and clinical navigation, not a definitive diagnosis.
- **Data Encryption:** TLS 1.3 encryption in transit and AES-256 encryption at rest.
- **Privacy by Design:** Strict anonymization and stripping of Personally Identifiable Information (PII) before passing medical reports to AI parsing pipelines.
- **Role-Based Isolation:** Doctors only access medical records for patients with active bookings or explicit data consent.

---

## 7. Business Model & Monetization Strategy

MedDoc employs a sustainable B2C and B2B hybrid model centered on the **MedDoc ePass Membership**:

| Tier | Target | Key Inclusions | Price Model |
|------|--------|----------------|-------------|
| **Standard (Free)** | General Public | Hospital booking, directory search, standard AI symptom triage (limited queries). | Free |
| **Silver Health ePass** | Individuals | Unlimited AI health consultations, priority appointment booking, cloud health records, partner lab discounts. | Monthly / Annual |
| **Gold Care ePass** | Families | Multi-member coverage (up to 5), complimentary monthly telemedicine consultation, priority customer care, home lab sample collection. | Monthly / Annual |
| **Platinum ePass** | Executive & Senior Care | Dedicated healthcare concierge, annual executive screening packages, accelerated hospital admission, comprehensive care management. | Premium Annual |

**B2B Streams:** Hospital SaaS subscriptions for clinical queue management, diagnostic lab referral commissions, and telemedicine platform transaction fees.
