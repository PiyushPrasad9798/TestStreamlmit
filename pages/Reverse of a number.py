import streamlit as st
from background import set_bg
set_bg()
st.title("Reverse Python Code")
t1=st.slider("Enter a Number",1,10000)
temp=t1
rev=0
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10
st.success(f"Reverse Number = {rev}")
code='''
import streamlit as st
from background import set_bg
set_bg()
st.title("Reverse Python Code")
t1=st.slider("Enter a Number",1,10000)
temp=t1
rev=0
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10
st.success(f"Reverse Number = {rev}")
'''
with st.expander("Show Python Code"):
    st.code(code, language="python")
