# -*- coding: utf-8 -*-
"""
自动生成配置文件
从环境变量生成 config.yaml
"""

import os
import yaml

def generate_config():
    """从环境变量生成 config.yaml"""
    
    config = {}
    
    # GitHub
    token = os.environ.get('GITHUB_TOKEN', '').strip()
    if token:
        config['github'] = {
            'token': token,
            'owner': os.environ.get('GITHUB_OWNER', 'adminlove520'),
            'repo': os.environ.get('GITHUB_REPO', 'ClawFeeds'),
        }
    
    # push 配置
    push = {}
    
    # GitHub Discussion
    if os.environ.get('GH_DISCUSSION_SWITCH', '').strip().upper() == 'ON':
        push['github_discussion'] = {
            'switch': 'ON',
            'discussion_owner': os.environ.get('GH_DISCUSSION_OWNER', ''),
            'discussion_repo': os.environ.get('GH_DISCUSSION_REPO', ''),
            'discussion_number': int(os.environ.get('GH_DISCUSSION_NUMBER', 0)),
            'mode': os.environ.get('GH_DISCUSSION_MODE', 'each'),
        }
    
    # 钉钉
    webhook = os.environ.get('DINGDING_WEBHOOK', '').strip()
    secret = os.environ.get('DINGDING_SECRET', '').strip()
    if webhook:
        push['dingding'] = {
            'webhook': webhook,
            'secret_key': secret,
            'switch': os.environ.get('DINGDING_SWITCH', 'OFF'),
        }
    
    # Discord
    if os.environ.get('DISCARD_WEBHOOK', '').strip():
        push['discard'] = {
            'webhook': os.environ.get('DISCARD_WEBHOOK', ''),
            'switch': os.environ.get('DISCARD_SWITCH', 'OFF'),
        }
    
    if push:
        config['push'] = push
    
    # AI Comment
    if os.environ.get('AI_COMMENT_SWITCH', '').strip().upper() == 'ON':
        config['ai_comment'] = {
            'switch': 'ON',
            'api_key': os.environ.get('MINIMAX_API_KEY', ''),
        }
    
    # 代理
    if os.environ.get('PROXY_ENABLE', '').strip().upper() == 'ON':
        config['proxy'] = {
            'enable': 'ON',
            'http_proxy': os.environ.get('HTTP_PROXY', 'http://127.0.0.1:7890'),
            'https_proxy': os.environ.get('HTTPS_PROXY', 'http://127.0.0.1:7890'),
        }
    
    # 夜间休眠
    config['night_sleep'] = {
        'switch': os.environ.get('NIGHT_SLEEP_SWITCH', 'ON'),
    }
    
    return config

def save_config():
    """保存配置到 config.yaml"""
    config = generate_config()
    
    if config:
        with open('config.yaml', 'w', encoding='utf-8') as f:
            yaml.dump(config, f, allow_unicode=True, default_flow_style=False)
        print("config.yaml generated")
    else:
        print("No config from env vars")

if __name__ == '__main__':
    save_config()
