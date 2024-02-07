#Example3
import streamlit as st
import streamlit.components.v1 as components

components.html(
    """
<p>Hello</p>

<button type="button"
onclick="document.getElementById('demo').innerHTML = Date()">
Click me to display Date and Time.</button>

<p id="demo"></p>


<p id="demo1"></p>
<script>
let x, y, z;  // Statement 1
x = 5;        // Statement 2
y = 6;        // Statement 3
z = x + y;    // Statement 4

document.getElementById("demo1").innerHTML =
"The value of z is " + z + ".";
</script>


    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <div id="accordion">
      <div class="card">
        <div class="card-header" id="headingOne">
          <h5 class="mb-0">
            <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
            Collapsible Group Item #1
            </button>
          </h5>
        </div>
        <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
          <div class="card-body">
            Collapsible Group Item #1 content
          </div>
        </div>
      </div>
      <div class="card">
        <div class="card-header" id="headingTwo">
          <h5 class="mb-0">
            <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
            Collapsible Group Item #2
            </button>
          </h5>
        </div>
        <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
          <div class="card-body">
            Collapsible Group Item #2 content
          </div>
        </div>
      </div>
    </div>
    """,
    height=600,
)


def register_user(username, password):
    # You can store the user data in a database or any persistent storage
    st.session_state.registered_users[username] = password


def login_user(username, password):
    # Check if the provided username exists and the password matches
    if username in st.session_state.registered_users and st.session_state.registered_users[username] == password:
        return True
    else:
        return False

def ToLogin():
    st.session_state.page = 1

def ToReg():
    st.session_state.page = 2

    

# Initialize session_state variables
if "registered_users" not in st.session_state:
    st.session_state.registered_users = {}


# Page 1 (Login)
if "page" not in st.session_state:
    st.session_state.page = 1


if st.session_state.page == 1:
    st.title("Login")
    login_username = st.text_input("Username")
    login_password = st.text_input("Password", type="password")


    if st.button("Login"):
        if login_user(login_username, login_password):
            st.success("Login successful!")
        else:
            st.error("Invalid username or password")

    # Add button to navigate to the Register page
    #if st.button("Go to Register"):
        #st.session_state.page = 2
    st.button('Go to Register', on_click=ToReg())


# Page 2 (Register)
elif st.session_state.page == 2:
    st.title("Register")
    register_username = st.text_input("Username")
    register_password = st.text_input("Password", type="password")


    if st.button("Register"):
        register_user(register_username, register_password)
        st.success("Registration successful!")


        # After registration, navigate back to the Login page
        st.session_state.page = 1


    # Add button to navigate back to the Login page
    #if st.button("Go to Login"):
        #st.session_state.page = 1
    st.button('Go to Login', on_click=ToLogin())
