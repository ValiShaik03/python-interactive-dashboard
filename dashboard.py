import streamlit as st


st.set_page_config(
    page_title="Python Interactive Dashboard",
    page_icon ="📗",
    layout="wide",
)
st.title("Python Interactive Dashboard")

with st.sidebar:
    st.header("Configuration")
    data_type=st.selectbox("Select Data Type",
    ["Variables and Data Types",
    "Control Flow and Loops",
    "Functions and Modules",
    "File Handling"])

if data_type == "Variables and Data Types":
    st.header("Variables and Data Types")
    var_name=st.text_input("Enter Variable Name",value="my_string")
    var_value=st.text_input("Enter Variable value",value="Hello Worlds")
    if var_name and var_value:
        code=f"{var_name} = {repr(var_value)}"
        exec(code)
        st.code(code,language="python")
        st.write(f"Variable `{var_name}` created with value: {var_value}")
        st.write(globals()[var_name])

    data_obj={"String":"Hello","Integer":42,"Float":3.14,"List":[1,2,3],"Dictionary":{"key":"value"}}
    st.subheader("Predefined Data Types")
    for name,obj in data_obj.items():
        st.write(f"**{name}:** {obj} (Type:{type(obj).__name__})")
        st.markdown("---")
elif data_type == "Control Flow and Loops":
    st.header("Control Flow and Loops")
    st.write("This section will demonstrate control flow and loops in Python.")
    num=st.number_input("Enter a number to check if it's even or odd",min_value=0,max_value=100,value=10,step=1)
    if num % 2 == 0:
        st.success(f"{num} is Even")
    else:
        st.error(f"{num} is Odd")

    st.subheader("Loop Example")
    count=st.slider("Select a number to loop up to",0,20,5)
    st.write(f"Looping from 0 to {count}:")
    for i in range(count+1):
        st.write(i)
elif data_type == "Functions and Modules":
    st.header("Functions and Modules")
    st.write("This section will demonstrate functions and modules in Python.")
    def greet(name):
        return f"Hello, {name}!"
    name=st.text_input("Enter your name",value="User")
    if name:
        greeting=greet(name)
        st.success(greeting)

    st.subheader("Using Math Module")
    import math
    number=st.number_input("Enter a number to calculate its square root",min_value=0.0,value=16.0,step=1.0)
    sqrt_value=math.sqrt(number)
    st.write(f"The square root of {number} is {sqrt_value}")
elif data_type == "File Handling":
    st.header("File Handling")
    st.write("This section will demonstrate file handling in Python.")
    uploaded_file=st.file_uploader("Upload a text file",type=["txt"])
    if uploaded_file is not None:
        content=uploaded_file.read().decode("utf-8")
        st.subheader("File Content:")
        st.text_area("File Content",value=content,height=200)

    st.subheader("Write to a File")
    file_name=st.text_input("Enter file name to save",value="output.txt")
    file_content=st.text_area("Enter content to write to the file",value="Hello, this is a sample text.")
    if st.button("Save to File"):
        with open(file_name,"w") as f:
            f.write(file_content)
        st.success(f"Content saved to {file_name}")