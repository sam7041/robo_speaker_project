# 🤖 Robo Speaker Project

![Python](https://img.shields.io/badge/python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-active-success?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

**Robo Speaker** is a smart text-to-speech application that gives a voice to your text. It features a robust fallback engine that prioritizes the `pyttsx3` library but automatically switches to native system commands (Windows PowerShell or macOS `say`) if dependencies are missing, ensuring it works on almost any machine.

## ✨ Features

-   **Smart Fallback System**:
    -   **Primary**: Uses `pyttsx3` for consistent cross-platform audio.
    -   **Windows**: Falls back to `System.Speech` via PowerShell.
    -   **macOS**: Falls back to the native `say` command.
    -   **Fallback**: Gracefully degrades to printing text if no audio is possible.
-   **Interactive Mode**: A continuous CLI loop to type and speak instantly.
-   **CLI Arguments**: Supports one-shot commands (e.g., `--test "Hello"`) for quick testing.

## 📂 Project Structure

robo_speaker_project/
├── .idea/ # PyCharm project settings
├── .venv/ # Virtual environment files
├── pycache/ # Python bytecode cache
├── requirements # Dependencies list
├── robo_speaker.py # Main application source code
└── test_robo_speaker.py # Unit tests for the application


## 🛠️ Installation

1.  **Clone the repository**
    ```
    git clone https://github.com/yourusername/robo_speaker_project.git
    ```

2.  **Navigate to the project directory**
    ```
    cd robo_speaker_project
    ```

3.  **Install dependencies**
    Install the required packages using the `requirements` file:
    ```
    pip install -r requirements
    ```

## 🚀 Usage

### Interactive Mode
Run the script to start the conversation loop:

python robo_speaker.py

Welcome to RoboSpeaker 1.1. Created by Sameer Shukla.
Type text and press Enter to speak. Type 'q', 'quit' or 'exit' to stop.

Enter what you want me to speak: Hello World!


### Command Line Mode
You can use flags to speak a single phrase without entering the loop:

python robo_speaker.py --test "This is a quick test"


## 🧪 Running Tests

This project comes with a test suite to ensure the speech logic works correctly.

pytest



## 👤 Author

**Sameer Shukla**

-   Github: [@sam7041](https://github.com/sam7041)

## 📄 License

This project is licensed under the MIT License.

