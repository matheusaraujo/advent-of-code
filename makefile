default: help

.PHONY: help
help: # Show help for each of the Makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

.PHONY: create
create: # Create a new solution for given [year] and [day]
ifndef year
	@echo "[year] must be defined"
else ifndef day
	@echo "[day] must be defined"
else ifneq ("$(wildcard src/$(year)/day$(day))", "")
	@echo "directory already exists"
else
	@mkdir src/$(year)/day$(day)
	@cp src/0000/day00/* src/$(year)/day$(day)
	@sed -i .bak 's/0000/${year}/g' src/$(year)/day$(day)/test_part1.py
	@sed -i .bak 's/00/${day}/g' src/$(year)/day$(day)/test_part1.py
	@sed -i .bak 's/0000/${year}/g' src/$(year)/day$(day)/test_part2.py
	@sed -i .bak 's/00/${day}/g' src/$(year)/day$(day)/test_part2.py
	@rm src/$(year)/day$(day)/*.py.bak
	@echo "$(year)/day$(day) created! good coding!"
endif

.PHONY: test
test: # Execute the solution tests for given [year] and [day]
ifndef year
	@echo "[year] must be defined"
else ifndef day
	@echo "[day] must be defined"
else ifeq ("$(wildcard src/$(year)/day$(day))", "")
	@echo "directory does not exist"
else
	@cd src && pytest --no-header -v $(year)/day$(day)
endif

.PHONY: install
install: # Install all dependencies
	@cd src && pip install -r requirements.txt -r requirements_dev.txt

.PHONY: lint
lint: # Check code using isort and black
	@cd src && isort --check-only . && black --check .

.PHONY: lintfix
lintfix: # Fix code using isort and black
	@cd src && isort . && black . -l 88