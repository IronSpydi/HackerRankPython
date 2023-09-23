""""
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s)
 of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically and
 print each name on a new line.
"""
if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    second_lowest_score = list(set([score[-1] for score in records]))
    second_lowest_score.sort()
    second_lowest_scorer_names = [sls_name[0] for sls_name in records if sls_name[-1] == second_lowest_score[1] ]
    second_lowest_scorer_names.sort()
    for name in second_lowest_scorer_names:
        print(name)


# refered code 

# a = [[input(), float(input())] for i in range(int(input()))]
# s = sorted(set([x[1] for x in a]))
# for name in sorted(x[0] for x in a if x[1] == s[1]):
#     print(name)

"""
find the smallest number that appears the most times in string
"""
# from collections import Counter
# def find_smallest_number_with_highest_count(input_string):
#     num_count = Counter(input_string)
#     max_val = 0
#     smallest_number = None
#     for key,value in num_count.items():
#         if value > max_val:
#             smallest_number = key
#             max_val = value
#     return smallest_number

# # Example usage:
# input_string = "1222344411555"

# result = find_smallest_number_with_highest_count(input_string)
# print("Smallest number with the highest count:", result)
