# FINAL-PROJECT 
# COMP 340 Project 4 - Baby Programming Language

This project is a small interpreter for a simple arithmetic language. It was built for COMP 340: Organization of Programming Languages.

The program can read and evaluate basic math expressions using:

- Numbers
- Addition: `+`
- Subtraction: `-`
- Multiplication: `*`
- Division: `/`
- Parentheses: `( )`
- Negative numbers like `-5`, `--5`, and `-(-5)`

## Files

### lexer.py
Breaks the input string into tokens.

Example:

```text
1 * (2 + 5)
