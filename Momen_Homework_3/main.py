# Total, Average and the Largest number

print()
values = []
total = 0
counter = 0
while counter < 5:
    enteredValue = input("Please enter a number: ")
    try:
        num = float(enteredValue)
        values.append(num)
        total += values[counter]
        counter += 1
    except:
        print()
        print("You have to enter a valid number")

average = total/len(values)
largest_number = max(values)

print("Total = " + str(total))
print("Average = " + str(average))
print("Largest number = " + str(largest_number))
print()

















