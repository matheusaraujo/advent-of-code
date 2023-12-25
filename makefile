GREEN:=\033[0;32m
NC:=\033[0m
RED:=\033[0;31m

YEARS:=$(shell seq -w 2015 2035)
DAYS:=$(shell seq -w 1 25)

COMMIG_MSG_SCRIPT:=.githooks/commit-msg.sh
GIT_HOOKS_DIR:=.git/hooks
COMMIT_MSG_HOOK_NAME:=commit-msg

default: help

###
### help
###

.PHONY: help
help: # Show help for each of the Makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

###
### configure-hooks
###

.PHONY: configure-hooks
configure-hooks: # Configure git hooks
	@echo "Installing Git hooks..."
	@if [ ! -f "$(COMMIG_MSG_SCRIPT)" ]; then \
		echo "Error: Pre-commit script not found."; \
		exit 1; \
	fi
	@cp $(COMMIG_MSG_SCRIPT) $(GIT_HOOKS_DIR)/$(COMMIT_MSG_HOOK_NAME)
	@chmod +x $(GIT_HOOKS_DIR)/$(COMMIT_MSG_HOOK_NAME)
	@echo "$(GREEN)Git hooks installed successfully.$(NC)"
	@[ ! -f ".session.cookie" ] && touch "session.cookie"

###
### install
###

.PHONY: install
install: # Install common dependencies
	@pip install -r requirements.txt

###
### create
###

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
	@cp 1988/day00/* $(year)/day$(day)
	@sed -i .bak 's/1988/${year}/g' $(year)/day$(day)/test_part1.py
	@sed -i .bak 's/00/${day}/g' $(year)/day$(day)/test_part1.py
	@sed -i .bak 's/1988/${year}/g' $(year)/day$(day)/test_part2.py
	@sed -i .bak 's/00/${day}/g' $(year)/day$(day)/test_part2.py
	@rm $(year)/day$(day)/*.py.bak
	@python3 utils/get_puzzle_input.py $(year) $(day)
	@echo "$(year)/day$(day) created! good coding!"
endif

###
### test
###

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

###
### test-pypy
###

.PHONY: test-pypy
test-pypy: # Execute the solution tests for given [year] and [day] using pypy
ifndef year
	@echo "[year] must be defined"
else ifndef day
	@echo "[day] must be defined"
else ifeq ("$(wildcard $(year)/day$(day))", "")
	@echo "directory does not exist"
else
	@pypy3 -m pytest -v $(year)/day$(day) -s
endif

###
### test-watch
###

.PHONY: test-watch
test-watch: # Execute the solution tests for given [year] and [day] in a watch mode
ifndef year
	@echo "[year] must be defined"
else ifndef day
	@echo "[day] must be defined"
else ifeq ("$(wildcard $(year)/day$(day))", "")
	@echo "directory does not exist"
else
	@ptw $(year)/day$(day)
endif

###
### lint
###

.PHONY: lint
lint: # Analysis code using pylint for given [year] and [day]
ifndef year
	@echo "[year] must be defined"
else ifndef day
	@echo "[day] must be defined"
else ifeq ("$(wildcard $(year)/day$(day))", "")
	@echo "directory does not exist"
else
	@pylint --init-hook="import sys; sys.path.append('utils')" $(year)/day$(day)/*.py
endif

###
### validate
###

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

.PHONY: readme
readme: # Create the readme file for a solved puzzle for given [year] and [day]
ifndef year
	@echo "[year] must be defined"
else ifndef day
	@echo "[day] must be defined"
else ifeq ("$(wildcard $(year)/day$(day))", "")
	@echo "directory does not exist"
else
	@python3 utils/get_puzzle_readme.py $(year) $(day)
endif

###
### test-all
###

.PHONY: test-all
test-all: # Execute all tests
	@for year in $(YEARS); do \
        for day in $(DAYS); do \
            if [ -d "$$year/day$$day" ]; then \
                echo "----------------------------------------------------------------------"; \
            	echo "${GREEN}Running tests for $$year day $$day ...${NC}"; \
                make test year=$$year day=$$day || { echo "${RED}Test failed for $$year day $$day${NC}"; exit 1; }; \
            fi; \
        done; \
    done

###
### lint-all
###

.PHONY: lint-all
lint-all: # Analysis the entire code
	@pylint utils/*.py
	@for year in $(YEARS); do \
        for day in $(DAYS); do \
            if [ -d "$$year/day$$day" ]; then \
                echo "----------------------------------------------------------------------"; \
                echo "${GREEN}Running lint for $$year day $$day ...${NC}"; \
                make lint year=$$year day=$$day || { echo "${RED}Lint failed for $$year day $$day${NC}"; exit 1; }; \
            fi; \
        done; \
    done

###
### format-check
###

.PHONY: format-check
format-check: # Check code formating using isort and black
	@isort --check-only . && black --check .

###
### format-fix
###

.PHONY: format-fix
format-fix: # Format code using isort and black
	@isort . && black . -l 88