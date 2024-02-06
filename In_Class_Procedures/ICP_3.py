def main():
    # Create a tuple containing names of sisters and brothers
    sisters = ("Alice", "Emily", "Grace")
    brothers = ("John", "David", "Michael")
    print("Sisters:", sisters)
    print("Brothers:", brothers)

    # Join brothers and sisters tuples and assign it to siblings
    siblings = brothers + sisters
    print("Siblings:", siblings)

    # How many siblings do you have?
    num_siblings = len(siblings)
    print("Number of Siblings:", num_siblings)

    # Modify the siblings tuple and add the name of your father and mother
    father_and_mother = ("Joe", "Jane")
    family_members = siblings + father_and_mother
    print("Family Members:", family_members)


main()

