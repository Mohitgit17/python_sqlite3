s = "Apple"
s = s.lower()

vowels = 0
letter = 0

for char in s :
    if 'a'<= char <= 'z':
        letter += 1
        if char in 'aeiou':
            vowels += 1

    
print("vowels are given string is :",vowels)
print("total leter in geven string is :",letter)