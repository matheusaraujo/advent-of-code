define read-json
	$(eval ARGS := \
		"title=$(shell jq -r '.title' $(1))" \
		"year=$(shell jq -r '.year' $(1))" \
		"day=$(shell jq -r '.day' $(1))" \
		"part1_solved=$(shell jq -r '.part1.solved' $(1))" \
		"part1_outputfile=$(shell jq -r '.part1.outputFile' $(1))" \
		"inputfile=$(shell jq -r '.inputFile' $(1))"
	)
endef