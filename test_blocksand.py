# test_blocksand.py
"""
Tests for BlockSand module.
"""

import unittest
from blocksand import BlockSand

class TestBlockSand(unittest.TestCase):
    """Test cases for BlockSand class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockSand()
        self.assertIsInstance(instance, BlockSand)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockSand()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
