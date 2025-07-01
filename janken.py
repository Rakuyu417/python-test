import random

options = ["グー", "チョキ", "パー"]
user_score = 0
computer_score = 0

print("じゃんけん3回勝負、スタート！")

for round in range(1, 4):
    print(f"\n【第{round}回戦】")
    user = input("グー・チョキ・パー のどれかを入力：")
    computer = random.choice(options)

    print(f"あなた：{user}")
    print(f"コンピュータ：{computer}")

    if user == computer:
        print("あいこ！")
    elif (user == "グー" and computer == "チョキ") or \
         (user == "チョキ" and computer == "パー") or \
         (user == "パー" and computer == "グー"):
        print("あなたの勝ち！")
        user_score += 1
    else:
        print("あなたの負け…")
        computer_score += 1

# 最終結果の表示
print("\n🎉 結果発表 🎉")
print(f"あなたの勝ち数：{user_score}")
print(f"コンピュータの勝ち数：{computer_score}")

if user_score > computer_score:
    print("✨ あなたの勝利です！ ✨")
elif user_score < computer_score:
    print("💻 コンピュータの勝ちです…")
else:
    print("🤝 引き分けです！")
