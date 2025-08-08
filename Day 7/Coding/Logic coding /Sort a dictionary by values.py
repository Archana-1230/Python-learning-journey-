#Sort a dictionary by values

sorted_by_values = dict(sorted(marks.items(), key=lambda x: x[1]))
print(sorted_by_values)

#Output:{'English': 85, 'Math': 90, 'Science': 92}
