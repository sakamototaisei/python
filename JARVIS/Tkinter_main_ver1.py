import tkinter


class Application(tkinter.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=750, height=550, borderwidth=1, relief='groove')
        self.root = root
        self.pack()
        self.pack_propagate(0)
        self.create_widgets()

    def create_widgets(self):
        # 閉じるボタン
        quit_btn = tkinter.Button(self)
        quit_btn['text'] = '終了する'
        quit_btn['command'] = self.root.destroy
        quit_btn.pack(side='bottom')

        # 指示ボタン
        button = tkinter.Button(
            self, text='ご用件', command=self.jarvis_first_command)
        button.pack()

        # テキストボックス
        self.text_box = tkinter.Entry(self, width=30)
        self.text_box.pack()

        # 実行ボタン
        submit_btn = tkinter.Button(self)
        submit_btn['text'] = '実行'
        submit_btn['command'] = self.input_handler
        submit_btn.pack()

        # メッセージの出力
        self.message = tkinter.Message(self, width=300)
        self.message.pack()

        # チェックボタン
        self.is_student = tkinter.BooleanVar()  # チェックされているのか知るためのオブジェクト
        chk_btn = tkinter.Checkbutton(
            self, text='ゲーム', variable=self.is_student)
        chk_btn.pack()

        # ラジオボタン
        self.selected_radio = tkinter.StringVar()
        radio_1 = tkinter.Radiobutton(
            self, text='ゲーム', value=1, variable=self.selected_radio)
        radio_2 = tkinter.Radiobutton(
            self, text='株価分析', value=2, variable=self.selected_radio)
        radio_3 = tkinter.Radiobutton(
            self, text='Gmail送信', value=3, variable=self.selected_radio)
        radio_4 = tkinter.Radiobutton(
            self, text='QR発行', value=4, variable=self.selected_radio)
        radio_1.pack()
        radio_2.pack()
        radio_3.pack()
        radio_4.pack()

        # メニューボタン
        menu = tkinter.Menu(self.root)
        # メニューをアプリから切り離す設定をoffにしておく
        menu1 = tkinter.Menu(menu, tearoff=False)
        menu1.add_command(label='画面設定', command=self.screen_setting)
        menu1.add_command(label='音量設定', command=self.volume_setting)
        menu.add_cascade(label='設定', menu=menu1)
        self.root.config(menu=menu)

    def input_handler(self):
        # 入力された値を取得する
        text = self.text_box.get()
        if text not in ' ':
            print(f'入力された値：{text}')
            self.message['text'] = text
        else:
            text = '未入力'
            self.message['text'] = text
        # チェックボックス判定
        print(f'チェックボックス判定:{self.is_student.get()}')
        # ラジオボタン判定
        radio = self.selected_radio.get()
        if radio not in ' ':
            print(f'ラジオボタン判定:{radio}')
        print('-'*50)

    def jarvis_first_command(self):
        print('ご用件を承りました')
        print('-'*50)

    def screen_setting(self):
        print('画面設定が押されました')
        print('-'*50)

    def volume_setting(self):
        print('音量設定が押されました')
        print('-'*50)


root = tkinter.Tk()
root.title('JARVIS')
root.geometry('800x600')
app = Application(root=root)
app.mainloop()  # アプリの起動
