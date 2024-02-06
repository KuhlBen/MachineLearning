def main():
    it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
    A = {19, 22, 24, 20, 25, 26}
    B = {19, 22, 20, 25, 26, 24, 28, 27}
    age = [22, 19, 24, 25, 26, 24, 25, 24]

    # Find the length of the set it_companies
    length_it_companies = len(it_companies)
    print("Length of it_companies:", length_it_companies)

    # Add 'Twitter' to it_companies
    it_companies.add('Twitter')
    print("Updated it_companies with Twitter:", it_companies)

    # Insert multiple IT companies at once to the set it_companies
    it_companies.update(['LinkedIn', 'Netflix', 'Samsung'])
    print("Updated it_companies with LinkedIN, Netflix, and Samsung:", it_companies)

    # Remove one of the companies from the set it_companies
    it_companies.remove('IBM')
    print("Removed IBM from it_companies:", it_companies)

    # What is the difference between remove and discard?
    # - The remove method raises a KeyError if the element is not found, while discard does not.

    # Join A and B
    joined_set = A.union(B)
    print("Joined set of A and B:", joined_set)

    # Find A intersection B
    intersection_set = A.intersection(B)
    print("Intersection of A and B:", intersection_set)

    # Is A subset of B
    is_subset = A.issubset(B)
    print("Is A subset of B:", is_subset)

    # Are A and B disjoint sets
    are_disjoint = A.isdisjoint(B)
    print("Are A and B disjoint sets:", are_disjoint)

    # Join A with B and B with A
    joined_A_B = A.union(B)
    print("Joined A with B:", joined_A_B)
    joined_B_A = B.union(A)
    print("Joined B with A:", joined_B_A)

    # What is the symmetric difference between A and B
    symmetric_difference_set = A.symmetric_difference(B)
    print("Symmetric difference between A and B:", symmetric_difference_set)

    # Delete the sets completely
    del it_companies
    del A
    del B

    # Convert the ages to a set and compare the length of the list and the set
    age_set = set(age)
    length_age_list = len(age)
    length_age_set = len(age_set)
    print("Length of age list:", length_age_list)
    print("Length of age set:", length_age_set)


main()