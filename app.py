import streamlit as st

st.title("Student Grade Calculator")

num_subjects = st.number_input("Enter number of subjects:", min_value=1, step=1, value=1)

marks = []
for i in range(int(num_subjects)):
    mark = st.number_input(f"Enter marks for subject {i+1} (out of 100):", min_value=0.0, max_value=100.0, step=0.1, key=f"mark_{i}")
    marks.append(mark)

if st.button("Calculate Percentage and Grade"):
    if len(marks) == num_subjects:
        total_marks = sum(marks)
        percentage = (total_marks / num_subjects)
        
        if percentage >= 90:
            grade = "A"
        elif percentage >= 80:
            grade = "B"
        elif percentage >= 70:
            grade = "C"
        elif percentage >= 60:
            grade = "D"
        else:
            grade = "F"
        
        st.success(f"Total Marks: {total_marks:.2f}")
        st.success(f"Percentage: {percentage:.2f}%")
        st.success(f"Grade: {grade}")
    else:
        st.error("Please enter marks for all subjects.")

