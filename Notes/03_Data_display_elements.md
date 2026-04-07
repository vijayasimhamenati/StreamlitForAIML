# 📊 Streamlit Data Display Elements

When building an AI or Data Science dashboard, how you present the data determines how useful the app is. Streamlit offers different elements tailored for different types of data: from massive interactive datasets to quick, high-level metrics.

## 1. The Interactive Table: `st.dataframe()`
This is the workhorse for displaying tabular data. It renders a Pandas DataFrame (or PyArrow table) as an interactive UI element where users can sort, resize, and scroll.

**Basic Usage:**
```python
import streamlit as st
import pandas as pd

st.header("1. Interactive DataFrames")

# Dummy dataset
df = pd.DataFrame({
    'Model': ['Random Forest', 'XGBoost', 'Neural Network'],
    'Accuracy': [0.85, 0.92, 0.89],
    'Training Time (s)': [12, 45, 120]
})

# Display as an interactive table
st.dataframe(df)
```

**🔥 Advanced: Column Configuration & Styling**
You don't just have to show raw text. Streamlit allows you to format columns into progress bars, charts, or formatted numbers directly inside the dataframe.

```python
import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'Model': ['Random Forest', 'XGBoost', 'Neural Network'],
    'Accuracy': [0.85, 0.92, 0.89]
})

st.subheader("Styled DataFrame")

# Using Pandas Styler to highlight the highest accuracy
st.dataframe(df.style.highlight_max(subset=['Accuracy'], color='lightgreen'))

st.subheader("Column Configuration")
# Using Streamlit's native column config for professional formatting
st.dataframe(
    df,
    column_config={
        "Accuracy": st.column_config.NumberColumn(
            "Model Accuracy",
            help="The accuracy score on the holdout test set.",
            format="%.2f",
        ),
    },
    hide_index=True # Hides the default 0, 1, 2 row numbers
)
```

---

## 2. The Static Table: `st.table()`
While `st.dataframe()` is interactive, sometimes you just want a clean, static table that shows all its data at once without scrollbars. `st.table()` is perfect for small summaries or parameter lists.

*Warning: Do not use `st.table()` for large datasets, as it will render the entire thing on the screen and freeze the browser.*

**Example:**
```python
import streamlit as st
import pandas as pd

# Hyperparameters for an AI model
params = pd.DataFrame({
    'Parameter': ['Learning Rate', 'Batch Size', 'Epochs'],
    'Value': [0.001, 32, 100]
})

st.header("2. Static Summary Table")
st.table(params)
```

---

## 3. High-Level KPIs: `st.metric()`
When a user opens an AI dashboard, they usually want to see the most important numbers first. `st.metric()` creates beautiful KPI (Key Performance Indicator) cards, complete with "delta" arrows showing changes.

**Example: Displaying Model Performance**
```python
import streamlit as st

st.header("3. Metric Cards")

# Use columns to place metrics side-by-side
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Current Accuracy", value="92%", delta="4%")

with col2:
    st.metric(label="Training Loss", value="0.14", delta="-0.05", delta_color="inverse") 
    # delta_color="inverse" makes a negative drop green (good for loss!)

with col3:
    st.metric(label="API Requests", value="1,204", delta="120", delta_color="normal")
```

---

## 4. Viewing Raw Structures: `st.json()` and `st.write()`
If you are working with Large Language Models (LLMs) or complex APIs, you frequently deal with nested JSON data or Python dictionaries. Streamlit can render these natively as collapsible trees.

**Example: Displaying an API Payload**
```python
import streamlit as st

st.header("4. JSON and Dictionaries")

llm_response = {
    "id": "chatcmpl-123",
    "object": "chat.completion",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "The capital of France is Paris."
            },
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 12,
        "completion_tokens": 7,
        "total_tokens": 19
    }
}

# Renders an interactive, collapsible JSON viewer
st.json(llm_response, expanded=False) 
```

---

## 🛠 Practice Exercise for Your Repo
**Task:** Build a "Model Evaluation Dashboard".
1. Create a dictionary representing the evaluation metrics of 3 different models (e.g., Model A, Model B, Model C).
2. Convert that dictionary into a Pandas DataFrame.
3. Use `st.columns()` to display three `st.metric()` cards showing the top model's stats at the top of the page.
4. Below the metrics, display the full DataFrame using `st.dataframe()`, and ensure the index is hidden.
5. Create an expandable section using `st.expander("View Raw Config")` and use `st.json()` inside it to show the hyperparameter configuration used for the top model.