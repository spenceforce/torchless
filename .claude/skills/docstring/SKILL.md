---
name: docstring
description: Add or improve Python docstrings and inline comments in a file or across the project. Use when asked to document a file, add docstrings, or improve code documentation.
argument-hint: "[file-path]"
disable-model-invocation: true
allowed-tools: Read, Edit, Glob, Grep
---

Add or improve Google-style docstrings and inline comments for Python files.

Style reference: [google-style-guide.md](google-style-guide.md) — covers module, class, function, and inline comment rules with examples. Consult it before writing any docstring if you are unsure of the correct format.

## Mode

**Single file** — if `$ARGUMENTS` contains a file path, document that file only.

**Whole project** — if no argument is given, use Glob to find all `.py` files, then document any missing or incomplete docstrings across the project. Process files one at a time.

## Procedure (per file)

1. **Read** the file in full before making any edits.
2. **Identify gaps** — find every module, class, public method, and function that is missing a docstring or has one that is incomplete (missing Args/Returns/Raises sections when they apply).
3. **Write docstrings** following the rules below.
4. **Add inline comments** for non-obvious logic only.

## Style choices

* Hanging indent: use two spaces
