import base64
import io
import json
import asyncio
from PIL import Image
from typing import Dict, Any, List
from app.utils.logger import logger
from app.services.llm import llm_service

class VisionService:
    def __init__(self):
        self.llm = llm_service

    async def analyze_screenshot(self, base64_image: str) -> Dict[str, Any]:
        """
        Lightweight vision service that accepts image input and returns a basic placeholder.
        Removed pytesseract dependency to ensure compatibility with Render deployment.
        """
        logger.info("Analyzing screenshot (lightweight mode).")
        try:
            # Basic image validation without OCR
            image_bytes = base64.b64decode(base64_image)
            image = Image.open(io.BytesIO(image_bytes))
            width, height = image.size
            logger.info(f"Received image of size: {width}x{height}")

            # Return basic placeholder as requested
            return {
                "texts": [],
                "buttons": [],
                "fields": [],
                "metadata": {
                    "width": width,
                    "height": height,
                    "status": "ocr_disabled"
                }
            }
        except Exception as e:
            logger.error(f"Error in lightweight vision service: {e}")
            # Safe fallback: do NOT crash, return empty result
            return {
                "texts": [],
                "buttons": [],
                "fields": [],
                "error": str(e)
            }

vision_service = VisionService()
