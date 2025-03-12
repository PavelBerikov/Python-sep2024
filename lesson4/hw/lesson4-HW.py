try:
    with open('emails.txt', 'r') as file:
       with open('gmail_list', 'a') as file2:
           for line in file:
                split = line.split()
                mail = split[-1]
                if 'gmail.com' in mail:
                    file2.write(mail+'\n')
except Exception as e:
    print(e)

