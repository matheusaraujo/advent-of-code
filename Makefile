include make/c.mk
include make/cpp.mk
include make/csharp.mk
include make/go.mk
include make/java.mk
include make/js.mk
include make/python.mk

prepare:
	@cd aoc && pip install -r requirements.txt

load-puzzle: check_year_and_day
	@python3 aoc/py/load_puzzle.py $(year) $(day)

prepare-py:
	@pip install -r aoc/py/requirements.txt

prepare-csharp:
	@dotnet restore aoc/csharp/run.csproj

run: check_year_and_day
ifndef lang
	@echo "[lang] must be defined"
	@exit 1
else ifeq ("$(wildcard $(year)/day$(day))", "")
	@echo "directory does not exist"
	@exit 1
else ifeq ($(lang), c)
	$(call run-c)
else ifeq ($(lang), cpp)
	$(call run-cpp)
else ifeq ($(lang), csharp)
	$(call run-csharp)
else ifeq ($(lang), go)
	$(call run-go)
else ifeq ($(lang), java)
	$(call run-java)
else ifeq ($(lang), js)
	$(call run-js)
else ifeq ($(lang), python)
	$(call run-python)
else
	@echo "invalid value for [lang]"
	@echo "supported: c|cpp|csharp|go|java|js|python"
endif


check_year_and_day:
ifndef year
	@echo "[year] must be defined"
	@exit 1
else ifndef day
	@echo "[day] must be defined"
	@exit 1
endif