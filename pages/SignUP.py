import streamlit as st
import mysql.connector
conn=mysql.connector.connect(host="127.0.0.1",user="root",database="streamlit_test",passwd="")
my=conn.cursor()
from background import set_bg
set_bg()
st.title("📝 Sign Up 💻")
t1=st.text_input("🙋‍♂️ Username")
t2=st.text_input("🔑 Password",type="password")
t3=st.text_input("📞 Mobile Number")
t4=st.text_input("📩 Email Id")
t5=st.date_input("🐣 DOB")
b1=st.button("SIGNUP")
if b1:
       my.execute("insert into user_info values("+"'"+t1+"'"+","+"'"+t2+"'"+","+"'"+t3+"'"+","+"'"+t4+"'"+","+"'"+str(t5)+"'"+")")
       conn.commit()
       st.success("✅ Sign Up Successfull")
code='''
import streamlit as st
import mysql.connector
conn=mysql.connector.connect(host="127.0.0.1",user="root",database="streamlit_test",passwd="")
my=conn.cursor()
from background import set_bg
set_bg()
st.title("Sign Up")
t1=st.text_input("Username")
t2=st.text_input("Password",type="password")
t3=st.text_input("Mobile Number")
t4=st.text_input("Email Id")
t5=st.date_input("DOB")
b1=st.button("SIGNUP")
if b1:
       my.execute("insert into user_info values("+"'"+t1+"'"+","+"'"+t2+"'"+","+"'"+t3+"'"+","+"'"+t4+"'"+","+"'"+str(t5)+"'"+")")
       conn.commit()
       st.success("Sign Up Successfully")
'''
with st.expander("Show Python Code"):
    st.code(code, language="python")
