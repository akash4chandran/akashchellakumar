string=input()
lengthofstring = len(string)
string1=''
countofstring=0
temp_string=[]
for i in range(lengthofstring):
    if(string[i] not in string1):
        string1 =string1+string[i]
        countofstring+=1
    else:
        string1=string[i]
        temp_string.append(countofstring)
        countofstring=1
temp_string.append(countofstring)
temp_string1 = temp_string[0]
for i in range(len(temp_string)):
    if(temp_string1<temp_string[i]):
        temp_string1 = temp_string[i]
print(temp_string1)
