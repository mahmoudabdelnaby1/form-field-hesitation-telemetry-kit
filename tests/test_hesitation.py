import unittest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from aggregate_hesitation import aggregate_hesitation

class TestHesitation(unittest.TestCase):
    def test_agg(self):
        e = Path(__file__).resolve().parent.parent / "examples" / "sample_form_events.json"
        out = Path(__file__).resolve().parent.parent / "reports" / "hesitation_heatmap.html"
        res = aggregate_hesitation(str(e), str(out))
        self.assertGreater(len(res), 0)

if __name__ == "__main__":
    unittest.main()
