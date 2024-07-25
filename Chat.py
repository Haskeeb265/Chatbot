import google.generativeai as genai

GOOGLE_API_KEY = ""
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('')
question = ''
response = model.generate_content(question)
response.resolve()
response.text