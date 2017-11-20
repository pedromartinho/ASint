import webapp2
from webapp2_extras import routes
from webapp2_extras import jinja2
from webapp2_extras import json
from string import Template


import library
import mimetypes


from jinja2 import Environment, select_autoescape, FileSystemLoader
env = Environment(
	loader = FileSystemLoader('./templates'),
    autoescape=select_autoescape(['html', 'xml', 'json'])
)


bd = library.library("mylib")

def sendFile(response, FileName):
	response.headers.add_header('Content-Type', mimetypes.guess_type(FileName)[0])
	f = open(FileName, 'r')
	response.write(f.read())
	f.close()
	

class MainPage(webapp2.RequestHandler):
    def get(self):
		sendFile(self.response, 'index.html')

class BooksListHandler(webapp2.RequestHandler):
	def get(self):
		#return
		s = ""
		books = bd.listBooks()['books']
		for b in books:
			s+= '<a href="/html/books/%s"> %s</a> <b>' %( b['id'], b['title'])
		temp = env.get_template('template-books.html')
		s= temp.render(books=books)
		
		self.response.write(s)
		
class newBookHandler(webapp2.RequestHandler):
	def get(self):
		sendFile(self.response, 'new.html')
	def post(self):
		bd.addBook(self.request.get('author'), self.request.get('title'), self.request.get('year'))
		s = ""
		for b in bd.listBooks()['books']:
			s+= '<a href="/html/books/%s"> %s</a> <b>' %( b['id'], b['title'])
		self.response.write(s)
		
		
		
class BookInfoHandler(webapp2.RequestHandler):
	def get(self, book_id):
		
		b = bd.getBook(int(book_id))
		self.response.write(b)
#		return
		f = open("show_book.html", 'r')
		templ_str = Template(f.read())		
		s = templ_str.substitute(n_score = b['votes'], n_title =  b['title'],  n_date= b['date'],  n_author= b['author'])


		self.response.write(s)

class AuthorsListHandler(webapp2.RequestHandler):
	def get(self):
		s = ""
		for b in bd.listAuthors()['authors']:
			s+= '<a href="/html/authors/%s"> %s</a> <b>' %( b, b)
		self.response.write(s)
		


class AuthorInfoHandler(webapp2.RequestHandler):
	def get(self, author_id):
		s = "<h1>"+ author_id+"</h1>"
		for b in bd.listBooks(author_id)['books']:
			s+= '<a href="/html/books/%s"> %s</a> <b>' %( b['id'], b['title'])
		self.response.write(s)
		

class BooksByAuthorHandler(webapp2.RequestHandler):
	def get(self, author_id):
		self.response.write('Books by Author %s!'% bd.listBooks(author_id))



class Books(webapp2.RequestHandler):
	def get(self):
		self.response.content_type='application/json'
		b=bd.listBooks()
		self.response.write(json.encode(b))

class BookByID(webapp2.RequestHandler):
	def get(self, book_id):
		self.response.content_type = 'application/json'
		b = bd.getBook(int(book_id))
		self.response.write(json.encode(b))

class BooksByAuthor(webapp2.RequestHandler):
	def get(self, author_id):
		self.response.content_type = 'application/json'
		b=bd.listBooks(author_id)
		self.response.write(json.encode(b))

class Authors(webapp2.RequestHandler):
	def get(self):
		self.response.content_type = 'application/json'
		b = bd.listAuthors()
		self.response.write(json.encode(b))

app = webapp2.WSGIApplication([
    webapp2.Route(r'/', MainPage),
    webapp2.Route(r'/html/newbook', newBookHandler),
    webapp2.Route(r'/html/books', BooksListHandler),
    webapp2.Route(r'/html/books/<book_id>', BookInfoHandler),
    webapp2.Route(r'/html/authors', AuthorsListHandler),
    webapp2.Route(r'/html/authors/<author_id>', AuthorInfoHandler),
    webapp2.Route(r'/html/authors/<author_id>/books', BooksByAuthorHandler),
	webapp2.Route(r'/data/books', Books ),
	webapp2.Route(r'/data/books/<book_id>', BookByID ),
	webapp2.Route(r'/data/authors/<author_id>/books', BooksByAuthor),
	webapp2.Route(r'/data/authors', Authors),

], debug=True)



def main():
	from paste import httpserver
	httpserver.serve(app, host='127.0.0.1', port='8080')

if __name__ == '__main__':
	main()

