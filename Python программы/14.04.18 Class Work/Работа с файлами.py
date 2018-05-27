with open('new.txt','w') as f:
    f.write(
    """
hello
world
    """) 
f.close()

with open('new.txt','r') as f:
    print(f.read()) 
f.close()
