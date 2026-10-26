"""Smoke test: the empty package skeleton must be importable."""

import importlib


def test_package_imports() -> None:
    pkg = importlib.import_module("tamba_evals")
    assert pkg.__version__


def test_registry_imports() -> None:
    importlib.import_module("tamba_evals._registry")
