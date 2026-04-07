Here are the notes for **Chart Elements and Custom Charts in Streamlit**, structured perfectly for your GitHub repository. 

Visualizing data is arguably the most important part of an AI Engineering dashboard. Whether you are performing Exploratory Data Analysis (EDA) or plotting the loss curve of a neural network, Streamlit makes it seamless.

***

# 📈 Streamlit Chart Elements: Visualizing AI Data

In AI and Data Science, numbers alone are rarely enough. You need to visualize distributions, relationships, and model performance. Streamlit offers two main ways to plot data: 
1. **Native Charts** (Quick and easy).
2. **Custom Third-Party Charts** (Powerful and highly interactive).

## 1. Native Streamlit Charts (The Basics)
Streamlit provides built-in charting functions that are wrappers around the Altair library. They are incredibly easy to use and require zero configuration—just pass in a Pandas DataFrame or a Python dictionary.

**Basic Examples:**
```python
import streamlit as st
import pandas as pd
import numpy as np

st.header("1. Native Streamlit Charts")

# Generate some dummy data for a time series
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Model A Loss', 'Model B Loss', 'Baseline Loss']
)

# Line Chart (Great for training curves over time)
st.subheader("Line Chart")
st.line_chart(chart_data)

# Bar Chart (Great for comparing categorical metrics)
st.subheader("Bar Chart")
st.bar_chart(chart_data)

# Scatter Chart (Great for visualizing clusters or outliers)
st.subheader("Scatter Chart")
scatter_data = pd.DataFrame(
    np.random.randn(50, 2),
    columns=["Feature X", "Feature Y"]
)
st.scatter_chart(scatter_data)
```

**Pros:** One line of code. Automatically handles resizing and tooltips.
**Cons:** Limited customization. You cannot easily change axes labels, colors, or add complex annotations.

---

## 2. Matplotlib & Seaborn (The ML Classics)
As an AI Engineer, much of your existing code (or code you find online) will use Matplotlib or Seaborn. Streamlit can render these static plots perfectly using `st.pyplot()`.

**Example: Rendering a Seaborn Heatmap**
```python
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.header("2. Matplotlib & Seaborn Integration")

# Generate a correlation matrix (common in ML feature engineering)
data = np.random.rand(5, 5)
corr_matrix = np.corrcoef(data)

# Create the Matplotlib Figure and Axes explicitly
fig, ax = plt.subplots(figsize=(6, 4))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=ax)
ax.set_title("Feature Correlation Heatmap")

# Pass the 'fig' object to Streamlit
st.pyplot(fig)
```
*🔥 Pro-Tip: Always create explicit `fig, ax` objects when using Matplotlib in Streamlit. Relying on the global `plt` state can cause overlapping charts if multiple users access your app simultaneously.*

---

## 3. Plotly (The Industry Standard for Interactivity)
For modern AI dashboards, **Plotly** is the gold standard. It creates highly interactive charts where users can zoom, pan, and hover for detailed data. Streamlit integrates flawlessly with Plotly using `st.plotly_chart()`.

**Example: Interactive Plotly Chart**
```python
import streamlit as st
import plotly.express as px
import pandas as pd

st.header("3. Custom Interactive Charts with Plotly")

# Sample data: Evaluating model accuracy across different epochs
df = pd.DataFrame({
    "Epoch": [1, 2, 3, 4, 5],
    "Accuracy": [0.65, 0.72, 0.81, 0.88, 0.94],
    "Model": ["CNN", "CNN", "CNN", "CNN", "CNN"]
})

# Create a Plotly figure
fig = px.line(
    df, 
    x="Epoch", 
    y="Accuracy", 
    color="Model", 
    title="Model Training Progression",
    markers=True
)

# Display in Streamlit (use_container_width makes it responsive)
st.plotly_chart(fig, use_container_width=True)
```

---

## 4. Altair (Declarative Statistical Visualization)
If you need complex, layered statistical charts with custom interactions (like clicking a bar chart to filter a scatter plot), **Altair** is the best choice. Streamlit's native charts are built on Altair, but using `st.altair_chart()` unlocks its full power.

**Example: Custom Altair Chart**
```python
import streamlit as st
import altair as alt
import pandas as pd
import numpy as np

st.header("4. Advanced Altair Charts")

df = pd.DataFrame(
    np.random.randn(100, 2), 
    columns=['Prediction', 'Actual']
)

# Create an Altair chart with custom tooltips and colors
chart = alt.Chart(df).mark_circle(size=60).encode(
    x='Prediction',
    y='Actual',
    color=alt.value('red'),
    tooltip=['Prediction', 'Actual']
).interactive() # Makes it zoomable/pannable

st.altair_chart(chart, use_container_width=True)
```

---

## 🛠 Practice Exercise for Your Repo
**Task:** Build an "EDA (Exploratory Data Analysis) Visualizer".
1. Create a simple Pandas DataFrame with 3 columns: `Age`, `Salary`, and `Department`.
2. Use a native `st.bar_chart` to show the count of employees in each department.
3. Import Plotly Express and create a scatter plot mapping `Age` to `Salary`, colored by `Department`.
4. Render the Plotly chart using `st.plotly_chart()`.

