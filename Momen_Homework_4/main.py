myNumbers = [1, 2, 3, 4, 5, 4, 3, 2, 3, 1, 1, 1]

# key = myNumbers.count will count the uniqe unrepeted numbers that set(myNumbers) returns
mostFrequentNumber = max(set(myNumbers), key = myNumbers.count)

print(mostFrequentNumber)