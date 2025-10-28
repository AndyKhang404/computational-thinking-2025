with open('data.txt', 'wt') as f:
    for _ in range(5):
        f.write(input("Input student name:") + '\n')

with open('data.txt', 'rt') as f:
    for line in f:
        print(line.strip())