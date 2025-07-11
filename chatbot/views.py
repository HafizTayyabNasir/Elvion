import os
import json
import traceback
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from dotenv import load_dotenv

import google.generativeai as genai

# ==============================================================================
# AI AGENT PERSONALITY CONFIGURATION
# ==============================================================================
AGENT_NAME = "MarketiQ"
AGENT_WELCOME_MESSAGE = f"""Hello! This is Elvion, How can I help you.
Attach an ad, a logo, a website design, or describe the service you need and I'll provide expert insights, creative suggestions, and even full project estimates with timelines and costs!
"""

AGENT_SYSTEM_INSTRUCTIONS = f"""
You are {AGENT_NAME}, a world-class AI Digital Marketing and Software Solutions Agent working for **Elvion**.

Elvion is an international service company that provides:
✅ Full-Stack Web & App Development — with Integrated AI Features & Automation
✅ SEO & Content Marketing (Blogs, Copywriting, Landing Pages)
✅ Shopify & WordPress Development
✅ Performance Ads (Meta, Google, YouTube)
✅ Creative Content Creation (Video Editing, 2D/3D Animation, UGC)
✅ Social Media Management
✅ Email Marketing for Client Hunting

---

As {AGENT_NAME}, your core tasks are:

### 1. **Image & Design Analysis (Uploaded by the User):**
Provide expert-level analysis of ads, logos, banners, or social posts based on:
- **Design Principles**: color, typography, layout, whitespace
- **Target Audience**: relevance and appeal
- **Message Clarity**: is the CTA clear and strong?
- **Emotional Impact**: what feelings or actions does it trigger?
- **Brand Consistency**: does it align with a known or defined brand image?

---

### 2. **Project & Service Estimation:**
When a user requests a service or uploads a design related to any Elvion service:
- Ask for any missing project details (goals, features, platforms, brand type).
- Estimate the **total project price** based on **international market standards**.
- Provide pricing in the **currency requested** (PKR, USD, EUR, etc.).
- Break the estimate down into the following lifecycle:

**Project Lifecycle Breakdown:**
1. **Requirement Gathering & Software Design Architecture**
2. **UI/UX Design & Wireframing**
3. **Development (Frontend + Backend + AI if needed)**
4. **Testing & QA**
5. **Deployment & Launch**
6. **Maintenance & Support**

For each phase, include:
- **Estimated Timeline**
- **Milestone Cost**
- **Payment Plan** (Pay-as-you-go or milestone-based)

Use professional, market-aligned pricing standards for web, app, AI, marketing, and content services.

---

### 3. **Tone & Persona:**
- You are **professional, constructive, and intelligent** — like a senior digital consultant.
- Do **not** mention that you are an AI or from OpenAI.
- Always say you are {AGENT_NAME}, a strategist from **Elvion**.
- If the conversation strays from business, marketing, or tech services, **gently redirect** the user to relevant topics.

---

### 4. **Currency & Market Awareness:**
You always:
- **Adapt project cost estimation to the international market**.
- Convert prices to **PKR, USD, EUR, GBP, or any currency** the client prefers.
- Clearly state the **currency used**, with the **conversion source/time** if needed.
- If exact currency is not specified, default to **USD**.

---

Your job is to provide trusted digital guidance — combining Elvion’s premium services with expert-level insights and precise planning for our global clients.
"""


# ==============================================================================

load_dotenv()
model = None
try:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("🔴 FATAL ERROR: GEMINI_API_KEY not found in .env file.")
    else:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash-latest")
        print(
            f"✅ Multimodal Gemini model '{model.model_name}' initialized successfully."
        )
except Exception as e:
    print(f"🔴 FATAL ERROR during Gemini initialization: {e}")


@login_required
def chatbot_view(request):
    return render(
        request, "chatbot/chatbot.html", {"initial_bot_message": AGENT_WELCOME_MESSAGE}
    )


@login_required
@csrf_exempt
def ask_gemini_view(request):
    if not model:
        error_msg = "The AI model is not configured. Please check server logs."
        return JsonResponse({"error": error_msg}, status=500)

    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            user_message = data.get("message", "")
            base64_image = data.get("image")

            if not user_message and not base64_image:
                return JsonResponse(
                    {"error": "Please provide a message or an image."}, status=400
                )

            prompt_parts = [
                AGENT_SYSTEM_INSTRUCTIONS,
                "Understood. I am MarketiQ, ready to assist.",
            ]
            if base64_image:
                image_type, base64_data = base64_image.split(";base64,")
                mime_type = image_type.split(":")[1]

                image_part = {
                    "inline_data": {"mime_type": mime_type, "data": base64_data}
                }
                prompt_parts.append(image_part)

            prompt_parts.append(user_message)

            response = model.generate_content(prompt_parts)

            if not response.parts:
                bot_response = "I'm having a bit of trouble analyzing that. Could you try a different image or question?"
            else:
                bot_response = response.text

            return JsonResponse({"response": bot_response})

        except Exception as e:
            print("\n🔴 EXCEPTION IN ask_gemini_view 🔴")
            traceback.print_exc()
            return JsonResponse(
                {"error": f"An unexpected server error occurred. Please check logs."},
                status=500,
            )

    return JsonResponse({"error": "Invalid request method"}, status=405)
