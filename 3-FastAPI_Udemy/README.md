# 🚀 3 FastAPI Udemy Course

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white) ![Stars](https://img.shields.io/github/stars/PatriciaZan/Python?style=for-the-badge)

This repository contains 5 mini projects for study of FastAPI and testing.

_Key dependencies: `fastapi`, `pydantic`, `starlette`_

## 🧠 What I Learned

- **Python** — Core concepts + FastAPI + Testing and more
- **HTML5** — Impementing a simple HTML to python APIs
- **JavaScript** — For forms submissions to the backend
- **CSS3** — Styling using bootstrap

## 🏗️ Architecture Decisions

```text
Python/
├── src/
    ├── 01_Project_books
    ├── 02_Project_books_2
    ├── 03_Project_TodoApp
    ├── 04_Project_Pytest
    ├── 05_Project_Final_TodoApp
```

- **Why this structure?** Keeps concerns separated and easy to navigate.
- **Trade-offs:** Simplicity was prioritized over premature abstraction.

### Installation

```bash
    git clone https://github.com/PatriciaZan/Python.git
    cd Python
    python -m venv .venv && source .venv/bin/activate
    pip install -r requirements.txt
```

## Run

To run each project you must be in the correct folder and run the following command:

```bash
    uvicorn main:app --reload

```

To run the tests you must in the correct folder and run the following command:

```bash
    pytest

```
