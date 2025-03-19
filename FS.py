import streamlit as st


if 'SS' not in st.session_state:
  st.session_state['SS'] = 1

if st.session_state['SS'] == 1:
    with st.container(border = True):
                    c1, c2 = st.columns(2)
                    with c1:
                            st.write("")
                            st.write("")
                            st.write("")
                            st.write("")
                            st.title("Fluid")
                            st.title("Simulation")
                    with c2:
                            st.image("Logo1.png")
    
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("ABOUT THE SIMULATION")
        with st.container(border = True):
          st.write("This Fluid Simulation is an engaging and educational app designed to teach high school students the fundamentals of fluid mechanics through real-time simulation. Users can manipulate key factors like particle mass, velocity, pressure, and obstacles to observe how fluids behave in different conditions. The interactive visualizations make complex concepts—such as laminar vs. turbulent flow, Bernoulli’s principle, and vortex formation—intuitive and fun to explore.") 
    with c2:
        st.subheader("ABOUT THE AUTHOR")
        with st.container(border = True):
          st.write("I’m Rayan Gupta, a 12th-grade IBDP student passionate about physics, mathematics, and technology. I created Fluid Simulation to make fluid mechanics interactive and accessible for students like me. I love problem-solving, coding, and finding innovative ways to connect education with hands-on learning, making complex concepts easier to understand and explore.")
    
    if st.button("GET STARTED"):
      st.session_state['SS'] = 2
      
elif st.session_state['SS'] == 2:
  with st.container(border = True):
    st.header("Create Account")
    st.write("")
    st.text_input("Username", "", key = "username")
    st.write("")
    st.text_input("Password", "", key = "password")
    if st.button("LOGIN"):
      if st.session_state["username"] == "admin" and st.session_state["password"] == "admin":
        st.session_state['SS'] == 3
      else:
        st.error("Invalid Username or Password")
elif st.session_state['SS'] == 3:
  st.write("DASHBOARD")
    
    


