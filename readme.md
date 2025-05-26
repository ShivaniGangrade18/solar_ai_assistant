# ☀️ Solar Industry AI Assistant

This project is an AI-powered rooftop analysis tool that uses computer vision to evaluate the solar panel installation potential of rooftops using images. It simulates output, cost, and ROI (Return on Investment) for solar power generation based on the uploaded rooftop image.

---

## 📌 Features

- Upload any rooftop image
- Uses Hugging Face BLIP model to describe the rooftop visually
- Simulates:
  - Solar panel installation suitability
  - Expected solar output (kWh/month)
  - Suggested panel layout
  - Estimated cost and payback period

---

## 🧠 How It Works

1. The app loads the BLIP (Bootstrapped Language-Image Pretraining) model from Hugging Face.
2. You upload a rooftop image (JPEG or PNG).
3. The AI describes the image (e.g., "a flat rooftop with sunlight").
4. Based on the description, it simulates whether solar panels can be installed.

---

## 📁 Folder Structure

solar_ai_assistant/
├── app.py # Main Streamlit application code
├── rooftop.jpg # Sample rooftop image (you can test with this)
├── requirements.txt # All required Python libraries
└── README.md # Project documentation (this file)
2. Create and Activate a Virtual Environment
python -m venv venv
venv\Scripts\activate        # On Windows
3. Install All Dependencies
pip install -r requirements.txt
4. Run the App
streamlit run app.py
5. Open in Browser
Once it runs, it will open in your browser 

🖼 Example Use Case
Upload a clear rooftop image (e.g., a flat rooftop in sunlight).

The AI will analyze it and simulate:

Estimated output: 450–600 kWh/month

Layout suggestion: 10 panels (300W each)

Cost range: ₹1.5–2 lakhs

ROI: 3–4 years

🔧 Tech Stack
Streamlit – Web app framework

Transformers – Hugging Face library for models

BLIP Model – AI image captioning model

PyTorch – Deep learning framework

✨ Future Improvements
Use actual rooftop size and sunlight data for real output calculation

Add location detection via maps

Export analysis report to PDF

Deploy on Hugging Face Spaces