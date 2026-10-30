"""Regression tests for APIs removed from modern NumPy releases."""
import unittest

import numpy as np

from dribble import Lattice, Percolator
from dribble.nblist import NeighborList


class NumPyCompatibilityTests(unittest.TestCase):
    def setUp(self):
        self.vectors = np.array([[0, .5, .5], [.5, 0, .5], [.5, .5, 0]]) * 5

    def test_periodic_neighbors(self):
        neighbors = NeighborList([[0, 0, 0]], lattice_vectors=self.vectors)
        sites, distances, translations = neighbors.get_nearest_neighbors(0)
        self.assertEqual(len(sites), 12)
        np.testing.assert_allclose(distances, 5 / np.sqrt(2))
        self.assertEqual(len(translations), 12)

    def test_lattice_neighbors(self):
        lattice = Lattice(self.vectors, [[0, 0, 0]], supercell=(3, 3, 3))
        self.assertEqual(lattice.num_sites, 27)
        self.assertTrue(all(len(n) == 12 for n in lattice.nn))

    def test_nonwrapping_tortuosity(self):
        # Isolate the infinity API from simulation initialization.
        percolator = Percolator.__new__(Percolator)
        percolator.wrapping = [np.zeros(3, dtype=int)]
        for calculate in (percolator.get_tortuosity, percolator.get_tortuosity_slow):
            self.assertEqual(calculate(0), (np.inf, np.inf, 0.0))


if __name__ == '__main__':
    unittest.main()
