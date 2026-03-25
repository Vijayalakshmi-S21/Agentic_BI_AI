import google.generativeai as genai

genai.configure(api_key="AIzaSyD_-lCwnwkX1Ujd9BIala2Uoam5MmBGxfU")

model = genai.GenerativeModel("gemini-1.5-flash")

def ask_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text