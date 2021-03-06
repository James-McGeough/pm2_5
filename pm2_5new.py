import urllib, re

x = urllib.urlopen('http://www.aqichina.com').read()

y = re.findall('href="[\w]+/"', x)

cities = []

for href in y:
	cities.append(href[6:-2])

def get_pm2_5(c):
		u = urllib.urlopen('http://www.aqichina.com/' + c + '/').read()
		# print u
		pm = re.findall('PM2\.5:[\d]+[\.]?[\d]*', u)
		# print pm
		pm = pm[0][6:]
		# print pm
		return pm

context = dict()

# print cities

# get_pm2_5('anshan')

for city in cities:
	context[city] = get_pm2_5(city)

pol_sum = 0
pol_avg = None

for place in context:
	pol_sum += float(context[place])

pol_avg = pol_sum / len(context)

print pol_sum, pol_avg

