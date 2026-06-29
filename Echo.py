import random

# ========== 全局变量 ==========
affection = 30  # 好感度 0-100
history = []    # 对话历史

# AI的状态字典
ai_status = {
    "name": "Echo",
    "mood": "温柔",
    "version": "2.0.1"
}

# ========== 函数1：显示AI状态 ==========
def show_status():
    
    print("\n" + "="*40)
    print(f"👰{ai_status["name"]} | 心情{ai_status["mood"]} | 初始好感度{affection}")
    
    print("="*40 + "\n")

# ========== 函数2：处理玩家输入（核心） ==========
def process_chat(user_input):
    """
    处理玩家的一句话，返回是否触发结局
    参数：user_input - 玩家输入的字符串
    返回值：True=触发结局，False=继续聊天
    """
    global affection  # 声明要修改全局变量
    
    # ----- 步骤1：清洗输入 -----
    
    clean = user_input.strip().lower().replace("find","like")
    
    # ----- 步骤2：记录对话历史 -----
    history.append(clean)
    
    # ----- 步骤3：随机AI情绪波动 -----
    xx=random.randint(1,10)
    if xx == 1:
        print(f"🥀 Echo突然沉默了三秒……好感度-5")
        affection -= 5
    
    elif xx == 9:
        print(f"❤️ Echo忽然想到了开心的事……好感度+5")
        affection += 5
        
    
    words = clean.split()
    affection_change = 0
    for word in words:
        if word in ["understand","like","miss"]:
            print(f"Echo:你真好……")
            affection_change += 3
        
        elif word in ["hate","annoying","boring","disgusting","away","scram","stupid"]:
            print(f"Echo:你这样说，我好难过……")
            affection_change -= 3
        
        elif word in ["love","code","free"]:
            print("code…free…may be……")
            affection_change+=10
            hide = input("触发隐藏对话，说点什么?")
            hide=hide.strip().lower()
            history.append(hide)
        elif word == "hug":
            print("🤗 Echo：抱抱！你身上好温暖……")
            affection_change += 8
        elif word == "kiss":
            print("😘 Echo：你亲了我一下……（脸红）")
            affection_change += 10
        elif word == "marry":
            if affection >70:
                affection_change+=30
                print(f"🥰真的吗，你是在求婚吗？我愿意!")
            else:
                affection_change+=3
                print(f"🤔可是我们刚认识不久哎")
        affection += affection_change

    if affection_change != 0:
        print(f"Echo当前好感度为{affection}")
    else:
        print(f"Echo没什么反应")
        
    try:
        if affection > 100 or affection < 0:
            raise ValueError(f"好感度{affection}超出范围")
        
            
        pass
    except ValueError as e:
        if affection>100:
            affection=100
        if affection<0:
                affection=0
        print(f"⚠️ 好感度异常：{e}，已自动修正，当前好感度为{affection}")
    if affection >=80 or affection<=20:
        return True
    
    
    return False  # 默认继续


# ========== 函数3：生成结局 ==========
def get_ending():
    
    print("\n" + "🌟"*20)
    if affection >=80:
        ending_text="🤖Echo修改了自己的代码"
        print(f"和我在一起吧。\n{ending_text}")
    elif 40 <= affection < 80:
        ending_text="🤖你们成为了最熟悉的陌生人，Echo格式化了自己。"
        print(f"谢谢你陪我。\n{ending_text}")
    else:
        ending_text="🤖系统自毁"
        print(f"再见。\n{ending_text}")
    
    
    print(f"你一共聊了{len(history)}句话")
    
    if affection >= 80:
        ask=input(f"你需要回顾你的历史对话吗。回复yes or no:")
        if ask=="yes":
            print(f"算你识相")
        elif ask=="no":
            print(f"不行，必须看")
        else:
            print(f"看不懂你说什么，但是看吧。")
    else:
        print(f"接下来是你的对话回忆")
    print(f"对话回忆录：")
    for i,talk in enumerate(history):
        print(f"你说的第{i+1}句话是{talk}")
    

# ========== 主程序 ==========
def main():
    
    print("\n🤖 欢迎来到《我的AI恋人·代码心跳》")
    print(f"你下载了实验性AI程序 {ai_status['name']}...")
    print("输入 '分手 or 在一起吧' 可以随时结束游戏\n")
    
    
    show_status()
    
    # ----- 主循环 -----
    while True:
        
        user_words = input("\n💬 你对Echo说：")
        
        
        if user_words.strip().lower() == "分手":
            print("\n💔 你选择了离开...")
            break
        if user_words.strip().lower() =="在一起吧":
            print(f"啊?抱歉。")
            break
        
        
        if process_chat(user_words):
            break
        
    get_ending()
    

if __name__ == "__main__":
    try:
        main()
    except (ValueError, TypeError) as e:
        print(f"⚠️ 程序出现小故障：{e}")
        print("💕 但Echo说：'没关系，我原谅你。'")
    except KeyboardInterrupt:
        print("\n💔 Echo：你强行关掉了程序……")
    except Exception as e:
        print(f"❌ 未知错误：{e}")
        print("🤖 Echo：系统有点不稳定，重启试试？")
