import random

options = ["グー", "チョキ", "パー"]
print("じゃんけんしよう！")

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
else:
    print("あなたの負け…")
