string1 = "Hello"
string2 = input("Enter your Name: ")

string3 = string1 + " " + string2
print(string3)

string4 = ", welcome to Python programming"
string5 = string3 + string4
print(string5)

print("First character:", string5[0])

print("Last character:", string5[-1])

print("First 5 characters:", string5[:5])

print("Last 11 characters:", string5[-11:])

print("Reverse string:", string5[::-1])

print("Python:", string5[23:29])

print(string5)
print(string5.index("Python")) 

strM = "Python beginner tutorial"

print("Uppercase:", strM.upper())
print("Lowercase:", strM.lower())
print("Capitalize:", strM.capitalize())
print("Count of 't':", strM.count('t'))
print("Replace:", strM.replace("Python", "Machine Learning"))

t1 = (10, 20, 30)
t2 = (40, 50, 60)
t_combine = t1 + t2
print("Combined tuple:", t_combine)

print("Repeated tuple:", t_combine * 3)

print("3rd element:", t_combine[2])

print("First three elements:", t_combine[:3])

print("Last three elements:", t_combine[-3:])

