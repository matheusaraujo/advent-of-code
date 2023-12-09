YEARS:=$(shell seq -w 2015 2035)
DAYS:=$(shell seq -w 1 25)
GREEN=\033[0;32m
NC=\033[0m
RED=\033[0;31m

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
else ifneq ("$(wildcard $(year)/day$(day))", "")
	@echo "directory already exists"
else
	@mkdir -p $(year)/day$(day)
	@cp 0000/day00/* $(year)/day$(day)
	@sed -i .bak 's/0000/${year}/g' $(year)/day$(day)/test_part1.py
	@sed -i .bak 's/00/${day}/g' $(year)/day$(day)/test_part1.py
	@sed -i .bak 's/0000/${year}/g' $(year)/day$(day)/test_part2.py
	@sed -i .bak 's/00/${day}/g' $(year)/day$(day)/test_part2.py
	@rm $(year)/day$(day)/*.py.bak
	@echo "$(year)/day$(day) created! good coding!"
endif

.PHONY: test
test: # Execute the solution tests for given [year] and [day]
ifndef year
	@echo "[year] must be defined"
else ifndef day
	@echo "[day] must be defined"
else ifeq ("$(wildcard $(year)/day$(day))", "")
	@echo "directory does not exist"
else
	@pytest -v $(year)/day$(day) -s
endif

.PHONY: test-all
test-all: # Execute all tests
	@for year in $(YEARS); do \
        for day in $(DAYS); do \
            if [ -d "$$year/day$$day" ]; then \
                echo "----------------------------------------------------------------------"; \
            	echo "${GREEN}Running tests for $$year day $$day ...{NC}"; \
                make test year=$$year day=$$day || { echo "${RED}Test failed for $$year day $$day${NC}"; exit 1; }; \
            fi; \
        done; \
    done

.PHONY: install
install: # Install all dependencies
	@pip install -r requirements.txt -r requirements_dev.txt

.PHONY: format-check
format-check: # Check code formating using isort and black
	@isort --check-only . && black --check .

.PHONY: format-fix
format-fix: # Format code using isort and black
	@isort . && black . -l 88

.PHONY: lint
lint: # Analysis code using pylint for given year and day
ifndef year
	@echo "[year] must be defined"
else ifndef day
	@echo "[day] must be defined"
else ifeq ("$(wildcard $(year)/day$(day))", "")
	@echo "directory does not exist"
else
	@pylint --init-hook="import sys; sys.path.append('utils')" $(year)/day$(day)/*.py
endif

.PHONY: lint-all
lint-all: # Analysis the entire code
	@for year in $(YEARS); do \
        for day in $(DAYS); do \
            if [ -d "$$year/day$$day" ]; then \
                echo "----------------------------------------------------------------------"; \
                echo "${GREEN}Running lint for $$year day $$day ...${NC}"; \
                make lint year=$$year day=$$day || { echo "${RED}Lint failed for $$year day $$day${NC}"; exit 1; }; \
            fi; \
        done; \
    done

.PHONY: validate
validate: # Runs tests, format and lint for a given year and day
ifndef year
	@echo "[year] must be defined"
else ifndef day
	@echo "[day] must be defined"
else ifeq ("$(wildcard $(year)/day$(day))", "")
	@echo "directory does not exist"
else
	@isort $(year)/day$(day) && black -l 88 $(year)/day$(day)
	@pylint --init-hook="import sys; sys.path.append('utils')" $(year)/day$(day)/*.py
	@pytest -v $(year)/day$(day) -s
endif