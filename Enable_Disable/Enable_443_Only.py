import subprocess as sp

def allow_443_incoming():
	sp.call('sudo iptables -F', shell=True)
	sp.call('sudo iptables -A INPUT -p tcp --dport 443 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT', shell=True)
	sp.call('sudo iptables -A INPUT -m conntrack -j ACCEPT  --ctstate RELATED,ESTABLISHED', shell=True)
	# sp.call('sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT', shell=True)
	sp.call('sudo iptables -A INPUT -j DROP', shell=True)
	# sp.call('sudo iptables -A OUTPUT -m state --state ESTABLISHED,RELATED -j ACCEPT', shell=True)
	# sp.call('sudo iptables -A OUTPUT -j DROP', shell=True)
	sp.call('sudo iptables -A FORWARD -m state --state ESTABLISHED,RELATED -j ACCEPT', shell=True)
	sp.call('sudo iptables -A FORWARD -j DROP', shell=True)


if __name__ == '__main__':

	allow_443_incoming()
