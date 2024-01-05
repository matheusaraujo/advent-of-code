KOTLINX_SERIALIZATION_CORE_VERSION := 1.6.2
KOTLINX_SERIALIZATION_JSON_VERSION := 1.6.2

define run-kotlin
	@if [ ! -f aoc/kotlin/kotlinx.serialization.jar ]; then \
		curl -o aoc/kotlin/kotlinx.serialization.jar \
			https://repo1.maven.org/maven2/org/jetbrains/kotlinx/kotlinx-serialization-core/$(KOTLINX_SERIALIZATION_CORE_VERSION)/kotlinx-serialization-core-$(KOTLINX_SERIALIZATION_CORE_VERSION).jar; \
	fi
	@if [ ! -f aoc/kotlin/kotlinx.serialization.json.jar ]; then \
		curl -o aoc/kotlin/kotlinx.serialization.json.jar \
			https://repo1.maven.org/maven2/org/jetbrains/kotlinx/kotlinx-serialization-json/$(KOTLINX_SERIALIZATION_JSON_VERSION)/kotlinx-serialization-json-$(KOTLINX_SERIALIZATION_JSON_VERSION).jar; \
	fi

	@kotlinc -include-runtime -verbose \
		-classpath aoc/kotlin/kotlinx.serialization.jar:aoc/kotlin/kotlinx.serialization.json.jar \
		-d aoc/kotlin/Run.jar aoc/kotlin/Run.kt
	@kotlin -classpath aoc/kotlin/Run.jar RunKt $(1) $(2)
endef

