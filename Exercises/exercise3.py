import tkinter as tk
from tkinter import messagebox, ttk

# Sample student data
students = [
    {"id": "1345", "name": "John Curry", "coursework_total": 8 + 15 + 7, "exam_mark": 45},
    {"id": "2345", "name": "Sam Sturtivant", "coursework_total": 14 + 15 + 14, "exam_mark": 77},
    {"id": "9876", "name": "Lee Scott", "coursework_total": 17 + 11 + 16, "exam_mark": 99},
    {"id": "3724", "name": "Matt Thompson", "coursework_total": 19 + 11 + 15, "exam_mark": 81},
    {"id": "1212", "name": "Ron Herrema", "coursework_total": 14 + 17 + 18, "exam_mark": 66},
    {"id": "8439", "name": "Jake Hobbs", "coursework_total": 10 + 11 + 10, "exam_mark": 43},
    {"id": "2344", "name": "Jo Hyde", "coursework_total": 6 + 15 + 10, "exam_mark": 55},
    {"id": "9384", "name": "Gareth Southgate", "coursework_total": 5 + 6 + 8, "exam_mark": 33},
    {"id": "8327", "name": "Alan Shearer", "coursework_total": 20 + 20 + 20, "exam_mark": 100},
    {"id": "2983", "name": "Les Ferdinand", "coursework_total": 15 + 17 + 18, "exam_mark": 92}
]

# Calculate grade based on percentage
def calculate_grade(percentage):
    if percentage >= 70:
        return 'A'
    elif percentage >= 60:
        return 'B'
    elif percentage >= 50:
        return 'C'
    elif percentage >= 40:
        return 'D'
    else:
        return 'F'

def view_all_records():
    output = ""
    for student in students:
        overall_percentage = ((student['coursework_total'] + student['exam_mark']) / 160) * 100
        grade = calculate_grade(overall_percentage)
        output += (f"Name: {student['name']}\n"
                   f"Number: {student['id']}\n"
                   f"Coursework Total: {student['coursework_total']}\n"
                   f"Exam Mark: {student['exam_mark']}\n"
                   f"Overall Percentage: {overall_percentage:.2f}%\n"
                   f"Grade: {grade}\n\n")
    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, output)
    
def view_individual_record():
    selected_name = student_selector.get()
    for student in students:
        if student['name'] == selected_name:
            overall_percentage = ((student['coursework_total'] + student['exam_mark']) / 160) * 100
            grade = calculate_grade(overall_percentage)
            output = (f"Name: {student['name']}\n"
                      f"Number: {student['id']}\n"
                      f"Coursework Total: {student['coursework_total']}\n"
                      f"Exam Mark: {student['exam_mark']}\n"
                      f"Overall Percentage: {overall_percentage:.2f}%\n"
                      f"Grade: {grade}")
            text_output.delete(1.0, tk.END)
            text_output.insert(tk.END, output)
            return
    messagebox.showinfo("Info", "Student not found.")

def show_highest_score():
    if not students:
        messagebox.showinfo("Info", "No students found.")
        return
    highest_student = max(students, key=lambda x: ((x['coursework_total'] + x['exam_mark']) / 160) * 100)
    overall_percentage = ((highest_student['coursework_total'] + highest_student['exam_mark']) / 160) * 100
    grade = calculate_grade(overall_percentage)
    output = (f"Name: {highest_student['name']}\n"
              f"Number: {highest_student['id']}\n"
              f"Coursework Total: {highest_student['coursework_total']}\n"
              f"Exam Mark: {highest_student['exam_mark']}\n"
              f"Overall Percentage: {overall_percentage:.2f}%\n"
              f"Grade: {grade}")
    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, output)

def show_lowest_score():
    if not students:
        messagebox.showinfo("Info", "No students found.")
        return
    lowest_student = min(students, key=lambda x: ((x['coursework_total'] + x['exam_mark']) / 160) * 100)
    overall_percentage = ((lowest_student['coursework_total'] + lowest_student['exam_mark']) / 160) * 100
    grade = calculate_grade(overall_percentage)
    output = (f"Name: {lowest_student['name']}\n"
              f"Number: {lowest_student['id']}\n"
              f"Coursework Total: {lowest_student['coursework_total']}\n"
              f"Exam Mark: {lowest_student['exam_mark']}\n"
              f"Overall Percentage: {overall_percentage:.2f}%\n"
              f"Grade: {grade}")
    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, output)
# Add a new student record
def add_student():
    student_id = entry_id.get()
    name = entry_name.get()
    coursework = int(entry_coursework.get())
    exam = int(entry_exam.get())
    
    coursework_total = coursework * 3  # Convert average back to total
    overall_percentage = ((coursework_total + exam) / 160) * 100
    grade = calculate_grade(overall_percentage)
    
    students.append({
        "id": student_id,
        "name": name,
        "coursework_total": coursework_total,
        "exam_mark": exam,
    })
    
 # Update the student selector dropdown
    update_student_selector()
    
    messagebox.showinfo("Info", "Student added successfully!")

# Update the student selector dropdown with the list of student names
def update_student_selector():
    student_selector['values'] = [student['name'] for student in students]
    student_selector.set('')  # Reset the selection

def delete_student():
    selected_name = student_selector.get()
    if not selected_name or selected_name == "Select Student:":
        messagebox.showinfo("Info", "Please select a student to delete.")
        return

    for student in students:
        if student['name'] == selected_name:
            students.remove(student)
            update_student_selector()  
            messagebox.showinfo("Success", f"Student '{selected_name}' has been deleted successfully!")
            return
    
    messagebox.showinfo("Info", "Student not found or not selected.")       

# Function to handle saving changes to the selected student
def save_changes():
    selected_name = student_selector.get()
    if not selected_name or selected_name == "Select Student:":
        messagebox.showinfo("Info", "Please select a student to save changes.")
        return

    for student in students:
        if student['name'] == selected_name:
            # Save the updated details
            student['id'] = entry_id.get()
            student['name'] = entry_name.get()
            student['coursework_total'] = int(entry_coursework.get()) * 3  # Convert back to total
            student['exam_mark'] = int(entry_exam.get())
            
            # Update the dropdown and notify the user
            update_student_selector()
            messagebox.showinfo("Success", f"Changes saved for student '{selected_name}'!")
            return

    messagebox.showinfo("Info", "Student not found.")

# Function to update data and enable the "Save Changes" button
def update_student_data_with_save():
    selected_name = student_selector.get()
    if not selected_name or selected_name == "Select Student:":
        messagebox.showinfo("Info", "Please select a student to edit.")
        return

    for student in students:
        if student['name'] == selected_name:
            # Pre-fill entry fields
            entry_id.delete(0, tk.END)
            entry_id.insert(0, student['id'])
            
            entry_name.delete(0, tk.END)
            entry_name.insert(0, student['name'])
            
            entry_coursework.delete(0, tk.END)
            entry_coursework.insert(0, student['coursework_total'] // 3)  # Convert back to average
            
            entry_exam.delete(0, tk.END)
            entry_exam.insert(0, student['exam_mark'])
            
            # Enable the "Save Changes" button
            save_button.grid(row=7, column=3)
            return

    messagebox.showinfo("Info", "Student not found.")  

# Function to sort student records
def sort_student_records():
    sort_order = sort_order_selector.get()  # Get selected order from dropdown
    if sort_order == "Ascending":
        sorted_students = sorted(students, key=lambda x: ((x['coursework_total'] + x['exam_mark']) / 160) * 100)
    elif sort_order == "Descending":
        sorted_students = sorted(students, key=lambda x: ((x['coursework_total'] + x['exam_mark']) / 160) * 100, reverse=True)
    else:
        messagebox.showinfo("Info", "Please select a sort order.")
        return
    
 # Display the sorted records
    output = ""
    for student in sorted_students:
        overall_percentage = ((student['coursework_total'] + student['exam_mark']) / 160) * 100
        grade = calculate_grade(overall_percentage)
        output += (f"Name: {student['name']}\n"
                   f"Number: {student['id']}\n"
                   f"Coursework Total: {student['coursework_total']}\n"
                   f"Exam Mark: {student['exam_mark']}\n"
                   f"Overall Percentage: {overall_percentage:.2f}%\n"
                   f"Grade: {grade}\n\n")
    
    # Display the sorted output in the text box
    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, output)      

# Initialize GUI
root = tk.Tk()
root.title("Student Manager")
root.configure(bg="#F5F5F5")  
root.geometry("700x650")  

# Title Label
title_label = tk.Label(root, text="Student Manager", font=("Arial", 20, "bold"), bg="#F5F5F5", fg="#333333")
title_label.grid(row=0, column=1, columnspan=3, pady=5 )

# Create buttons for View All, Highest, and Lowest Scores
view_all_button = tk.Button(root, text="View All Records", command=view_all_records, font=("Arial", 12, "bold"), 
bg="#66CDAA", fg="white", relief="raised", height=2, width=20)
view_all_button.grid(row=1, column=1, padx=10, pady=10)

highest_score_button = tk.Button(root, text="Highest Score", command=show_highest_score, font=("Arial", 12, "bold"), 
bg="#66CDAA", fg="white", relief="raised", height=2, width=20)
highest_score_button.grid(row=1, column=2, padx=10, pady=10 )

lowest_score_button = tk.Button(root, text="Lowest Score", command=show_lowest_score, font=("Arial", 12, "bold"), 
bg="#66CDAA", fg="white", relief="raised", height=2, width=20)
lowest_score_button.grid(row=1, column=3, padx=10, pady=10)

# Move student selector and View Record button to row 2
tk.Label(root, text="View Individual Student Record:", bg="#F5F5F5", font=("Arial", 12)).grid(row=2, column=1, padx=5, pady=5)

student_selector = ttk.Combobox(root, values=[student['name'] for student in students])
student_selector.grid(row=2, column=2, padx=5, pady=5)

# Update student selector with the placeholder
student_selector = ttk.Combobox(root, values=[student['name'] for student in students], font=("Arial", 12))
student_selector.grid(row=2, column=2, padx=5, pady=5)
student_selector.set("Select Student:")  

view_individual_button = tk.Button(root, text="View Record", command=view_individual_record, font=("Arial", 12, "bold"), 
bg="#66CDAA", fg="white", relief="raised", height=2, width=20)
view_individual_button.grid(row=2, column=3, padx=8, pady=5)

# Output text box
text_output = tk.Text(root, width=84, height=14, bg="#F0F8FF", fg="#333333", wrap="word")
text_output.grid(row=3, column=1, columnspan=4, padx=5, pady=5)

# Entry fields for adding a new student (placed vertically)
tk.Label(root, text="ID", bg="#F5F5F5").grid(row=4, column=1, padx=10, pady=5, sticky="e")
entry_id = tk.Entry(root)
entry_id.grid(row=4, column=2, padx=10, pady=5)

tk.Label(root, text="Name", bg="#F5F5F5").grid(row=5, column=1, padx=10, pady=5, sticky="e")
entry_name = tk.Entry(root)
entry_name.grid(row=5, column=2, padx=10, pady=5)

tk.Label(root, text="Coursework Avg", bg="#F5F5F5").grid(row=6, column=1, padx=10, pady=5, sticky="e")
entry_coursework = tk.Entry(root)
entry_coursework.grid(row=6, column=2, padx=10, pady=5)

tk.Label(root, text="Exam Mark", bg="#F5F5F5").grid(row=7, column=1, padx=10, pady=5, sticky="e")
entry_exam = tk.Entry(root)
entry_exam.grid(row=7, column=2, padx=10, pady=5)

add_button = tk.Button(root, text="Add Student", command=add_student, font=("Arial", 12, "bold"), 
bg="#66CDAA", fg="white", relief="raised", height=1, width=15)
add_button.grid(row=4, column=3)

# Add Delete Button below the Add Button
delete_button = tk.Button(root, text="Delete Student", command=delete_student, font=("Arial", 12, "bold"),
bg="#66CDAA", fg="white", relief="raised", height=1, width=15)
delete_button.grid(row=5, column=3)

# Add "update Data (With Save)" Button
update_with_save_button = tk.Button(root, text="update Student ", command=update_student_data_with_save, 
font=("Arial", 12, "bold"), bg="#66CDAA", fg="white", relief="raised", height=1, width=15)
update_with_save_button.grid(row=6, column=3)

save_button = tk.Button(root, text="Save Changes", command=save_changes, font=("Arial", 12, "bold"),
bg="#66CDAA", fg="white", relief="raised", height=1, width=15)
save_button.grid_remove()

# Add Sort Order Dropdown and Button
tk.Label(root, text="Sort Student Records:", bg="#F5F5F5", font=("Arial", 12)).grid(row=8, column=1, padx=5, pady=5)
sort_order_selector = ttk.Combobox(root, values=["Ascending", "Descending"], font=("Arial", 12))
sort_order_selector.grid(row=8, column=2, padx=5, pady=5)
sort_order_selector.set("Ascending")  # Default to Ascending
sort_button = tk.Button(root, text="Sort Student Records", command=sort_student_records, font=("Arial", 12, "bold"),
bg="#66CDAA", fg="white", relief="raised", height=1, width=15)
sort_button.grid(row=8, column=3, padx=10, pady=10)

# Run the main GUI loop
root.mainloop()
