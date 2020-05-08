import os
import subprocess
import sys
import unittest

# /path/to/map-coloring/
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestDemo(unittest.TestCase):
    def test_smoke(self):
        """Run map_coloring.py and check that nothing crashes"""

        demo_file = os.path.join(project_dir, 'map_coloring.py')
        subprocess.check_output([sys.executable, demo_file])
