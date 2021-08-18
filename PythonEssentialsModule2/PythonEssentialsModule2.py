
#task 2.1.1.18 solution
print("Programming","Essentials","in", sep="***", end="...")

#2.1.1.19 original
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

#bullet 1
print("     *\n", "   * *\n", "  *   *\n", " *     *\n", "***   ***\n", "  *   *\n", "  *   * \n", "  *****\n")
#or
print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")

#bullet 3 
print("    *     "*2)
print("   * *    "*2)
print("  *   *   "*2)
print(" *     *  "*2)
print("***   *** "*2)
print("  *   *   "*2)
print("  *   *   "*2)
print("  *****   "*2)

#operators

#apples lab

#bullet 1 and 2
john = 3
mary = 5
adam = 6

#bullet 3
print(john,mary,adam,sep=",")

#bullet 4
total_apples = john+adam+mary

#bullet 5
print(total_apples)

#average
appleAverage = (john + mary + adam) // 3
print(appleAverage)

#lab on converting km to miles

kilometers = 12.25 #normal assignment of 12.25 to new km variable
miles = 7.38 #normal assigment of 7.38 to new miles variable

miles_to_kilometers = miles/0.62 # evaluate expression of miles/0.62 and assign 
kilometers_to_miles = kilometers/1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers") # print statement
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

#maths formula lab 
x =  -1 #normal assignment
y=(3 * x**3) - (2 * x**2) + (3 * x) -1 # converstion of maths to python 
print("y =", float(y))

#SImple input output with casting
valueA = float(input("Value A Please? "))
valueB = float(input("Value B Please? "))

print(str(valueA+valueB))# output the result of addition here
print(str(valueA-valueB))# output the result of subtraction here
print(str(valueA*valueB))# output the result of multiplication here
print(str(valueA/valueB))# output the result of division here
print("\nThat's all, folks!")


#recipricol problem
x = float(input("Enter value for x: "))
y = 1/(x+1/(x+1/(x+1/(x))))
print("y =", y)

#hours minutes days modulo question
hour = int(input("Starting time (hours): ")) #receive 3 inputs
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
#example input 2(hours) 20(mins) 50(dura)

totalOriginalMins = (60 * hour) + mins #get original total minutes less dura:  140 mins
#print(totalOriginalMins) #test to make sure variable computes number of mins
totalNewMins = totalOriginalMins + dura #add dura to get new total of: 190 mins
#print(totalNewMins) #test to make sure total mins is correct
newHours = (int(totalNewMins/60)%24) #divide totalNewMins by 60 to get the new hours. Mod it with 24 so it removes longer than 24 hours
newMins = (mins+dura)%60 #to get the new mins, add the mins and dura together and mod it by 60 so it remvoes longer than 60 mins
print(newHours,newMins,sep=":") #output
