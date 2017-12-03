import fenixedu
import webapp2
from webapp2_extras import routes
from webapp2_extras import jinja2
from webapp2_extras import json
from string import Template
import mimetypes
from jinja2 import Environment, select_autoescape, FileSystemLoader



config = fenixedu.FenixEduConfiguration.fromConfigFile('fenixedu.ini')

client = fenixedu.FenixEduClient(config)
url = client.get_authentication_url()
print (url)

all_campus = client.get_spaces()

for campus in all_campus:
    print(">"+campus['name'])
    campus_info = client.get_space(campus['id'])
    buildings = campus_info['containedSpaces']
    for building in buildings:
        print("--->"+building['name'])
        building_info = client.get_space(building['id'])
        floor_rooms = building_info['containedSpaces']
        for floor_room in floor_rooms:
            if floor_room['type'] == "ROOM":
                room = floor_room
                print("--------->"+room['name'])
            if floor_room['type'] == "FLOOR":
                floor = floor_room
                print("------>" + floor['name'])
                floor_info = client.get_space(floor['id'])
                rooms = floor_info['containedSpaces']
                for room in rooms:
                    print("--------->" + room['name'])



#user = client.get_user_by_code('b050c37141750ce3ca786bdcf384997d645fd8fba144b298e6a0a6607ca0047b86e5b3b9ab9abc6e0dce287e78936d78b1940595b39313b1bc8b227a1316b614')

#person = client.get_person(user)

#classes = client.get_person_classes_calendar(user)

#print(classes)

#print(person)

env = Environment(
    loader=FileSystemLoader('./templates'),
    autoescape=select_autoescape(['html', 'xml', 'json'])
)

def sendFile(response, FileName):
    response.headers.add_header('Content-Type', mimetypes.guess_type(FileName)[0])
    f = open(FileName, 'r')
    response.write(f.read())
    f.close()

class MainPage(webapp2.RequestHandler):
    def get(self):
        sendFile(self.response, 'main.html')


class authentication(webapp2.RequestHandler):
    def get(self):
        url = "/login"
        print(url)
        s = "<head><title>Authentication</title></head>"
        s += '<h1> Click the button to authenticate: </h1><a href="%s">ta da</a>' % url
        self.response.write(s)

        #url = client.get_authentication_url()
        #print(url)
        #self.response.write(url)

class test(webapp2.RequestHandler):
    def get(self):
        url = client.get_authentication_url()
        print(url)
        self.redirect("%s" % url)

class HomePage(webapp2.RequestHandler):
    def get(self):
        code = self.request.get('code')
        user = client.get_user_by_code('%s' % code)
        person = client.get_person(user)
        s = "<head><title>Authentication Done</title></head>"
        s += '<h1></h1><script>document.getElementsByTagName("h1")[0].innerText = "Authentication successful for %s";</script></body></html>' % person.get('displayName')
        self.response.write(s)

app = webapp2.WSGIApplication([
    webapp2.Route(r'/', MainPage),
    webapp2.Route(r'/authentication', authentication),
    webapp2.Route(r'/login', test),
    webapp2.Route(r'/istspaces', HomePage),
], debug=True)


def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8070')


if __name__ == '__main__':
    main()