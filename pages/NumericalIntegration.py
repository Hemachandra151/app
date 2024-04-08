import streamlit as st

def trapezoidal(n,h,y):
    part1 = y[0] + y[n-1]
    part2 = 0
    for i in range(1,n-1):
        part2 = part2 + y[i]
    area = h*(part1 + 2*part2)/2
    return round(area,6)
def Simp2(n,h,y):
    part1 = y[0] +y[n-1]
    part2 = 0
    part3 = 0
    for i in range(1,n-1):
        if i%2==0:
            part2 = part2 + y[i]
        else:
            part3 = part3 + y[i]
    area = h*(part1 + 2*part2 + 4*part3)/3
    return round(area,6)
def Simp3(n,h,y):
    part1 = y[0] + y[n-1]
    part2 = 0
    part3 = 0
    for i in range(1,n-1):
        if i%3==0:
            part3 = part3 + y[i]
        else:
            part2 = part2 + y[i]
    area = 3*h*(part1 + 3*part2 + 2*part3)/8
    return round(area,6)

st.title("Numerical Integration")
y = []
h = st.number_input("Enter the Step length")
sy = st.text_input("Enter the y values")
ny = sy.split(",")
a = st.button("Trapezoidal rule")
b = st.button("Simpson 1/3rd rule")
c = st.button("Simpson 3/8th rule")
if a or b or c:
    for i in range(len(ny)):
        y.append(float(ny[i]))
    n = len(y)
    if a:
        A = trapezoidal(n,h,y)
        st.subheader(f"The value of the Integral is {A}")
    elif b:
        if (n-1)%2==0:
            A = Simp2(n,h,y)
            st.subheader(f"The value of the Integral is {A}")
        else:
            st.subheader("Cannot apply Simpson 1/3rd rule")
    elif c:
        if (n-1)%3==0:
            A = Simp3(n,h,y)
            st.subheader(f"The value of the integral is {A}")
        else:
            st.subheader("Cannot apply Simpson 3/8th rule")
