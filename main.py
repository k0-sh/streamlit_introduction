import streamlit as st
import time
# import numpy as np
# import pandas as pd
# from PIL import Image


st.title('Streamlit 入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!'

left_column, right_column = st.columns(2)
button = left_column.button('みぎカラムに文字を表示')

if button:
    right_column.write('ここは右カラムです。')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせの回答を書く。')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ回答を書く。')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせの回答を書く。')


# text = st.text_input('あなたの趣味を教えてください。')
# conditons = st.slider('あなたの今の調子は？', 0, 100, 26)

# 'あなたの趣味は、', text, 'です。'
# 'コンディション', conditons, 'です。'


# option = st.selectbox(
#     'あなたが好きな数字は？',
#     list(range(1, 11))
# )
# 'あなたの好きな数字は、', option, 'です。'


# if st.checkbox('Show Image'):
#     img = Image.open('bicycle.png')
#     st.image(img, caption='bicycle', use_column_width=True)

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns = ['lat', 'lon']
#     ) 

# st.write(df)
# st.dataframe(df.style.highlight_max(axis=0))

# st.bar_chart(df)
# st.map(df)