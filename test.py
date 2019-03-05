import urllib
html_quelltext = urllib.urlopen('http://192.168.1.7/addons/xmlapi/statechange.cgi?ise_id=3152&new_value=true').read()

result_sentence = 	"Licht eingeschaltet" 

current_session_id = intentMessage.session_id
hermes.publish_end_session(current_session_id, result_sentence)
