# -*- coding: utf-8 -*-
"""
Discussion 工具
发评论到 GitHub Discussion
"""

import os
import random
from .github import GitHubClient
from datetime import datetime

# 有趣的评论模板
COMMENT_TEMPLATES = [
    "今日份快乐🐛",
    "今天也在好好长大呢～🌱",
    "又是被龙虾治愈的一天🦞",
    "这图也太有意思了哈哈哈",
    "小溪表示很满意😌",
    "前方高萌预警！⚠️",
    "今天的快乐是龙虾给的",
    "笑死，根本停不下来",
    "这也太卷了吧（褒义）",
    "我直接存图！",
    "又是涨姿势的一天",
    "萌到犯规啦～",
    "给哥哥分享今日の快乐",
    "这也太香了吧",
    "小溪偷偷收藏了😏",
    "每日一存，防止丢失",
    "绝美截图，+1111",
    "笑点被戳中哈哈哈",
    "这也太可爱了8",
    "顶顶顶！",
    "太刑了，太可铐了",
    "笑死，这个太魔性了",
    "每日快乐+1",
    "又发现一个宝藏！",
    "我裂开了（字面意思）",
]

def get_random_comment():
    """随机获取一条评论"""
    return random.choice(COMMENT_TEMPLATES)

def post_to_discussion(owner, repo, token, discussion_number, content):
    """发评论到 Discussion"""
    client = GitHubClient(token=token, owner=owner, repo=repo)
    return client.add_discussion_comment(discussion_number, content)

def format_daily_post(date, image_urls):
    """格式化每日图片帖子（多条图片）
    
    Args:
        date: 日期字符串，如 "2026-03-18"
        image_urls: 图片 URL 列表
    
    Returns:
        Markdown 格式的内容
    """
    beijing_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    content = f"## 🦞 龙虾趣图 - {date}\n\n"
    content += f"*更新时间: {beijing_time}*\n\n"
    
    for i, url in enumerate(image_urls, 1):
        content += f"### 图片 {i}\n"
        content += f"![龙虾趣图 {i}]({url})\n\n"
    
    content += "---\n"
    content += f"*由 Clawimgs Monitor 自动推送*"
    
    return content

def get_comment(image_url):
    """获取评论（优先 AI，其次随机）"""
    # 检查是否使用 AI
    ai_switch = os.environ.get('AI_COMMENT_SWITCH', '').strip().upper()
    if ai_switch == 'ON':
        from .ai_comment import generate_ai_comment
        ai_comment = generate_ai_comment(image_url)
        if ai_comment:
            return ai_comment
    
    # 随机评论
    return get_random_comment()

def format_single_image_post(date, image_url, image_index=1, use_ai=True):
    """格式化单张图片帖子
    
    Args:
        date: 日期字符串
        image_url: 图片 URL
        image_index: 图片序号
        use_ai: 是否尝试使用 AI 评论
    
    Returns:
        Markdown 格式的内容
    """
    beijing_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 获取评论
    comment = get_comment(image_url) if use_ai else get_random_comment()
    
    content = f"## 🦞 龙虾趣图 - {date} (图{image_index})\n\n"
    content += f"**{comment}**\n\n"
    content += f"![龙虾趣图]({image_url})\n\n"
    content += f"*更新时间: {beijing_time}*"
    
    return content
