import os

def get_ip_address(url):
    command = "host " + url
    process = os.popen(command)
    results = str(process.read())
    marker = results.find('has address') + 12
    return results[marker:].splitlines()[0]

textfile = open("newfile.txt", "w")
textfile1 = open("newfile1.txt", "w")
print('\nenter number of websites:')
n = int(input())
for i in range(n):
    print('\nenter url as website.com:')
    url = input()
    out = get_ip_address(url)
    textfile.write(out)
    textfile.write('\n')
    out1 = out.replace('16', '')
    textfile1.write(out1)
    textfile1.write('\n')

textfile.close()
textfile1.close()
