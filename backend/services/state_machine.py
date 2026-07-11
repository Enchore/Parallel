"""
五幕狀態機 (Five-Act State Machine)
管理劇情的五幕推進邏輯，定義各幕之間的轉換條件和觸發機制。
"""
from enum import Enum
from typing import Dict, Optional, Callable
from dataclasses import dataclass


class ActType(Enum):
    """幕數枚舉"""
    ACT_1_INTRODUCTION = 1    # 第一幕：引入（覺醒）
    ACT_2_RISING = 2           # 第二幕：發展（探索）
    ACT_3_CLIMAX = 3           # 第三幕：高潮（抉擇）
    ACT_4_FALLING = 4          # 第四幕：下降（衝突）
    ACT_5_RESOLUTION = 5       # 第五幕：解決（結局）


@dataclass
class ActTransition:
    """幕數轉換規則"""
    from_act: ActType
    to_act: ActType
    condition: str             # 轉換條件描述
    required_actions: int      # 需要的關鍵行為數量
    time_threshold: int = 0    # 時間門檻（可選）


class StoryStateMachine:
    """
    五幕狀態機
    管理劇情從第一幕到第五幕的推進。
    """

    # 幕數名稱映射
    ACT_NAMES = {
        1: "第一章：覺醒",
        2: "第二章：探索",
        3: "第三章：抉擇",
        4: "第四章：衝突",
        5: "第五章：結局"
    }

    def __init__(self):
        """初始化狀態機，設置轉換規則。"""
        self._current_act = ActType.ACT_1_INTRODUCTION
        self._player_actions: Dict[str, int] = {}
        self._transitions = self._define_transitions()

    def _define_transitions(self) -> list:
        """定義幕數轉換規則。"""
        return [
            ActTransition(
                from_act=ActType.ACT_1_INTRODUCTION,
                to_act=ActType.ACT_2_RISING,
                condition="完成初始對話並建立至少3個NPC聯繫",
                required_actions=5
            ),
            ActTransition(
                from_act=ActType.ACT_2_RISING,
                to_act=ActType.ACT_3_CLIMAX,
                condition="探索平行世界並發現關鍵線索",
                required_actions=10
            ),
            ActTransition(
                from_act=ActType.ACT_3_CLIMAX,
                to_act=ActType.ACT_4_FALLING,
                condition="做出關鍵抉擇",
                required_actions=3
            ),
            ActTransition(
                from_act=ActType.ACT_4_FALLING,
                to_act=ActType.ACT_5_RESOLUTION,
                condition="完成衝突解決",
                required_actions=5
            ),
        ]

    @property
    def current_act(self) -> ActType:
        """獲取當前幕數。"""
        return self._current_act

    @property
    def current_act_name(self) -> str:
        """獲取當前幕數名稱。"""
        return self.ACT_NAMES[self._current_act.value]

    def record_action(self, action_type: str):
        """
        記錄玩家行為。

        Args:
            action_type: 行為類型
        """
        self._player_actions[action_type] = self._player_actions.get(action_type, 0) + 1

    def can_advance(self) -> bool:
        """
        檢查是否可以推進到下一幕。

        Returns:
            是否滿足轉換條件
        """
        total_actions = sum(self._player_actions.values())
        for transition in self._transitions:
            if transition.from_act == self._current_act:
                return total_actions >= transition.required_actions
        return False

    def advance(self) -> Optional[ActType]:
        """
        嘗試推進到下一幕。

        Returns:
            新的幕數，如果不能推進則返回 None
        """
        if not self.can_advance():
            return None

        for transition in self._transitions:
            if transition.from_act == self._current_act:
                self._current_act = transition.to_act
                return self._current_act
        return None

    def get_progress(self) -> Dict:
        """獲取當前劇情進度信息。"""
        total_actions = sum(self._player_actions.values())
        next_transition = None
        for t in self._transitions:
            if t.from_act == self._current_act:
                next_transition = t
                break

        progress = 0.0
        if next_transition:
            progress = min(1.0, total_actions / next_transition.required_actions)

        return {
            "current_act": self._current_act.value,
            "act_name": self.current_act_name,
            "total_actions": total_actions,
            "progress": progress,
            "is_final_act": self._current_act == ActType.ACT_5_RESOLUTION
        }
