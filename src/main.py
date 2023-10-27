# This is main function
import os

persona = os.environ.get('PERSONA')

def main(persona):
    print(f"Run {persona} function...")

if __name__ == "__main__":
    main(persona)
