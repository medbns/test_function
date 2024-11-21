# test/test_sample.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.sample import func

def test_answer():
    assert func(3) == 5