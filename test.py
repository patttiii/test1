import urllib

print('start')

html_quelltext = urllib.urlopen('http://192.168.1.7/addons/xmlapi/statechange.cgi?ise_id=3152&new_value=true').read()

print('done')
