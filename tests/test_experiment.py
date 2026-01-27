from __future__ import annotations

import random
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from ctrlr.control import CtrlrError
from ctrlr.experiment import budget, seeded


def test_budget_consume_and_remaining():
    b = budget(2, label="demo")
    assert b.remaining == 2
    b.consume()
    assert b.used == 1
    assert b.remaining == 1


def test_budget_exceeded_raises():
    b = budget(1)
    b.consume()
    with pytest.raises(CtrlrError):
        b.consume()


def test_seeded_restores_state():
    state_before = random.getstate()
    with seeded(123):
        first = random.random()
        second = random.random()
    assert random.getstate() == state_before
    with seeded(123):
        assert random.random() == first
        assert random.random() == second
