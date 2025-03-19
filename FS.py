import streamlit as st


if 'SS' not in st.session_state:
  st.session_state['SS'] = 1
  st.session_state["username_correct"] = ["admin"]
  st.session_state["password_correct"] = ["admin"]

#---------------------------------------------------------------------------------------------------------
#HOME SCREEN

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

#---------------------------------------------------------------------------------------------------------
#LOGIN SCREEN
      
elif st.session_state['SS'] == 2:
  st.write(st.session_state['SS'])
  with st.container(border = True):
    st.header("Create Account")
    st.write("")
    st.text_input("Username", "", key = "username")
    st.write("")
    st.text_input("Password", "", key = "password", type = "password")
    
    if st.button("LOGIN"):
      for i in range(len(st.session_state["username_correct"])):
        if st.session_state["username"] == st.session_state["username_correct"][i] and st.session_state["password"] == st.session_state["password_correct"][i]:
          st.session_state['SS'] = 3
        else:
          st.error("Invalid Username or Password")

    if st.button("CREATE ACCOUNT"):
      st.session_state["username_correct"].append(st.session_state["username"])
      st.session_state["password_correct"].append(st.session_state["password"])
      st.caption("CREATED ACCOUNT")

#---------------------------------------------------------------------------------------------------------
#HOW TO USE SIMULATION SCREEN
      
elif st.session_state['SS'] == 3:
  st.title("HOW TO USE SIMULATION")
  with st.container(border = True):
    c1, c2 = st.columns(2)
    with c1:
      st.write("To use Fluid Simulation, start by launching the app and selecting a scenario, such as pipe flow, aerodynamics, or open channels. Next, adjust key parameters like viscosity, velocity, pressure, or obstacles to customize the simulation. Once set, run the simulation and observe real-time changes in fluid behavior. Watch how different factors influence flow patterns, turbulence, and pressure distribution. Use visual tools to analyze results, compare different settings, and gain deeper insights into fluid mechanics. Experiment with various conditions to see how fluids react in different environments, reinforcing key physics concepts through hands-on learning.")
    with c2:
      st.write("")
      st.write("")
      st.write("")
      st.image("Logo2.png")
  if st.button("Countinue to Simulation"):
    st.session_state['SS'] = 4

#---------------------------------------------------------------------------------------------------------
#SIMULATION SCREEN

elif st.session_state['SS'] == 4:
  with st.container(border = True): 
    c1, c2, c3, c4 = st.columns(4)
    with c1: #Pause-Play-Restart Menu
      with st.container(border = True): 
        if st.button(label = None, icon="⏸️"):
          st.write("Pause")
    with c2: #Particle Settings
      with st.expander("Particle Settings"):
        st.text_input("Particle Mass", key = "particleMass")
        st.text_input("Particle Density", key = "particleDensity")
        st.text_input("Particle X Speed", key = "particleXSpeed")
        st.text_input("Particle Y Speed", key = "particleYSpeed")
        st.text_input("Particle Force Coefficient", key = "particleForce")
        st.text_input("Particle Collision Coefficient", key = "particleCollision")
    with c3: #Simulation Environment
      with st.expander("Simulation Environment"):
        st.text_input("Gravity", key = "Gravity")
        st.text_input("X Boundary", key = "Bx")
        st.text_input("Y Boundary", key = "By")
    with c4: #Analysis Tools
      with st.expander("Analysis Tools"):
        st.write("Resultant Y Force: " + "10")
        st.write("Resultant X Force: " + "2")
        st.write("Total Pressure: " + "4")
        st.write("Average Temprature: " + "3")
    
    


