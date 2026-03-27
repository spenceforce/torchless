# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

**Torchless** is an educational project teaching neural networks from scratch. It combines a Quarto book (with Jupyter notebook chapters) and a Python package (`torchless/`) that is the code companion to the book.

## Commands

**Package management** (uses `uv`):
```bash
uv sync              # Install dependencies
uv run python        # Run Python with the package available
```

**Install package in editable mode**:
```bash
uv run pip install -e .
```

There are currently no tests or linting configuration.

## Scope

Work is limited to the `torchless/` Python package only. Do not modify Quarto configuration, book chapters, or any `.qmd`/`.ipynb` files.

## Docstring Task

Claude's job in this repo is to improve documentation of the `torchless` package by:
1. Adding module-level docstrings to each `.py` file
2. Adding class docstrings explaining purpose, attributes, and design intent
3. Adding function/method docstrings with Args and Returns
4. Adding inline comments where logic is non-obvious

Docstrings should be written for a learner audience — someone working through the book who wants to understand how the code connects to neural network concepts.
