"""Tests for example_python_research_package."""

import pytest


def test_import():
    """Test that the package can be imported."""
    import example_python_research_package
    
    assert hasattr(example_python_research_package, "__version__")
