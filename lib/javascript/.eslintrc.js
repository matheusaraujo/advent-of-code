module.exports = {
  extends: [
    "eslint:recommended",
    "plugin:prettier/recommended"
  ],
  plugins: ["prettier"],
  rules: {
    "prettier/prettier": "error",
    "no-console": "warn",
    "no-debugger": "warn"
  }
};
