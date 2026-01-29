FROM python:3.12-slim

WORKDIR /app

# Install uv
RUN pip install uv

# Copy project files
COPY pyproject.toml .
COPY *.py .

# Install dependencies
RUN uv sync

# Expose Streamlit port
EXPOSE 8501

# Run the app
CMD ["uv", "run", "streamlit", "run", "app.py", "--server.address", "0.0.0.0"]