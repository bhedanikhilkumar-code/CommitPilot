from src.state import load_state


def export_json_checkpoint_1(path: str):
    state = load_state()
    import json
    with open(path, 'w', encoding='utf-8') as fp:
        json.dump(state, fp, indent=2)
    return path

def export_json_checkpoint_9(path: str):
    state = load_state()
    import json
    with open(path, 'w', encoding='utf-8') as fp:
        json.dump(state, fp, indent=2)
    return path

def export_json_checkpoint_17(path: str):
    state = load_state()
    import json
    with open(path, 'w', encoding='utf-8') as fp:
        json.dump(state, fp, indent=2)
    return path

def export_json_checkpoint_25(path: str):
    state = load_state()
    import json
    with open(path, 'w', encoding='utf-8') as fp:
        json.dump(state, fp, indent=2)
    return path

def export_json_checkpoint_33(path: str):
    state = load_state()
    import json
    with open(path, 'w', encoding='utf-8') as fp:
        json.dump(state, fp, indent=2)
    return path
