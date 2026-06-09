#!/usr/bin/env python3
import os
import sys
import requests
import json

NOTES_DIR = os.path.expanduser("~/Vanguard-lab/notes")

def get_note_files():
    note_files = []
    for root, dirs, files in os.walk(NOTES_DIR):
        for file in files:
            if file.endswith(".md"):
                note_files.append(os.path.join(root, file))
    return note_files

def read_note(filepath):
    with open(filepath, "r") as f:
        return f.read()

def quiz_me(note_content):
    prompt = f"""You are a technical quiz master helping a network engineering student study.
Based on these study notes, ask me ONE question at a time.
After I answer, tell me if I was correct and explain briefly.
Then ask the next question.
Start with the first question now.

NOTES:
{note_content}"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "phi3",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]

def main():
    notes = get_note_files()
    if not notes:
        print("No notes found. Add markdown files to ~/Vanguard-lab/notes/")
        sys.exit(1)

    print("\nAvailable notes:")
    for i, note in enumerate(notes):
        print(f"{i+1}. {note}")

    choice = int(input("\nWhich note to study? Enter number: ")) - 1
    content = read_note(notes[choice])

    print("\nStarting quiz session. Type your answers and press Enter.")
    print("Type 'quit' to exit.\n")

    question = quiz_me(content)
    print(f"QUIZ MASTER: {question}\n")

    while True:
        answer = input("YOUR ANSWER: ")
        if answer.lower() == "quit":
            print("Session ended. Good work.")
            break

        follow_up = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi3",
                "prompt": f"Student answered: {answer}\nEvaluate their answer based on the notes and ask the next question.",
                "stream": False
            }
        )
        print(f"\nQUIZ MASTER: {follow_up.json()['response']}\n")

if __name__ == "__main__":
    main()
