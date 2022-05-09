import cgi


# class which we can use to work
# with the submitted form data
form = cgi.FieldStorage()

haight = int(form.getvalue('haight'))

# to get the data from fields
weight = int(form.getvalue('weight'))

bmi = haight / (weight * weight)

print("Content-type:text/html\n")
print("<html>")
print("<head>")
print("<title>Body Mass Index</title>")
print("</head>")
print("<body>")
print("<h2>Hello, your haight is %s , and your weight %s</h2>"
      % (haight, weight))
print("<h2> Your BMI: %s </h2>"
      % bmi)

print("</body>")
print("</html>")
