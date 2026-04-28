# Git & GitHub Practice Lab

This repository is not a production project.  
It is a **hands-on learning space** where I explored Git and GitHub workflows — from basic commands to advanced, production-level concepts used in SaaS environments.

---

## 📚 What This Repo Covers

### 🔹 Basics
- `git init`
- `git clone`
- `git add`
- `git commit`
- `git status`
- `git log`
- `.gitignore`

### 🔹 Branching & Merging
- `git branch`
- `git checkout`
- `git switch`
- `git merge`
- Merge conflicts & resolution

### 🔹 Remote Repositories
- `git remote add origin`
- `git push`
- `git pull`
- `git fetch`

---

## ⚙️ Intermediate Concepts

- Rewriting history with:
  - `git commit --amend`
  - `git rebase`
- Stashing changes:
  - `git stash`
- Viewing differences:
  - `git diff`
- Cleaning up:
  - `git reset`
  - `git restore`

---

## 🏗️ Advanced / Production-Level Concepts

### ✅ Conventional Commits
Structured commit messages for better collaboration and automation.

**Examples:**
```bash

feat: add user authentication
fix: resolve login bug
chore: update dependencies
docs: update README

```

---

### 🔖 Versioning & Tags
Used to mark release points in history.

```bash
git tag v1.0.0
git push origin v1.0.0
````

---

### 🍒 Cherry-Picking

Applying specific commits across branches.

```bash
git cherry-pick <commit-hash>
```

---

### 🔄 GitHub Actions (CI/CD Basics)

* Automating workflows
* Running tests on push
* Build pipelines

Example:

```yaml
name: CI

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3
      - name: Run a script
        run: echo "Hello, GitHub Actions!"
```

---

## 🧠 Why This Repo Exists

Instead of just reading documentation, I used this repository to:

* Experiment with real Git workflows
* Simulate team collaboration scenarios
* Practice production-ready version control strategies
* Understand how Git fits into SaaS development pipelines

---

## 📌 Key Learnings

* Clean commit history matters
* Branching strategy is crucial for teams
* Automation (CI/CD) saves time and reduces errors
* Git is not just a tool — it's a **core part of software delivery**

---

## ⚠️ Disclaimer

This repository is purely for **learning and experimentation**.
It may contain:

* Trial commits
* Rewritten history
* Non-linear workflows

---

## 🛠️ Future Improvements

* Add branching strategy examples (Git Flow, Trunk-Based)
* Add real CI/CD pipelines
* Simulate pull request reviews
* Add release notes automation

---

## 📎 References

* Official Git Documentation: [https://git-scm.com/docs](https://git-scm.com/docs)
* Conventional Commits: [https://www.conventionalcommits.org/](https://www.conventionalcommits.org/)
* GitHub Actions Docs: [https://docs.github.com/en/actions](https://docs.github.com/en/actions)

---

## 👨‍💻 Auth: Tharvesh Muhaideen

Maintained as part of my continuous learning journey in Git, DevOps, and SaaS development.

---

If you want, I can also:
- Make it **more minimal (for recruiters)**
- Or turn it into a **“portfolio-style” README** that actually impresses hiring managers instead of looking like practice notes

