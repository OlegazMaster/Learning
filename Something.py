import random

a = ["False", "False", " False", 
 "False", "False", " False", 
 "False", " False", "False", 
 "True"]
b = ["False", "False", " False", 
 "False", "False", " False", 
 "False", " False", "True", 
 "True"]
c = ["False", "False", " False", 
 "False", "False", " False", 
 "False", " True", "True", 
 "True"]
d = ["False", "False", " False", 
 "False", "False", " False", 
 "True", " True", "True", 
 "True"]
e = ["False", "False", " False", 
 "False", "False", "True", 
 "True", " True", "True", 
 "True"]
f = ["False", "False", " False", 
 "False", "True", "True", 
 "True", " True", "True", 
 "True"]
g =["False", "False", " False", 
 "True", "True", "True", 
 "True", " True", "True", 
 "True"]
o = ["False", "False", " True", 
 "True", "True", "True", 
 "True", " True", "True", 
 "True"]
w = ["False", "True", " True", 
 "True", "True", "True", 
 "True", " True", "True", 
 "True"]
n = ["True", "True", " True", 
 "True", "True", "True", 
 "True", " True", "True", 
 "True"]
get = float(input("Введите вероятность: ")) 

def func():
 if get == 0.1:
     print(a[random.randint(0,10)])
 elif get == 0.2:
     print(b[random.randint(0,10)]) 
 elif get == 0.3:
     print(c[random.randint(0, 10)])
 elif get == 0.4:
     print(d[random.randint(0, 10)])
 elif get == 0.5:
     print(e[random.randint(0, 10)])
 elif get == 0.6:
     print(f[random.randint(0, 10)])
 elif get == 0.7:
     print(g[random.randint(0, 10)])
 elif get == 0.8:
     print(o[random.randint(0, 10)])
 elif get == 0.9:
     print(w[random.randint(0, 10)])
 elif get == 1:
     print(n[random.randint(0, 10)])

func()