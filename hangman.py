def hungman(word):
    wrong=0
    stages =["",
             "_____________            ",
             "|                        ",
             "|            |           ",
             "|            o           ",
             "|           /|\          ",
             "|           / \          ",
             "|                        "
            ]
    rletters = list(word)#答えをリスト化
    board = ["_"]* len (word)
    win = False#最後の if not winのために設定
    print("ハングマンへようこそ！")


    while wrong < len(stages) -1:
        print("\n")#改行
        msg ="1文字を予想してね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char#boardのcind番目がcharに変換する
            rletters[cind]= '$'#すでに入力した正解値を＄として見なし、同じ値を入力しても同じだと認識しないようにする。例：dogが答えで入力したoがもう正解と見做さないように$とみなすようにする
        else:
            wrong += 1
        print(" ".join(board))#見やすいように_の間にスペースが入る
        e= wrong +1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board)) 
            win = True
            break
        if not win:#if ():()がtrueだったら下のコマンドが実行される、今回の場合はnot winが（）の部分にあたる
            print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は{}.".format(word))

hungman("dog")