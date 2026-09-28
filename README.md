# Parallel — 平行世界多智能体叙事系统

> Multi-Agent Interactive Narrative System | FastAPI + LLM Agents + Flutter

## 项目简介

一个多智能体编排的互动叙事后端。玩家与"平行世界"中的角色进行即时通讯与邮件往来，对话内容由 LLM 智能体实时生成，系统按玩家行为推进五幕剧情并判定结局。

**当前完成度：后端可用，前端为骨架。** 详见文末「当前边界」。

## 架构

```
玩家输入
   │
   ▼
PEPOrchestrator（编排器）
   ├── WorldAgent   维护世界观、时间线、NPC 状态
   ├── ChatAgent    生成即时通讯回复（SSE 流式输出）
   ├── MailAgent    生成剧情邮件
   └── StoryAgent   推进五幕状态机、判定结局
```

四个智能体由 `backend/services/orchestrator.py` 统一调度，世界观一致性与剧情连贯性由编排器保证。

## 功能特性

- **四智能体编排**：World / Chat / Mail / Story 各司其职，通过 PEP 协议协作
- **五幕状态机**：`backend/services/state_machine.py` 管理幕次推进
- **五种结局**：good / neutral / bad / hidden / true，依玩家行为数据判定
- **SSE 流式输出**：`/api/chat/stream` 逐 token 返回对话内容
- **邮件系统**：收件箱、已读标记、单封邮件查询
- **容器化部署**：提供 Dockerfile 与 docker-compose.yml

## 技术栈

| 层级 | 技术 |
|------|------|
| 后端框架 | FastAPI + Uvicorn |
| 智能体 | OpenAI SDK（GPT-4o-mini / Qwen-Plus） |
| 流式传输 | SSE（sse-starlette） |
| 配置管理 | pydantic-settings |
| 前端 | Flutter / Dart |
| 部署 | Docker |

## 项目结构

```
Parallel/
├── backend/
│   ├── main.py                  # FastAPI 入口，注册三个路由模块
│   ├── agents/                  # 四个智能体实现
│   │   ├── world_agent.py
│   │   ├── chat_agent.py
│   │   ├── mail_agent.py
│   │   └── story_agent.py
│   ├── routes/                  # API 路由
│   │   ├── chat.py              # /api/chat/*
│   │   ├── mail.py              # /api/mail/*
│   │   └── story.py             # /api/story/*
│   ├── services/
│   │   ├── orchestrator.py      # PEP 编排器
│   │   └── state_machine.py     # 五幕状态机
│   ├── config/settings.py       # 配置项
│   └── requirements.txt
├── agents/                      # 智能体声明式定义（yaml）
│   ├── world/definition.yaml
│   ├── chat/definition.yaml
│   ├── mail/definition.yaml
│   └── story/definition.yaml
├── prompts/                     # 各智能体系统提示词
├── frontend/
│   ├── lib/main.dart            # Flutter 入口（当前为骨架）
│   └── pubspec.yaml
└── docker/
    ├── Dockerfile
    └── docker-compose.yml
```

## API 端点

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/api/health` | 健康检查 |
| GET | `/api/chat/stream` | SSE 流式对话 |
| POST | `/api/chat/send` | 发送消息 |
| GET | `/api/mail/inbox` | 收件箱列表 |
| GET | `/api/mail/{mail_id}` | 单封邮件详情 |
| PUT | `/api/mail/{mail_id}/read` | 标记已读 |
| GET | `/api/story/status` | 当前剧情进度 |
| GET | `/api/story/endings` | 结局列表 |

启动后访问 `/docs` 查看自动生成的 Swagger 文档。

## 快速开始

```bash
git clone https://github.com/Enchore/Parallel.git
cd Parallel/backend

pip install -r requirements.txt

# 配置 LLM 密钥
export OPENAI_API_KEY="your-key"

uvicorn backend.main:app --reload
```

或使用 Docker：

```bash
cd docker && docker compose up -d
```

## 当前边界

以下为**尚未完成**的部分，如实列出：

- **Flutter 前端仅完成外壳**：`frontend/lib/main.dart` 实现了首页与四个 Tab（消息／邮箱／剧情／设定）的导航框架，但每个 Tab 的内容目前是占位组件，**尚未实现页面逻辑，也未与后端 API 对接**
- **数据库未接入**：`settings.py` 中预留了 `SQLITE_DB_PATH` 与 `REDIS_URL` 配置项，`aioredis` 亦在依赖列表中，但代码中尚无实际的数据库读写，会话状态目前不持久化
- **NPC 角色未定义**：智能体定义中描述了为 10 个 NPC 生成内容的能力，但仓库内**没有 NPC 角色定义文件**，需自行添加
- **无单元测试与 CI**

## 许可证

本项目基于 [MIT License](LICENSE) 开源。
