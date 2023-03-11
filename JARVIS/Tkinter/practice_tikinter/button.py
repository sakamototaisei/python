import tkinter

# ウィンドウの作成
root = tkinter.Tk()
root.title('Window practice')
root.iconbitmap('JARVIS/Tkinter/icon.ico')
root.geometry('500x800')
# サイズの変更を禁止する0 OK1 (X, Y)
root.resizable(0, 0)
root.config(bg='grey')

# ボタンの作成
button_1 = tkinter.Button(root, text='ボタン1')
# 二次元配列では所を指定可能
button_1.grid(row=0, column=0)

button_2 = tkinter.Button(root, text='ボタン2')
button_2.grid(row=0, column=1)

button_3 = tkinter.Button(root, text='ボタン3', bg='pink',
                          activebackground='yellow')
button_3.grid(row=1, column=2, padx=10, pady=10, ipadx=10, ipady=10)

button_4 = tkinter.Button(root, text='ボタン4', borderwidth=5)
button_4.grid(row=1, column=0, columnspan=3, sticky='WE')

button_5 = tkinter.Button(root, text='テスト')
button_6 = tkinter.Button(root, text='テスト')
button_7 = tkinter.Button(root, text='テスト')
button_8 = tkinter.Button(root, text='テスト')
button_9 = tkinter.Button(root, text='テスト')
button_10 = tkinter.Button(root, text='テスト')

button_5.grid(row=2, column=0, padx=5, pady=5)
button_6.grid(row=2, column=1, padx=5, pady=5)
button_7.grid(row=2, column=2, padx=5, pady=5, sticky='w')
button_8.grid(row=3, column=0, padx=5, pady=5)
button_9.grid(row=3, column=1, padx=5, pady=5)
button_10.grid(row=3, column=2, padx=5, pady=5, sticky='w')


# ウィンドウのループ処理
root.mainloop()
