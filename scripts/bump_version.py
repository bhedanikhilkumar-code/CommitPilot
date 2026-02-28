from pathlib import Path

VERSION_FILE = Path('VERSION')


def bump_patch(version: str) -> str:
    major, minor, patch = map(int, version.strip().split('.'))
    return f"{major}.{minor}.{patch + 1}"


def main():
    current = VERSION_FILE.read_text(encoding='utf-8').strip()
    new_version = bump_patch(current)
    VERSION_FILE.write_text(new_version + '\n', encoding='utf-8')
    print(f"Bumped version: {current} -> {new_version}")


if __name__ == '__main__':
    main()
