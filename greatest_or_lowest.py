#A code to check 3 numbers
#taking input from user
a=int(input("Enter 3 numbers:"))
b=int(input())                  
c=int(input())
#int() is there because when we take some input, python (by default) takes it as string and thus causes more errors

#show the numbers
print(f"\nNumbers entered:\t{a}\t{b}\t{c}\n")


#Check and print the largest number
if a>b and a>c:
  print(f"{a}", end="")
elif b>a and b>c:
  print(f"{b}",end="")
elif c>a and c>b:
  print(f"{c}",end="")
else:
  print("A bit out of my syllabus TvT.")
  # if it is not possible to find the largest num
  
print(" is the greatest among the three.")


#now for the smallest number 
if a<b and a<c:
    print(f"{a}",end="")
elif b<a and b<c:
    print(f"{b}",end="")
elif c<a and c<b:
    print(f"{c}",end="")
else:
  print("A bit out of my syllabus too lol TvT.")
  # if it wasnt possible to distinguish the smallest number
  
print(" is the smallest among the three.")





