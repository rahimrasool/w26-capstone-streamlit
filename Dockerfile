FROM python:3.12-slim

WORKDIR /app

# Install uv
RUN pip install uv

# Copy project files
COPY pyproject.toml .
COPY *.py .

# Install CPU-only PyTorch first, then other dependencies
RUN uv pip install --system torch torchvision --index-url https://download.pytorch.org/whl/cpu
RUN uv pip install --system streamlit pillow

# Expose Streamlit port
EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port", "8501", "--server.address", "0.0.0.0"]
