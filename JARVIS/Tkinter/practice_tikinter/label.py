import tkinter
import tkinter.font as font


root = tkinter.Tk()
root.title('label practice')
root.geometry('500x500')
root.resizable(0, 0)
root.config(bg='red')

# ラベルの作成
label_1 = tkinter.Label(root, text='よろしくお願いいたします')
# ウィンドウ上に設置
label_1.pack()

label_2 = tkinter.Label(root, text='よろしくお願いいたします', font=('Arial', 10, 'bold'))
label_2.pack()

label_3 = tkinter.Label(root, text='よろしくお願いいたします',
                        font=('Arial', 10, 'bold'), bg='gray')
label_3.pack(padx=10, pady=10)

label_4 = tkinter.Label(root, text='よろしくお願いいたします', font=(
    'Arial', 10, 'bold'), bg='gray', fg='green')
"""
pad:外側空白
ipad:内側空白
"""
label_4.pack(padx=10, pady=(0, 10), ipadx=50, ipady=20, anchor='w')

label_5 = tkinter.Label(root, text='よろしくお願いいたします',
                        font=('Arial', 10, 'bold'), bg='gray')
label_5.pack(padx=10, pady=(0, 10), fill='x')

# label_6 = tkinter.Label(root, text='よろしくお願いいたします',
#                         font=('Arial', 10, 'bold'), bg='gray')
# label_6.pack(padx=10, pady=(0, 10), fill='y', expand=True)

label_7 = tkinter.Label(root, text='よろしくお願いいたします',
                        font=('Arial', 10, 'bold'), bg='gray')
label_7.pack(padx=10, pady=(0, 10), fill='both', expand=True)

# 使用できるフォントを確認
# print(font.families())


root.mainloop()
