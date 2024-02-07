#Example3
import streamlit as st
import streamlit.components.v1 as components

def sumProduct(list1, list2):
    return sum(map(lambda x, y: x * y, list1, list2))

st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;} </style>', unsafe_allow_html=True)

answer = []
score = [25,50,100]
chose = st.radio('第一題', ("0", "1"))
answer.append(int(chose))
chose = st.radio('第二題', ("0", "1"))
answer.append(int(chose))
chose = st.radio('第三題', ("0", "1"))
answer.append(int(chose))
st.write(f"Answer: {answer}")
finalscore = sumProduct(answer, score)
st.write(f"final: {finalscore}")
