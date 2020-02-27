import web
from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant')

web.config.debug = True
urls = ('/(.*)', 'Index')
app = web.application(urls, globals())

class Index:
	def __init__(self):
		self.render = web.template.render('templates/')

	def GET(self, name):
		return self.render.index("Wegenies python")

if __name__ == "__main__":
	app.run()
