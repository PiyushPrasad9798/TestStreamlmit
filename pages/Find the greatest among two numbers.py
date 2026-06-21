import streamlit as st
from background import set_bg
set_bg()
st.title("Find the greatest among two numbers")
t1 = st.number_input("Enter First Number")
t2 = st.number_input("Enter Second Number")
if t1 > t2:
    st.success(f"{t1} is greater")
else:
    st.success(f"{t2} is greater")
st.subheader("Python Code")
code='''
import streamlit as st
from background import set_bg
set_bg()
st.title("Find the greatest among two numbers")
t1 = st.number_input("Enter First Number")
t2 = st.number_input("Enter Second Number")
if t1 > t2:
    st.success(f"{t1} is greater")
else:
    st.success(f"{t2} is greater")
st.subheader("Python Code")'''
with st.expander("Show Python Code"):
    st.code(code, language="python")
