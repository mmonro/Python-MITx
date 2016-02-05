s = 'zcbbbgghkl'

count = 0

for letter in s:
    if letter in 'aeiouAEIOU':
        count = count + 1
        
print ('Number of vowels: ' + str(count))
