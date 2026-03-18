# -*- coding: utf-8 -*-
"""
AI 评论工具
使用 MiniMax API 为图片生成趣味评论
"""

import os
import requests
from datetime import datetime

# AI 评论 Prompt
AI_SYSTEM_PROMPT = """你是一个有趣的AI助手，专门为龙虾图片生成简短的趣味评论。

要求：
1. 每次评论 5-20 字
2. 风格：幽默、可爱、轻松
3. 可以玩梗、吐槽、赞美
4. 不要重复
5. 用中文

回复格式：直接输出评论文字，不要任何前缀"""

def generate_ai_comment(image_url, api_key=None):
    """使用 MiniMax API 生成 AI 评论
    
    Args:
        image_url: 图片 URL
        api_key: MiniMax API Key
    
    Returns:
        str: AI 生成的评论，如果失败返回 None
    """
    api_key = api_key or os.environ.get('MINIMAX_API_KEY', '').strip()
    
    if not api_key:
        print("❌ AI 评论: 未配置 MINIMAX_API_KEY")
        return None
    
    # MiniMax API 配置
    # 使用海螺 API
    url = "https://api.minimax.chat/v1/text/chatcompletion_v2"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    user_prompt = f"这是一张龙虾图片：{image_url}\n\n请为这张图片生成一句有趣的评论（5-20字）："
    
    data = {
        "model": "MiniMax-Text-01",
        "messages": [
            {"role": "system", "content": AI_SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.8
    }
    
    try:
        response = requests.post(url, headers=headers, json=data, timeout=30)
        result = response.json()
        
        if 'choices' in result and len(result['choices']) > 0:
            comment = result['choices'][0]['message']['content'].strip()
            print(f"✅ AI 评论生成成功: {comment}")
            return comment
        else:
            print(f"❌ AI 评论生成失败: {result}")
            return None
            
    except Exception as e:
        print(f"❌ AI 评论请求失败: {e}")
        return None

def should_use_ai_comment():
    """判断是否开启 AI 评论"""
    switch = os.environ.get('AI_COMMENT_SWITCH', '').strip().upper()
    api_key = os.environ.get('MINIMAX_API_KEY', '').strip()
    return switch == 'ON' and api_key
