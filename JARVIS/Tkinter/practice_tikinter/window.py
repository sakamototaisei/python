import tkinter


# ウィンドウの作成
root = tkinter.Tk()
root.title('Window practice')
root.iconbitmap('JARVIS/Tkinter/icon.ico')
root.geometry('500x800')
# サイズの変更を禁止する0 OK1 (X, Y)
root.resizable(0, 0)
root.config(bg='grey')

# サブウィンドウの作成
sub_window1 = tkinter.Toplevel()
# カラーコードでの色指定可能
sub_window1.config(bg='#123123')
# 表示位置を指定
sub_window1.geometry('200x800+500+0')

# サブウィンドウは複数作成可能
sub_window2 = tkinter.Toplevel()
sub_window2.geometry('300x800+700+0')
sub_window2.config(bg='blue')

sub_window3 = tkinter.Toplevel()
sub_window3.geometry('440x800+1000+0')
sub_window3.config(bg='black')

"""
ちょうど良いサイズ
縦800
横1440
メインウィンドウを閉じるとサブウィンドウも閉じる
"""

# ウィンドウのループ処理
root.mainloop()