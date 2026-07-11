"""
智能體編排器 (Orchestrator)
基於 PEP (Protocol for Exchange of Protocols) 協議協調多個 LLM 智能體。
管理 World/Chat/Mail/Story 四個智能體的通信與協作。
"""
from typing import Dict, Optional
from backend.agents.world_agent import WorldAgent
from backend.agents.chat_agent import ChatAgent
from backend.agents.mail_agent import MailAgent
from backend.agents.story_agent import StoryAgent


class PEPOrchestrator:
    """
    PEP 協議智能體編排器
    協調四個智能體的通信，確保世界觀一致性和劇情連貫性。
    """

    def __init__(self):
        """初始化編排器，創建四個智能體實例。"""
        self._world = WorldAgent()
        self._chat = ChatAgent()
        self._mail = MailAgent()
        self._story = StoryAgent()

    async def handle_player_message(
        self,
        player_id: str,
        npc_id: str,
        message: str,
        channel: str = "chat"
    ) -> Dict:
        """
        處理玩家消息並協調智能體回應。

        Args:
            player_id: 玩家 ID
            npc_id: NPC ID
            message: 玩家消息
            channel: 通信頻道（chat/mail）

        Returns:
            編排結果
        """
        # 1. 查詢世界觀狀態
        world_context = await self._world.query_world_state("current")

        # 2. 記錄玩家行為到劇情系統
        action_event = await self._story.process_player_action({
            "player_id": player_id,
            "npc_id": npc_id,
            "message": message,
            "channel": channel
        })

        # 3. 根據頻道選擇智能體處理
        if channel == "chat":
            response = await self._chat.generate_response(
                npc_id, message, [world_context]
            )
        else:
            response = await self._mail.generate_mail(
                npc_id, world_context
            )

        # 4. 檢查是否觸發劇情事件
        result = {
            "response": response,
            "story_event": action_event,
            "world_state": world_context
        }

        return result

    async def check_story_progression(self, player_id: str) -> Dict:
        """
        檢查劇情是否需要推進（幕數變化或結局觸發）。

        Args:
            player_id: 玩家 ID

        Returns:
            劇情進展信息
        """
        # TODO: 查詢玩家行為數據，評估是否觸發幕數推進或結局
        return {"progression": None}
