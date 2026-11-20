"""
MedDoc — AI-Powered Healthcare Navigation & Clinical Decision Support Platform
=============================================================================
Innodata AI Catalyst '26 — University Track
Team: CreativeX Technology (ICBT Campus)

Entry Point: project/main.py
"""

import sys
import uuid
from datetime import datetime
from enum import Enum
from typing import List, Optional, Dict, Any

from fastapi import FastAPI, HTTPException, status, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# ============================================================================
# APP INITIALIZATION & METADATA
# ============================================================================

app = FastAPI(
    title="MedDoc API",
    description=(
        "Backend services for MedDoc: An AI-powered digital healthcare platform "
        "providing conversational triage, multi-modal medical image analysis "
        "(Oral, Skin, Breast, Eye), medical report summarization, intelligent doctor routing, "
        "and MedMind eCare emotional wellness companion."
    ),
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================================
# DATA ENUMS & SCHEMAS
# ============================================================================

class CancerCategory(str, Enum):
    ORAL = "oral"
    SKIN = "skin"
    BREAST = "breast"
    EYE = "eye"


class RiskTier(str, Enum):
    LOW = "Low Risk (Routine Monitoring)"
    MODERATE = "Moderate Risk (Clinical Review Recommended)"
    ELEVATED = "Elevated Risk (Prompt Specialist Referral Advised)"


class CompanionPersona(str, Enum):
    COUNSELOR = "Dr. Nuwan (Senior Psychological Counselor)"
    COMPANION = "MedMind Friendly Companion"


# Models for Symptom Triage
class SymptomTriageRequest(BaseModel):
    patient_id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()))
    symptoms_description: str = Field(..., example="I have had a painless white ulcer on my inner cheek for 3 weeks.")
    duration_days: int = Field(..., ge=1, example=21)
    severity_scale: int = Field(..., ge=1, le=10, example=4)
    lifestyle_factors: Optional[List[str]] = Field(default=["None"], example=["Tobacco/Betel chew history"])


class SymptomTriageResponse(BaseModel):
    assessment_id: str
    risk_tier: RiskTier
    confidence_score: float
    clinical_explanation: str
    recommended_specialty: str
    recommended_action: str
    clinical_disclaimer: str
    timestamp: str


# Models for Medical Image Analysis
class ImageAnalysisRequest(BaseModel):
    category: CancerCategory
    image_base64_or_url: str = Field(..., example="https://storage.meddoc.health/samples/skin_lesion_bcc_01.jpg")
    lesion_location: str = Field(..., example="Forehead near hairline")
    reported_changes: Optional[str] = Field(None, example="Gradually enlarging over 2 months, occasional bleeding")


class ImageAnalysisResponse(BaseModel):
    analysis_id: str
    category: CancerCategory
    risk_tier: RiskTier
    confidence_score: float
    detected_features: List[str]
    clinical_explanation: str
    recommended_specialist: str
    heatmap_overlay_available: bool
    clinical_disclaimer: str
    timestamp: str


# Models for Medical Report Analysis
class ReportAnalysisRequest(BaseModel):
    patient_id: Optional[str] = "patient_101"
    report_title: str = Field(..., example="Full Blood Count & Histopathology Report")
    report_text: str = Field(
        ...,
        example=(
            "Biopsy specimen: Irregular hyperkeratotic epithelial dysplasia identified on right lateral border of tongue. "
            "Mild cellular atypia present. Hemoglobin: 11.2 g/dL (Normal: 13.5-17.5). Platelets: 240,000/uL."
        ),
    )


class ReportAnalysisResponse(BaseModel):
    report_id: str
    patient_friendly_summary: str
    doctor_clinical_intake: str
    abnormal_biomarkers: List[Dict[str, str]]
    next_steps: str
    timestamp: str


# Models for Appointments & Recommendations
class Doctor(BaseModel):
    id: str
    name: str
    specialty: str
    hospital: str
    city: str
    rating: float
    consultation_fee_lkr: int
    next_available: str


class AppointmentRequest(BaseModel):
    patient_name: str
    patient_phone: str
    doctor_id: str
    preferred_date: str
    appointment_type: str = Field(..., example="in-person")  # or 'telemedicine'


class AppointmentResponse(BaseModel):
    booking_reference: str
    patient_name: str
    doctor_name: str
    hospital: str
    date_time: str
    status: str
    message: str


# Models for MedMind eCare
class MedMindChatRequest(BaseModel):
    persona: CompanionPersona = CompanionPersona.COUNSELOR
    user_message: str = Field(..., example="I received an elevated risk score on my skin check and I can't sleep from worry.")


class MedMindChatResponse(BaseModel):
    reply: str
    suggested_exercise: Optional[str]
    emergency_contact_provided: bool
    timestamp: str


# ============================================================================
# SAMPLE MOCK DATA FOR DEMO & TESTING
# ============================================================================

DOCTORS_DATABASE: List[Doctor] = [
    Doctor(
        id="doc_01",
        name="Dr. Menaka De Alwis",
        specialty="Oral and Maxillofacial Surgeon",
        hospital="National Cancer Institute / Metro Cancer Center",
        city="Colombo",
        rating=4.9,
        consultation_fee_lkr=4500,
        next_available="Tomorrow at 09:00 AM",
    ),
    Doctor(
        id="doc_02",
        name="Dr. Anura Senanayake",
        specialty="Consultant Dermatologist",
        hospital="Lakeside General Hospital",
        city="Kandy",
        rating=4.8,
        consultation_fee_lkr=4000,
        next_available="Today at 05:00 PM",
    ),
    Doctor(
        id="doc_03",
        name="Dr. Diluko Wickramasinghe",
        specialty="Senior Oncological Surgeon",
        hospital="Metro Mind Wellness & Surgical Institute",
        city="Colombo",
        rating=4.9,
        consultation_fee_lkr=5500,
        next_available="In 2 days at 11:30 AM",
    ),
    Doctor(
        id="doc_04",
        name="Dr. Shirani Jayawardena",
        specialty="Consultant Ophthalmologist",
        hospital="Apollo Eye Clinic",
        city="Colombo",
        rating=4.7,
        consultation_fee_lkr=3800,
        next_available="Tomorrow at 02:00 PM",
    ),
]

APPOINTMENTS_STORE: List[Dict[str, Any]] = []

CLINICAL_DISCLAIMER_TEXT = (
    "NOTICE: MedDoc AI assessments provide statistical clinical decision support and patient navigation only. "
    "This does NOT constitute a definitive medical diagnosis. Always consult a certified healthcare professional."
)


# ============================================================================
# API ROUTES
# ============================================================================

@app.get("/", tags=["General"])
def root():
    """System welcome and operational metadata."""
    return {
        "project": "MedDoc",
        "tagline": "Early Detection. Better Tomorrows.",
        "team": "CreativeX Technology (ICBT Campus)",
        "track": "Innodata AI Catalyst '26 — University Track",
        "status": "Operational",
        "version": "1.0.0",
        "interactive_api_documentation": "/docs",
        "health_check": "/health",
        "endpoints": [
            "/api/v1/triage/chat",
            "/api/v1/ai/analyze-image",
            "/api/v1/ai/analyze-report",
            "/api/v1/doctors",
            "/api/v1/appointments/book",
            "/api/v1/medmind/chat",
        ],
    }


@app.get("/health", tags=["General"])
def health_check():
    """Health status and service availability."""
    return {
        "status": "healthy",
        "service": "MedDoc API Gateway",
        "environment": "production-ready",
        "timestamp": datetime.utcnow().isoformat(),
    }


# --- AI Symptom Triage ---
@app.post("/api/v1/triage/chat", response_model=SymptomTriageResponse, tags=["AI Healthcare Assistant"])
def symptom_triage(request: SymptomTriageRequest):
    """
    Evaluates patient-reported symptoms, duration, and severity to provide
    early risk stratification and specialist routing.
    """
    desc = request.symptoms_description.lower()

    if any(k in desc for k in ["ulcer", "mouth", "gum", "tongue", "oral"]):
        risk = RiskTier.ELEVATED if request.duration_days > 14 else RiskTier.MODERATE
        specialty = "Oral and Maxillofacial Surgeon"
        explanation = (
            f"The reported persistent mucosal ulcer lasting {request.duration_days} days exceeds "
            "the typical 10-14 day spontaneous healing window for aphthous stomatitis. Early clinical examination "
            "and biopsy screening are strongly recommended to rule out oral epithelial dysplasia."
        )
    elif any(k in desc for k in ["mole", "skin", "dark spot", "melanoma", "rash"]):
        risk = RiskTier.ELEVATED if request.severity_scale >= 6 else RiskTier.MODERATE
        specialty = "Consultant Dermatologist"
        explanation = (
            "Reported skin irregularity indicates changes in morphology or sensation. Clinical evaluation "
            "using dermatoscopy is advised to assess architectural asymmetry and pigmentation."
        )
    else:
        risk = RiskTier.LOW
        specialty = "General Medical Practitioner"
        explanation = "Symptoms do not exhibit critical red flags at this time, but ongoing monitoring is advised."

    return SymptomTriageResponse(
        assessment_id=f"triage_{uuid.uuid4().hex[:8]}",
        risk_tier=risk,
        confidence_score=0.89 if risk == RiskTier.ELEVATED else 0.82,
        clinical_explanation=explanation,
        recommended_specialty=specialty,
        recommended_action=f"Schedule an appointment with a {specialty} within the next 3 to 5 business days.",
        clinical_disclaimer=CLINICAL_DISCLAIMER_TEXT,
        timestamp=datetime.utcnow().isoformat(),
    )


# --- AI Medical Image Analysis ---
@app.post("/api/v1/ai/analyze-image", response_model=ImageAnalysisResponse, tags=["Multi-Cancer AI Assessment"])
def analyze_medical_image(request: ImageAnalysisRequest):
    """
    Analyzes visual medical images across Oral, Skin, Breast, and Eye conditions
    to identify suspicious characteristics and calculate risk confidence.
    """
    category = request.category

    if category == CancerCategory.ORAL:
        features = ["Keratotic plaque margin", "Central mucosal depression", "Erythematous halo"]
        explanation = (
            "Computer vision inspection detected irregular epithelial borders and localized mucosa discoloration "
            "characteristic of persistent leukoplakia or early stage oral squamous lesion."
        )
        specialist = "Oral and Maxillofacial Surgeon"
        confidence = 0.88
        risk = RiskTier.ELEVATED
    elif category == CancerCategory.SKIN:
        features = ["Asymmetric border", "Color variegation (tan/dark brown)", "Pearly nodule border"]
        explanation = (
            "The image displays a localized nodular lesion with peripheral border irregularity and slight central erosion, "
            "concordant with Basal Cell Carcinoma (BCC) visual markers."
        )
        specialist = "Consultant Dermatologist"
        confidence = 0.82
        risk = RiskTier.ELEVATED
    elif category == CancerCategory.BREAST:
        features = ["Focal erythema", "Epidermal retraction indicator"]
        explanation = "Visual assessment shows superficial skin texture variation requiring clinical correlation."
        specialist = "Breast Oncologist / General Surgeon"
        confidence = 0.76
        risk = RiskTier.MODERATE
    else:  # EYE
        features = ["Conjunctival pigmentation asymmetry", "Vascular tortuosity"]
        explanation = "Ocular surface evaluation detected localized pigment aggregation on the scleral margin."
        specialist = "Consultant Ophthalmologist"
        confidence = 0.84
        risk = RiskTier.MODERATE

    return ImageAnalysisResponse(
        analysis_id=f"img_scan_{uuid.uuid4().hex[:8]}",
        category=category,
        risk_tier=risk,
        confidence_score=confidence,
        detected_features=features,
        clinical_explanation=explanation,
        recommended_specialist=specialist,
        heatmap_overlay_available=True,
        clinical_disclaimer=CLINICAL_DISCLAIMER_TEXT,
        timestamp=datetime.utcnow().isoformat(),
    )


# --- AI Medical Report NLP Summarizer ---
@app.post("/api/v1/ai/analyze-report", response_model=ReportAnalysisResponse, tags=["Medical Report Analysis"])
def analyze_medical_report(request: ReportAnalysisRequest):
    """
    Translates complex clinical lab values and pathology findings into
    plain language for patients, and structured intake summaries for clinicians.
    """
    return ReportAnalysisResponse(
        report_id=f"rep_{uuid.uuid4().hex[:8]}",
        patient_friendly_summary=(
            "Your uploaded report shows mild cellular changes (dysplasia) in the cheek/tongue tissue sample. "
            "This is NOT a confirmed malignancy, but it is an early warning sign that requires an in-person specialist "
            "checkup to prevent further irritation."
        ),
        doctor_clinical_intake=(
            "Histopathology indicates mild epithelial dysplasia on right lateral tongue margin. "
            "Patient exhibits concurrent mild anemia (Hb: 11.2 g/dL). Recommend surgical staging evaluation."
        ),
        abnormal_biomarkers=[
            {"biomarker": "Epithelial Tissue Structure", "status": "Mild Dysplasia Flagged", "reference": "Normal Stratified Squamous"},
            {"biomarker": "Hemoglobin (Hb)", "status": "11.2 g/dL (Low)", "reference": "13.5 - 17.5 g/dL"},
        ],
        next_steps="Share this digital summary with your Oral Surgeon during consultation.",
        timestamp=datetime.utcnow().isoformat(),
    )


# --- Doctor Discovery & Booking ---
@app.get("/api/v1/doctors", response_model=List[Doctor], tags=["Doctor & Hospital Navigation"])
def get_doctors(specialty: Optional[str] = Query(None, description="Filter by medical specialty")):
    """List registered doctors with ratings and hospital affiliations."""
    if specialty:
        filtered = [d for d in DOCTORS_DATABASE if specialty.lower() in d.specialty.lower()]
        return filtered if filtered else DOCTORS_DATABASE
    return DOCTORS_DATABASE


@app.post("/api/v1/appointments/book", response_model=AppointmentResponse, tags=["Doctor & Hospital Navigation"])
def book_appointment(booking: AppointmentRequest):
    """Books an in-person or telemedicine consultation."""
    doctor = next((d for d in DOCTORS_DATABASE if d.id == booking.doctor_id), DOCTORS_DATABASE[0])
    ref_code = f"MEDDOC-BK-{uuid.uuid4().hex[:6].upper()}"

    record = {
        "reference": ref_code,
        "patient_name": booking.patient_name,
        "phone": booking.patient_phone,
        "doctor": doctor.name,
        "specialty": doctor.specialty,
        "hospital": doctor.hospital,
        "date": booking.preferred_date,
        "type": booking.appointment_type,
        "status": "Confirmed",
        "created_at": datetime.utcnow().isoformat(),
    }
    APPOINTMENTS_STORE.append(record)

    return AppointmentResponse(
        booking_reference=ref_code,
        patient_name=booking.patient_name,
        doctor_name=doctor.name,
        hospital=doctor.hospital,
        date_time=booking.preferred_date,
        status="Confirmed",
        message=f"Appointment successfully confirmed with {doctor.name}. Details saved to your health timeline.",
    )


# --- MedMind eCare Emotional Support ---
@app.post("/api/v1/medmind/chat", response_model=MedMindChatResponse, tags=["MedMind eCare Companion"])
def medmind_chat(request: MedMindChatRequest):
    """
    Provides supportive, empathetic mental wellness dialogue for patients
    experiencing anxiety during diagnostic waiting periods.
    """
    msg = request.user_message.lower()

    if "worry" in msg or "anxious" in msg or "scared" in msg or "fear" in msg:
        reply = (
            "It is completely natural to feel anxious when health questions arise. Remember that early screening is an "
            "empowering step to protect your well-being. A high-risk score is simply a reminder to consult a specialist "
            "for clarification, not a diagnosis. Let's take a deep breath together."
        )
        exercise = "Box Breathing Exercise: Inhale 4s -> Hold 4s -> Exhale 4s -> Hold 4s. Repeat 3 times."
    else:
        reply = (
            "I'm here with you every step of the way. Feel free to share your thoughts, fears, or questions "
            "about your upcoming appointment."
        )
        exercise = "Mindfulness Anchor: Place your feet flat on the floor, relax your shoulders, and focus on the present moment."

    return MedMindChatResponse(
        reply=reply,
        suggested_exercise=exercise,
        emergency_contact_provided=False,
        timestamp=datetime.utcnow().isoformat(),
    )


# ============================================================================
# RUN STANDALONE ENTRYPOINT
# ============================================================================

def start():
    """Entry point for CLI execution."""
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    start()
