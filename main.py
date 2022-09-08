from xml.sax.handler import DTDHandler
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('DataFrame')

'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!'    

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ１')
expander1.write('問い合わせ１の回答')
expander2 = st.expander('問い合わせ２')
expander2.write('問い合わせ２の回答')
expander3 = st.expander('問い合わせ３')
expander3.write('問い合わせ３の回答')

# if st.checkbox('Show Image'):
#     img =Image.open('ap.jpg')
#     st.image(img, caption='airplane', use_column_width=True)

# text = st.text_input('あなたの趣味を教えてください。')
# 'あなたの趣味：', text

# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション：', condition


# option = st.selectbox(
#     'あなたが好きな県を教えて下さい、',
#     ['愛知', '岐阜', '三重', '静岡', '長野']
# )

# 'あなたの好きな数字は、', option, 'です。'


# df = pd.DataFrame({
#     # '1列目':[927, 9891, 33436, 47912, 90214, 110711, 171882, 230704, 293689, 321419, 520042, 581376, 752079,
#     # 197774, 158264, 752349, 481989, 217013, 284753, 625945, 863108, 672677]
#     '1列目':[2928, 2815, 3580, 2164, 1527, 1966, 1617, 2098, 1127, 297, 764, 827, 287, 977]
# })
# st.write(df)

# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )

# df = pd.DataFrame(
#     np.random.rand(50, 2)/[10, 10] + [35.12, 136.83],
#     columns=['lat', 'lon']
# )
# st.map(df)

# df = pd.DataFrame(
#     np.random.rand(1, 1)*[0, 0] + [35.17, 136.882],
#     columns=['lat', 'lon']
# )

# df = pd.DataFrame(
#     [35.69, 139.70]
#     # columns=['lat', 'lon']
# )

# st.write(df)
# st.dataframe(df.style.highlight_max(axis=0))
# st.table(df.style.highlight_max(axis=0))

# st.line_chart(df)
# st.bar_chart(df)