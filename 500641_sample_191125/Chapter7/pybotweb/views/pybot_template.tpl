<html>
<body>
<h1>pybot Webアプリケーション</h1>
<form method="post" action="/hello" enctype="multipart/form-data">
メッセージを入力してください: <input type="text" name="input_text"><br>
画像を選択してください: <input type="file" name="input_image"><br>
<input type="submit" value="送信">
</form>
<ul>
<li>入力されたメッセージ: {{input_text}}</li>
<li>pybotからの応答メッセージ: {{!output_text}}</li>
</ul>
</body>
</html>
