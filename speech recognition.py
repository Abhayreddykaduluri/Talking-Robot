import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Function to convert speech to text
def speech_to_text():
    with sr.Microphone() as source:
        print("Listening... Speak something:")
        try:
            # Adjust the listening duration with timeout parameter (in seconds)
            audio = recognizer.listen(source, timeout=5)
            # Use recognize_google() to convert speech to text
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

# Call the function to convert speech to text
speech_to_text()
