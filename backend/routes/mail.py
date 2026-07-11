"""
郵件路由
提供郵件收發查詢接口
"""
from fastapi import APIRouter, Query
from typing import List, Optional

router = APIRouter()


@router.get("/inbox")
async def get_inbox(player_id: str = Query(...)):
    """
    獲取玩家郵箱列表
    """
    # TODO: 調用 MailAgent 獲取郵箱
    return {"mails": [], "unread_count": 0}


@router.get("/{mail_id}")
async def get_mail_detail(mail_id: str):
    """
    獲取郵件詳情
    """
    # TODO: 查詢郵件詳情
    return {"mail_id": mail_id, "subject": "", "body": ""}


@router.put("/{mail_id}/read")
async def mark_as_read(mail_id: str):
    """
    標記郵件為已讀
    """
    return {"status": "ok"}
