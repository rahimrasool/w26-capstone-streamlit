# Packaging with uv

This guide explains how to package and manage this project using `uv`, a fast Python package manager.

## Prerequisites

Install uv if you haven't already:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Initial Setup

### 1. Initialize the Project

If the project doesn't have a `pyproject.toml` file yet, initialize it:
```bash
uv init
```

This creates a basic `pyproject.toml` file with project metadata.

### 2. Add Dependencies

Add the required dependencies for this project:
```bash
uv add streamlit
uv add torch
uv add torchvision
uv add pillow
```

These packages are required for:
- `streamlit` - Web application framework for the UI
- `torch` - PyTorch for deep learning inference
- `torchvision` - Pretrained MobileNetV2 model and image transforms
- `pillow` - Image loading and processing

### 3. Add Development Dependencies (Optional)

For development tools like linters or formatters:
```bash
uv add --dev pytest
uv add --dev black
uv add --dev ruff
```

## Syncing Dependencies

After adding dependencies or when setting up the project on a new machine:

```bash
uv sync
```

This command:
- Reads `pyproject.toml`
- Resolves all dependencies
- Creates/updates the virtual environment
- Installs all packages

## Running Scripts

### Option 1: Using uv run (Recommended)

Run the Streamlit image classifier app:
```bash
uv run streamlit run app.py
```

Run the simple main script:
```bash
uv run python main.py
```

This automatically uses the project's virtual environment.

### Option 2: Activate Virtual Environment

Alternatively, activate the virtual environment first:
```bash
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate     # On Windows
```

Then run scripts normally:
```bash
streamlit run app.py
python main.py
```

## Project Files

| File | Description |
|------|-------------|
| `app.py` | Streamlit web app for image classification |
| `classifier.py` | ImageClassifier class using MobileNetV2 |
| `main.py` | Simple entry point script |

## Common Commands

| Command | Description |
|---------|-------------|
| `uv init` | Initialize a new project |
| `uv add <package>` | Add a dependency |
| `uv add --dev <package>` | Add a development dependency |
| `uv remove <package>` | Remove a dependency |
| `uv sync` | Sync dependencies from pyproject.toml |
| `uv run <command>` | Run a command in the project environment |
| `uv lock` | Generate/update the lock file |
| `uv pip list` | List installed packages |

## Project Structure

After initialization, your project will have:
```
streamlit-app/
├── pyproject.toml      # Project metadata and dependencies
├── uv.lock             # Locked dependency versions
├── .venv/              # Virtual environment (auto-created)
├── app.py              # Streamlit web interface
├── classifier.py       # MobileNetV2 image classifier module
└── main.py             # Simple entry point script
```

## Tips

- Always run `uv sync` after pulling changes that modify `pyproject.toml`
- Use `uv run` to ensure you're using the correct environment
- The `.venv` directory is created automatically - add it to `.gitignore`
- `uv.lock` ensures reproducible installs - commit it to version control
