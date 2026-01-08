import streamlit as st
from php_interpreter import MiniPHPInterpreter

st.set_page_config(page_title="Mini PHP-like Interpreter", layout="centered")

st.title("Mini PHP-like Interpreter")
st.caption("Mendukung: assignment, IF–ELSE, PRINT")

st.markdown("### Input Source Code")

code = st.text_area(
    "",
    height=260,
    help="Gunakan format IF–ELSE PHP-like sesuai spesifikasi tugas"
)

st.markdown("### Output")

if st.button("Run Interpreter"):
    if not code.strip():
        st.info("Silakan masukkan source code terlebih dahulu.")
    else:
        try:
            interpreter = MiniPHPInterpreter()
            output = interpreter.execute(code)
            if output.strip():
                st.success(output)
            else:
                st.warning("Program tidak menghasilkan output.")
        except Exception:
            st.error("Source code tidak sesuai dengan grammar yang didukung.")
