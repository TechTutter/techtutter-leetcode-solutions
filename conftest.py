"""Pytest configuration to add test directories to Python path.

This allows importing solution.py from test files without modifying sys.path
in each test file.
"""
import sys
from pathlib import Path


def pytest_collect_file(file_path, parent):
    """Add test file's directory to sys.path when collecting."""
    if file_path.suffix == ".py" and ("test" in file_path.stem.lower()):
        test_dir = file_path.parent.resolve()
        test_dir_str = str(test_dir)
        
        # Remove solution from cache to avoid conflicts between different directories
        if "solution" in sys.modules:
            del sys.modules["solution"]
        
        # Add test directory to path if not already there
        if test_dir_str not in sys.path:
            sys.path.insert(0, test_dir_str)


def pytest_runtest_setup(item):
    """Ensure test's directory is first in path before running."""
    test_dir = Path(item.fspath).parent.resolve()
    test_dir_str = str(test_dir)
    
    # Remove solution from cache to force reimport from correct directory
    if "solution" in sys.modules:
        del sys.modules["solution"]
    
    # Move test directory to front of path
    if test_dir_str in sys.path:
        sys.path.remove(test_dir_str)
    sys.path.insert(0, test_dir_str)

