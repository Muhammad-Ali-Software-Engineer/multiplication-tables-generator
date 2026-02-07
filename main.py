# 3. Write a program to generate multiplication tables from 2 to 20 and write it to different fies. Place these files in a folder for a 13-years old.
def generateTable(n):
    table = ""
    for i in range(1,11):
        # table += (f"{n} x {i} = {n*i}\n")
        
        if i<=9:
            table += (f"{n} x {i} = {n*i}\n")
        else:
            table += (f"{n} x {i} = {n*i}")
    
    f= open(f"tables/table_{n}.txt","w")
    f.write(table)
    f.close()

for i in range(2,21):
    generateTable(i) 