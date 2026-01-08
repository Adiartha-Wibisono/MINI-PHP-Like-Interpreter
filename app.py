import streamlit as st
from php_interpreter import MiniPHPInterpreter

st.set_page_config(page_title="Mini PHP Interpreter")

st.title("Mini PHP Interpreter (IF – ELSE)")
st.write("Simple Conditional IF with Block")

default_code = """<?php
$num1 = 10;
$num2 = 20;

IF ($num1 > $num2) {
    $bignum = $num1;
    PRINT "Big Number is " . $bignum;
}
ELSE {
    $bignum = $num2;
    PRINT "Big Number is " . $bignum;
}
?>"""

code = st.text_area("Input PHP-like Code", default_code, height=250)

if st.button("Run"):
    interpreter = MiniPHPInterpreter()
    output = interpreter.execute(code)
    st.subheader("Output")
    st.text(output)
