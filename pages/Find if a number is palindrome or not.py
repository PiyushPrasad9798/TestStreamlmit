import streamlit as st
from background import set_bg
set_bg()
st.title("Palindrome Python Code")
t1=st.slider("Select a Number",1,1000)
temp=t1
rev=0
while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10
if rev==t1:
    st.success("Number is palindrome")
else:
    st.error("Number is not palindrome")
code='''
import streamlit as st
from background import set_bg
set_bg()
st.title("Palindrome Python Code")
t1=st.slider("Select a Number",1,1000)
temp=t1
rev=0
while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10
if rev==t1:
    st.success("Number is palindrome")
else:
    st.error("Number is not palindrome")'''
with st.expander("Show Python Code"):
    st.code(code, language="python")
