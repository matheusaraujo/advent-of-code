import globals from "globals";
import pluginJs from "@eslint/js";
import js from "@eslint/js";
import eslintPluginPrettier from "eslint-plugin-prettier";

/** @type {import('eslint').Linter.Config[]} */
export default [
  js.configs.recommended,
  // JavaScript files config
  {
    files: ["**/*.js"],
    languageOptions: {
      sourceType: "commonjs",
      globals: globals.node, // Node globals
    },
    rules: {
      // Add any additional rules you want here
      "prettier/prettier": "error",
    },
    plugins: { preetier: eslintPluginPrettier },
  },
  
  // PluginJs recommended config directly
  pluginJs.configs.recommended,
];
