import shodan

SHODAN_API_KEY = 'NxJs7lpgCiLNyDid3ojgvc8wPyNQfDfI'

api = shodan.Shodan(SHODAN_API_KEY)

ip_adr = input("Scan the following IP Address: ")

host = api.host(ip_adr)

print("""
        IP: {}
        Organization: {}
        Operating System: {}
""".format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))

for item in host['data']:
    print("""
              Port: {}
              Banner: {}

""".format(item['port'], item['data']))

