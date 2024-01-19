# L5 binary search
maximum = int(input("Enter the highest number to search for: "))
number = int(input("Enter the number to search for: "))
minimum = 1
searches = 0
midpoint = (maximum + minimum)//2
while number != midpoint:
    if number < midpoint:
        maximum = midpoint-1
    else:
        minimum = midpoint + 1
    print("Maximum number is:", maximum)
    print("Minimum number is:",minimum);
    print("Midpoint is:", midpoint)
    searches = searches+1
    midpoint = (maximum + minimum)//2
searches = searches+1
print("The number to find was:", midpoint)
print("It took",searches,"searches to find the number")