.PHONY: build run clean remove

# Build Docker image
build:
	docker build -t streamlit-classifier .

# Run Docker container in detached mode
run:
	docker run -d -p 8501:8501 --name streamlit-app streamlit-classifier

# Clean up generated files
clean:
	rm -rf .venv __pycache__ *.pyc .pytest_cache

# Remove Docker container and image
remove:
	docker stop streamlit-app || true
	docker rm streamlit-app || true
	docker rmi streamlit-classifier || true