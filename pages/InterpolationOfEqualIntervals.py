import streamlit as st
import numpy as np

def apprun(n,x,y,x0):
    p=(x0-x[0])/(x[1]-x[0])
    s=0
    arr=np.zeros((n,n))
    for i in range(n):
        arr[0][i]=y[i]
    for i in range(1,n):
        for j in range(n-i):
            arr[i][j]=arr[i-1][j+1]-arr[i-1][j]
    coef=value(p,n)
    for i in range(n):
        s=s+arr[i][0]*coef[i]
    newsum=round(s,3)
    st.subheader(f"The value of y at x = {x0} is equal to {newsum}")
def value(p,n):
    c=[]
    c.append(1)
    for i in range(1,n):
        c.append(chain(p,i)/fact(i))
    return c
def chain(p,n):
    if n>1:
        return (p-(n-1))*chain(p,n-1)
    else:
        return p
def fact(n):
    if n>0:
        return n*fact(n-1)
    else:
        return 1
def apprun2(n,x,y,x0):
    p = (x0 - x[n-1]) / (x[1] - x[0])
    s = 0
    arr = np.zeros((n, n))
    for i in range(n):
        arr[0][i] = y[i]
    for i in range(1,n):
        for j in range(i,n):
            arr[i][j] = arr[i - 1][j] - arr[i - 1][j - 1]
    coef = value2(p, n)
    for i in range(n):
        s = s + arr[i][n-1] * coef[i]
    newsum = round(s, 3)
    st.subheader(f"The value of y at x = {x0} is equal to {newsum}")
def value2(p,n):
    c = []
    c.append(1)
    for i in range(1, n):
        c.append(chain2(p, i) / fact(i))
    return c
def chain2(p,n):
    if n>1:
        return (p+(n-1))*chain2(p,n-1)
    else:
        return p
st.title("Newton Gregory Interpolation")
x = []
y = []
sx = st.text_input("Enter the x values")
sy = st.text_input("Enter the y values")
nx = sx.split(",")
ny = sy.split(",")
x0 = st.number_input("Enter the point of interest")
a = st.button("Forward Interpolation")
b = st.button("Backward Interpolation")
if a or b:
    for i in range(len(nx)):
        x.append(float(nx[i]))
        y.append(float(ny[i]))
    if a:
        apprun(len(x),x,y,x0)
    elif b:
        apprun2(len(x),x,y,x0)
