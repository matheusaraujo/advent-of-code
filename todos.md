- create init target on make file

  - must create scaffold
  - must download init data
  - must define env vars, if no-env-vars is undefined

- create load puzzle define on makefile

  - must check command line arguments
  - must check env vars

- create detect run mode define on makefile

  - must check command line arguments
  - must read json file
  - must define mode based on cli args or json file

- create finish target on make file

  - must unset env vars

- create update_puzzle.py

  - must check local .json file
  - must call aoc data
  - must update local .json file if needed

- create update_tests.py

  - create `show` operation
  - create `create` operation
  - create `delete` operation
  - create `inactivate` operation
  - create `activate` operation
