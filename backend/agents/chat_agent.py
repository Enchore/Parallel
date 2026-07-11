"""
即時通訊智能體 (Chat Agent)
負責生成 NPC 與玩家的即時通訊對話內容。
通過 SSE 實時推送消息給前端。
"""
from typing import AsyncGenerator, Optional
from dataclasses import dataclass


@dataclass
class ChatMessage:
    """即時通訊消息"""
    sender_id: str
    sender_name: str
    content: str
    timestamp: str
    message_type: str = "text"   # text / image / system


class ChatAgent:
    """
    即時通訊智能體
    為 NPC 角色生成即時通訊對話內容。
    """

    def __init__(self, model_name: str = "gpt-4o-mini"):
        """
        初始化即時通訊智能體。

        Args:
            model_name: LLM 模型名稱
        """
        self._model_name = model_name

    async def generate_response(
        self,
        npc_id: str,
        player_message: str,
        context: list
    ) -> AsyncGenerator[str, None]:
        """
        生成 NPC 的回覆消息（SSE 流式輸出）。

        Args:
            npc_id: NPC 角色 ID
            player_message: 玩家發送的消息
            context: 對話上下文

        Yields:
            流式生成的文本片段
        """
        # TODO: 調用 LLM API 進行流式生成
        yield f"[{npc_id}] 正在思考..."

    async def get_chat_history(self, player_id: str, npc_id: str) -> list:
        """獲取玩家與 NPC 的歷史聊天記錄。"""
        # TODO: 從數據庫查詢
        return []
