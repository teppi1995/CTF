lines = []

with open ("key") as f:
    lines = f.readlines()
print(lines.reverse())
    
with open("reverse_key", "w") as f:
    for w in lines:
        f.write(w)


        
