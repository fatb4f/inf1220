from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from ctrlr.contracts import Lens, Phase, Pillar, Span, Step
from ctrlr.mermaid import to_mermaid_calltree, to_mermaid_flow


def test_mermaid_flow_basic():
    steps = [Step(step_id="s-1", name="start"), Step(step_id="s-2", name="end")]
    output = to_mermaid_flow(steps)
    assert output.startswith("flowchart")
    assert "start" in output
    assert "end" in output
    assert "-->" in output


def test_mermaid_calltree_basic():
    lens = Lens(lens_id="lens-1", pillar=Pillar.P1, phase=Phase.GEN)
    spans = [
        Span(span_id="root", name="root", lens=lens),
        Span(span_id="child", name="child", lens=lens, parent_span_id="root"),
    ]
    output = to_mermaid_calltree(spans)
    assert output.startswith("flowchart")
    assert "root" in output
    assert "child" in output
    assert "-->" in output
