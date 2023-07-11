import streamlit as st

st.title("Calculator ")

col1, col2, col3 = st.columns(3)
with col1:
    x = st.number_input('Enter first number')

with col2:
    y = st.number_input('Enter second number')

with col3:
    m = st.selectbox('Select  operation', ['+', '-', '*', '%'])


if st.button('calculate'):
    if (m == '+'):
        st.write("The Calculated value is ", x+y)
    elif (m == '-'):
        st.write("The Calculated value is ", x-y)
    elif (m == '*'):
        st.write("The Calculated value is ", x*y)
    elif (m == '%'):
        st.write("The Calculated value is ", x % y)
