
# ClawFeeds

> Telegram 频道图片自动监控推送到 Zeabur/Docker/本地

**当前版本：V2.1.0**

---

## ✨ 特性

- 📱 **Telegram RSS 监控**：监控 Telegram 频道更新
- 🤖 **AI 评论**：支持 MiniMax API 自动生成趣味评论
- 💬 **多平台推送**：Discord、钉钉、飞书、Telegram、GitHub Discussion
- ☁️ **Zeabur 部署**：一键部署到 Zeabur
- 🔄 **自动重试**：429 自动退避重试

---

## 🚀 快速部署到 Zeabur

### 1. Fork 本仓库

### 2. 部署到 Zeabur

[![Deploy on Zeabur](https://zeabur.com/button.svg)](https://zeabur.com/templates/AYP?referralCode=adminlove520)

### 3. 配置环境变量

在 Zeabur 服务页面 → 环境变量 中添加：

```bash
# 必填
GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxx

# GitHub Discussion（可选）
GH_DISCUSSION_SWITCH=ON
GH_DISCUSSION_OWNER=ythx-101
GH_DISCUSSION_REPO=openclaw-qa
GH_DISCUSSION_NUMBER=133

# AI 评论（可选）
MINIMAX_API_KEY=your_minimax_api_key
AI_COMMENT_SWITCH=ON

# 钉钉推送（可选）
DINGDING_WEBHOOK=https://oapi.dingtalk.com/robot/send?access_token=xxx
DINGDING_SECRET=SECxxx
DINGDING_SWITCH=ON

# Discord 推送（可选）
DISCARD_WEBHOOK=https://discord.com/api/webhooks/xxx
DISCARD_SWITCH=ON

# 代理（可选）
PROXY_ENABLE=ON
HTTP_PROXY=http://127.0.0.1:7890
HTTPS_PROXY=http://127.0.0.1:7890
```

### 4. 搞定！

服务会自动启动，每 15 分钟检查一次 Telegram 频道更新。

---

## 📋 环境变量说明

| 变量 | 必填 | 说明 |
|------|------|------|
| `GITHUB_TOKEN` | ✅ | GitHub Token |
| `GH_DISCUSSION_SWITCH` | - | ON/OFF |
| `GH_DISCUSSION_OWNER` | - | Discussion 仓库 owner |
| `GH_DISCUSSION_REPO` | - | Discussion 仓库名 |
| `GH_DISCUSSION_NUMBER` | - | Discussion 编号 |
| `MINIMAX_API_KEY` | - | MiniMax API Key |
| `AI_COMMENT_SWITCH` | - | ON/OFF |
| `DINGDING_WEBHOOK` | - | 钉钉 Webhook |
| `DINGDING_SECRET` | - | 钉钉加签密钥 |
| `DINGDING_SWITCH` | - | ON/OFF |
| `DISCARD_WEBHOOK` | - | Discord Webhook |
| `DISCARD_SWITCH` | - | ON/OFF |
| `PROXY_ENABLE` | - | ON/OFF |
| `HTTP_PROXY` | - | HTTP 代理 |
| `HTTPS_PROXY` | - | HTTPS 代理 |

---

## 🏠 本地开发

```bash
# 克隆
git clone https://github.com/adminlove520/ClawFeeds.git
cd ClawFeeds

# 复制配置
cp config-example.yaml config.yaml
# 编辑 config.yaml 填入配置

# 运行
pip install -r requirements.txt
python Rss_monitor.py
```

---

## 📂 项目结构

```
.
├── Rss_monitor.py          # 主程序
├── rss.yaml               # RSS 源配置
├── Dockerfile             # Docker 镜像
├── utils/
│   ├── notify.py         # 推送
│   ├── rss.py            # RSS 解析
│   ├── config.py         # 配置加载
│   ├── db.py            # 数据库
│   ├── github.py        # GitHub API
│   ├── discussion.py    # Discussion
│   └── ai_comment.py    # AI 评论
└── requirements.txt
```

---

## 📜 许可证

MIT

---

🦞 小溪的作品
