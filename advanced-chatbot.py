import random
import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Predefined responses
responses = {
    "greetings": ["Hi!", "Hello!", "Hey there!", "Hi, how can I help you?"],
    "how_are_you": ["I'm doing well, thanks!", "Great, how about you?", "I'm fine, hope you're too!"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a nice day!"],
    "default": ["Sorry, I didn't understand that.", "Can you please rephrase?", "Hmm, I'm not sure I follow."]
}

# Keywords
keywords = {
    "greetings": ["hi", "hello", "hey", "good morning", "good evening"],
    "how_are_you": ["how are you", "how’s it going", "how are you doing"],
    "bye": ["bye", "goodbye", "see you", "later"]
}

def speak(text):
    print("Chatbot:", text)
    engine.say(text)
    engine.runAndWait()

def get_response(user_input):
    user_input = user_input.lower()
    for category, keys in keywords.items():
        if any(phrase in user_input for phrase in keys):
            return random.choice(responses[category])
    return random.choice(responses["default"])

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Speak now:")
        audio = recognizer.listen(source)

        try:
            query = recognizer.recognize_google(audio)
            print("You:", query)
            return query
        except sr.UnknownValueError:
            return "error"
        except sr.RequestError:
            return "error"

def chatbot():
    speak("Hello! I am your voice chatbot. Say something, or say 'exit' to stop.")

    while True:
        user_input = listen()
        if user_input == "error":
            speak("Sorry, I couldn't hear you clearly.")
            continue

        if "exit" in user_input.lower():
            speak("Goodbye! Have a great day.")
            break

        response = get_response(user_input)
        speak(response)

# Run the chatbot
chatbot()
