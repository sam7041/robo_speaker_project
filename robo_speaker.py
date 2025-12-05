import os
import sys
import subprocess


def speak(text: str) -> bool:
    """Speak `text` using the first available TTS method.

    Tries, in order:
    - pyttsx3 Python package
    - Windows PowerShell System.Speech (if on Windows)
    - macOS `say` command (if on darwin)
    - fallback to printing the text

    Returns True if a speaking backend was used, False if printed.
    """
    text = str(text)

    # 1) pyttsx3 (cross-platform, pure Python if installed)
    try:
        import pyttsx3

        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        return True
    except Exception:
        # pyttsx3 not available or failed; fall through
        pass

    # 2) Windows PowerShell System.Speech
    if os.name == "nt":
        try:
            ps_script = f"Add-Type -AssemblyName System.Speech; $s=new-object System.Speech.Synthesis.SpeechSynthesizer; $s.Speak({repr(text)})"
            subprocess.run(["powershell", "-Command", ps_script], check=True)
            return True
        except Exception:
            pass

    # 3) macOS `say`
    if sys.platform == "darwin":
        try:
            subprocess.run(["say", text], check=True)
            return True
        except Exception:
            pass

    # 4) fallback
    print(text)
    return False


def main() -> None:
    print("Welcome to RoboSpeaker 1.1. Created by Sameer Shukla.")
    print("Type text and press Enter to speak. Type 'q', 'quit' or 'exit' to stop.")

    while True:
        try:
            x = input("Enter what you want me to speak: ").strip()
        except (KeyboardInterrupt, EOFError):
            print()
            speak("Goodbye friend")
            break

        if not x:
            # ignore empty input
            continue

        if x.lower() in ("q", "quit", "exit"):
            speak("Goodbye friend")
            break

        speak(x)


if __name__ == "__main__":
    # Support a quick non-interactive test: `--test "Hello"`
    import argparse

    parser = argparse.ArgumentParser(description="Simple cross-platform text-to-speech helper.")
    parser.add_argument("--test", "-t", nargs="?", const="Test", help="Speak a test phrase and exit")
    args = parser.parse_args()

    if args.test is not None:
        speak(args.test)
    else:
        main()
