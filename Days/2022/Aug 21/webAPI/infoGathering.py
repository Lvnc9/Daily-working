#!/usr/bin/python
# Start
# Gathering Information from web APIs
# Modules
import requests
import shodan


shodan_api_key = "{zzcyAmXJy3OxcdQl98Jz7PLC8igPkQhA}"
api = shodan.Shodan(shodan_api_key)

target = "www.packtpub.com"

dnsresolve = "https://api.shodan.io/dns/resolve?hostnames=" +\
    target + "&key=" + shodan_api_key

def main():
    try:
        # First we need to resolve our target to an API
        resolved = requests.get(dnsresolve)
        host_ip = resolved.json()[target]
        
        # Then we need to do a shodan search on that ip
        host = api.host(host_ip)
        print(f"IP {host.get['ip_str']}")
        print(f"Organization: {host.get('org', 'n/a')}")
        print(f"Operating System: {host.get('os', 'n/a')}")
    
        # print all banners
        for item in host['data']:
            print(f"Port: {item['port']}")
            print(f"Banner: {item['data']}")
        
    
        # Print vuln information
        for item in host['vulns']:
            CVE = item.replace('!','')
            print('Vulns: %s' % item)
            exploits = api.exploits.search(CVE)
            for item in exploits['matches']:
                if item.get('cve')[0] == CVE:
                    print(item.get('description'))
    
    except Exception:
        'An error occured'
            
if __name__ == "__main__":
    main()
# End