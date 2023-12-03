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
	@mkdir $(year)/day$(day)
	@cp day00/* $(year)/day$(day)
	@echo "$(year)/day$(day) created! good luck!"
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
	@cd $(year)/day$(day) && python3 -m unittest tests.py
endif


