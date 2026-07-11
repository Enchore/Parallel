# Parallel 技術架構文檔

## 系統架構

### 多智能體編排架構

Parallel 系統採用基於 PEP（Protocol for Exchange of Protocols）的多智能體編排架構，包含四個核心智能體：

1. **World Agent（世界觀智能體）**
   - 模型：Qwen-Plus
   - 職責：維護世界觀一致性，提供背景信息

2. **Chat Agent（即時通訊智能體）**
   - 模型：GPT-4o-mini
   - 職責：生成 NPC 即時通訊對話，SSE 流式輸出

3. **Mail Agent（郵件智能體）**
   - 模型：GPT-4o-mini
   - 職責：生成 NPC 郵件，推進劇情

4. **Story Agent（劇情智能體）**
   - 模型：Qwen-Plus
   - 職責：管理五幕劇情狀態機，判定結局

### PEP 協議

智能體間通信採用 PEP 協議，確保世界觀一致性和劇情連貫性。
