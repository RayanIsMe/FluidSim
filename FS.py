import random, math
import pandas as pd
import numpy as np
import streamlit as st
import time


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
      st.rerun()

#---------------------------------------------------------------------------------------------------------
#LOGIN SCREEN
      
elif st.session_state['SS'] == 2:
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
          st.rerun()
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
    st.rerun()
  s1, s2, s3, s4, s5, s6 = st.columns(6)
  with s6:
    if st.button("LOGOUT"):
      st.session_state['SS'] = 1
      st.rerun()

#---------------------------------------------------------------------------------------------------------
#SIMULATION SCREEN

elif st.session_state['SS'] == 4:
  with st.container(border = True): 
    c1, c2, c3, c4 = st.columns(4)
    with c1: #Pause-Play-Restart Menu
      with st.container(border = True): 
        b1, b2, b3 = st.columns(3)
        with b1:
          if st.button("", icon="⏸️"):
            st.session_state["PausePlay"] = 0
        with b2:
          if st.button("", icon="▶️"):
            st.session_state["PausePlay"] = 1
        with b3:
          if st.button("", icon="🔄"):
            st.session_state["timeP"] = 0
    with c2: #Particle Settings
      with st.expander("Particle Settings"):
        st.number_input("Particle Mass", value = 0.5, key = "particleMass")
        st.number_input("Particle Density", value = 5, key = "particleDensity")
        st.number_input("Particle X Speed", value = 0.7, key = "particleXSpeed")
        st.number_input("Particle Y Speed", value = 0, key = "particleYSpeed")
        st.number_input("Particle Force Coefficient", value = 0.005, key = "particleForce")
        st.number_input("Particle Collision Coefficient", value = 0.05, key = "particleCollision")
    with c3: #Simulation Environment
      with st.expander("Simulation Environment"):
        st.number_input("Iterations", value = 100, key = "Iterations")
        st.number_input("Gravity", value = 0, key = "Gravity")
        st.number_input("X Boundary", value = 30, key = "Bx")
        st.number_input("Y Boundary", value = 10, key = "By")
    with c4: #Analysis Tools
      with st.expander("Analysis Tools"):
        st.write("Resultant Y Force: " + "--")
        st.write("Resultant X Force: " + "--")
        st.write("Total Pressure: " + "--")
        st.write("Average Temprature: " + "--")
  #SIMULATION ---------------------------------------------------------------------------------------------------------------------------------------------------------------
  #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  placeholder = st.empty()
  class particle:
        x, y, Vx, Vy = 0, 0, 0, 0
        def __init__(self, x, y, Vx, Vy):
            self.x = x
            self.y = y
            self.Vx = Vx
            self.Vy = Vy
    
  class object(particle):
          def __init__(self, x, y, Vx, Vy):
              self.x = x
              self.y = y
              self.Vx = Vx
              self.Vy = Vy
      
  
  if 'Sim' not in st.session_state:
      st.session_state['Sim'] = 1
  
  if st.session_state['Sim'] == 1:
      
      #VARIABLES-------------------------------------------
  
      #defining variables
      st.session_state["timeP"] = 0 #variable keeping track of number of interations. This variable increases by one every time the program runs through the while loop.
      st.session_state["particleCount"] = 0 #variable to keep track of number of particles
  
      
      #control variables
      st.session_state["initialSpeed"] = 0.5 #initial speed the particle travels at
      st.session_state["newParticles"] = 6 #number of particles that are added per time frame
      st.session_state["energyLoss"] = 0.7 #amount of energy lost when colliding with edge
      st.session_state["repulsiveDistance"] = 0.5
      st.session_state["repulsiveStrength"] = 0.05
      st.session_state["objectStrength"] =  0.05 * st.session_state["initialSpeed"] * 4
      st.session_state["objectDistance"] = 1
  
      #analysis tools
      st.session_state["forcex"] = 0
      st.session_state["forcey"] = 0
      
      #defining particles
      st.session_state["p"] = [] #object list for air particle objects
      st.session_state["ob"] = [] #object list for object particle objects
  
      #plotting lists
      st.session_state["plotx"] = []
      st.session_state["ploty"] = []
      st.session_state["its"] = st.session_state["Iterations"]
      
      #OBJECT DEFINITION-----------------------------------------------------------------------------------------------
      st.session_state["objCount"] = 0 #keeps track of number of object particles. Stays constant
      for h in range(8):
          st.session_state["ob"].append(object(10+(h/16), 5+(h/16), 0, 0))
          st.session_state["ob"].append(object(10+(h/4), 5-(h/20), 0, 0))
          st.session_state["objCount"] += 2
      
      st.session_state['Sim'] = 2
      st.rerun()
  
  elif st.session_state['Sim'] == 2: #-----------------------------------------------------------------------------------------------------------------------
      # SETTING VARIABLES AND LIST TO 0
          
      pltx = []
      pltx.append(0)
      pltx.append(st.session_state["Bx"])
      plty = []
      plty.append(0)
      plty.append(st.session_state["By"])
      deleteList = []
  
      st.session_state["timeP"] += 1  # add one to time variable every time we go through the loop
  
      # Add particles every increment of this condition. If initial speed is higher,
      # more frequent new particles to simulate constant density
      if st.session_state["timeP"] % 5 == 0:   #int(2 / st.session_state["initialSpeed"])
          #st.write("NEW PARTICLES")
          for i in range(st.session_state["newParticles"]):
              # create a new particle with initial x velocity and initial random vertical position
              st.session_state["p"].append(particle(0, random.randint(0, st.session_state["By"] - 1) + random.random(), st.session_state["initialSpeed"], 0))
              st.session_state["particleCount"] += 1
          
  
      # LOOPING PARTICLES-----------------------------------------------------------------------------------------------------------------------------------------
      for i in range(st.session_state["particleCount"]):
  
          # UPDATE POSITIONS
          st.session_state["p"][i].x += st.session_state["p"][i].Vx
          st.session_state["p"][i].y += st.session_state["p"][i].Vy

          st.session_state["p"][i].y -= st.session_state["Gravity"]
  
          # Border collision
          if st.session_state["p"][i].y < 0:
              st.session_state["p"][i].y = 0
              st.session_state["p"][i].Vy *= -st.session_state["energyLoss"]
          elif st.session_state["p"][i].y > st.session_state["By"]:
              st.session_state["p"][i].y = st.session_state["By"]
              st.session_state["p"][i].Vy *= -st.session_state["energyLoss"]
  
          if st.session_state["p"][i].x < 0:
              st.session_state["p"][i].x = 0
              st.session_state["p"][i].Vx *= -st.session_state["energyLoss"]
          elif st.session_state["p"][i].x > st.session_state["Bx"]:
              deleteList.append(i)
  
          # REPULSIVE FORCE FROM OTHER PARTICLES
          for j in range(st.session_state["particleCount"]):
              if i != j:
                  # Distance variable stores numerical value of distance between two particles
                  distance = ((st.session_state["p"][i].x - st.session_state["p"][j].x) ** 2 + (st.session_state["p"][i].y - st.session_state["p"][j].y) ** 2) ** 0.5
                  if distance < st.session_state["repulsiveDistance"]:
                      # Find the angle
                      if st.session_state["p"][j].x - st.session_state["p"][i].x != 0:
                          angle = math.atan((st.session_state["p"][j].y - st.session_state["p"][i].y) / (st.session_state["p"][j].x - st.session_state["p"][i].x))
                      else:
                          angle = 90
  
                      # Change velocity of particle[i]
                      if st.session_state["p"][i].x <= st.session_state["p"][j].x:
                          if distance != 0:
                                  st.session_state["p"][i].Vx += -math.cos(angle) * (st.session_state["repulsiveDistance"] / distance) * st.session_state["repulsiveStrength"]
                                  st.session_state["p"][i].Vy += -math.sin(angle) * (st.session_state["repulsiveDistance"] / distance) * st.session_state["repulsiveStrength"]
                      elif st.session_state["p"][i].x >= st.session_state["p"][j].x:
                          if distance != 0:
                                  st.session_state["p"][i].Vx += math.cos(angle) * (st.session_state["repulsiveDistance"] / distance) * st.session_state["repulsiveStrength"]
                                  st.session_state["p"][i].Vy += math.sin(angle) * (st.session_state["repulsiveDistance"] / distance) * st.session_state["repulsiveStrength"]
  
  
              # REPULSIVE FORCE FROM objects
              for j in range(len(st.session_state["ob"])):
  
                  #if in range
                  distance = ((st.session_state["p"][i].x - st.session_state["ob"][j].x)**2 + (st.session_state["p"][i].y - st.session_state["ob"][j].y)**2)**0.5
                  if distance < st.session_state["objectDistance"]:
  
                      #find the angle
                      if st.session_state["ob"][j].x - st.session_state["p"][i].x != 0:
                          angle = math.atan((st.session_state["ob"][j].y - st.session_state["p"][i].y)/(st.session_state["ob"][j].x - st.session_state["p"][i].x))
                      else:
                          angle = 90
                      
                      #chnage velocity
                      if st.session_state["p"][i].x < st.session_state["ob"][j].x:
                          st.session_state["p"][i].Vx += -math.cos(angle) * (distance/st.session_state["objectDistance"]) * st.session_state["objectStrength"]
                          st.session_state["p"][i].Vy += -math.sin(angle) * (distance/st.session_state["objectDistance"]) * st.session_state["objectStrength"]
                          st.session_state["forcex"] += math.cos(angle) * (distance/st.session_state["objectDistance"]) * st.session_state["objectStrength"]
                          st.session_state["forcey"] += math.sin(angle) * (distance/st.session_state["objectDistance"]) * st.session_state["objectStrength"]
                      elif st.session_state["p"][i].x > st.session_state["ob"][j].x:
                          st.session_state["p"][i].Vx += math.cos(angle) * (distance/st.session_state["objectDistance"]) * st.session_state["objectStrength"]
                          st.session_state["p"][i].Vy += math.sin(angle) * (distance/st.session_state["objectDistance"]) * st.session_state["objectStrength"]
                          st.session_state["forcex"] += -math.cos(angle) * (distance/st.session_state["objectDistance"]) * st.session_state["objectStrength"]
                          st.session_state["forcey"] += -math.sin(angle) * (distance/st.session_state["objectDistance"]) * st.session_state["objectStrength"]
                      elif st.session_state["p"][i].y > st.session_state["ob"][j].y:
                          st.session_state["p"][i].Vy += math.sin(angle) * (distance/st.session_state["objectDistance"]) * st.session_state["objectStrength"]
                          st.session_state["forcey"] += -math.sin(angle) * (distance/st.session_state["objectDistance"]) * st.session_state["objectStrength"]
                      else:
                          st.session_state["p"][i].Vy += -math.sin(angle) * (distance/st.session_state["objectDistance"]) * st.session_state["objectStrength"]
                          st.session_state["forcey"] += math.sin(angle) * (distance/st.session_state["objectDistance"]) * st.session_state["objectStrength"]
                      
  
  
  
          
  
          #ADD PLOTS
          if st.session_state["p"][i].x < st.session_state["Bx"]:
            pltx.append(st.session_state["p"][i].x)
            plty.append(st.session_state["p"][i].y)
  
          
      #DELETE REQUIRED OBJECTS
      for j in range(len(deleteList)):
              del st.session_state["p"][deleteList[j]]
              st.session_state["particleCount"] -= 1
  
  
      for j in range(len(st.session_state["ob"])):
              pltx.append(st.session_state["ob"][j].x)
              plty.append(st.session_state["ob"][j].y)
  
      st.session_state["timeP"] += 1
      #PLOTTING
  
  
      st.session_state["plotx"].append(pltx)
      st.session_state["ploty"].append(plty)
  
      
      placeholder.progress(st.session_state["timeP"]/(st.session_state["its"]+5), text = "Progress")
  
      if st.session_state["timeP"] > st.session_state["its"]:
                  st.session_state['Sim'] = 3
                  st.session_state["timeP"] = 0
                  st.session_state["PausePlay"] = 0
  
      st.rerun()
                  
  elif st.session_state['Sim'] == 3: #---------------------------------------------------------------------------------------------------------------------------------------
          if st.session_state["timeP"] < len(st.session_state["plotx"]):
                  df = pd.DataFrame({
                      'x': st.session_state["plotx"][st.session_state["timeP"]],
                      'y': st.session_state["ploty"][st.session_state["timeP"]],
                  })
                  if st.session_state["PausePlay"] == 1:
                    st.session_state["timeP"] += 1
                  
                  with placeholder.container():
                          st.scatter_chart(data = df, x = 'x', y = 'y', width = 700, height = 400)
                          # st.write(st.session_state["plotx"][st.session_state["timeP"]-1])
                          # st.write( st.session_state["ploty"][st.session_state["timeP"]-1])
                  time.sleep(0.1)
                  st.rerun()
          else:
                  st.header("SIMULATION OVER. CLICK RESTART TO RERUN SAME SIMULATION OR CLICK RECALCULATE WITH NEW VARIABLES TO RERENDER THE SIMULATION.")
                  if st.button("Recalculate"):
                    st.session_state['Sim'] = 1
                    st.rerun()
                    
  s1, s2, s3, s4, s5, s6 = st.columns(6)
  with s6:
    if st.button("LOGOUT"):
      st.session_state['SS'] = 1
      st.rerun()
  
      
      
  
  
