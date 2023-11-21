list_a = ['this', 'list', 'has', 'bad', 'words', 'in', 'it', 'bad', 'naughty', 'impish']
list_b = ['good', 'nice', 'friendly']
sol = list_a[1:7]
sol.remove('bad')
print('Updated list:', sol)
list.append(sol,'including')
print(sol)
sol.insert(2,'good')
print(sol)
sol.extend(list_b)
print(sol)

lst.remove(sol) ### take a look of the output, 1 will be removed.
print(f"lst after removing the first True is {lst}")

current = 21
last = 13

current = (current + last)
print(current)

last = (current-last)
print(last)



marks = [65,71,68,74,61]
total_marks = sum(marks)
print(total_marks)

