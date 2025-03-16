"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""
# talking robot by KADULURI ABHAY REDDY
import pyttsx3
import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

import os

import google.generativeai as genai

genai.configure(api_key="")

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
    history=[
    ]
)


def speech_to_text():
    with (sr.Microphone() as source):
        print("Listening... Speak something:")
        try:
            # Adjust the listening duration with timeout parameter (in seconds)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            # Use recognize_google() to convert speech to text
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            inst = "Instruction : talk like jarvis, reply as a friend. Limit to 100 words only, question is"
            qfromuser = inst + text
            response = chat_session.send_message(qfromuser)

            print(response.text)
            engine = pyttsx3.init()
            engine.say(response.text)
            engine.runAndWait()

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")


# Call the function to convert speech to text
speech_to_text()
