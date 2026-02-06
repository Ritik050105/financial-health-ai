from fastapi import APIRouter

router = APIRouter()

@router.get("/gst/status")
def gst_status():
    return {
        "last_filing": "2024-12-31",
        "status": "COMPLIANT",
        "refund_pending": False
    }
