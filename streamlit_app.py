import re

import streamlit as st

st.title("🛠️ Tranquilpeak helper")

st.write("markdown to Tranquilpeak 主题的小工具。")


input_text = st.text_area(label="请输入你的 markdown")
submit = st.button(label="转换")

if submit:
    output_text = re.sub(
        r"!\[(.*)\]\((.*)\)", r'{% image fancybox center \g<2> "\g<1>" %}', input_text
    )
    st.code(output_text, language="markdown")
