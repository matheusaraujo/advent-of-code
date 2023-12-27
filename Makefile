include make/c.mk
include make/cpp.mk
include make/csharp.mk
include make/go.mk
include make/java.mk
include make/js.mk
include make/python.mk

prepare:
	$(call install-dependencies-python)

load-puzzle: check_year_and_day
	@python3 aoc/py/load_puzzle.py ${year} ${day}

lint: check_year_and_day
ifneq ($(wildcard ${year}/day${day}/part1.py),)
ifndef fix
	$(call lint-python)
else
	$(call lint-python-fix)
endif
endif

run: check_year_and_day
ifeq ("$(wildcard ${year}/day${day})", "")
	@echo "directory does not exist"
	@exit 1
endif
ifneq ($(wildcard ${year}/day${day}/part1.c),)
	$(call run-c)
endif
ifneq ($(wildcard ${year}/day${day}/part1.cpp),)
	$(call run-cpp)
endif
ifneq ($(wildcard ${year}/day${day}/Part1.cs),)
	$(call run-csharp)
endif
ifneq ($(wildcard ${year}/day${day}/part1.go),)
	$(call run-go)
endif
ifneq ($(wildcard ${year}/day${day}/Part1.java),)
	$(call run-java)
endif
ifneq ($(wildcard ${year}/day${day}/part1.js),)
	$(call run-js)
endif
ifneq ($(wildcard ${year}/day${day}/part1.py),)
	$(call run-python)
endif


check_year_and_day:
ifndef year
	@echo "[year] must be defined"
	@exit 1
else ifndef day
	@echo "[day] must be defined"
	@exit 1
endif