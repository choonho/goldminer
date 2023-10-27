# Read name

import yaml

persona_file = "CHARACTER.yml"

class Persona:
    def __init__(self, name, **kwargs):
        self.name = name
        for k, v in kwargs.items():
            setattr(self, k, v)


    def load_persona(self):
        persona_path = f"{self.persona_dir}/{self.name}/{persona_file}"
        data = yaml.safe_load(open(persona_path))
        print(data)

def main(name):
    load_persona(name)

if __name__ == "__main__":
    name = "Belty"
    p = Persona(name, directory_path=f"./jellys")
    p.load_persona()
