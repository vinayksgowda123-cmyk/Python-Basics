with open('data.txt','r') as file:
    content=file.read()
    print(content)

with open('data.txt','w') as file:
    file.write("Hello vinay")