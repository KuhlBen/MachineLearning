def main():
    # Create and Sort the list of ages
    ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
    ages.sort()
    print(ages)

    # Find the Min and max ages and add back to the list
    minVal = min(ages)
    ages.append(minVal)
    maxVal = max(ages)
    ages.append((maxVal))

    # Re-sort the list
    ages.sort()
    print("The list after adding the min and max values into the list again:", ages)

    # Find the Median Age
    mid = ages[int(len(ages) / 2)]
    print("Median Value:", mid)

    # Find the Average Age
    sum = 0
    for age in ages:
        sum += age
    mean = sum / len(ages)
    print("Average Age:", mean)


main()
