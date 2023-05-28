import re

try:
    
    file = open("sip.txt")
    for line in file:
        line = line.strip()
        emails = re.findall(r"@[\w-]+\.[\w.-]+", line)
        if(len(emails) > 0):
            g = open(f'{emails}.txt', 'a', encoding='utf-8')
            g.write(line + '\n')
            g.close()
            
except FileNotFoundError as e:
    print(e)    
    
#Djhuty