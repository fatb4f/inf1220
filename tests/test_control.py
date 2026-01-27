from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from ctrlr.control import CtrlrError, ensure, invariant, require


def test_control_gates_pass():
    require(True, "ok")
    ensure(True, "ok")
    invariant(True, "ok")


def test_control_gate_failure_includes_data():
    data = {"key": "value"}
    try:
        require(False, "nope", data)
    except CtrlrError as exc:
        message = str(exc)
        assert "nope" in message
        assert "key" in message
        assert "value" in message
    else:
        raise AssertionError("expected CtrlrError")
