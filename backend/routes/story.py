"""
劇情路由
提供劇情狀態查詢與結局查詢接口
"""
from fastapi import APIRouter, Query
from typing import Optional

router = APIRouter()


@router.get("/status")
async def get_story_status(player_id: str = Query(...)):
    """
    獲取當前劇情狀態
    """
    return {
        "current_act": 1,
        "act_name": "第一章：覺醒",
        "progress": 0.0,
        "available_endings": []
    }


@router.get("/endings")
async def get_available_endings(player_id: str = Query(...)):
    """
    獲取可用結局列表
    """
    return {
        "endings": [
            {"type": "good_ending", "name": "光明的平行線", "unlocked": False},
            {"type": "neutral_ending", "name": "交叉的路口", "unlocked": False},
            {"type": "bad_ending", "name": "消逝的世界", "unlocked": False},
            {"type": "hidden_ending", "name": "被遺忘的信", "unlocked": False},
            {"type": "true_ending", "name": "平行世界的真相", "unlocked": False}
        ]
    }
