"""
世界觀智能體 (World Agent)
負責維護平行世界的整體世界觀設定，為其他智能體提供一致的背景信息。
採用 PEP 協議與其他智能體通信。
"""
from typing import Dict, Optional
from dataclasses import dataclass


@dataclass
class WorldState:
    """世界狀態數據類"""
    current_act: int = 1           # 當前幕數 (1-5)
    world_name: str = "平行世界"
    timeline_offset: int = 0       # 時間線偏移
    active_npcs: list = None       # 活躍 NPC 列表

    def __post_init__(self):
        if self.active_npcs is None:
            self.active_npcs = []


class WorldAgent:
    """
    世界觀智能體
    管理平行世界的整體狀態、世界觀規則和時間線。
    """

    def __init__(self, model_name: str = "qwen-plus"):
        """
        初始化世界觀智能體。

        Args:
            model_name: LLM 模型名稱
        """
        self._model_name = model_name
        self._state = WorldState()

    async def query_world_state(self, aspect: str) -> Dict:
        """
        查詢世界狀態。

        Args:
            aspect: 查詢的方面（如 "npcs", "timeline", "events"）

        Returns:
            世界狀態相關信息
        """
        # TODO: 調用 LLM 獲取世界狀態信息
        return {"aspect": aspect, "data": {}}

    async def update_world_state(self, event: Dict) -> bool:
        """
        根據玩家行為事件更新世界狀態。

        Args:
            event: 玩家行為事件

        Returns:
            是否成功更新
        """
        # TODO: 處理事件並更新世界狀態
        return True
