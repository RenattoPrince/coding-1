import matplotlib.pyplot as plt

students_names=["sanjay", "Rahual", "Karan", "Wasin", "Ramesh", "Ajay", "Sartaj", "Priya"]
students_marks=[35,50,50,95,65,90, 78, 95]


marks_perc = []
for x in students_marks:
  res = (x/50)*100
  marks_perc.append(res)

print(marks_perc)


#line chart

def marks_line_chart():
  plt.plot(students_names,students_marks)
  plt.title("Students Marks Graph")
  plt.xlabel("Students Names")
  plt.ylabel("Students Marks")

  plt.show()
marks_line_chart()