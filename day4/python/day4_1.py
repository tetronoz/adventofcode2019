def has_doubles(num):
    for i in range(1, len(num)):
        if num[i] == num[i-1]:
            return True
    return False

def never_decreases(num):
    for i in range(1, len(num)):
        if int(num[i]) < int(num[i-1]):
            return False
    return True

count = 0
for n in range(246515, 739106):
    if has_doubles(str(n)) and never_decreases(str(n)):
        count += 1

print(count)