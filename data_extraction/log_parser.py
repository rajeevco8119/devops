# Extract the file name and corresponding no of bytes if response is 200 OK only

sample_logs = '''
192.168.1.2 - - [17/Sep/2013:22:18:19 -0700] "GET /abc HTTP/1.1" 404 201
192.168.1.2 - - [17/Sep/2013:22:18:19 -0700] "GET /wp/wp-content/themes/twentyeleven HTTP/1.1" 200 1406
192.168.1.2 - - [17/Sep/2013:22:18:27 -0700] "GET /wp/wp-content/themes/twentytwelve HTTP/1.1" 200 5325
192.168.1.2 - - [17/Sep/2013:22:18:27 -0700] "GET /wp/wp-content/themes/twentytwelve HTTP/1.1" 200 35292
192.168.1.2 - - [17/Sep/2013:22:18:27 -0700] "GET /wp/wp-content/themes/twentyeleven HTTP/1.1" 200 35242
192.168.1.3 - - [17/Sep/2013:22:18:27 -0700] "GET /wp/wp-content/themes/twentytwelve HTTP/1.1" 200 863
'''

def log_parser(s):
    a = s.strip().split('\n')
    file = {}
    for i in a:
        b = i.split(' ')
        if b[-2] in [str(200),str(201)]:
            file[b[6].split('/')[-1]] = 0
    for i in a:
        b = i.split(' ')
        if b[6].split('/')[-1] in file.keys():
            file[b[6].split('/')[-1]] += int(b[-1])
    print(file)
log_parser(sample_logs)
