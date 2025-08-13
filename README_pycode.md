# 🤖 RoboSpeaker v1.2

A simple and fun command-line text-to-speech (TTS) application for Windows. Type anything, and your computer will say it out loud!

# A short animation showing the script welcoming the user, taking input, speaking it, and then quitting with 'q'

# ✨ Features
🗣️ Instant Text-to-Speech: Converts your text to spoken words immediately. 

⌨️ Simple CLI Interface: Runs directly in your terminal, no GUI needed.

🚀 Lightweight & Zero-Dependency: Uses built-in Windows tools, so no external Python libraries like pip install are required.

👋 Interactive Loop: Continuously prompts for new text until you decide to quit.

# 📋 Requirements
Operating System: Windows 10 or 11 (due to its reliance on PowerShell and the .NET Speech API).

Python: Python 3.x installed and added to your system's PATH.

# 🚀 Getting Started
Installation & Usage

<b>1. Clone the repository (or just download the robospeaker.py file):</b>

       
       git clone https://github.com/your-username/robospeaker.git

<b>2. Navigate to the project directory:</b>

       
       cd robospeaker

<b>3. Run the script from your terminal:</b>

       
       python robospeaker.py

<b>4. Start Speaking!</b>

# user manual
* The script will welcome you and ask for input.

* Type any sentence and press Enter.

* To exit the program, type q and press Enter.

# 🛠️ How It Works
<details>
<summary>Click to see the technical explanation</summary>


This script is a clever Python wrapper that doesn't perform the text-to-speech itself. 
Instead, it dynamically builds and executes a command using Windows PowerShell.


<b>The core command is:</b>

       powershell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('your text here')"

        
This command tells PowerShell to:

        1. Add-Type -AssemblyName System.Speech: Load the native .NET library responsible for speech functions.
       

        2. (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(...): Create an instance of the speech engine and call its Speak method with the text you provided.

</details>

# 👤 Credits
This project was created by
<b>Kushal p</b>.
