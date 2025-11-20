
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
	touch "$$EXERCISE_NAME/solution.ts"; \
	cp solutionTestTemplate.ts "$$EXERCISE_NAME/solution.test.ts"

# Prevent Make from trying to execute the exercise name as a target
%:
	@:

.PHONY: exercise