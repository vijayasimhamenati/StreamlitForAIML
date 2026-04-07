import streamlit as st

#title 
st.title("Streamlit ~~Fundamentals~~ Basics")

# Header 
st.header("This is Header")

# Sub Header
st.subheader("This is a Sub header")

# Markdown
st.markdown("""✅ How to **run** the Streamlit application :

```
cd 02_Fundamentals

py -m streamlit run 01_text_elements.py
```

""")

# caption
st.caption("This is a caption")

#code 
st.code("""import pandas as pd
pd.read_csv("path")
""")

# preformated text
st.text("Sample Text sample")

# LaTex
st.latex("y= z^2")

# divider

st.divider()

# write
st.write("Anything")


