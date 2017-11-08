total = 0;
with open('numbers.txt', 'r') as input:
    for line in input:
        try:
            num = float(line)
            total = total + num
        except ValueError:
            print('Hey! {} is not a number!'.format(line))

print (total)
