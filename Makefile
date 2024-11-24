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
	@lib/perl/create.sh $(year) $(day)
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
	@lib/run.sh $(year) $(day) $(part) $(test)
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
### lint
###

.PHONY: lint
lint: # Run perltidy on the solution for given [year] and [day]
ifndef year
	@echo "[year] must be defined"
else ifndef day
	@echo "[day] must be defined"
else ifeq ("$(wildcard $(year)/day$(day))", "")
	@echo "directory does not exists"
else
	@lib/perl/lint.sh $(year) $(day)
endif

###
### analysis
###

.PHONY: analysis
analysis: # Run perlcritic on the solution for given [year] and [day]
ifndef year
	@echo "[year] must be defined"
else ifndef day
	@echo "[day] must be defined"
else ifeq ("$(wildcard $(year)/day$(day))", "")
	@echo "directory does not exists"
else
	@lib/perl/analysis.sh $(year) $(day)
endif

###
### analysis-all
###

.PHONY: analysis-all
analysis-all: # Run perlcritic for all solutions
	@for year in $(YEARS); do \
        for day in $(DAYS); do \
            if [ -d "$$year/day$$day" ]; then \
                echo "----------------------------------------------------------------------"; \
            	echo "${GREEN}Running $$year day $$day ...${NC}"; \
                make analysis year=$$year day=$$day || { echo "${RED}Test failed for $$year day $$day${NC}"; exit 1; }; \
            fi; \
        done; \
    done

