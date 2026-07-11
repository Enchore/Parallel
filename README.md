# Parallel — 平行世界多智能體敘事系統

> Parallel — 平行世界多智能體敘事系統 | Multi-Agent Interactive Narrative System

## 項目簡介

一款基於多智能體編排架構的互動敘事應用，玩家透過手機模擬器介面與來自「平行世界」的同伴進行郵件、即時通訊等互動。所有通訊內容由 LLM 智能體即時生成，系統根據玩家行為數據自動推進五幕劇情並觸發多種結局。

## 項目亮點

- **多智能體編排架構**：4 個 LLM Agent（World/Chat/Mail/Story）+ PEP 協議
- **行為驅動多結局引擎**：根據玩家行為數據觸發 5 種不同結局
- **五幕狀態機**：完整的劇情推進狀態管理
- **10 個 NPC 角色模板引擎**：豐富的角色定義與個性化對話
- **Docker 容器化部署**：完整的容器化部署方案

## 技術棧

| 層級 | 技術 |
|------|------|
| 後端框架 | Python, FastAPI |
| LLM | GPT-4o-mini, Qwen-Plus |
| 即時通訊 | SSE (Server-Sent Events) |
| 數據庫 | SQLite, Redis |
| 前端框架 | Flutter, Dart |
| 部署 | Docker |

## 項目結構

```
Parallel/
├── backend/                   # FastAPI 後端
│   ├── agents/               # 智能體實現
│   │   ├── __init__.py
│   │   ├── world_agent.py    # 世界觀智能體
│   │   ├── chat_agent.py     # 即時通訊智能體
│   │   ├── mail_agent.py     # 郵件智能體
│   │   └── story_agent.py    # 劇情推進智能體
│   ├── routes/               # API 路由
│   │   ├── __init__.py
│   │   ├── chat.py
│   │   ├── mail.py
│   │   └── story.py
│   ├── services/              # 業務邏輯服務
│   │   ├── __init__.py
│   │   ├── orchestrator.py   # 智能體編排器（PEP 協議）
│   │   └── state_machine.py  # 五幕狀態機
│   ├── config/                # 配置
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── main.py                # 應用入口
│   └── requirements.txt
├── frontend/                  # Flutter 前端
│   ├── lib/
│   │   ├── main.dart          # Flutter 入口
│   │   ├── screens/          # 頁面
│   │   ├── widgets/          # 組件
│   │   ├── models/           # 數據模型
│   │   └── services/         # API 服務
│   ├── pubspec.yaml
│   └── README.md
├── agents/                    # LLM 智能體定義
│   ├── world/
│   ├── chat/
│   ├── mail/
│   └── story/
├── prompts/                    # 系統提示詞
│   ├── world_system.txt
│   ├── chat_system.txt
│   ├── mail_system.txt
│   └── story_system.txt
├── docker/                    # Docker 配置
│   ├── Dockerfile
│   └── docker-compose.yml
├── docs/                       # 文檔
├── README.md
├── .gitignore
└── LICENSE
```

## 快速開始

### 後端

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

### 前端 (Flutter)

```bash
cd frontend
flutter pub get
flutter run
```

### Docker 部署

```bash
cd docker
docker-compose up -d
```

## 貢獻

歡迎提交 Issue 和 Pull Request。

## 許可證

本項目基於 [MIT License](LICENSE) 開源。
