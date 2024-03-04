import streamlit as st
import numpy as np
def apprun(n,x,y,xp):
    num=[]
    den=[]
    s=0
    for i in range(n):
        a = 1
        b = 1
        for j in range(n):
            if i != j:
                a = a * (xp - x[j])
                b = b * (x[i] - x[j])
        num.append(a)
        den.append(b)
    for i in range(n):
        s=s+y[i]*num[i]/den[i]
    st.subheader(f"The value of y at x = {xp} is equal to {round(s,3)}")
def divided(n,x,y,xp):
    s = 0
    c = []
    c.append(1)
    arr = np.zeros((n, n))
    for i in range(n):
        arr[0][i] = y[i]
    for i in range(1, n):
        for j in range(n - i):
            arr[i][j] = (arr[i - 1][j + 1] - arr[i - 1][j])/(x[j+i] - x[j])
    for i in range(n):
        a=1
        for j in range(i+1):
            a=a*(xp-x[j])
        c.append(a)
    for i in range(n):
        s=s+arr[i][0]*c[i]
    st.subheader(f"The value of y at x = {xp} is equal to {round(s,3)}")
st.title("Interpolation for unequal intervals")
x = []
y = []
flag=0
sx = st.text_input("Enter the x values")
sy = st.text_input("Enter the y values")
xp = st.number_input("Enter the point of interest")
nx = sx.split(",")
ny = sy.split(",")
a = st.button("Lagrange Interpolation")
b = st.button("Divided Difference")
if a or b:
    for i in range(len(nx)):
        x.append(float(nx[i]))
        y.append(float(ny[i]))
    if a:
        apprun(len(x),x,y,xp)
    elif b:
        divided(len(x),x,y,xp)