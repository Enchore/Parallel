"""五幕状态机的行为测试。

state_machine.py 只用标准库（enum / typing / dataclasses），
不依赖 FastAPI、Redis 或 OpenAI SDK，因此可以在纯 pytest 环境里跑。
需要真实网络/API 的智能体部分不纳入 CI。
"""
import pytest

from services.state_machine import ActType, StoryStateMachine


@pytest.fixture
def machine():
    return StoryStateMachine()


def test_starts_at_first_act(machine):
    assert machine.current_act is ActType.ACT_1_INTRODUCTION
    assert machine.current_act_name == "第一章：覺醒"


def test_progress_starts_empty(machine):
    progress = machine.get_progress()

    assert progress["current_act"] == 1
    assert progress["total_actions"] == 0
    assert progress["progress"] == 0.0
    assert progress["is_final_act"] is False


def test_record_action_accumulates_and_enables_advance(machine):
    assert machine.can_advance() is False
    assert machine.advance() is None

    for _ in range(5):
        machine.record_action("talk")

    assert machine.can_advance() is True
    assert machine.advance() is ActType.ACT_2_RISING
    assert machine.current_act_name == "第二章：探索"


def test_actions_are_counted_per_type(machine):
    machine.record_action("talk")
    machine.record_action("talk")
    machine.record_action("explore")

    progress = machine.get_progress()

    assert progress["total_actions"] == 3
    assert progress["progress"] == pytest.approx(3 / 5)


def test_can_walk_through_all_five_acts(machine):
    # 各幕的 required_actions 是按累计行为数判定的，
    # 所以第三幕（需 3 次）在累计达到 10 次后必定满足。
    for act in range(5):
        machine.record_action("any")

    seen = [machine.current_act]
    while True:
        for _ in range(10):
            machine.record_action("any")
        nxt = machine.advance()
        if nxt is None:
            break
        seen.append(nxt)

    assert seen == list(ActType)
    assert machine.get_progress()["is_final_act"] is True


def test_final_act_has_no_further_transition(machine):
    machine._current_act = ActType.ACT_5_RESOLUTION

    for _ in range(100):
        machine.record_action("any")

    assert machine.can_advance() is False
    assert machine.advance() is None
