x= "ayaj anhsirk" 
nos="1234 5678" 
# reverese_words=[x[::-1] for x in x.split(" ")]
# print(reverese_words)
reverse=""
for char in nos[::-1]:
    print(char)
    reverse+=char
print(reverse)