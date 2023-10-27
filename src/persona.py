# Read name

import yaml

persona_file = "CHARACTER.yml"

def load_persona(name):
    persona_path = f"./jellys/{name}/{persona_file}"
    data = yaml.safe_load(open(persona_path))
    print(data)

def main(name):
    load_persona(name)

if __name__ == "__main__":
    main("Belty")
