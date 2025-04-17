import eel 
from engine.command import allCommands, speak



def run_assistant():
    eel.init('web')  # your frontend directory
    eel.start('index.html', block=False)
    speak("Welcome back, Geeth. How can I help you today?")
    
    while True:
        try:
            allCommands()
        except Exception as e:
            print(f"⚠️ Error in assistant loop: {e}")