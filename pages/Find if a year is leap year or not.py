import streamlit as st
from background import set_bg
set_bg()
st.title("Leap Year Python Code")
t1=st.slider("Enter a Year",1,5000)
if t1%400==0:
    st.success("This year is a Leap Year")
elif t1%4==0:
    st.success("This Year is a Leap Year")
elif t1%100==0:
    st.error("This Year is not a Leap Year")
else:
    st.error("This Year is not a Leap Year")
code='''
import streamlit as st
from background import set_bg
set_bg()
st.title("Leap Year Python Code")
t1=st.slider("Enter a Year",1,5000)
if t1%400==0:
    st.success("This year is a Leap Year")
elif t1%4==0:
    st.success("This Year is a Leap Year")
elif t1%100==0:
    st.error("This Year is not a Leap Year")
else:
    st.error("This Year is not a Leap Year")
'''
with st.expander("Show Python Code"):
    st.code(code, language="python")
