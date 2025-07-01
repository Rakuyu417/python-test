todo_list = []

while True:
    task = input("やることを入力してください（終了するには 'exit' と入力）：")
    if task.lower() == "exit":
        break
    todo_list.append(task)

print("\nあなたのToDoリスト：")
for i, task in enumerate(todo_list, start=1):
    print(f"{i}. {task}")
    
todo_list = []  # 各項目を「(タスク名, 完了済みかどうか)」のタプルで管理

while True:
    print("\n--- ToDoメニュー ---")
    print("1. やることを追加")
    print("2. 完了した項目をチェック")
    print("3. ToDoリストを表示")
    print("4. 終了")
    
    choice = input("番号を選んでください：")

    if choice == "1":
        task = input("やることを入力してください：")
        todo_list.append((task, False))  # 完了フラグFalseで追加

    elif choice == "2":
        for i, (task, done) in enumerate(todo_list, start=1):
            status = "✓" if done else " "
            print(f"{i}. [{status}] {task}")
        done_num = input("完了した項目の番号を入力（複数可、カンマ区切り / スキップ可）：")
        if done_num:
            indexes = [int(x.strip()) - 1 for x in done_num.split(",") if x.strip().isdigit()]
            for idx in indexes:
                if 0 <= idx < len(todo_list):
                    todo_list[idx] = (todo_list[idx][0], True)  # 完了フラグTrueにする

    elif choice == "3":
        print("\n📋 あなたのToDoリスト：")
        for i, (task, done) in enumerate(todo_list, start=1):
            status = "✓" if done else " "
            print(f"{i}. [{status}] {task}")

    elif choice == "4":
        print("終了します。お疲れさまでした！")
        break

    else:
        print("無効な入力です。もう一度お試しください。")
