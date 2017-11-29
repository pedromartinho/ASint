import requests
import json
import datetime
filename = "help.txt"
fp = open(filename, 'w+')

req = requests.get('https://fenix.tecnico.ulisboa.pt/api/fenix/v1/degrees')
req_json = json.loads(req.text)
l = []
pk = 1
count = 1
aux =0
for entry in req_json:
    if (entry["acronym"] == "MEM" or aux == 1):
        aux = 1
        if count <=8:
            if count ==1:
                fp.write("<tr>\n")
            first = "\t<td>\n\t\t<div class=\"e1Div\">\n\t\t\t<input type=\"checkbox\" name=\""+entry["acronym"]+"\" id=\""+entry["acronym"]+"\" onchange=\"checkAddress(this)\"/>\n\t\t\t<label for=\"e1\">"+entry["acronym"]+"</label>\n\t\t</div>\n\t</td>"
            count = count+1
            fp.write(first)
        else:
            first = "\t<td>\n\t\t<div class=\"e1Div\">\n\t\t\t<input type=\"checkbox\" name=\""+entry["acronym"]+"\" id=\""+entry["acronym"]+"\" onchange=\"checkAddress(this)\"/>\n\t\t\t<label for=\"e1\">"+entry["acronym"]+"</label>\n\t\t</div>\n\t</td>"
            fp.write(first)
            fp.write("\n</tr>")
            count = 1

        fp.write("\n")
fp.close()
