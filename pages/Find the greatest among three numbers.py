import streamlit as st
st.title("Find the greatest among two numbers")
t1 = st.number_input("Enter First Number")
t2 = st.number_input("Enter Second Number")
t3 = st.number_input("Enter Third Number")
if t1 > t2 and t1>t3:
    st.success(f"{t1} is greater")
elif t2>t1 and t2>t3:
    st.success(f"{t2} is greater")
else:
    st.success(f"{t3} is greater")
st.subheader("Python Code")
code='''
import streamlit as st
st.title("Find the greatest among two numbers")
t1 = st.number_input("Enter First Number")
t2 = st.number_input("Enter Second Number")
t3 = st.number_input("Enter Third Number")
if t1 > t2 and t1>t3:
    st.success(f"{t1} is greater")
elif t2>t1 and t2>t3:
    st.success(f"{t2} is greater")
else:
    st.success(f"{t3} is greater")
'''
st.code(code)
