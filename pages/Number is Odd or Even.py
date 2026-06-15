import streamlit as st
st.title("Odd_Even python code")
t1=st.slider("Select a number",1,1000)
if t1%2==0:
    st.success("Number is Even")
else:
    st.success("Number is Odd")
st.subheader("Python Code")
code='''
import streamlit as st
st.title("Odd_Even python code")
t1=st.slider("Select a number",1,1000)
if t1%2==0:
    st.success("Number is Even")
else:
    st.success("Number is Odd")'''
st.code(code)
