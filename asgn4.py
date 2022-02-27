#Question1
print('Question 1\n')
def towerofhanoi(n, source, destination, aux):
    if n == 0:
        return
    
    towerofhanoi(n-1, source, aux, destination)
    print(f"Move Disk {n} from {source} to {destination}")
    towerofhanoi(n-1, aux, destination, source)

#calling TOH funtion 
towerofhanoi(3, 'A', 'C', 'B')


#------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------


# Question 2
print('\nQuestion 2\n')
n = int(input("Enter the number of rows for Pascal's Triangle: "))
# creating the pascal function and using recursion
print("Using recursions to create pascal's triangle: ")


def pascal(n, initial_n=n):
    if n == 0:
        return

    pascal(n-1, initial_n)
    print('  '*(initial_n-n), end='')
    a = 1
    for i in range(1, n+1):
        print(a, end='   ')
        a = a * (n - i) // i
    print()


pascal(n)

# Using loops to create pascal's triangle
print("Using loops to create pascal's triangle:")
for line in range(1, n+1):
    print('  '*(n - line), end='')
    b = 1
    for i in range(1, line+1):
        print(b, end='   ')
        b = b * (line - i) // i
    print()


#------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------
    
    
   
# Question3
print('\nQuestion 3\n')
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the first number: "))

# ensuring that denominator is not zero
while num2 == 0:
    num2 = int(
        input("Denominator cannot be zero. Please enter a non zero number : "))

q, r = divmod(num1, num2)
l = [q, r]


def division():
    q, r = divmod(num1, num2)
    print(f"Questiont:{q}\nRemainder:{r}")


division()


print('\n(a)')
print(callable(division))


print('\n(b)')
if all(divmod(num1, num2)):
    print('All the values are non zero')
else:
    print('All the values are not non zero')


print('\n(c)')
l.extend([4, 5, 6])
print("After adding 4,5,6 : ", l)
filtered = filter(lambda n: n > 4, l)
print("Values greater than 4 are : ", list(filtered))


print('\n(d)')
s = set(l)
print(s)


print('\n(e)')
f_s = frozenset(s)
print("Immutable set : ", f_s)


print('\n(f)')
m = max(f_s)
print(hash(str(m)))



#------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------


# Question 4
print("\nQuestion 4\n")


class Student:

    def __init__(self, name, roll_no):
        self.name = name.title()
        self.roll_no = roll_no
        print("Student created")

    def __del__(self):
        print("Student deleted")


# storing data in the student class
s1 = Student("sheldon", 100)
s2 = Student("leanord", 104)
s3 = Student("rajesh", 108)

print('Deleting...')
del s2


#------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------


# Question 5
print("\nQuestion 5\n")


class Employees:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # defining a function to print the details of all employees
    def record(self):
        print("Employee Name : ", self.name.title())
        print("Employee Salary : ", self.salary)
        print("\n")


e1 = Employees("Mehak", 40000)
e2 = Employees("Ashok", 50000)
e3 = Employees("Viren", 60000)


print("Record of all employees\n")
e1.record()
e2.record()
e3.record()


print("(a)")
print("Updated record of Mehak:")
e1.Salary = 70000
e1.record()

print("(b)")
del e3
print("Record of Vivek deleted")



#------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------


# Question 6
print("\nQuestion 6\n")

def friendship(word1, word2):

    word1 = word1.lower()
    word2 = word2.lower()

    # checking whether all the letters are same in both words
    if sorted(word1) == sorted(word2):
        print("Your friendship is real")
    else:
        print("Your friendship is fake")

w1 = input("Friend 1, please enter your word : ")
w2 = input("Friend 2, please enter your word : ")


#verifying new word's meaningfulness from shopkeeper
a=input("Is the new word meaningful?(Y/N) : ")

if a.upper()=="N":
    print("Your friendship is fake.")
elif a.upper()=="Y":
    friendship(w1, w2)
else:
    ("Error!")





