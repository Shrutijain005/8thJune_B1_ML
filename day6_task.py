#Assignment 1

# 2. Perform Following on Python Shell Window

# 5**9
# 3//2
# 7//3
# 7/3
# 6 == 6
# a = 20; a+= 30; a%=3; print(a)
# True * False
# True & False
# True and False
# ((6>3) and (7<4) or (18==3)) and (9>3)
# True is False
# False in ‘False’
# ((True == False) or (False > True)) and (False <= True)

print(5**9)
print(3//2)
print(7//3)
print(7/3)
print(6==6)
a = 20; a+= 30; a%=3; 
print(a)
print( True * False)
print( True & False)
print(True and False)
print(((6>3) and (7<4) or (18==3)) and (9>3))
print(True is False)
print("False" in "False")
print(((True == False) or (False > True)) and (False <= True))


# --------------------------------------------------------------------------

# 3. Try to get following output from two python strings
# s1 = “Nice to have it”
# s2 = “here”
# Expected output
# Nice to have it here

s1 = "Nice to have it"
s2 = "here"
print(s1+" "+s2)

# --------------------------------------------------------------------------

# 4. Given this nested list, use indexing to grab the word "hello"
# a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]

a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2][0])

# --------------------------------------------------------------------------

# 5. Try to insert above strings s1 and s2 in the list ‘a’ mentioned in
# que 4, in the beginning and end of it respectively

a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
s1 = "Nice to have it"
s2 = "here"
a.insert(0,s1)
a.append(s2)
print(a)

# --------------------------------------------------------------------------

# 6. Write a Python program to print out a set containing all the colours
# from color_list_1 which are not present in color_list_2.
# Test Data:
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# Expected Output:
# {'Black', 'White'}

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1.difference(color_list_2))

# --------------------------------------------------------------------------

#7. WAP to find if the given input string is Pangram or not
import string
str1=input("enter a string : ")
new_str=set(string.ascii_lowercase)
if ((set(str1)-new_str)==True):
    print("string is pangram")
else:    
    print("string is not pangram")

# --------------------------------------------------------------------------

# 8. Write a Python program that accepts an integer (n) and computes the
# value of n+nn+nnn.
# Sample value of n is 5
# Expected Result: 615


print(eval("{0}+{0}{0}+{0}{0}{0}".format(int(input("enter a number:"))))) 

# --------------------------------------------------------------------------

# 9. Write a program that accepts a comma separated sequence of words
# as input and prints the words in a comma-separated sequence after
# sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

l1=['without','hello','bag','world']
l1.sort()
print(l1)


# --------------------------------------------------------------------------

# 10. Write a Python function to find the name of person obtained
# highest marks in exam from given dictionary
# Example dictionary
# d = {‘Student’: [‘Rahul’, ‘Kishore’, ‘Vidhya’, ‘Raakhi’],
# ‘Marks’: [57,87,67,79]}
# Output: Kishore

d = {'Student': ['Rahul','Kishore','Vidhya','Raakhi'],'Marks': [57,87,67,79]}
m=(d['Marks'])
s=d['Student']
print(s[m.index(max(m))])
#############  OR   ######################3
print(d['Student'][(d['Marks']).index(max((d['Marks'])))])