# 📝 Streamlit Text Elements: Displaying Information

In any AI application, how you present information is just as important as the model running behind it. Streamlit provides a variety of text elements, ranging from basic headings to advanced Markdown and mathematical rendering. 

Here is a breakdown from basic usage to advanced formatting.

## 1. The Swiss Army Knife: `st.write()`
If you only remember one text command in Streamlit, make it `st.write()`. It is incredibly smart and automatically formats whatever you pass into it. 

**Basic Example:**
```python
import streamlit as st

# It handles standard text
st.write("Welcome to my AI Dashboard.")

# It handles numbers and variables seamlessly
accuracy = 0.95
st.write("Model Accuracy:", accuracy)

# It can even automatically render dictionaries as JSON!
sample_config = {"model": "GPT-4", "temperature": 0.7}
st.write(sample_config)
```
*Note: While `st.write()` is versatile, using specific text elements (like headers or markdown) gives you more explicit control over your app's structure.*

---

## 2. Structuring Your App (Typography)
Professional apps use a clear visual hierarchy. Use these elements to structure your pages just like you would a document.

**Typography Examples:**
```python
import streamlit as st

# The main title of your app (use only once per page)
st.title("🤖 Customer Churn Predictor")

# Section headers
st.header("1. Data Preprocessing")

# Sub-sections
st.subheader("Handling Missing Values")

# Standard text
st.text("This text renders in a fixed-width, standard font. Good for simple logs.")

# Small, muted text (great for disclaimers or image credits)
st.caption("Data provided by the Open Source ML Consortium.")
```

---

## 3. Advanced Text: `st.markdown()`
When you are building AI chat interfaces or generating reports, your models will often output Markdown. `st.markdown()` allows you to render bold text, italics, lists, links, and emojis.

**Markdown Example:**
```python
import streamlit as st

st.markdown("""
### Model Summary
This model uses a **Random Forest Classifier** to predict churn. 
* It handles non-linear data well.
* It prevents overfitting using ensemble techniques.

[Read the documentation here](https://scikit-learn.org)
""")
```

### 🔥 Advanced Pro-Tip: HTML Injection
By default, Streamlit blocks custom HTML for security reasons. However, if you need custom styling (like colored text, specific fonts, or custom div blocks), you can bypass this using `unsafe_allow_html=True`.

```python
import streamlit as st

# Injecting custom CSS/HTML for a professional warning banner
custom_html = """
<div style="background-color: #ffcccc; padding: 10px; border-radius: 5px; color: #990000;">
    <strong>Warning:</strong> The model is currently loading. Please wait.
</div>
"""
st.markdown(custom_html, unsafe_allow_html=True)
```

---

## 4. Specialized AI & Developer Elements
As an AI Engineer, you will frequently need to display code snippets or mathematical formulas. Streamlit has built-in functions just for this.

**Displaying Code (`st.code`):**
This renders a beautiful code block with a built-in "Copy to Clipboard" button.
```python
import streamlit as st

code_snippet = """
def calculate_loss(y_true, y_pred):
    return mean_squared_error(y_true, y_pred)
"""
st.code(code_snippet, language='python')
```

**Displaying Math (`st.latex`):**
If you are explaining the math behind an algorithm, you can render standard LaTeX equations directly.
```python
import streamlit as st

st.write("The formula for calculating Mean Squared Error is:")
st.latex(r"MSE = \frac{1}{n} \sum_{i=1}^{n} (Y_i - \hat{Y}_i)^2")
```

---

## 🛠 Practice Exerciseo
**Task:** Build a "Model Documentation Card" using only text elements.
1. Use `st.title()` for the model's name.
2. Use `st.markdown()` to create a bulleted list of the model's strengths and weaknesses.
3. Use `st.latex()` to display a mathematical formula relevant to the model (e.g., Sigmoid function or Euclidean distance).
4. Use `st.code()` to show a 3-line example of how a user would initialize this model in Python.
5. Add a `st.caption()` at the very bottom stating "Generated on [Today's Date]".