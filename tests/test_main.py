import tempfile
import unittest
from main import run_demo

class TempfileLifecycleTests(unittest.TestCase):
    def test_context_managers_clean_up(self):
        with tempfile.TemporaryDirectory() as folder:
            report = run_demo(folder)
        self.assertTrue(report["temporary_directory"]["directory_exists_inside_context"])
        self.assertFalse(report["temporary_directory"]["directory_exists_after_context"])
        self.assertTrue(report["named_file"]["exists_inside_context"])
        self.assertFalse(report["named_file"]["exists_after_context"])
