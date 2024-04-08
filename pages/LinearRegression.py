import streamlit as st
import math

def apprun(x,y):
    n = len(x)
    Exy = 0
    Ex = 0
    Ey =0
    xm=sum(x)/n
    ym=sum(y)/n
    for i in range(n):
        Exy = Exy + (x[i]-xm)*(y[i]-ym)
        Ex = Ex + pow(x[i]-xm,2)
        Ey = Ey + pow(y[i]-ym,2)
    r = Exy/(math.sqrt(Ex*Ey))
    if flag==0:
        byx = r * math.sqrt(Ey/Ex)
        c = ym - xm * byx
        return r,byx,c
    else:
        bxy = r * math.sqrt(Ex/Ey)
        c = xm - ym * bxy
        return r,bxy,c
def correl(r):
    if r == 0:
        st.subheader("No Correlation")
    elif r>0:
        st.subheader(f'r = {round(r,3)}')
        st.subheader("Correlation is Positive")
    else:
        st.subheader(f'r = {round(r,3)}')
        st.subheader("Correlation is negative")

st.title("Regression Analysis")
x = []
y = []
sx = st.text_input("Enter the x values")
sy = st.text_input("Enter the y values")
nx = sx.split(",")
ny = sy.split(",")
a = st.button("Line y on x")
b = st.button("Line x on y")
if a:
    for i in range(len(nx)):
        x.append(float(nx[i]))
        y.append(float(ny[i]))
    flag=0
    r,m,c = apprun(x,y)
    correl(r)
    if r!=0:
        newstr = f"y = {round(m,3)}x "
        if c>0:
            newstr = newstr + f" + {round(c,3)}"
        elif c<0:
            newstr = newstr + f" {round(c,3)} "
    st.subheader("Line y on x is ")
    st.subheader(f"$$ {newstr} $$")
if b:
    for i in range(len(nx)):
        x.append(float(nx[i]))
        y.append(float(ny[i]))
    flag=1
    r,m,c = apprun(x,y)
    correl(r)
    if r!=0:
        newstr = f"x = {round(m,3)}y "
        if c>0:
            newstr = newstr + f" + {round(c,3)}"
        elif c<0:
            newstr = newstr + f" {round(c,3)} "
    st.subheader("Line x on y is ")
    st.subheader(f"$$ {newstr} $$")
