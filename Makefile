GREEN:=\033[0;32m
NC:=\033[0m
RED:=\033[0;31m

YEARS:=$(shell seq -w 2015 2035)
DAYS:=$(shell seq -w 1 25)

COMMIG_MSG_SCRIPT:=.githooks/commit-msg.sh
GIT_HOOKS_DIR:=.git/hooks
COMMIT_MSG_HOOK_NAME:=commit-msg

###
### help
###

default: help
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
	@cp -r 1988/day00/part1.pl $(year)/day$(day)
	@cp -r 1988/day00/part2.pl $(year)/day$(day)
	@curl -b session=$(shell cat session.cookie) https://adventofcode.com/$(year)/day/$(shell echo $(day) | sed 's/^0*//')/input -o $(year)/day$(day)/input.txt
	@echo "$(year)/day$(day) created! good coding!"
endif

###
### run
###

.PHONY: run
run: # Execute the solution for given [year] and [day]
ifndef year
	@echo "[year] must be defined"
else ifndef day
	@echo "[day] must be defined"
else ifeq ("$(wildcard $(year)/day$(day))", "")
	@echo "directory does not exists"
else
	@./main.pl $(year) $(day) $(input) $(test)
endif

###
### run-all
###

.PHONY: run-all
run-all: # Execute all solutions
	@for year in $(YEARS); do \
        for day in $(DAYS); do \
            if [ -d "$$year/day$$day" ]; then \
                echo "----------------------------------------------------------------------"; \
            	echo "${GREEN}Running $$year day $$day ...${NC}"; \
                make run year=$$year day=$$day || { echo "${RED}Test failed for $$year day $$day${NC}"; exit 1; }; \
            fi; \
        done; \
    done

###
### tidy
###

.PHONY: tidy
tidy: # Run perltidy on the solution for given [year] and [day]
ifndef year
	@echo "[year] must be defined"
else ifndef day
	@echo "[day] must be defined"
else ifeq ("$(wildcard $(year)/day$(day))", "")
	@echo "directory does not exists"
else
	@perltidy -b $(year)/day$(day)/part1.pl
	@perltidy -b $(year)/day$(day)/part2.pl
endif

###
### critic
###

.PHONY: critic
critic: # Run perlcritic on the solution for given [year] and [day]
ifndef year
	@echo "[year] must be defined"
else ifndef day
	@echo "[day] must be defined"
else ifeq ("$(wildcard $(year)/day$(day))", "")
	@echo "directory does not exists"
else
	@perlcritic $(year)/day$(day)/
endif

###
### critic-all
###

.PHONY: critic-all
critic-all: # Run perlcritic for all solutions
	@for year in $(YEARS); do \
        for day in $(DAYS); do \
            if [ -d "$$year/day$$day" ]; then \
                echo "----------------------------------------------------------------------"; \
            	echo "${GREEN}Running $$year day $$day ...${NC}"; \
                make critic year=$$year day=$$day || { echo "${RED}Test failed for $$year day $$day${NC}"; exit 1; }; \
            fi; \
        done; \
    done

