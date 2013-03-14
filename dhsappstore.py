import webapp2
import cgi
import random
import urllib
import datetime
import jinja2

from google.appengine.ext import db
from google.appengine.api import users


class NewApp(db.Model):
	name = db.StringProperty()
	creator = db.StringProperty()
	description = db.StringProperty(multiline=True)
	image = db.StringProperty()
	id = db.IntegerProperty()
	ranktime = db.IntegerProperty()
	rankscore = db.IntegerProperty()
	rank = db.FloatProperty()
	
class Review(db.Model):
	author = db.StringProperty()
	appname = db.StringProperty()
	content = db.StringProperty(multiline = True)
	date = db.DateTimeProperty(auto_now_add=True)

def guestbook_key(app_name=None):
  return db.Key.from_path('app_name', app_name)
	
class MainPage(webapp2.RequestHandler):
  def get(self):
	  self.response.out.write('''
	  
	<!DOCTYPE html>
    <head>
        <meta charset="utf-8">
        <title>D'App Store</title>
        <meta name="viewport" content="width=device-width">

		<link rel="icon" href = "/static/favicon.ico">
        <link rel="stylesheet" href="static/stylesheets/main.css">
    </head>
    <body>
        
		<header class = "center blue">
			<h1> D'APP STORE</h1>
		</header>
		
		<!-- Navigational sidebar -->
		
		<div id = "sidebar" class = "center blue">
		<ul>
			<li><a href = "/learning" >Learning</a></li>
			<li><a href = "/utilities" >Utilities</a></li>
			<li><a href = "/leisure" >Leisure</a></li>
			<li><a href = "/cca" >CCA</a></li>
			<li><a href = "/about" >About</a></li>
			<li><a href = "/contact" >Contact</a></li>
		</ul>
		</div>
		
		<!-- Main content goes here (Main page) -->
		
		<div id = "content" class = "center blue">
			<h2>Welcome to the DHS App Store!</h2>
			
			<figure class = "center red" id = "showcase">
			<h3>  App Showcase!  </h3>
			<img src = "/static/img/phonylu.jpg" alt = "App Showcase" id = "showcase">
			<p>Phony Lu the great leader of all, he shall let us rise and rise again, from lamb become lion.</p>
			<p>The night is never ending.</p>
			</figure>
		</div>
		
		<div id = "footer" class = "clear center">
			<p>DHS App Store</p>
			<p>&copy DHS Year 5 Computing Class 2013</p>
		</div>

        <!-- Google Analytics-->
        <script>
            var _gaq=[['_setAccount','UA-XXXXX-X'],['_trackPageview']];
            (function(d,t){var g=d.createElement(t),s=d.getElementsByTagName(t)[0];
            g.src=('https:'==location.protocol?'//ssl':'//www')+'.google-analytics.com/ga.js';
            s.parentNode.insertBefore(g,s)}(document,'script'));
        </script>
    </body>
</html>
	  
	  
	  '''
	)
	  
	#
	#
	#About section
	#
	#
	#
	  
	  
class About(webapp2.RequestHandler):	  
	def get(self):
	  self.response.out.write('''
	<!DOCTYPE html>
    <head>
        <meta charset="utf-8">
        <title>D'App Store</title>
        <meta name="viewport" content="width=device-width">

		<link rel="icon" href = "/static/favicon.ico">
        <link rel="stylesheet" href="/static/stylesheets/main.css">
    </head>
    <body>
        
		<header class = "center blue">
			<h1> D'APP STORE</h1>
		</header>
		
		<!-- Navigational sidebar -->
		
		<div id = "sidebar" class = "center blue">
		<ul>
			<li><a href = "/">Home</a></li>
			<li><a href = "/learning" >Learning</a></li>
			<li><a href = "/utilities" >Utilities</a></li>
			<li><a href = "/leisure" >Leisure</a></li>
			<li><a href = "/cca" >CCA</a></li>
			<li><a href = "/contact" >Contact</a></li>
		</ul>
		</div>
		
		<div id = "content" class = "about blue justified">
			
			<h2>About This App Store</h2>
			
			<p> This app store is still in development, for example, the front page image/text are still currently placeholders. Sorry!
			Check back soon for new progress on this "App Store" :)</p>
			
			<p> To do: Backend (Database), Ranking, (Hopefully) Individual Pages + reviews, Content improvement, Getting screenshots/descriptions for the apps.</p>
			
			<p>This "App Store" was made to help organise, access and let Dunmanians learn more about the different apps created by computing students to help the school.</p>
			
			<p>In this "App Store", you can help to rank the apps displayed through an easy drop-down selection list. This ranking will be shown with the app's infomation.</p>
			
			<p>Later modifications include reviews so people will better know what to expect out of the app, as well as possibly reporting functions to allow a centralised location to send bug reports in.</p>			
			
			<p>You can select a catagory though the navigational menu on the left to view all the apps listed under that catagory.</p>
			
			<p>The front page randomly showcases an app to help all the different apps on this site to gain popularity. It can also help introduce you to a new app you haven't tried out before!</p>
			
			<p>Click on home in the navigational menu to return to the front page of this app! </p>
			
			<p>If you spot any bugs, typos and such or have any ideas for improvement, you can head over to the Contact page and let me know about it.</p>
			
			<p>I hope you will find D'App Store to be of great help to you by introducing you to new apps that will help make your life easier.</p>
			
			<p>This "App Store" was done by Alvin Yan. All the apps that are linked to by this "App Store" are productions of other computing students.</p>
			
		</div>
		
		<div id = "footer" class = "clear center">
			<p>DHS App Store</p>
			<p>&copy DHS Year 5Computing Class 2013</p>
		</div>
		
	</body>
	</html>
	  '''
	 )
		
		
		#
		#
		#Contact section
		#
		#
		
		
class Contact(webapp2.RequestHandler):	  
	def get(self):
	  self.response.out.write('''
	  <!DOCTYPE html>
    <head>
        <meta charset="utf-8">
        <title>D'App Store</title>
        <meta name="viewport" content="width=device-width">

		<link rel="icon" href = "/static/favicon.ico">
        <link rel="stylesheet" href="/static/stylesheets/main.css">
    </head>
    <body>
		<header class = "center blue">
			<h1> D'APP STORE</h1>
		</header>
		
		<!-- Navigational sidebar -->
		
		<div id = "sidebar" class = "center blue">
		<ul>
			<li><a href = "/">Home</a></li>
			<li><a href = "/learning" >Learning</a></li>
			<li><a href = "/utilities" >Utilities</a></li>
			<li><a href = "/leisure" >Leisure</a></li>
			<li><a href = "/cca" >CCA</a></li>
			<li><a href = "/about" >About</a></li>
		</ul>
		</div>
		
		<div id = "content" class = "about blue justified">
			
			<h2>Contacts</h2>
			<p>You can email me regarding any issues with D'App Store by sending me an email at yan.hongyao.alvin(at)dhs.sg.</p>
			<p>If there is any info regarding the other apps you have visited, you can contact me and I will help to send the feedback to them.</p>
			
		</div>
		
		<div id = "footer" class = "clear center">
			<p>DHS App Store</p>
			<p>&copy DHS Year 5 Computing Class 2013</p>
		</div>
		
	</body>
	</html>
	  '''
	)
	  
	  #
	  #
	  #Learning
	  #
	  #
	  #  
	  
	  
class Learning(webapp2.RequestHandler):	  
	def get(self):
	  self.response.out.write('''
	<!DOCTYPE html>
    <head>
        <meta charset="utf-8">
        <title>D'App Store</title>
        <meta name="viewport" content="width=device-width">
		<link rel="icon" href = "/static/favicon.ico">
        <link rel="stylesheet" href="/static/stylesheets/main.css">
    </head>
    <body>
		<header class = "center blue">
			<h1> D'APP STORE</h1>
		</header>
		
		<!-- Navigational sidebar -->
		
		<div id = "sidebar" class = "center blue">
		<ul>
			<li><a href = "/">Home</a></li>
			<li><a href = "/utilities" >Utilities</a></li>
			<li><a href = "/leisure" >Leisure</a></li>
			<li><a href = "/cca" >CCA</a></li>
			<li><a href = "/about" >About</a></li>
			<li><a href = "/contact" >Contact</a></li>
		</ul>
		</div>
		
		<div id = "content" class = "about blue justified applist">
			
			<a href = "/cip">
			<div class = "app">
				<p>DHS CIP Opportunities</p>
			</div>
			</a>
			
			<a href = "/nowork">
			<div class = "app">
				<p>DHS NoWork!</p>
			</div>
			</a>
			
			<a href = "/quora">
			<div class = "app">
				<p>DHS Quora</p>
			</div>
			</a>
			
			<a href = "/lecture">
			<div class = "app">
				<p>DHS Lecture</p>
			</div>
			</a>
			
		</div>
		
		<div id = "footer" class = "clear center">
			<p>DHS App Store</p>
			<p>&copy DHS Year 5 Computing Class 2013</p>
		</div>
		
	</body>
	</html>
	  '''
	)
	  
	  #
	  #
	  #Leisure
	  #
	  #
	  
class Utilities(webapp2.RequestHandler):	  
	def get(self):
	  self.response.out.write('''
	  <!DOCTYPE html>
    <head>
        <meta charset="utf-8">
        <title>D'App Store</title>
        <meta name="viewport" content="width=device-width">
		<link rel="icon" href = "/static/favicon.ico">
        <link rel="stylesheet" href="/static/stylesheets/main.css">
    </head>
    <body>
        
		<header class = "center blue">
			<h1> D'APP STORE</h1>
		</header>
		
		<!-- Navigational sidebar -->
		
		<div id = "sidebar" class = "center blue">
		<ul>
			<li><a href = "/">Home</a></li>
			<li><a href = "/learning" >Learning</a></li>
			<li><a href = "/leisure" >Leisure</a></li>
			<li><a href = "/cca" >CCA</a></li>
			<li><a href = "/about" >About</a></li>
			<li><a href = "/contact" >Contact</a></li>
		</ul>
		</div>
		
		<div id = "content" class = "about blue justified applist">
			
			<a href = "/lostnfound">
			<div class = "app">
				<p>DHS LostnFound</p>
			</div>
			</a>
			
			<a href = "/announcement">
			<div class = "app">
				<p>DHS Announcements</p>
			</div>
			</a>
			
			<a href = "/feedback">
			<div class = "app">
				<p>DHS Feedback</p>
			</div>
			</a>
			
			<a href = "/temperature">
			<div class = "app">
				<p>DHS Temperature</p>
			</div>
			</a>
			
			<a href = "/tickets">
			<div class = "app">
				<p>DHS Tickets</p>
			</div>	
			</a>
			
			<a href = "/rollcall">
			<div class = "app">
				<p>DHS Rollcall</p>
			</div>
			</a>
			
			<a href = "/canteen">
			<div class = "app">	
				<p>Canteen Review</p>
			</div>
			</a>
			
			<a href = "/share">
			<div class = "app">
				<p>DHS Share</p>
			</div>
			</a>
			
			<a href = "/treasurer">
			<div class = "app">
				<p>Treasurer's Kit</p>
			</div>
			</a>
			
			<a href = "/report">
			<div class = "app">
				<p>DHS Report</p>
			</div>
			</a>
			
			<a href = "/response">
			<div class = "app">
				<p>DHS Responses</p>
			</div>
			</a>
			
		</div>
		
		<div id = "footer" class = "clear center">
			<p>DHS App Store</p>
			<p>&copy DHS Year 5 Computing Class 2013</p>
		</div>
		
	</body>
	</html>
	  '''
	)
	  
	  #
	  #
	  # CCA section
	  #
	  #
	  
class Leisure(webapp2.RequestHandler):	  
	def get(self):
	  self.response.out.write('''
	  <!DOCTYPE html>
      <head>
        <meta charset="utf-8">
        <title>D'App Store</title>
        <meta name="viewport" content="width=device-width">
		<link rel="icon" href = "/static/favicon.ico">
        <link rel="stylesheet" href="/static/stylesheets/main.css">
      </head>
      <body>
        
		<header class = "center blue">
			<h1> D'APP STORE</h1>
		</header>
		
		<!-- Navigational sidebar -->
		
		<div id = "sidebar" class = "center blue">
		<ul>
			<li><a href = "/">Home</a></li>
			<li><a href = "/learning" >Learning</a></li>
			<li><a href = "/utilities" >Utilities</a></li>
			<li><a href = "/cca" >CCA</a></li>
			<li><a href = "/about" >About</a></li>
			<li><a href = "/contact" >Contact</a></li>
		</ul>
		</div>
		
		<div id = "content" class = "about blue justified applist">
			
			<a href = "/gag">
			<div class = "app">
				<p>DHS Gag</p>
			</div>
			</a>
			
			<a href = "/sendasmile">
			<div class = "app">
				<p>DHS Send A Smile</p>
			</div>
			</a>
			
			<a href = "/jokes">
			<div class = "app">
				<p>DHS Jokes</p>
			</div>
			</a>
			
			<a href = "/know">
			<div class = "app">
				<p>DHS Get-to-know-each-other</p>
			</div>
			</a>
			
			<a href = "/art">
			<div class = "app">
				<p>Art Space</p>
			</div>
			</a>
			
			<a href = "/crushes">
			<div class = "app">
				<p>DHS Crushes</p>
			</div>
			</a>
			
		</div>
		
		<div id = "footer" class = "clear center">
			<p>DHS App Store</p>
			<p>&copy DHS Year 5 Computing Class 2013</p>
		</div>
		
	</body>
	</html>
	  '''
	)
	
class Cca(webapp2.RequestHandler):	  
	def get(self):
	  self.response.out.write('''
	  <!DOCTYPE html>
      <head>
        <meta charset="utf-8">
        <title>D'App Store</title>
        <meta name="viewport" content="width=device-width">
		<link rel="icon" href = "/static/favicon.ico">
        <link rel="stylesheet" href="/static/stylesheets/main.css">
      </head>
      <body>
        
		<header class = "center blue">
			<h1> D'APP STORE</h1>
		</header>
		
		<!-- Navigational sidebar -->
		
		<div id = "sidebar" class = "center blue">
		<ul>
			<li><a href = "/">Home</a></li>
			<li><a href = "/learning" >Learning</a></li>
			<li><a href = "/leisure" >Leisure</a></li>
			<li><a href = "/utilities" >Utilities</a></li>
			<li><a href = "/about" >About</a></li>
			<li><a href = "/contact" >Contact</a></li>
		</ul>
		</div>
		
		<div id = "content" class = "about blue justified applist" >
			
			<a href = "/dhsjab">
			<div class = "app">
				<p>DHSJAB Parade State</p>
			</div>
			</a>
			<a href = "/interact">
			<div class = "app">
				<p>DHS CCA Interaction</p>
			</div>
			</a>
			
		</div>
		
		<div id = "footer" class = "clear center">
			<p>DHS App Store</p>
			<p>&copy DHS Year 5 Computing Class 2013</p>
		</div>
		
	</body>
	</html>
	  '''
	)

	

class Admin(webapp2.RequestHandler):	  
	def get(self):
	  self.response.out.write('''
		<!DOCTYPE html>
		<body>
		<form action = "/addapp" method = "post">
		<p> Form for entering info for apps </p>
		Name: <input type = "text" name = "name"><br />
		Creator: <input type = "text" name = "creator"><br />
		Description: <textarea name = "description" rows"2" cols = "100"></textarea><br />
		Image URL: <input type = "text" name = "image"><br />
		Type: <input type = "text" name = "type"><br />
		ID: <input type = "number" name = "id"></br />
		<input type = "submit" value = "Submit app info">
		</form>
		</body>
		</html> ''')

class Addapp(webapp2.RequestHandler):
	def post(self):
		a_name=cgi.escape(self.request.get('name'))
		a_creator=cgi.escape(self.request.get('creator'))
		a_description=cgi.escape(self.request.get('description'))
		a_url=cgi.escape(self.request.get('url'))
		a_type=cgi.escape(self.request.get('type'))
		a_id=cgi.escape(self.request.get('id'))
		a_ranktime = 0
		a_rankscore = 0
		app = NewApp(name = a_name,
				  creator = a_creator,
				  description = a_description,
				  url = a_url,
				  type = a_type,
				  id = int(a_id),
				  ranktime = a_ranktime,
				  rankscore = a_rankscore)
		app.put()
		print ""

		
class Cip(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('''
	  <!DOCTYPE html>
      <head>
        <meta charset="utf-8">
        <title>D'App Store</title>
        <meta name="viewport" content="width=device-width">
		<link rel="icon" href = "/static/favicon.ico">
        <link rel="stylesheet" href="/static/stylesheets/main.css">
      </head>
      <body>
        
		<header class = "center blue">
			<h1> D'APP STORE</h1>
		</header>
		
		<!-- Navigational sidebar -->
		
		<div id = "sidebar" class = "center blue">
		<ul>
			<li><a href = "/">Home</a></li>
			<li><a href = "/learning" >Learning</a></li>
			<li><a href = "/leisure" >Leisure</a></li>
			<li><a href = "/utilities" >Utilities</a></li>
			<li><a href = "/cca">CCA</a></li>
			<li><a href = "/about" >About</a></li>
			<li><a href = "/contact" >Contact</a></li>
		</ul>
		</div>
		
		<div id = "content" class = "center blue">
		<a href = "/learning"> <- Back</a><br /><br />
		<a href = "http://cip.dhs.sg"><img class = "screenshot" src = "/static/img/cip.jpg"></a>
		<h3 class = "desc">''')
		self.response.out.write(10)
		self.response.out.write('''
		<img id = "starpic" src = "/static/img/star.jpg"></h4>
		<h3 class = "desc">By: Nie Shuyue<h3>
		<h3 class = "desc">Description: </h3>
		<p>A webpage for students to post different CIP opportunities and the updates. If students want to find CIP to do, they can go to the webpage to view the opportunities and register online so that students do not have to find the CIP emails in the mail box. Make the life easier for both students and the CIP organizers/students.</p>
	
		Reviews here
		Form here
		</div>
		<div id = "footer" class = "clear center">
			<p>DHS App Store</p>
			<p>&copy DHS Year 5 Computing Class 2013</p>
		</div>
		</body>
		</html>
		''')
		
class Nowork(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('''
	  <!DOCTYPE html>
      <head>
        <meta charset="utf-8">
        <title>D'App Store</title>
        <meta name="viewport" content="width=device-width">
		<link rel="icon" href = "/static/favicon.ico">
        <link rel="stylesheet" href="/static/stylesheets/main.css">
      </head>
      <body>
        
		<header class = "center blue">
			<h1> D'APP STORE</h1>
		</header>
		
		<!-- Navigational sidebar -->
		
		<div id = "sidebar" class = "center blue">
		<ul>
			<li><a href = "/">Home</a></li>
			<li><a href = "/learning" >Learning</a></li>
			<li><a href = "/leisure" >Leisure</a></li>
			<li><a href = "/utilities" >Utilities</a></li>
			<li><a href = "/cca">CCA</a></li>
			<li><a href = "/about" >About</a></li>
			<li><a href = "/contact" >Contact</a></li>
		</ul>
		</div>
		
		<div id = "content" class = "center blue">
		<a href = "/learning"> <- Back</a><br /><br />
		<a href = "http://nowork.dhs.sg"><img class = "screenshot" src = "/static/img/nowork.jpg"></a>
		<h3 class = "desc">''')
		self.response.out.write(10)
		self.response.out.write('''
		<img id = "starpic" src = "/static/img/star.jpg"></h4>
		<h3 class = "desc">By: Justin Leow<h3>
		<h3 class = "desc">Description: </h3>
		<p>DHS NoWork! is a notification sharing centre where staff and students can create groups by adding in their classmates, and proceed to post notifications and/or homework reminders to the entire group through a very simple sharing system. Users who open the webapp will immediately see notifications and/or homework reminders, and can proceed to mark though a "noted" or a "done" field, which the group admin will be able to check and be actively informed of the progress of the class.</p>
		''')
		
		reviews = db.GqlQuery("SELECT * "
							  "FROM Review")
		for review in reviews:
			self.response.out.write(
            '<b>%s</b> wrote:' % review.author)
			self.response.out.write('<blockquote>%s</blockquote>' % cgi.escape(review	.content))
			
		self.response.out.write('''
		<form action="/review?app_name=nowork" method="post">
            <div><textarea name="content" rows="3" cols="60"></textarea></div>
            <div><input type="submit" value="Submit Review"></div>
        </form>
		  
		</div>
		<div id = "footer" class = "clear center">
			<p>DHS App Store</p>
			<p>&copy DHS Year 5 Computing Class 2013</p>
		</div>
		</body>
		</html>
		''')
		
class Quora(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('''
	  <!DOCTYPE html>
      <head>
        <meta charset="utf-8">
        <title>D'App Store</title>
        <meta name="viewport" content="width=device-width">
		<link rel="icon" href = "/static/favicon.ico">
        <link rel="stylesheet" href="/static/stylesheets/main.css">
      </head>
      <body>
        
		<header class = "center blue">
			<h1> D'APP STORE</h1>
		</header>
		
		<!-- Navigational sidebar -->
		
		<div id = "sidebar" class = "center blue">
		<ul>
			<li><a href = "/">Home</a></li>
			<li><a href = "/learning" >Learning</a></li>
			<li><a href = "/leisure" >Leisure</a></li>
			<li><a href = "/utilities" >Utilities</a></li>
			<li><a href = "/cca">CCA</a></li>
			<li><a href = "/about" >About</a></li>
			<li><a href = "/contact" >Contact</a></li>
		</ul>
		</div>
		
		<div id = "content" class = "center blue">
		<a href = "/learning"> <- Back</a><br /><br />
		<a href = "http://qna.dhs.sg"><img class = "screenshot" src = "/static/img/quora.jpg"></a>
		<h3 class = "desc">''')
		self.response.out.write(10)
		self.response.out.write('''
		<img id = "starpic" src = "/static/img/star.jpg"></h4>
		<h3 class = "desc">By: Wang Zexin<h3>
		<h3 class = "desc">Description: </h3>
		<p>An app for dunmanians to ask questions and help others</p>
	
		Reviews here
		Form here
		</div>
		<div id = "footer" class = "clear center">
			<p>DHS App Store</p>
			<p>&copy DHS Year 5 Computing Class 2013</p>
		</div>
		</body>
		</html>
		''')	
	
class Lecture(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('Hello!')

class Lostnfound(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('Hello!')

class Announcement(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('Hello!')		

class Feedback(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('Hello!')

class Temperature(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('Hello!')			
		
class Tickets(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('Hello!')

class Rollcall(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('Hello!')

class Canteen(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('Hello!')			
		
class Share(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('Hello!')	

class Treasurer(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('Hello!')		

class Report(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('Hello!')			

class Responses(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('Hello!')	

class Gag(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('Hello!')

class Sendasmile(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('Hello!')
	
class Jokes(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('Hello!')

class Know(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('Hello!')		
	
class Art(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('Hello!')	

class Crushes(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('Hello!')	

class Dhsjab(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('Hello!')	

class Interact(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('Hello!')		
	
class Submitreview(webapp2.RequestHandler):
	def post(self):
		app_name = str(self.request.get('app_name'))
		review = Review()
		if users.get_current_user():
			review.author = users.get_current_user().nickname()
		review.content = self.request.get('content')
		review.appname = app_name
		review.put()
		
	
app = webapp2.WSGIApplication([('/', MainPage),
							   ('/about', About),
							   ('/leisure', Leisure),
							   ('/contact', Contact),
							   ('/utilities', Utilities),
							   ('/learning', Learning),
							   ('/cca', Cca),
							   ('/admin', Admin),
							   ('/addapp', Addapp),
							   ('/cip', Cip),
							   ('/nowork', Nowork),
							   ('/quora', Quora),
							   ('/lecture', Lecture),
							   ('/lostnfound', Lostnfound),
							   ('/announcement', Announcement),
							   ('/feedback', Feedback),
							   ('/temperature', Temperature),
							   ('/tickets', Tickets),
							   ('/rollcall', Rollcall),
							   ('/canteen', Canteen),
							   ('/share', Share),
							   ('/treasurer', Treasurer),
							   ('/report', Report),
							   ('/responses', Responses),
							   ('/gag', Gag),
							   ('/sendasmile', Sendasmile),
							   ('/jokes', Jokes),
							   ('/know', Know),
							   ('/art', Art),
							   ('/crushes', Crushes),
							   ('/Dhsjab', Dhsjab),
							   ('/Interact', Interact),
							   ('/review', Submitreview)
							   ]
							   ,
                               debug=True)