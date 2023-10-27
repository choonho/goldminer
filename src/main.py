# This is main function
import os
import persona

persona_name = os.environ.get('PERSONA', 'Wonny')

def _list_all_jellys():
    directory_path = './jellys'
    contents = os.listdir(directory_path)
    result = []
    for item in contents:
        result.append(item)
    return result

def _run_jelly(persona_name):
    try:
        print(f"Run {persona_name} jelly...")
        persona.main(persona_name)
    except Exception as e:
        print(e)

def main(persona_name):
    if persona_name == 'Wonny':
        jellys = _list_all_jellys()
    else:
        jellys = [persona_name]

    for jelly in jellys:
        _run_jelly(jelly)


if __name__ == "__main__":
    main(persona_name)
