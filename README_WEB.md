# 🤖 Web RoboSpeaker

A fun, interactive text-to-speech (TTS) web application with an animated robot face. This project brings the classic RoboSpeaker concept to the browser using pure HTML, CSS, and JavaScript.


# 🚀 Live Demo
You can try out the live version of RoboSpeaker here:

 https://kushal-p16.github.io/Robo_speaker_1.2/


# ✨ Features
🗣️ Browser-Native TTS: Utilizes the built-in Web Speech API for high-quality, zero-latency speech synthesis.

🤖 Animated Robot: A friendly robot face with blinking eyes and a mouth that animates when it speaks.

📱 Responsive Design: A clean and modern UI that looks great on both desktop and mobile devices, built with Tailwind CSS.

⚡ Instant Feedback: Type in the text area, press the button (or Enter), and hear the robot speak immediately.

✅ Compatibility Check: Gracefully informs the user if their browser does not support the Web Speech API.

⌨️ Keyboard Shortcut: Press the Enter key in the text area to trigger the speech.



# 🛠️ Tech Stack
HTML5: For the basic structure and content.

Tailwind CSS: For rapid, utility-first styling.

Custom CSS: For the robot face animations (@keyframes).

JavaScript (ES6+): To handle user interactions and the Web Speech API.

Web Speech API: The core browser technology used for text-to-speech.


# 📂 How to Run Locally

1. Clone the repository:

        git clone https://github.com/kushal-p16/Robo_speaker.git


2. Navigate to the project directory:
 
        cd Robo_speaker

   
3. Open in Browser: Open the index.html file in any modern web browser (like Chrome, Firefox, Edge, or Safari).

# 💡 How It Works
<details>
<summary>Click to see the technical explanation</summary> 


The application's logic is self-contained within the index.html file.

DOM Manipulation: JavaScript first gets references to the necessary HTML elements (the button, textarea, robot mouth, etc.).

API Check: It checks if window.speechSynthesis exists to determine if the browser supports the required API.

Event Listeners:

A click listener on the "Make Me Speak" button triggers the main function.

A keydown listener on the textarea checks for the Enter key to provide a convenient shortcut.

Speech Synthesis:

When triggered, a SpeechSynthesisUtterance object is created with the text from the textarea.

The window.speechSynthesis.speak() method is called to voice the utterance.

Animation Sync:

The utterance object has onstart and onend event handlers.

When the speech starts (onstart), a .speaking CSS class is added to the robot's mouth element, which activates the animation.

When the speech ends (onend), the class is removed, stopping the animation.

</details>
