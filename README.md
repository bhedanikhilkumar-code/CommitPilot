# CommitPilot

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Status](https://img.shields.io/badge/Status-Active-success)
![CI](https://github.com/bhedanikhilkumar-code/CommitPilot/actions/workflows/ci.yml/badge.svg)

CommitPilot is a lightweight Python CLI that helps developers plan, track, and sustain daily coding consistency.

## 🚀 Why CommitPilot?
Maintaining momentum is hard when goals are vague. CommitPilot turns contribution targets into clear, actionable daily progress.

## ✨ Core Features
- **Goal tracking** for daily commit targets
- **Task management** (add, list, mark complete)
- **Progress metrics** with completion percentage
- **Quick reporting** for status and task breakdown
- **Simple local JSON state** (no database setup required)

## 🧱 Project Structure
```text
CommitPilot/
├── data/
│   └── state.json
├── docs/
├── src/
│   ├── cli.py
│   ├── goals.py
│   ├── metrics.py
│   ├── reports.py
│   ├── state.py
│   ├── streak.py
│   └── tasks.py
├── main.py
├── requirements.txt
└── ROADMAP.md
```

## 🏷️ Versioning & Release
- Current version is tracked in VERSION.
- Bump patch version locally using:
  - python scripts/bump_version.py`n- Create a release by pushing a tag:
  - git tag v0.1.1 && git push origin v0.1.1`n
## ⚙️ Getting Started
### 1) Clone the repository
```bash
git clone https://github.com/bhedanikhilkumar-code/CommitPilot.git
cd CommitPilot
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
```

### 3) Run the CLI
```bash
python main.py
```

## 🗺️ Roadmap
Planned improvements are tracked in [`ROADMAP.md`](./ROADMAP.md), including:
- richer CLI commands
- export/reporting options
- improved streak analytics

## 🤝 Contributing
Contributions are welcome. If you’d like to improve CommitPilot:
1. Fork the repo
2. Create a feature branch
3. Commit with clear messages
4. Open a pull request

## 🖼️ Screenshots
> Add screenshots to `docs/screenshots/` and link them below.

### CLI Overview
![CLI Overview](docs/screenshots/cli-overview.png)

### Progress Output
![Progress Output](docs/screenshots/progress-output.png)

## 📄 License
This project is licensed under the [MIT License](./LICENSE).


## Iterative Enhancements
- Iterative feature checkpoint 7
- Iterative feature checkpoint 15
- Iterative feature checkpoint 23
- Iterative feature checkpoint 31
- Iterative feature checkpoint 39
- Iterative feature checkpoint 47
- Iterative feature checkpoint 55
- Iterative feature checkpoint 63
- Iterative feature checkpoint 71
- Iterative feature checkpoint 79
- Iterative feature checkpoint 87
