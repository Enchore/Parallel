"""
劇情智能體 (Story Agent)
負責管理五幕劇情的推進、結局判定與玩家行為追蹤。
"""
from enum import Enum
from typing import Dict, Optional
from dataclasses import dataclass


class EndingType(Enum):
    """結局類型枚舉"""
    GOOD_ENDING = "good_ending"           # 好結局
    NEUTRAL_ENDING = "neutral_ending"       # 普通結局
    BAD_ENDING = "bad_ending"              # 壞結局
    HIDDEN_ENDING = "hidden_ending"        # 隱藏結局
    TRUE_ENDING = "true_ending"            # 真結局


@dataclass
class StoryEvent:
    """劇情事件"""
    event_id: str
    act: int                # 所屬幕數 (1-5)
    trigger_conditions: dict
    event_content: str
    consequences: list = None

    def __post_init__(self):
        if self.consequences is None:
            self.consequences = []


class StoryAgent:
    """
    劇情智能體
    管理五幕劇情狀態機，根據玩家行為推進劇情並判定結局。
    """

    def __init__(self, model_name: str = "qwen-plus"):
        """
        初始化劇情智能體。

        Args:
            model_name: LLM 模型名稱
        """
        self._model_name = model_name
        self._current_act = 1

    async def process_player_action(self, action: Dict) -> Optional[StoryEvent]:
        """
        處理玩家行為，觸發對應劇情事件。

        Args:
            action: 玩家行為數據

        Returns:
            觸發的劇情事件（如果有）
        """
        # TODO: 評估玩家行為，觸發劇情事件
        return None

    async def advance_act(self, player_data: Dict) -> int:
        """
        推進到下一幕。

        Args:
            player_data: 玩家累積行為數據

        Returns:
            新的幕數
        """
        if self._current_act < 5:
            self._current_act += 1
        return self._current_act

    async def determine_ending(self, player_data: Dict) -> EndingType:
        """
        根據玩家累積行為數據判定結局。

        Args:
            player_data: 玩家行為數據

        Returns:
            結局類型
        """
        # TODO: 綜合玩家行為數據進行結局判定
        return EndingType.NEUTRAL_ENDING
