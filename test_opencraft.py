# test_opencraft.py
"""
Tests for OpenCraft module.
"""

import unittest
from opencraft import OpenCraft

class TestOpenCraft(unittest.TestCase):
    """Test cases for OpenCraft class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OpenCraft()
        self.assertIsInstance(instance, OpenCraft)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OpenCraft()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
