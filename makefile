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
	echo "# $$EXERCISE_NAME" > "$$EXERCISE_NAME/readme.md"; \
	cp solution_test_template.py "$$EXERCISE_NAME/solution_test.py"; \
	cp solution_template.py "$$EXERCISE_NAME/solution.py"

# Prevent Make from trying to execute the exercise name as a target
%:
	@:

.PHONY: exercise