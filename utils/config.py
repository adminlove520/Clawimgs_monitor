import yaml
import os
from datetime import datetime

# 加载配置文件
def load_config():
    config = {}
    
    # 1. 先尝试加载 config.yaml（本地开发用）
    config_path = 'config.yaml'
    if not os.path.exists(config_path):
        config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.yaml')
    
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f) or {}
        except Exception as e:
            print(f"加载config.yaml出错: {e}")
    
    # 2. 环境变量覆盖（Zeabur/生产环境用）
    
    # GitHub 配置
    github_config = config.get('github', {})
    config['github'] = {
        'token': os.environ.get('GITHUB_TOKEN', github_config.get('token', '')),
        'owner': os.environ.get('GITHUB_OWNER', github_config.get('owner', 'adminlove520')),
        'repo': os.environ.get('GITHUB_REPO', github_config.get('repo', 'Clawimgs_monitor')),
    }
    
    # 代理配置
    proxy_config = config.get('proxy', {})
    config['proxy'] = {
        'enable': os.environ.get('PROXY_ENABLE', proxy_config.get('enable', 'OFF')),
        'http_proxy': os.environ.get('HTTP_PROXY', proxy_config.get('http_proxy', 'http://127.0.0.1:7890')),
        'https_proxy': os.environ.get('HTTPS_PROXY', proxy_config.get('https_proxy', 'http://127.0.0.1:7890')),
        'no_proxy': os.environ.get('NO_PROXY', proxy_config.get('no_proxy', 'localhost,127.0.0.1')),
    }
    
    # 夜间休眠
    night_config = config.get('night_sleep', {})
    config['night_sleep'] = {
        'switch': os.environ.get('NIGHT_SLEEP_SWITCH', night_config.get('switch', 'ON'))
    }
    
    # 推送配置
    push_config = config.get('push', {})
    
    # 钉钉
    dingding = push_config.get('dingding', {})
    push_config['dingding'] = {
        'webhook': os.environ.get('DINGDING_WEBHOOK', dingding.get('webhook', '')),
        'secret_key': os.environ.get('DINGDING_SECRET', dingding.get('secret_key', '')),
        'switch': os.environ.get('DINGDING_SWITCH', dingding.get('switch', 'OFF')),
    }
    
    # 飞书
    feishu = push_config.get('feishu', {})
    push_config['feishu'] = {
        'webhook': os.environ.get('FEISHU_WEBHOOK', feishu.get('webhook', '')),
        'switch': os.environ.get('FEISHU_SWITCH', feishu.get('switch', 'OFF')),
    }
    
    # Telegram
    tg_bot = push_config.get('tg_bot', {})
    push_config['tg_bot'] = {
        'token': os.environ.get('TELEGRAM_TOKEN', tg_bot.get('token', '')),
        'group_id': os.environ.get('TELEGRAM_GROUP_ID', tg_bot.get('group_id', '')),
        'switch': os.environ.get('TELEGRAM_SWITCH', tg_bot.get('switch', 'OFF')),
    }
    
    # Discord
    discard = push_config.get('discard', {})
    push_config['discard'] = {
        'webhook': os.environ.get('DISCARD_WEBHOOK', discard.get('webhook', '')),
        'switch': os.environ.get('DISCARD_SWITCH', discard.get('switch', 'OFF')),
    }
    
    # GitHub Discussion
    gh_discussion = push_config.get('github_discussion', {})
    push_config['github_discussion'] = {
        'switch': os.environ.get('GH_DISCUSSION_SWITCH', gh_discussion.get('switch', 'OFF')),
        'discussion_owner': os.environ.get('GH_DISCUSSION_OWNER', gh_discussion.get('discussion_owner', '')),
        'discussion_repo': os.environ.get('GH_DISCUSSION_REPO', gh_discussion.get('discussion_repo', '')),
        'discussion_number': os.environ.get('GH_DISCUSSION_NUMBER', gh_discussion.get('discussion_number', 0)),
        'mode': os.environ.get('GH_DISCUSSION_MODE', gh_discussion.get('mode', 'each')),
        'add_comment': os.environ.get('GH_DISCUSSION_ADD_COMMENT', gh_discussion.get('add_comment', 'ON')),
    }
    
    config['push'] = push_config
    
    return config

# 判断是否应该进行夜间休眠
def should_sleep():
    config = load_config()
    sleep_switch = config.get('night_sleep', {}).get('switch', 'ON')
    if sleep_switch != 'ON':
        return False
    
    now_utc = datetime.utcnow()
    now_bj = now_utc.hour + 8
    if now_bj >= 24:
        now_bj -= 24
    
    return now_bj < 7

# 获取代理配置
def get_proxies():
    config = load_config()
    proxy_config = config.get('proxy', {})
    
    if proxy_config.get('enable', 'OFF') == 'OFF':
        return None
    
    proxies = {}
    if proxy_config.get('http_proxy'):
        proxies['http'] = proxy_config.get('http_proxy')
    if proxy_config.get('https_proxy'):
        proxies['https'] = proxy_config.get('https_proxy')
    
    return proxies if proxies else None
