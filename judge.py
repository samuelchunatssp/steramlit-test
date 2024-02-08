#Example3
import streamlit as st
import streamlit.components.v1 as components

def sumProduct(list1, list2):
    return sum(map(lambda x, y: x * y, list1, list2))

st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;} </style>', unsafe_allow_html=True)

answer = []
score = [25,50,100]
for i in range(len(score)):
    chose = st.radio('Question'+str(i+1)+':'+score[i], ("0", "1"))
    answer.append(int(chose))
st.write(f"Answer: {answer}")
finalscore = sumProduct(answer, score)
st.write(f"final: {finalscore}")
