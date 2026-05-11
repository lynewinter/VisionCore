# test_visioncore.py
"""
Tests for VisionCore module.
"""

import unittest
from visioncore import VisionCore

class TestVisionCore(unittest.TestCase):
    """Test cases for VisionCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = VisionCore()
        self.assertIsInstance(instance, VisionCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = VisionCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
