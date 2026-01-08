import streamlit as st
from php_interpreter import MiniPHPInterpreter

st.set_page_config(page_title="Mini PHP Interpreter")

st.title("Mini PHP-like Interpreter")
st.caption("Hanya mendukung: assignment, IF–ELSE, PRINT")

code = st.text_area(
    "Masukkan Source Code PHP-like:",
    placeholder=(
        "<?php\n"
        "$num1 = 10;\n"
        "$num2 = 20;\n\n"
        "IF ($num1 > $num2) {\n"
        "    $bignum = $num1;\n"
        "    PRINT \"Big Number is \" . $bignum;\n"
        "}\n"
        "ELSE {\n"
        "    $bignum = $num2;\n"
        "    PRINT \"Big Number is \" . $bignum;\n"
        "}\n"
        "?>"
    ),
    height=300
)

if st.button("Run Interpreter"):
    if not code.strip():
        st.warning("Masukkan source code terlebih dahulu.")
    elif "IF" not in code or "PRINT" not in code:
        st.error("Source code tidak sesuai format IF–ELSE yang didukung.")
    else:
        interpreter = MiniPHPInterpreter()
        try:
            output = interpreter.execute(code)
            st.subheader("Output")
            st.text(output)
        except Exception as e:
            st.error("Terjadi error saat menjalankan interpreter.")
