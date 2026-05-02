#print(len(a))
#rev = a[::-1] #(method 1)
#print(rev)

#reversed="".join(reversed(a)) (method 2)
#print(reversed)


text = input("Enter Text: ")

reversed_text = ""

# Start at index len-1, end before -1, step by -1

for i in range(len(text) - 1, -1, -1):


    reversed_text += text[i]

print(reversed_text)




