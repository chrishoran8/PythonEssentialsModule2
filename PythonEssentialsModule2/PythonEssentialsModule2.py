
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
