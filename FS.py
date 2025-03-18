import streamlit as st

with st.container(border = True):
                c1, c2 = st.columns(2)
                with c1:
                        st.write("")
                        st.write("")
                        st.title("StellarThrust")
                        st.subheader("A Rocket Launch Simulator")
                with c2:
                        st.image("Logo1.jpg")
