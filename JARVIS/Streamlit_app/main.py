from PIL import *
import streamlit as st
import numpy as np
import pandas as pd
import time


st.title('Streamlit 超入門')
st.write('DataFrame')

# プログレスバー
# st.write('プログレスバーの表示')
# 'Start'
# latest_iteration = st.empty()
# bar = st.progress(0)
# for i in range(100):
#     latest_iteration.text(f'Iteration {i + 1}')
#     bar.progress(i + 1)
#     time.sleep(0.1)
# 'Done!!'

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})
df1 = pd.DataFrame(np.random.rand(20, 3), columns=['a', 'b', 'c'])
# 折れ線グラフの表示
st.line_chart(df1)

# 表の表示
st.write(df)
st.dataframe(df.style.highlight_max(axis=0), width=400, height=200)

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

# 新宿付近のマップの表示
df2 = pd.DataFrame(np.random.rand(100, 2) /
                   [50, 50] + [35.69, 139.70], columns=['lat', 'lon'])
if st.checkbox('show map'):
    st.map(df2)

# 画像の表示
if st.checkbox('show image'):
    st.write('display image')
    img = Image.open('JARVIS/Streamlit_app/jastina.jpeg')
    st.image(img, caption='jastina', use_column_width=True)

# セレクトボックス
option = st.selectbox(
    'あなたの好きな数字を教えてください',
    list(range(1, 11))
)
'あなたの好きな数字は、', option, 'です。'

# テキスト入力欄
st.write('interactive widgets')
text = st.text_input('あなたの趣味はなんですが?')
'あなたの趣味：', text

# スライダー
condition = st.slider('あなたの今の調子は?', 0, 100, 50)
'コンディション：', condition

# カラム作成
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右のカラムです')

# エクスパンダー
expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせの2回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせの3回答')
