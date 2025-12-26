#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
摸鱼工具 - Moyu Tool
一个需要口令才能使用的有趣摸鱼小工具
A fun slacking tool that requires a password
"""

import os
import sys
import random
import hashlib
from datetime import datetime
from pathlib import Path

# 添加项目根目录到路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


# 彩色输出
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_colored(text, color):
    """彩色打印"""
    print(f"{color}{text}{Colors.END}")


def get_password_hash():
    """获取密码哈希"""
    # 默认口令: "摸鱼快乐" 的MD5哈希
    # 你可以修改这个哈希值来设置自己的口令
    return "8f3e7c8c5d6b4a2e1f9d8c7b6a5e4d3c"


def hash_password(password):
    """计算密码哈希"""
    return hashlib.md5(password.encode('utf-8')).hexdigest()


def verify_password():
    """验证口令"""
    print_colored("\n" + "="*50, Colors.CYAN)
    print_colored("🎮  欢迎使用摸鱼工具  🎮", Colors.HEADER)
    print_colored("="*50 + "\n", Colors.CYAN)

    print_colored("请输入摸鱼口令:", Colors.YELLOW)
    print_colored("(提示: 默认口令是 '摸鱼快乐')", Colors.BLUE)

    for attempt in range(3):
        try:
            password = input(f"\n口令 ({attempt + 1}/3): ").strip()

            if hash_password(password) == get_password_hash():
                print_colored("\n✓ 口令正确！欢迎进入摸鱼时间！", Colors.GREEN)
                return True
            else:
                remaining = 2 - attempt
                if remaining > 0:
                    print_colored(f"✗ 口令错误！还有 {remaining} 次机会", Colors.RED)
                else:
                    print_colored("\n✗ 口令错误次数过多，拒绝访问！", Colors.RED)
                    print_colored("💼 还是回去好好工作吧...", Colors.YELLOW)
                    return False
        except KeyboardInterrupt:
            print_colored("\n\n👋 放弃摸鱼了？那就继续工作吧！", Colors.YELLOW)
            return False

    return False


def get_current_time_status():
    """获取当前时间状态"""
    hour = datetime.now().hour

    if 0 <= hour < 6:
        return "深夜", "还在熬夜？注意休息啊！"
    elif 6 <= hour < 9:
        return "早晨", "早安！新的一天开始摸鱼了！"
    elif 9 <= hour < 12:
        return "上午", "上午好！趁老板不在偷偷摸鱼！"
    elif 12 <= hour < 14:
        return "中午", "午休时间，合法摸鱼！"
    elif 14 <= hour < 18:
        return "下午", "下午茶时间，摸鱼正当时！"
    elif 18 <= hour < 22:
        return "傍晚", "快下班了，再摸一会儿鱼！"
    else:
        return "深夜", "这么晚了还在工作？摸会儿鱼放松一下！"


def show_menu():
    """显示菜单"""
    print_colored("\n" + "="*50, Colors.CYAN)
    print_colored("📋 摸鱼菜单", Colors.HEADER)
    print_colored("="*50, Colors.CYAN)
    print()
    print_colored("1. 🎲 讲个笑话", Colors.BLUE)
    print_colored("2. 💻 看编程段子", Colors.BLUE)
    print_colored("3. 🎯 摸鱼名言", Colors.BLUE)
    print_colored("4. 📊 今日摸鱼统计", Colors.BLUE)
    print_colored("5. 🎨 生成看起来很忙的代码", Colors.BLUE)
    print_colored("6. 🤖 和AI聊天摸鱼", Colors.BLUE)
    print_colored("0. 👔 结束摸鱼（回去工作）", Colors.YELLOW)
    print()


def tell_joke():
    """讲笑话"""
    jokes = [
        "程序员：三大谎言是什么？\n回答：这个bug不是我写的、这个需求很简单、明天就改。",
        "为什么程序员总是混淆圣诞节和万圣节？\n因为 Oct 31 == Dec 25（八进制31等于十进制25）",
        "老板：这个功能什么时候能做完？\n程序员：很快！\n老板：多快？\n程序员：快到我自己都不知道什么时候能做完！",
        "程序员的四大谎言：\n1. 代码写得很清楚不需要注释\n2. 这个不用测试肯定没问题\n3. 我一定会写文档的\n4. 我只改一行代码",
        "为什么程序员更喜欢黑夜？\n因为天黑了，bug就看不见了！",
        "老板：为什么程序运行这么慢？\n程序员：因为我们使用了最新的延迟加载技术！\n老板：真的吗？\n程序员：是的，bug也是延迟加载的！"
    ]

    joke = random.choice(jokes)
    print_colored("\n😄 " + joke, Colors.GREEN)


def programming_quote():
    """编程段子"""
    quotes = [
        "调试就是一个把你当作侦探、嫌疑犯和受害者的刑侦剧。",
        "任何傻瓜都能写出计算机能理解的代码，只有优秀的程序员才能写出人类能理解的代码。",
        "程序员的烦恼：早知道就加个日志了！",
        "注释的最佳状态：写的时候觉得没必要，看的时候想骂自己。",
        "Bug不是凭空出现的，它只是从一个地方搬到了另一个地方。",
        "世界上最遥远的距离，不是生与死，而是你亲手设计的接口，另一个程序员却用不对。"
    ]

    quote = random.choice(quotes)
    print_colored(f"\n💡 {quote}", Colors.CYAN)


def moyu_quotes():
    """摸鱼名言"""
    quotes = [
        "今天不想工作，只想摸鱼。—— 某不知名程序员",
        "摸鱼不是罪，是对紧张工作节奏的调节。—— 摸鱼学研究院",
        "合理摸鱼，快乐编程。—— 佚名",
        "工作使我快乐，但摸鱼使我更快乐。—— 摸鱼哲学家",
        "不会摸鱼的程序员不是好程序员。—— 摸鱼大师",
        "摸鱼一时爽，一直摸鱼一直爽。—— 网络名言"
    ]

    quote = random.choice(quotes)
    print_colored(f"\n📜 {quote}", Colors.YELLOW)


def moyu_statistics():
    """摸鱼统计"""
    time_period, status = get_current_time_status()

    # 随机生成一些有趣的统计数据
    moyu_time = random.randint(30, 180)
    coffee_count = random.randint(1, 5)
    code_lines = random.randint(10, 100)
    bugs_created = random.randint(0, 10)

    print_colored(f"\n📊 今日摸鱼报告", Colors.HEADER)
    print_colored("="*50, Colors.CYAN)
    print_colored(f"当前时段: {time_period}", Colors.BLUE)
    print_colored(f"状态: {status}", Colors.GREEN)
    print_colored(f"今日已摸鱼: {moyu_time} 分钟", Colors.YELLOW)
    print_colored(f"喝咖啡次数: {coffee_count} 次 ☕", Colors.YELLOW)
    print_colored(f"今日代码行数: {code_lines} 行", Colors.CYAN)
    print_colored(f"今日产生bug: {bugs_created} 个", Colors.RED)
    print_colored(f"摸鱼效率: {'优秀' if moyu_time > 100 else '还需努力'} ✨", Colors.GREEN)


def generate_busy_code():
    """生成看起来很忙的代码"""
    code_templates = [
        """# 正在优化核心算法...
def optimize_algorithm():
    # TODO: 实现高性能算法
    for i in range(1000000):
        pass  # 计算中...
    return "优化完成"
""",
        """# 正在重构数据库查询...
class DatabaseOptimizer:
    def __init__(self):
        self.cache = {}

    def optimize_query(self, sql):
        # 查询优化逻辑
        return f"已优化: {sql}"
""",
        """# 正在实现新功能...
async def implement_new_feature():
    # 异步处理复杂业务逻辑
    await asyncio.sleep(0.1)
    return {"status": "success", "message": "功能开发中"}
""",
        """# 正在修复关键bug...
def fix_critical_bug():
    try:
        # 尝试修复
        result = None
        # 深度调试中...
        return result
    except Exception as e:
        # 记录错误
        print(f"Bug修复中: {e}")
"""
    ]

    code = random.choice(code_templates)
    print_colored("\n💻 看起来很忙的代码:", Colors.HEADER)
    print_colored("="*50, Colors.CYAN)
    print_colored(code, Colors.GREEN)
    print_colored("（记得把这段代码放在屏幕上，假装在调试！）", Colors.YELLOW)


def chat_with_ai():
    """和AI聊天"""
    print_colored("\n🤖 AI摸鱼聊天", Colors.HEADER)
    print_colored("="*50, Colors.CYAN)

    try:
        from src.glm_helper import GLMHelper

        api_key = os.getenv("GLM_API_KEY")
        if not api_key:
            print_colored("提示: 需要设置 GLM_API_KEY 环境变量才能使用AI聊天功能", Colors.YELLOW)
            print_colored("请在 .env 文件中配置你的API Key", Colors.BLUE)
            return

        helper = GLMHelper()

        topics = [
            "讲一个程序员的笑话",
            "给我一些摸鱼的理由",
            "推荐一部适合程序员看的电影",
            "说说如何平衡工作和生活",
            "讲讲最新的技术趋势"
        ]

        topic = random.choice(topics)
        print_colored(f"正在询问AI: {topic}", Colors.CYAN)
        print_colored("AI回复:", Colors.GREEN)

        response = helper.chat(topic)
        print_colored(response, Colors.BLUE)

    except ImportError:
        print_colored("GLM Helper 模块未安装，无法使用AI聊天功能", Colors.RED)
    except Exception as e:
        print_colored(f"AI聊天出错: {e}", Colors.RED)
        print_colored("没关系，继续摸鱼！", Colors.YELLOW)


def main():
    """主函数"""
    # 验证口令
    if not verify_password():
        sys.exit(1)

    # 显示欢迎信息
    time_period, status = get_current_time_status()
    print_colored(f"\n⏰ {time_period} - {status}", Colors.CYAN)

    # 主循环
    while True:
        show_menu()

        try:
            choice = input(f"{Colors.BOLD}请选择 (0-6): {Colors.END}").strip()

            if choice == '1':
                tell_joke()
            elif choice == '2':
                programming_quote()
            elif choice == '3':
                moyu_quotes()
            elif choice == '4':
                moyu_statistics()
            elif choice == '5':
                generate_busy_code()
            elif choice == '6':
                chat_with_ai()
            elif choice == '0':
                print_colored("\n" + "="*50, Colors.CYAN)
                print_colored("👔 摸鱼结束，继续加油工作！", Colors.GREEN)
                print_colored("记住：劳逸结合才能高效工作！", Colors.YELLOW)
                print_colored("="*50 + "\n", Colors.CYAN)
                break
            else:
                print_colored("\n❌ 无效选择，请输入 0-6", Colors.RED)

            input(f"\n{Colors.CYAN}按回车继续...{Colors.END}")

        except KeyboardInterrupt:
            print_colored("\n\n👋 被抓住摸鱼了？赶紧溜！", Colors.YELLOW)
            break
        except Exception as e:
            print_colored(f"\n❌ 出错了: {e}", Colors.RED)


if __name__ == "__main__":
    main()
