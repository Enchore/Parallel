"""
即時通訊路由
提供 SSE 流式聊天接口
"""
from fastapi import APIRouter, Request
from sse_starlette.sse import EventSourceResponse

router = APIRouter()


@router.get("/stream")
async def chat_stream(request: Request, npc_id: str, player_id: str):
    """
    SSE 流式聊天接口
    接收玩家消息並流式返回 NPC 回覆
    """
    async def event_generator():
        # TODO: 調用 ChatAgent 生成流式回覆
        yield {"data": '{"type": "typing", "npc_id": "' + npc_id + '"}'}
        yield {"data": '{"type": "message", "content": "你好，來自平行世界的旅人..."}'}

    return EventSourceResponse(event_generator())


@router.post("/send")
async def send_message(npc_id: str, player_id: str, content: str):
    """
    發送消息接口
    """
    # TODO: 存儲消息並觸發 NPC 回覆
    return {"status": "ok", "message_id": "placeholder"}
