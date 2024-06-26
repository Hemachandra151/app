import streamlit as st
import numpy as np

def apprun(n,xn,yn):

    a = np.zeros((n, n + 1))
    x = np.zeros(n)
    z = np.zeros(n)

    if flag==0:
        for i in range(n):
            for j in range(n):
                a[i][j] = pow(xn[i], j)

        for i in range(n):
            a[i][n] = yn[i]
    else:
        for i in range(n):
            for j in range(n):
                a[i][j] = pow(xn[i],j+1)

        for i in range(n):
            a[i][n] = yn[i]-con

    for i in range(n):
        for j in range(i + 1, n):
            ratio = a[j][i] / a[i][i]
            for k in range(n + 1):
                a[j][k] = a[j][k] - ratio * a[i][k]

    x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        x[i] = a[i][n]

        for j in range(i + 1, n):
            x[i] = x[i] - a[i][j] * x[j]

        x[i] = x[i] / a[i][i]

    for i in range(n):
        z[i] = round(x[i], 3)
    st.subheader("The Polynomial is ")
    newstr = "y= "
    if flag==0:
        for i in range(n, 1, -1):
            if (z[i-1]>0 and newstr == "y= ") or z[i-1]<0:
                newstr = newstr + f" {z[i - 1]}x^{i - 1} "
            elif z[i-1]>0:
                newstr = newstr + f" + {z[i -1]}x^{i - 1}"
        if z[0]>0 and newstr != "y= ":
            newstr = newstr + f" + {z[0]} "
        elif z[0]<0 or newstr == "y= ":
            newstr = newstr + f" {z[0]}"
    else:
        for i in range(n,0,-1):
            if (z[i-1]!=0 and newstr == "y= ") or z[i-1]<0:
                newstr = newstr + f" {z[i-1]}x^{i}  "
            elif z[i-1]>0:
                newstr = newstr + f" + {z[i-1]}x^{i} "
        if con>0 and newstr == "y= ":
            newstr = newstr + f" + {con} "
        elif con<0:
            newstr = newstr + f" {con} "
    st.subheader(f"$$ {newstr} $$")
st.title("Constructing a Polynomial")
x = []
y = []
flag=0
sx = st.text_input("Enter the x values")
sy = st.text_input("Enter the y values")
nx = sx.split(",")
ny = sy.split(",")

a = st.button("Construct")
if a:
    for i in range(len(nx)):
        x.append(float(nx[i]))
        y.append(float(ny[i]))
    for i in range(len(x)):
        if x[i]==0:
            con=y[i]
            y.pop(i)
            x.pop(i)
            flag=1
            break
    apprun(len(x),x,y)
