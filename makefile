exercise:
	@EXERCISE_NAME=""; \
	for arg in $(filter-out exercise,$(MAKECMDGOALS)); do \
		EXERCISE_NAME="$$EXERCISE_NAME $$arg"; \
	done; \
	EXERCISE_NAME=$$(echo $$EXERCISE_NAME | sed 's/^ *//'); \
	if [ -z "$$EXERCISE_NAME" ]; then \
		echo "Error: Exercise name not specified. Use: make exercise 88. Merge Sorted Array"; \
		exit 1; \
	fi; \
	mkdir -p "$$EXERCISE_NAME"; \
	touch "$$EXERCISE_NAME/readme.md"; \
	touch "$$EXERCISE_NAME/solution.py"; \
	cp solution_test_template.py "$$EXERCISE_NAME/solution_test.py"

VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

init:
	@echo "Checking Python installation..."
	@python3 --version || (echo "Error: Python3 not found. Please install Python3." && exit 1)
	@echo "Creating virtual environment..."
	@python3 -m venv $(VENV) || (echo "Error: Failed to create virtual environment. Install python-venv with: sudo pacman -S python-venv" && exit 1)
	@echo "Installing Python dependencies..."
	@$(PIP) install --upgrade pip --quiet
	@$(PIP) install -e ".[dev]" --quiet
	@echo "Setup complete! You can now run 'make test' to run tests."

test:
	@if [ ! -d "$(VENV)" ]; then \
		echo "Virtual environment not found. Run 'make init' first."; \
		exit 1; \
	fi
	@$(PYTHON) -m pytest -v

test-watch:
	@if [ ! -d "$(VENV)" ]; then \
		echo "Virtual environment not found. Run 'make init' first."; \
		exit 1; \
	fi
	@$(PYTHON) -m pytest -v --watch

clean:
	@echo "Cleaning Python cache files..."
	@find . -type d -name "__pycache__" -exec rm -r {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@find . -type f -name "*.pyo" -delete 2>/dev/null || true
	@find . -type d -name "*.egg-info" -exec rm -r {} + 2>/dev/null || true
	@rm -rf .pytest_cache .coverage htmlcov .tox 2>/dev/null || true
	@echo "Clean complete!"

# Prevent Make from trying to execute the exercise name as a target
%:
	@:

.PHONY: init exercise test test-watch clean