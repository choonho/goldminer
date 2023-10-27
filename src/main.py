# This is main function
import os
from persona import Persona

persona_name = os.environ.get('PERSONA', 'Belty')

script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)

# Environments for all class
kargs = {
    'persona_dir': os.path.join(script_directory, 'characters'),
    }

def _run_character(persona_name):
    try:
        print(f"Run {persona_name} Persona...")
        p = Persona(persona_name, **kargs)
        p.load_persona()
    except Exception as e:
        print(e)

def main(persona_name):
    _run_character(persona_name)


if __name__ == "__main__":
    main(persona_name)
