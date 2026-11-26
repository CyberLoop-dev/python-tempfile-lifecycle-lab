<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:0f766e&height=170&section=header&text=python%20tempfile%20lifecycle%20lab&fontSize=36&fontColor=ffffff&animation=twinkling" alt="Animated wave header"/></p>
<p align="center"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&duration=2800&pause=900&color=14B8A6&center=true&vCenter=true&width=760&lines=python%20tempfile%20lifecycle%20lab%20%7C%20inspect%2C%20understand%2C%20improve" alt="Animated title"/></p>
<p align="center"><img src="https://img.shields.io/github/license/CyberLoop-dev/python-tempfile-lifecycle-lab?style=for-the-badge" alt="License"/> <img src="https://img.shields.io/github/languages/top/CyberLoop-dev/python-tempfile-lifecycle-lab?style=for-the-badge" alt="Language"/> <img src="https://img.shields.io/github/stars/CyberLoop-dev/python-tempfile-lifecycle-lab?style=for-the-badge" alt="Stars"/> <img src="https://img.shields.io/github/last-commit/CyberLoop-dev/python-tempfile-lifecycle-lab?style=for-the-badge" alt="Last commit"/></p>
<p align="center"><img src="assets/mark.svg" alt="python-tempfile-lifecycle-lab project mark" width="520"/></p>

## 🧭 Overview

`python-tempfile-lifecycle-lab` runs a safe, self-contained demonstration of Python's temporary-file helpers. It shows when temporary paths exist, how context managers clean them up, and why closing a named temporary file matters for cross-platform workflows.

## ✨ Features

- 📁 Demonstrates `TemporaryDirectory` creation and cleanup
- 📄 Demonstrates `NamedTemporaryFile` visibility while its context is open
- 🧹 Confirms paths are gone after their context managers exit
- 🧪 Includes unit tests for the lifecycle report
- 🛡️ Creates only temporary demo data and never touches user-selected files

## 🧪 Demo

Run `python main.py`. The CLI prints the existence state inside and after each context. Use `--json` for structured output. No hosted demo is published.

## 🚀 Quick Start

```bash
python main.py
python main.py --json
python -m unittest discover -s tests
```
Requires Python 3.10 or newer. Uses only the standard library.

## 🧰 Tech Stack

- **Stack:** Python 3.10+ (tempfile, pathlib, argparse, json, unittest)
- **Approach:** small, local-first tooling with clear output

## 🗂️ Folder Structure

```text
python-tempfile-lifecycle-lab/
├── assets/mark.svg
├── tests/test_main.py
├── main.py
├── pyproject.toml
├── .gitignore
├── LICENSE
└── README.md
```

## 🛣️ Roadmap

- Add a separate example for securely creating a temporary file descriptor
- Document platform differences in named-file reopening behavior

## 🤝 Contributing

Issues and focused pull requests are welcome. Explain the use case, keep changes small, and add tests for behavior changes. Run the project using the Quick Start instructions before submitting.

## 📄 License

Released under the [MIT License](LICENSE).

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f766e,100:0f172a&height=120&section=footer&animation=twinkling" alt="Animated wave footer"/></p>
