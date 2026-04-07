# 🧠 Streamlit Internals: Architecture & Execution Model

To build production-grade AI applications, you need to understand what happens under the hood when a user interacts with a Streamlit app. Streamlit abstracts away the frontend, but knowing its internal plumbing helps you write faster, bug-free code.

## 1. The Client-Server Architecture
Unlike traditional web frameworks (like Django or Flask) that rely on complex routing and REST APIs, Streamlit uses a real-time, persistent connection. 

Streamlit is built on a **Client-Server Architecture**:
* **The Backend (Server):** When you run `streamlit run app.py`, Streamlit starts a local web server powered by **Tornado** (a Python web framework and asynchronous networking library). This server executes your Python code.
* **The Frontend (Client):** The UI you see in the browser is built using **React**. It renders the HTML, CSS, and JavaScript required to display the widgets and charts.
* **The Bridge (WebSockets):** The React frontend and the Python backend communicate in real-time via a **WebSocket** connection. This allows two-way communication without needing to constantly refresh the webpage.

## 2. The Execution Model (The Golden Rule)
The most important concept in Streamlit is its execution model. It behaves fundamentally differently from standard Python scripts or Jupyter Notebooks.

**The Golden Rule:** Every time a user interacts with a widget (clicks a button, types in a text box, moves a slider), **Streamlit reruns your entire Python script from top to bottom.**

### How an Interaction Works:
1. **User Action:** The user clicks a "Submit" button on the React frontend.
2. **WebSocket Message:** The frontend sends a message via the WebSocket to the Tornado backend saying, *"The Submit button was clicked."*
3. **Execution:** The backend updates the button's internal state to `True` and reruns `app.py` from line 1 to the last line.
4. **Data Serialization:** The backend packages the new UI instructions and data using **Protocol Buffers** and **Apache Arrow** (for highly efficient tabular data transfer).
5. **Render:** The backend sends this package back over the WebSocket to the frontend, and React updates the screen.

---

## 3. Code Example: The "Rerun" Problem
Because the script reruns entirely on every interaction, normal Python variables get reset. This is the #1 trap for beginners.

**❌ The Wrong Way (Variables Reset)**
```python
import streamlit as st

st.header("The Rerun Problem")

# This variable gets reset to 0 every single time a button is clicked!
counter = 0 

if st.button("Add 1"):
    counter += 1

# This will only ever show 0 or 1. It will never reach 2.
st.write(f"Counter is at: {counter}")
```

## 4. The Solution: `st.session_state`
To bypass the top-to-bottom reset, Streamlit provides `st.session_state`. This is a dictionary-like object that survives the reruns and stores data specific to a single user's browser tab.

**✅ The Right Way (Using Session State)**
```python
import streamlit as st

st.header("The Session State Solution")

# 1. Initialize the variable in session_state if it doesn't exist yet
if 'true_counter' not in st.session_state:
    st.session_state.true_counter = 0

# 2. Update the session state variable
if st.button("Add 1 to True Counter"):
    st.session_state.true_counter += 1

# 3. Display the persistent variable
st.write(f"Counter is safely at: {st.session_state.true_counter}")
```

---

## 5. Advanced Internals: How Streamlit handles Data
When you build AI tools, you often pass massive datasets or Large Language Model (LLM) outputs to the UI. How does Streamlit do this without crashing the browser?

* **Apache Arrow:** Under the hood, Streamlit uses Apache Arrow as its primary data format. Arrow is a cross-language, in-memory data format that allows Streamlit to serialize huge Pandas DataFrames in the Python backend and deserialize them in the JavaScript frontend instantly, without heavy conversion overhead.
* **Smart Delta Generator:** During a rerun, Streamlit doesn't just blindly send the entire webpage back to the browser. It uses a "Delta Generator." It calculates exactly what changed between the last run and the current run, and only sends the *deltas* (the changes) over the WebSocket. This keeps the app incredibly fast.

