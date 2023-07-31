import streamlit as st
import math

def linear(x,y):
    Exy=0
    Ex2=0
    Ey = sum(y)
    Ex = sum(x)
    for i in range(n):
        Exy = Exy + x[i]*y[i]
        Ex2 = Ex2 + pow(x[i],2)
    det = (n * Ex2 - Ex * Ex)
    detb = (Ex2 * Ey - Ex * Exy)
    deta = (Exy * n - Ex * Ey)
    a = deta/det
    b = detb/det
    return round(a,3),round(b,3)
def quadratic(x,y):
    Ey = sum(y)
    Ex = sum(x)
    Exy = 0
    Ex2y = 0
    Ex2 = 0
    Ex3 = 0
    Ex4 = 0
    for i in range(n):
        Exy = Exy + x[i]*y[i]
        Ex2y = Ex2y + pow(x[i],2)*y[i]
        Ex2 = Ex2 + pow(x[i],2)
        Ex3 = Ex3 + pow(x[i],3)
        Ex4 = Ex4 + pow(x[i],4)
    det = Ex2*(Ex2*Ex2 - Ex*Ex3) - Ex*(Ex2*Ex3 - Ex*Ex4) + n*(Ex3*Ex3 - Ex2*Ex4)
    deta = Ey*(Ex2*Ex2 - Ex*Ex3) - Ex*(Ex2*Exy - Ex*Ex2y) + n*(Ex3*Exy - Ex2*Ex2y)
    detb = Ex2*(Ex2*Exy - Ex*Ex2y) - Ey*(Ex2*Ex3 - Ex*Ex4) + n*(Ex3*Ex2y - Ex4*Exy)
    detc = Ex2*(Ex2*Ex2y - Ex3*Exy) - Ex*(Ex3*Ex2y - Ex4*Exy) + Ey*(Ex3*Ex3 - Ex4*Ex2)
    a = deta/det
    b = detb/det
    c = detc/det

    return round(a,3),round(b,3),round(c,3)
def assign():
    for i in range(len(nx)):
        x.append(float(nx[i]))
        y.append(float(ny[i]))
st.title("Curve Fitting")
radio = ['y=ax+b', 'y=ax^2+bx+c', 'y=ab^x', 'y=ax^b', 'y=1/(ax+b)']
res = st.radio('Choose the Curve',radio)
x = []
y = []
sx = st.text_input("Enter the x values")
sy = st.text_input("Enter the y values")
nx = sx.split(",")
ny = sy.split(",")
n = len(nx)
re = st.button("Fit")
if re:
    if res=='y=ax+b':
        assign()
        a,b=linear(x,y)
        st.subheader("The curve is")
        st.subheader(f"$$ y=({a})x+({b}) $$")
    elif res=='y=ax^2+bx+c':
        assign()
        a,b,c=quadratic(x,y)
        st.subheader("The curve is")
        st.subheader(f"$$ y=({a})x^2+({b})x+({c}) $$")
    elif res=='y=ab^x':
        assign()
        lny = []
        for i in range(n):
            lny.append(math.log(y[i],2))
        lnb,lna = linear(x,lny)
        a = round(pow(2,lna),3)
        b = round(pow(2,lnb),3)
        st.subheader("The curve is")
        st.subheader(f"$$ y=({a})({b})^x $$")
    elif res=='y=ax^b':
        assign()
        lnx = []
        lny = []
        for i in range(n):
            lnx.append(math.log(x[i],2))
            lny.append(math.log(x[i],2))
        b,lna=linear(lnx,lny)
        a = round(pow(2,lna))
        st.subheader("The curve is")
        st.subheader(f"$$ y=({a})x^({b}) $$")
    elif res=='y=1/(ax+b)':
        assign()
        recy = []
        for i in range(n):
            recy.append(1/y[i])
        a,b=linear(x,recy)
        st.subheader("The curve is")
        st.subheader(f"$$ y=1/[({a})x+({b})] $$")
