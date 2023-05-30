import socket
print('''
  _                             _    
 | |                           | |   
 | |__   ___ _ __ ___  ___ _ __| | __
 | '_ \ / _ \ '__/ __|/ _ \ '__| |/ /
 | |_) |  __/ |  \__ \  __/ |  |   < 
 |_.__/ \___|_|  |___/\___|_|  |_|\_\
                                     
                                     
''')
def get_ip_info(ip):
    try:
        data = socket.gethostbyaddr(ip)
        hostname, aliases, addresses = data
        print('Hostname :', hostname)
        print('Aliases  :', aliases)
        print('Addresses:', addresses)
    except socket.herror:
        print('O IP {} não foi encontrado'.format(ip))
        get_ip_info('8.8.8.8')
        import requests

def get_ip_geo_info(ip):
    url = 'http://ip-api.com/json/' + ip
    r = requests.get(url)
    data = r.json()
    if data['status'] == 'success':
        print('País   :', data['country'])
        print('Estado :', data['regionName'])
        print('Cidade :', data['city'])
        print('Rua    :', data['query'])
        print('Bairro :', data['isp'])
        print('Capital do País:', data[country_capital])
        print('Moeda:', data['currency_name'])
        print('línguas:', data['languages'])
    else:
        print('O IP {} não foi encontrado'.format(ip))