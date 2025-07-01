import random

options = ["✊", "✌", "✋"]
user_score = 0
computer_score = 0
round_count = 1

print("じゃんけん！3回勝った方が勝ちです✨")

while user_score < 3 and computer_score < 3:
    print(f"\n【第{round_count}回戦】")
    user = input("✊・✌・✋ のどれかを入力：")
    computer = random.choice(options)

    print(f"あなた：{user}")
    print(f"コンピュータ：{computer}")

    if user == computer:
        print("あいこ！")
    elif (user == "✊" and computer == "✌") or \
         (user == "✌" and computer == "✋") or \
         (user == "✋" and computer == "✊"):
        print("あなたの勝ち！")
        user_score += 1
    else:
        print("あなたの負け…")
        computer_score += 1

    print(f"スコア → あなた：{user_score}勝 | コンピュータ：{computer_score}勝")
    round_count += 1

# 勝敗の表示
print("\n🎉 結果発表 🎉")
if user_score == 3:
    print("✨ あなたの勝利です！おめでとう！ ✨")
else:
    print("💻 コンピュータの勝ちです…また挑戦してね！")
