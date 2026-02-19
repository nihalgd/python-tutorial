a = "nihal goud"
print(len(a))

marks = [343,25,46,456,85525]
print(marks[0],[1])
print(len("marks"))

a = "nihal"
print(a[0:4])
print(a[-5:-1])

a = "nihhhal"
print(a.endswith("l"))
print(a.capitalize ())
print(a.replace( "n", "l"))
print(a.find ("h"))
print(a.count ("h"))

name = input("name")
print(name)
print(len(name))

student = ['nihal' , 'gourav', 'aryan' , "vicky" , "niharika"]
print(student [2])
print(student)
print(type(student))
print(len(student))

a = [ 1 , 2 , 3 ]
a.append(4)
a.reverse ()
a.sort(reverse=True)
print(a)

govind = {
    "name" : "nihal" ,
    "age" : 19 ,
    "place" : "indore",
}
print(dict)
print(type(govind))


count = 5
while count < 10 :
    print("nihaal")
    count = 10 + 1

    
count = 5
while count < 10 :
    print("nihaal" , count)
    count = 10 + 1

i = 1
while i <= 5:
    if (i == 3):
        break
    print("nihal")
    i  = i+1


# i = 0
# while i < 5:
#     if (i == 3):
#         i+1=1
#         continue
#     print("nihal")
#     i  = i+1
  

student = ['nihal' , 'gourav', 'aryan' , "vicky" , "niharika"]
for name in student:
    print(name)

for i in range (1,11):
    print(i)

a = 48
b = 18
while b != 0:
    a, b = b, a % b
print(a)

n = 25
x = n
for i in range(10):
    x = (x + n/x)/2
print(x)

print("helllo")
