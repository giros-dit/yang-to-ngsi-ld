import sys
import os
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import unittest

from ngsi_ld_models.models.interface import Interface
from ngsi_ld_models.models.statistics import Statistics

class Interfaces(unittest.TestCase):
    def test_interface(self):
        self.assertIsInstance(
            Interface.parse_file(
                "examples/ietf-interfaces/interface/example-normalized.json"),
            Interface)
    def test_statistics(self):
        self.assertIsInstance(
            Statistics.parse_file(
                "examples/ietf-interfaces/statistics/example-normalized.json"),
            Statistics)

if __name__ == '__main__':
    unittest.main()