import streamlit as st
import numpy as np

def apprun(n,x,y,x0):
    p=(x0-x[0])/(x[1]-x[0])
    h=x[1]-x[0]
    s=0
    arr=np.zeros((n,n))
    fy=[]
    for i in range(n):
        arr[0][i]=y[i]
    for i in range(1,n):
        for j in range(n-i):
            arr[i][j]=arr[i-1][j+1]-arr[i-1][j]
    for i in range(1,n):
        fy.append(arr[i][0])
    ci=val(p,n)
    for i in range(n-1):
        s=s+fy[i]*ci[i]/fact(i+1)
    newsum=round(s/h,3)
    st.subheader(f"The derivative of y at x = {x0} is equal to {newsum}")
def val(p,n):
    c=[]
    c.append(1)
    for i in range(2, n):
        new = 0
        for j in range(i):
            a = 1
            for k in range(i):
                if k != j:
                    a = a * (p - k)
            new = new + a
        c.append(new)
    return c
def fact(n):
    if n>0:
        return n*fact(n-1)
    else:
        return 1
st.title("Numerical Differentiation")
x = []
y = []
sx = st.text_input("Enter the x values")
sy = st.text_input("Enter the y values")
nx = sx.split(",")
ny = sy.split(",")
x0 = st.number_input("Enter the point of interest")
a = st.button("Calculate")
if a:
    for i in range(len(nx)):
        x.append(float(nx[i]))
        y.append(float(ny[i]))
    apprun(len(x),x,y,x0)
