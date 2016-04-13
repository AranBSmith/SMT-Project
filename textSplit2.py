
count = 0

with open("Hunchback_Parallel.txt", "r+") as file:
    lines = file.read()
    lines = str.splitlines(lines)
with open("hunchback_result.en", "w") as file2:
    with open("hunchback_result.fr", "w") as file:
        for sentence in lines:
            if count%2==1:
                file.write(sentence+"\n") 
            if count%2==0:
                file2.write(sentence+"\n") 
            count = count+1
