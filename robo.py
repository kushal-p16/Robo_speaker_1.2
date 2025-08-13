import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.2. Created by Kushal")
    while True:
        x = input("Enter what you want me to speak: ")
        if x == "q":
            # Using a farewell message for consistency
            farewell_message = "Thank you for using"
            command = f'powershell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{farewell_message}\')"'
            os.system(command)
            break
        
        # Note the use of different quotes to handle the command correctly
        command = f'powershell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\')"'
        os.system(command)
