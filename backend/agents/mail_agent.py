"""
郵件智能體 (Mail Agent)
負責生成 NPC 發送的郵件內容，模擬平行世界中的郵件系統。
"""
from typing import List, Optional
from dataclasses import dataclass


@dataclass
class Mail:
    """郵件數據類"""
    mail_id: str
    sender_id: str
    sender_name: str
    subject: str
    body: str
    timestamp: str
    is_read: bool = False
    attachments: list = None

    def __post_init__(self):
        if self.attachments is None:
            self.attachments = []


class MailAgent:
    """
    郵件智能體
    為 NPC 角色生成郵件內容，推進劇情。
    """

    def __init__(self, model_name: str = "gpt-4o-mini"):
        """
        初始化郵件智能體。

        Args:
            model_name: LLM 模型名稱
        """
        self._model_name = model_name

    async def generate_mail(
        self,
        npc_id: str,
        context: dict,
        purpose: str = "story_progression"
    ) -> Mail:
        """
        生成 NPC 發送的郵件。

        Args:
            npc_id: 發送者 NPC ID
            context: 上下文信息
            purpose: 郵件目的（劇情推進/日常互動/緊急通知）

        Returns:
            生成的郵件對象
        """
        # TODO: 調用 LLM 生成郵件標題和正文
        return Mail(
            mail_id="",
            sender_id=npc_id,
            sender_name="",
            subject="",
            body=""
        )

    async def get_mailbox(self, player_id: str) -> List[Mail]:
        """獲取玩家的郵箱列表。"""
        # TODO: 從數據庫查詢
        return []
