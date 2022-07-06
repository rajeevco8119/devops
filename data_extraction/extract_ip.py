sample = '''
This is first ip 10.64.13.12 and 
this is second ip 192.31.10.31 and there is one
invalid ip as well 1.0.1118.2 , we need to extract ips from
this sentence and arrange them in lexographic order.
just 23.100.12.34 and 14.341.32.13 are added here as well just for testing purpose
'''

def getIP(s):
    a = s.split(' ')
    ip_list = []
    b = '.'
    for i in a:
        if b in i and i[0].isdigit():
            ip_list.append(i)
    for a in ip_list:
        b = a.split('.')
        for j in b:
            if 0<int(j)<255:
                continue
            else:
                ip_list.remove(a)
                break
    print(ip_list)


getIP(sample)
