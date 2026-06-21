import streamlit as st
from background import set_bg
set_bg()
st.title("Armstrong Python Code")
t1=st.slider("Enter a number",1,1000)
temp=t1
sum=0
while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
if sum==t1:
    st.success("Armstrong Number")
else:
    st.error("Not an Armstrong Number")
code='''
import streamlit as st
from background import set_bg
set_bg()
st.title("Armstrong Python Code")
t1=st.slider("Enter a number",1,1000)
temp=t1
sum=0
while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
if sum==t1:
    st.success("Armstrong Number")
else:
    st.error("Not an Armstrong Number")
'''
with st.expander("Show Python Code"):
    st.code(code, language="python")
