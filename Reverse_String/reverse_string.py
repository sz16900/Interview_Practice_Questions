string = "Primo is cool"
reversed_string = ""

for x in range(len(string)-1, -1, -1):
 	reversed_string = reversed_string + string[x]

print (reversed_string)