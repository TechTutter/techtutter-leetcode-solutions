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
	TARGET_DIR="leetproblems/$$EXERCISE_NAME"; \
	mkdir -p "$$TARGET_DIR"; \
	echo "# $$EXERCISE_NAME" > "$$TARGET_DIR/README.md"; \
	cp solution_test_template.py "$$TARGET_DIR/solution_test.py"; \
	cp solution_template.py "$$TARGET_DIR/solution.py"; \
	$(MAKE) update-readme

update-readme:
	@COUNT=$$(find leetproblems -mindepth 1 -maxdepth 1 -type d | wc -l | xargs); \
	perl -i -pe "s/Total Solved: \d+ <!-- LEET_COUNT -->/Total Solved: $$COUNT <!-- LEET_COUNT -->/" README.md; \
	echo "README.md updated with $$COUNT problems solved."

# Prevent Make from trying to execute the exercise name as a target
%:
	@:

.PHONY: exercise update-readme