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
	rankscore = db.IntegerProperty()
	ranktime = db.IntegerProperty()
	
class Review(db.Model):
	author = db.StringProperty()
	appname = db.StringProperty()
	content = db.StringProperty(multiline = True)
	date = db.DateTimeProperty(auto_now_add=True)

def review_key(appname=None):
	return db.Key.from_path('AppName', appname)
	
def rank_key(appname=None):
	return db.Key.from_path('App_Name', appname)
	
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
			<li><a href = "/">Home</a></li>
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
			<h3>Use the links in the navigational bar to view the apps and get started!</h3>
			<h3>I hope you find some apps that you like :)</h3>
			<h3> Version 1 of D'App Store has finally been completed! Enjoy your stay here!<h3>
		</div>
		
		<div id = "footer" class = "clear center">
			<p>DHS App Store</p>
			<p>&copy DHS Year 5 Computing Class 2013</p>
		</div>

        <!-- Google Analytics-->
        <script>
            var _gaq=[['_setAccount','UA-39299614-1'],['_trackPageview']];
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
			<li><a href = "/about" >About</a></li>
			<li><a href = "/contact" >Contact</a></li>
		</ul>
		</div>
		
		<div id = "content" class = "about blue justified">
			
			<h2>About This App Store</h2>
			
			<p> The App Store is currently running in Open Beta - Try it out, help report any feedback to me! :)</p>
			
			<p>This App Store was made to help organise, access and let Dunmanians learn more about the different apps created by computing students to help the school.</p>
			
			<p>In this App Store, you can help to rank the apps displayed through an easy drop-down selection list. This ranking will be shown with the app's infomation.</p>
			
			<p>You can also post reviews for all the different apps, letting your schoolmates have a better overall view on how well the app works! :)</p>			
			
			<p>You can select a catagory though the navigational menu on the left to view all the apps listed under that catagory.</p>
			
			<p>Click on home in the navigational menu to return to the front page of this app! </p>
			
			<p>If you spot any bugs, typos and such or have any ideas for improvement, you can head over to the Contact page and let me know about it.</p>
			
			<p>I hope you will find D'App Store to be of great help to you by introducing you to new apps that will help make your life easier.</p>
			
			<p>This "App Store" was done by Alvin Yan. All the apps that are linked to by this "App Store" are productions of other computing students.</p>
			
			<p>Many thanks, of course, to Mr Gi who helped teach the programming knowledge that aided me in creating this app store.</p>
			
		</div>
		
		<div id = "footer" class = "clear center">
			<p>DHS App Store</p>
			<p>&copy DHS Year 5Computing Class 2013</p>
		</div>
		<script type="text/javascript">
		  var _gaq = _gaq || [];
		  _gaq.push(['_setAccount', 'UA-39299614-1']);
		  _gaq.push(['_trackPageview']);

		  (function() {
			var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
			ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
			var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
		  })();

</script>
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
			<li><a href = "/contact" >Contact</a></li>
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
			<li><a href = "/learning" >Learning</a></li>
			<li><a href = "/utilities" >Utilities</a></li>
			<li><a href = "/leisure" >Leisure</a></li>
			<li><a href = "/cca" >CCA</a></li>
			<li><a href = "/about" >About</a></li>
			<li><a href = "/contact" >Contact</a></li>
		</ul>
		</div>
		
		<div id = "content" class = "about blue justified applist">
			
			<h2> Learning </h2>
			
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
			<li><a href = "/utilities" >Utilities</a></li>
			<li><a href = "/leisure" >Leisure</a></li>
			<li><a href = "/cca" >CCA</a></li>
			<li><a href = "/about" >About</a></li>
			<li><a href = "/contact" >Contact</a></li>
		</ul>
		</div>
		
		<div id = "content" class = "about blue justified applist">
			
			<h2> Utilities </h2>
			
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
				<p>DHS Response</p>
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
			<li><a href = "/leisure" >Leisure</a></li>
			<li><a href = "/cca" >CCA</a></li>
			<li><a href = "/about" >About</a></li>
			<li><a href = "/contact" >Contact</a></li>
		</ul>
		</div>
		
		<div id = "content" class = "about blue justified applist">
			
			<h2> Leisure </h2>
			
			<a href = "/gags">
			<div class = "app">
				<p>DHS Gag</p>
			</div>
			</a>
			
			<a href = "/smile">
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
			
			<a href = "/artspace">
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
			<li><a href = "/utilities" >Utilities</a></li>
			<li><a href = "/leisure" >Leisure</a></li>
			<li><a href = "/cca" >CCA</a></li>
			<li><a href = "/about" >About</a></li>
			<li><a href = "/contact" >Contact</a></li>
		</ul>
		</div>
		
		<div id = "content" class = "about blue justified applist" >
			
			<h2> CCA </h2>
			
			<a href = "/dhsjabps">
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
			<li><a href = "/utilities" >Utilities</a></li>
			<li><a href = "/leisure" >Leisure</a></li>
			<li><a href = "/cca" >CCA</a></li>
			<li><a href = "/about" >About</a></li>
			<li><a href = "/contact" >Contact</a></li>
		</ul>
		</div>
		
		<div id = "content" class = "center blue">
		<a href = "/learning"> <- Back</a><br /><br />
		<a href = "http://cip.dhs.sg"><img class = "screenshot" src = "/static/img/cip.jpg"></a>
		<h3 class = "left">''')
		
		rank = db.Query(NewApp)
		rank.filter('name =', 'cip')
		for app in rank:
			if app.ranktime>0:
				self.response.out.write(app.rankscore/app.ranktime)
			else:
				self.response.out.write(0)
		self.response.out.write('''
		<img id = "starpic" src = "/static/img/star.jpg"></h3>
		<h3 class = "left">CIP Opportunities</h3>
		<h3 class = "left">By: Nie Shuyue<h3>
		<h3 class = "left">Description: </h3>
		<p>A webpage for students to post different CIP opportunities and the updates. If students want to find CIP to do, they can go to the webpage to view the opportunities and register online so that students do not have to find the CIP emails in the mail box. Make the life easier for both students and the CIP organizers/students.</p>
		<h3 class = "left">Reviews</h3>
		''')
		
		
		reviews = db.Query(Review)
		reviews.filter('appname =', 'cip')
		reviews.order("-date")
		for review in reviews:
			self.response.out.write('''<figure class = "blue">''')
			self.response.out.write('%s reviewed:' % review.author)
			self.response.out.write('<blockquote>%s</blockquote>' % cgi.escape(review.content))
			#if users.get_current_user().nickname() == review.author:
			#	self.response.out.write('''
			#		<form action = "/delete?app_name=cip" method = "post">
			#		<input type = "submit" value = "Delete" name="username">
			#		</form>
			#	''')
			self.response.out.write('''</figure>''')
		self.response.out.write('''
			<form action = "/delete?app_name=cip" method = "post">
			<input type = "submit" value = "Delete all your reviews!">
			</form>
		''')
			
			
		self.response.out.write('''
		
		<h3>Rank the App!</h3>
		<form action = "/rank?app_name=cip" method = "post">
			<div>
			<select name="score">
			<option value="1">1</option>
			<option value="2">2</option>
			<option value="3">3</option>
			<option value="4">4</option>
			<option value="5">5</option>
			<option value="6">6</option>
			<option value="7">7</option>
			<option value="8">8</option>
			<option value="9">9</option>
			<option value="10">10</option>
			</div>
			<div><input type = "submit" value = "Rank!"></div>
		</form>
		
		<h3> Submit your own review!</h3>
		<form action="/review?app_name=cip" method="post">
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
			<li><a href = "/utilities" >Utilities</a></li>
			<li><a href = "/leisure" >Leisure</a></li>
			<li><a href = "/cca" >CCA</a></li>
			<li><a href = "/about" >About</a></li>
			<li><a href = "/contact" >Contact</a></li>
		</ul>
		</div>
		
		<div id = "content" class = "center blue">
		<a href = "/learning"> <- Back</a><br /><br />
		<a href = "http://nowork.dhs.sg"><img class = "screenshot" src = "/static/img/nowork.jpg"></a>
		<h3 class = "left">''')
		
		rank = db.Query(NewApp)
		rank.filter('name =', 'nowork')
		for app in rank:
			if app.ranktime>0:
				self.response.out.write(app.rankscore/app.ranktime)
			else:
				self.response.out.write(0)
		self.response.out.write('''
		<img id = "starpic" src = "/static/img/star.jpg"></h3>
		<h3 class = "left">NoWork!</h3>
		<h3 class = "left">By: Justin Leow<h3>
		<h3 class = "left">Description: </h3>
		<p>DHS NoWork! is a notification sharing centre where staff and students can create groups by adding in their classmates, and proceed to post notifications and/or homework reminders to the entire group through a very simple sharing system. Users who open the webapp will immediately see notifications and/or homework reminders, and can proceed to mark though a "noted" or a "done" field, which the group admin will be able to check and be actively informed of the progress of the class.</p>
		<h3 class = "left">Reviews</h3>
		''')
		
		
		reviews = db.Query(Review)
		reviews.filter('appname =', 'nowork')
		reviews.order("-date")
		for review in reviews:
			self.response.out.write('''<figure class = "blue">''')
			self.response.out.write('%s reviewed:' % review.author)
			self.response.out.write('<blockquote>%s</blockquote>' % cgi.escape(review.content))
			#if users.get_current_user().nickname() == review.author:
			#	self.response.out.write('''
			#		<form action = "/delete?app_name=nowork" method = "post">
			#		<input type = "submit" value = "Delete" name="username">
			#		</form>
			#	''')
			self.response.out.write('''</figure>''')
		self.response.out.write('''
			<form action = "/delete?app_name=nowork" method = "post">
			<input type = "submit" value = "Delete all your reviews!">
			</form>
		''')
			
			
		self.response.out.write('''
		
		<h3>Rank the App!</h3>
		<form action = "/rank?app_name=nowork" method = "post">
			<div>
			<select name="score">
			<option value="1">1</option>
			<option value="2">2</option>
			<option value="3">3</option>
			<option value="4">4</option>
			<option value="5">5</option>
			<option value="6">6</option>
			<option value="7">7</option>
			<option value="8">8</option>
			<option value="9">9</option>
			<option value="10">10</option>
			</div>
			<div><input type = "submit" value = "Rank!"></div>
		</form>
		
		<h3> Submit your own review!</h3>
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
			<li><a href = "/utilities" >Utilities</a></li>
			<li><a href = "/leisure" >Leisure</a></li>
			<li><a href = "/cca" >CCA</a></li>
			<li><a href = "/about" >About</a></li>
			<li><a href = "/contact" >Contact</a></li>
		</ul>
		</div>
		
		<div id = "content" class = "center blue">
		<a href = "/learning"> <- Back</a><br /><br />
		<a href = "http://qna.dhs.sg"><img class = "screenshot" src = "/static/img/quora.jpg"></a>
		<h3 class = "left">''')
		
		rank = db.Query(NewApp)
		rank.filter('name =', 'quora')
		for app in rank:
			if app.ranktime>0:
				self.response.out.write(app.rankscore/app.ranktime)
			else:
				self.response.out.write(0)
		self.response.out.write('''
		<img id = "starpic" src = "/static/img/star.jpg"></h3>
		<h3 class = "left">Quora</h3>
		<h3 class = "left">By: Wang Zexin<h3>
		<h3 class = "left">Description: </h3>
		<p>An app for dunmanians to ask questions and help others.</p>
		<h3 class = "left">Reviews</h3>
		''')
		
		
		reviews = db.Query(Review)
		reviews.filter('appname =', 'quora')
		reviews.order("-date")
		for review in reviews:
			self.response.out.write('''<figure class = "blue">''')
			self.response.out.write('%s reviewed:' % review.author)
			self.response.out.write('<blockquote>%s</blockquote>' % cgi.escape(review.content))
			#if users.get_current_user().nickname() == review.author:
			#	self.response.out.write('''
			#		<form action = "/delete?app_name=quora" method = "post">
			#		<input type = "submit" value = "Delete" name="username">
			#		</form>
			#	''')
			self.response.out.write('''</figure>''')
		self.response.out.write('''
			<form action = "/delete?app_name=quora" method = "post">
			<input type = "submit" value = "Delete all your reviews!">
			</form>
		''')
			
			
		self.response.out.write('''
		
		<h3>Rank the App!</h3>
		<form action = "/rank?app_name=quora" method = "post">
			<div>
			<select name="score">
			<option value="1">1</option>
			<option value="2">2</option>
			<option value="3">3</option>
			<option value="4">4</option>
			<option value="5">5</option>
			<option value="6">6</option>
			<option value="7">7</option>
			<option value="8">8</option>
			<option value="9">9</option>
			<option value="10">10</option>
			</div>
			<div><input type = "submit" value = "Rank!"></div>
		</form>
		
		<h3> Submit your own review!</h3>
		<form action="/review?app_name=quora" method="post">
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
	
class Lecture(webapp2.RequestHandler):
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
			<li><a href = "/contact" >Contact</a></li>
		</ul>
		</div>
		
		<div id = "content" class = "center blue">
		<a href = "/learning"> <- Back</a><br /><br />
		<a href = "http://lecture.dhs.sg"><img class = "screenshot" src = "/static/img/lecture.jpg"></a>
		<h3 class = "left">''')
		
		rank = db.Query(NewApp)
		rank.filter('name =', 'lecture')
		for app in rank:
			if app.ranktime>0:
				self.response.out.write(app.rankscore/app.ranktime)
			else:
				self.response.out.write(0)
		self.response.out.write('''
		<img id = "starpic" src = "/static/img/star.jpg"></h4>
		<h3 class = "left">By: Zhan Yuli<h3>
		<h3 class = "left">Description: </h3>
		<p>An online app to share daily reflection and questions about all lectures. It is level-based and subject-based, not only allowing teachers to check students understanding of the lecture content but also providing a platform for students to do academic discussions. Every student can either post a question/reflection or answer the others' while teachers can collect similar questions and to give more targeted answers.</p>
		<h3 class = "left">Reviews</h3>
		''')
		
		
		reviews = db.Query(Review)
		reviews.filter('appname =', 'lecture')
		reviews.order("-date")
		for review in reviews:
			self.response.out.write('''<figure class = "blue">''')
			self.response.out.write('%s reviewed:' % review.author)
			self.response.out.write('<blockquote>%s</blockquote>' % cgi.escape(review.content))
			#if users.get_current_user().nickname() == review.author:
			#	self.response.out.write('''
			#		<form action = "/delete?app_name=lecture" method = "post">
			#		<input type = "submit" value = "Delete" name="username">
			#		</form>
			#	''')
			self.response.out.write('''</figure>''')
		self.response.out.write('''
			<form action = "/delete?app_name=lecture" method = "post">
			<input type = "submit" value = "Delete all your reviews!">
			</form>
		''')
			
			
		self.response.out.write('''
		
		<h3>Rank the App!</h3>
		<form action = "/rank?app_name=lecture" method = "post">
			<div>
			<select name="score">
			<option value="1">1</option>
			<option value="2">2</option>
			<option value="3">3</option>
			<option value="4">4</option>
			<option value="5">5</option>
			<option value="6">6</option>
			<option value="7">7</option>
			<option value="8">8</option>
			<option value="9">9</option>
			<option value="10">10</option>
			</div>
			<div><input type = "submit" value = "Rank!"></div>
		</form>
		
		<h3> Submit your own review!</h3>
		<form action="/review?app_name=lecture" method="post">
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

class Lostnfound(webapp2.RequestHandler):
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
			<li><a href = "/contact" >Contact</a></li>
		</ul>
		</div>
		
		<div id = "content" class = "center blue">
		<a href = "/utilities"> <- Back</a><br /><br />
		<a href = "http://lostnfound.dhs.sg"><img class = "screenshot" src = "/static/img/lostnfound.jpg"></a>
		<h3 class = "left">''')
		
		rank = db.Query(NewApp)
		rank.filter('name =', 'lostnfound')
		for app in rank:
			if app.ranktime>0:
				self.response.out.write(app.rankscore/app.ranktime)
			else:
				self.response.out.write(0)
		self.response.out.write('''
		<img id = "starpic" src = "/static/img/star.jpg"></h3>
		<h3 class = "left">Lost & Found</h3>
		<h3 class = "left">By: Chia Xiang Rong<h3>
		<h3 class = "left">Description: </h3>
		<p>
		   Users post what they have lost and the relevant details. Others can comment on whether they found it or post any items found in school. </p>
		<h3 class = "left">Reviews</h3>
		''')
		
		
		reviews = db.Query(Review)
		reviews.filter('appname =', 'lostnfound')
		reviews.order("-date")
		for review in reviews:
			self.response.out.write('''<figure class = "blue">''')
			self.response.out.write('%s reviewed:' % review.author)
			self.response.out.write('<blockquote>%s</blockquote>' % cgi.escape(review.content))
			#if users.get_current_user().nickname() == review.author:
			#	self.response.out.write('''
			#		<form action = "/delete?app_name=lostnfound" method = "post">
			#		<input type = "submit" value = "Delete" name="username">
			#		</form>
			#	''')
			self.response.out.write('''</figure>''')
		self.response.out.write('''
			<form action = "/delete?app_name=lostnfound" method = "post">
			<input type = "submit" value = "Delete all your reviews!">
			</form>
		''')
			
			
		self.response.out.write('''
		
		<h3>Rank the App!</h3>
		<form action = "/rank?app_name=lostnfound" method = "post">
			<div>
			<select name="score">
			<option value="1">1</option>
			<option value="2">2</option>
			<option value="3">3</option>
			<option value="4">4</option>
			<option value="5">5</option>
			<option value="6">6</option>
			<option value="7">7</option>
			<option value="8">8</option>
			<option value="9">9</option>
			<option value="10">10</option>
			</div>
			<div><input type = "submit" value = "Rank!"></div>
		</form>
		
		<h3> Submit your own review!</h3>
		<form action="/review?app_name=lostnfound" method="post">
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

class Announcement(webapp2.RequestHandler):
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
			<li><a href = "/contact" >Contact</a></li>
		</ul>
		</div>
		
		<div id = "content" class = "center blue">
		<a href = "/utilities"> <- Back</a><br /><br />
		<a href = "http://announce.dhs.sg"><img class = "screenshot" src = "/static/img/announcement.jpg"></a>
		<h3 class = "left">''')
		
		rank = db.Query(NewApp)
		rank.filter('name =', 'announcement')
		for app in rank:
			if app.ranktime>0:
				self.response.out.write(app.rankscore/app.ranktime)
			else:
				self.response.out.write(0)
		self.response.out.write('''
		<img id = "starpic" src = "/static/img/star.jpg"></h3>
		<h3 class = "left">DHS Announcements</h3>
		<h3 class = "left">By: David Fan<h3>
		<h3 class = "left">Description: </h3>
		<p>
		   Online announcements for school, cca, etc.   </p>
		<h3 class = "left">Reviews</h3>
		''')
		
		
		reviews = db.Query(Review)
		reviews.filter('appname =', 'announcement')
		reviews.order("-date")
		for review in reviews:
			self.response.out.write('''<figure class = "blue">''')
			self.response.out.write('%s reviewed:' % review.author)
			self.response.out.write('<blockquote>%s</blockquote>' % cgi.escape(review.content))
			#if users.get_current_user().nickname() == review.author:
			#	self.response.out.write('''
			#		<form action = "/delete?app_name=announcement" method = "post">
			#		<input type = "submit" value = "Delete" name="username">
			#		</form>
			#	''')
			self.response.out.write('''</figure>''')
		self.response.out.write('''
			<form action = "/delete?app_name=announcement" method = "post">
			<input type = "submit" value = "Delete all your reviews!">
			</form>
		''')
			
			
		self.response.out.write('''
		
		<h3>Rank the App!</h3>
		<form action = "/rank?app_name=announcement" method = "post">
			<div>
			<select name="score">
			<option value="1">1</option>
			<option value="2">2</option>
			<option value="3">3</option>
			<option value="4">4</option>
			<option value="5">5</option>
			<option value="6">6</option>
			<option value="7">7</option>
			<option value="8">8</option>
			<option value="9">9</option>
			<option value="10">10</option>
			</div>
			<div><input type = "submit" value = "Rank!"></div>
		</form>
		
		<h3> Submit your own review!</h3>
		<form action="/review?app_name=announcement" method="post">
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

class Feedback(webapp2.RequestHandler):
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
			<li><a href = "/contact" >Contact</a></li>
		</ul>
		</div>
		
		<div id = "content" class = "center blue">
		<a href = "/utilities"> <- Back</a><br /><br />
		<a href = "http://feedback.dhs.sg"><img class = "screenshot" src = "/static/img/feedback.jpg"></a>
		<h3 class = "left">''')
		
		rank = db.Query(NewApp)
		rank.filter('name =', 'feedback')
		for app in rank:
			if app.ranktime>0:
				self.response.out.write(app.rankscore/app.ranktime)
			else:
				self.response.out.write(0)
		self.response.out.write('''
		<img id = "starpic" src = "/static/img/star.jpg"></h3>
		<h3 class = "left">DHS Feedback</h3>
		<h3 class = "left">By: Jason Hong Wei Cong<h3>
		<h3 class = "left">Description: </h3>
		<p>
		   Online suggestion box. Student population can submit feedbacks to the school. The school would then be able to view these feedbacks and hopefully be able to address it.   </p>
		<h3 class = "left">Reviews</h3>
		''')
		
		
		reviews = db.Query(Review)
		reviews.filter('appname =', 'feedback')
		reviews.order("-date")
		for review in reviews:
			self.response.out.write('''<figure class = "blue">''')
			self.response.out.write('%s reviewed:' % review.author)
			self.response.out.write('<blockquote>%s</blockquote>' % cgi.escape(review.content))
			#if users.get_current_user().nickname() == review.author:
			#	self.response.out.write('''
			#		<form action = "/delete?app_name=feedback" method = "post">
			#		<input type = "submit" value = "Delete" name="username">
			#		</form>
			#	''')
			self.response.out.write('''</figure>''')
		self.response.out.write('''
			<form action = "/delete?app_name=feedback" method = "post">
			<input type = "submit" value = "Delete all your reviews!">
			</form>
		''')
			
			
		self.response.out.write('''
		
		<h3>Rank the App!</h3>
		<form action = "/rank?app_name=feedback" method = "post">
			<div>
			<select name="score">
			<option value="1">1</option>
			<option value="2">2</option>
			<option value="3">3</option>
			<option value="4">4</option>
			<option value="5">5</option>
			<option value="6">6</option>
			<option value="7">7</option>
			<option value="8">8</option>
			<option value="9">9</option>
			<option value="10">10</option>
			</div>
			<div><input type = "submit" value = "Rank!"></div>
		</form>
		
		<h3> Submit your own review!</h3>
		<form action="/review?app_name=feedback" method="post">
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

class Temperature(webapp2.RequestHandler):
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
			<li><a href = "/contact" >Contact</a></li>
		</ul>
		</div>
		
		<div id = "content" class = "center blue">
		<a href = "/utilities"> <- Back</a><br /><br />
		<a href = "http://temperaturetaking.dhs.sg"><img class = "screenshot" src = "/static/img/temperature.jpg"></a>
		<h3 class = "left">''')
		
		rank = db.Query(NewApp)
		rank.filter('name =', 'temperature')
		for app in rank:
			if app.ranktime>0:
				self.response.out.write(app.rankscore/app.ranktime)
			else:
				self.response.out.write(0)
		self.response.out.write('''
		<img id = "starpic" src = "/static/img/star.jpg"></h3>
		<h3 class = "left">Temperature Taking</h3>
		<h3 class = "left">By: Leong Xuhua<h3>
		<h3 class = "left">Description: </h3>
		<p>
		   Records down temperature of student and would alert management if student has fever.   </p>
		<h3 class = "left">Reviews</h3>
		''')
		
		
		reviews = db.Query(Review)
		reviews.filter('appname =', 'temperature')
		reviews.order("-date")
		for review in reviews:
			self.response.out.write('''<figure class = "blue">''')
			self.response.out.write('%s reviewed:' % review.author)
			self.response.out.write('<blockquote>%s</blockquote>' % cgi.escape(review.content))
			#if users.get_current_user().nickname() == review.author:
			#	self.response.out.write('''
			#		<form action = "/delete?app_name=temperature" method = "post">
			#		<input type = "submit" value = "Delete" name="username">
			#		</form>
			#	''')
			self.response.out.write('''</figure>''')
		self.response.out.write('''
			<form action = "/delete?app_name=temperature" method = "post">
			<input type = "submit" value = "Delete all your reviews!">
			</form>
		''')
			
			
		self.response.out.write('''
		
		<h3>Rank the App!</h3>
		<form action = "/rank?app_name=temperature" method = "post">
			<div>
			<select name="score">
			<option value="1">1</option>
			<option value="2">2</option>
			<option value="3">3</option>
			<option value="4">4</option>
			<option value="5">5</option>
			<option value="6">6</option>
			<option value="7">7</option>
			<option value="8">8</option>
			<option value="9">9</option>
			<option value="10">10</option>
			</div>
			<div><input type = "submit" value = "Rank!"></div>
		</form>
		
		<h3> Submit your own review!</h3>
		<form action="/review?app_name=temperature" method="post">
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
		
class Tickets(webapp2.RequestHandler):
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
			<li><a href = "/contact" >Contact</a></li>
		</ul>
		</div>
		
		<div id = "content" class = "center blue">
		<a href = "/utilities"> <- Back</a><br /><br />
		<a href = "http://ticketing.dhs.sg"><img class = "screenshot" src = "/static/img/tickets.jpg"></a>
		<h3 class = "left">''')
		
		rank = db.Query(NewApp)
		rank.filter('name =', 'tickets')
		for app in rank:
			if app.ranktime>0:
				self.response.out.write(app.rankscore/app.ranktime)
			else:
				self.response.out.write(0)
		self.response.out.write('''
		<img id = "starpic" src = "/static/img/star.jpg"></h3>
		<h3 class = "left">DHS Tickets</h3>
		<h3 class = "left">By: Ng Cheryl<h3>
		<h3 class = "left">Description: </h3>
		<p>
		   Ticketing app that allows students to view events and order tickets by choosing the number of tickets. Students will not be required to enter their name nor class, but they will be required to use a DHS account. App can be further extended to allowing public to order tickets, and for organisers to create their own events and set ticket prices. After closing date of sales, data list will be sent to organiser for them to contact students regarding collection/distribution of tickets.   </p>
		<h3 class = "left">Reviews</h3>
		''')
		
		
		reviews = db.Query(Review)
		reviews.filter('appname =', 'tickets')
		reviews.order("-date")
		for review in reviews:
			self.response.out.write('''<figure class = "blue">''')
			self.response.out.write('%s reviewed:' % review.author)
			self.response.out.write('<blockquote>%s</blockquote>' % cgi.escape(review.content))
			#if users.get_current_user().nickname() == review.author:
			#	self.response.out.write('''
			#		<form action = "/delete?app_name=tickets" method = "post">
			#		<input type = "submit" value = "Delete" name="username">
			#		</form>
			#	''')
			self.response.out.write('''</figure>''')
		self.response.out.write('''
			<form action = "/delete?app_name=tickets" method = "post">
			<input type = "submit" value = "Delete all your reviews!">
			</form>
		''')
			
			
		self.response.out.write('''
		
		<h3>Rank the App!</h3>
		<form action = "/rank?app_name=tickets" method = "post">
			<div>
			<select name="score">
			<option value="1">1</option>
			<option value="2">2</option>
			<option value="3">3</option>
			<option value="4">4</option>
			<option value="5">5</option>
			<option value="6">6</option>
			<option value="7">7</option>
			<option value="8">8</option>
			<option value="9">9</option>
			<option value="10">10</option>
			</div>
			<div><input type = "submit" value = "Rank!"></div>
		</form>
		
		<h3> Submit your own review!</h3>
		<form action="/review?app_name=tickets" method="post">
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

class Rollcall(webapp2.RequestHandler):
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
			<li><a href = "/contact" >Contact</a></li>
		</ul>
		</div>
		
		<div id = "content" class = "center blue">
		<a href = "/utilities"> <- Back</a><br /><br />
		<a href = "http://rollcall.dhs.sg"><img class = "screenshot" src = "/static/img/rollcall.jpg"></a>
		<h3 class = "left">''')
		
		rank = db.Query(NewApp)
		rank.filter('name =', 'rollcall')
		for app in rank:
			if app.ranktime>0:
				self.response.out.write(app.rankscore/app.ranktime)
			else:
				self.response.out.write(0)
		self.response.out.write('''
		<img id = "starpic" src = "/static/img/star.jpg"></h3>
		<h3 class = "left">DHS Rollcall</h3>
		<h3 class = "left">By: Ng Yuan Siang<h3>
		<h3 class = "left">Description: </h3>
		<p>
		   An app for teachers to indicate, submit and access attendance efficiently. Students may also use this as a convenient alternative to the leave forms at General Office. Students can also scan and submit their MCs via this app (eg. if on extended leave)   </p>
		<h3 class = "left">Reviews</h3>
		''')
		
		
		reviews = db.Query(Review)
		reviews.filter('appname =', 'rollcall')
		reviews.order("-date")
		for review in reviews:
			self.response.out.write('''<figure class = "blue">''')
			self.response.out.write('%s reviewed:' % review.author)
			self.response.out.write('<blockquote>%s</blockquote>' % cgi.escape(review.content))
			#if users.get_current_user().nickname() == review.author:
			#	self.response.out.write('''
			#		<form action = "/delete?app_name=rollcall" method = "post">
			#		<input type = "submit" value = "Delete" name="username">
			#		</form>
			#	''')
			self.response.out.write('''</figure>''')
		self.response.out.write('''
			<form action = "/delete?app_name=rollcall" method = "post">
			<input type = "submit" value = "Delete all your reviews!">
			</form>
		''')
			
			
		self.response.out.write('''
		
		<h3>Rank the App!</h3>
		<form action = "/rank?app_name=rollcall" method = "post">
			<div>
			<select name="score">
			<option value="1">1</option>
			<option value="2">2</option>
			<option value="3">3</option>
			<option value="4">4</option>
			<option value="5">5</option>
			<option value="6">6</option>
			<option value="7">7</option>
			<option value="8">8</option>
			<option value="9">9</option>
			<option value="10">10</option>
			</div>
			<div><input type = "submit" value = "Rank!"></div>
		</form>
		
		<h3> Submit your own review!</h3>
		<form action="/review?app_name=rollcall" method="post">
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

class Canteen(webapp2.RequestHandler):
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
			<li><a href = "/contact" >Contact</a></li>
		</ul>
		</div>
		
		<div id = "content" class = "center blue">
		<a href = "/utilities"> <- Back</a><br /><br />
		<a href = "http://canteen.dhs.sg"><img class = "screenshot" src = "/static/img/canteen.jpg"></a>
		<h3 class = "left">''')
		
		rank = db.Query(NewApp)
		rank.filter('name =', 'canteen')
		for app in rank:
			if app.ranktime>0:
				self.response.out.write(app.rankscore/app.ranktime)
			else:
				self.response.out.write(0)
		self.response.out.write('''
		<img id = "starpic" src = "/static/img/star.jpg"></h3>
		<h3 class = "left">Canteen Review</h3>
		<h3 class = "left">By: Ong Jun Hao Bryan<h3>
		<h3 class = "left">Description: </h3>
		<p>
		   Students who use the app can write a review for canteen food. Reviews can be ranked.   </p>
		<h3 class = "left">Reviews</h3>
		''')
		
		
		reviews = db.Query(Review)
		reviews.filter('appname =', 'canteen')
		reviews.order("-date")
		for review in reviews:
			self.response.out.write('''<figure class = "blue">''')
			self.response.out.write('%s reviewed:' % review.author)
			self.response.out.write('<blockquote>%s</blockquote>' % cgi.escape(review.content))
			#if users.get_current_user().nickname() == review.author:
			#	self.response.out.write('''
			#		<form action = "/delete?app_name=canteen" method = "post">
			#		<input type = "submit" value = "Delete" name="username">
			#		</form>
			#	''')
			self.response.out.write('''</figure>''')
		self.response.out.write('''
			<form action = "/delete?app_name=canteen" method = "post">
			<input type = "submit" value = "Delete all your reviews!">
			</form>
		''')
			
			
		self.response.out.write('''
		
		<h3>Rank the App!</h3>
		<form action = "/rank?app_name=canteen" method = "post">
			<div>
			<select name="score">
			<option value="1">1</option>
			<option value="2">2</option>
			<option value="3">3</option>
			<option value="4">4</option>
			<option value="5">5</option>
			<option value="6">6</option>
			<option value="7">7</option>
			<option value="8">8</option>
			<option value="9">9</option>
			<option value="10">10</option>
			</div>
			<div><input type = "submit" value = "Rank!"></div>
		</form>
		
		<h3> Submit your own review!</h3>
		<form action="/review?app_name=canteen" method="post">
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
		
class Share(webapp2.RequestHandler):
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
			<li><a href = "/contact" >Contact</a></li>
		</ul>
		</div>
		
		<div id = "content" class = "center blue">
		<a href = "/utilities"> <- Back</a><br /><br />
		<a href = "http://share.dhs.sg"><img class = "screenshot" src = "/static/img/share.jpg"></a>
		<h3 class = "left">''')
		
		rank = db.Query(NewApp)
		rank.filter('name =', 'share')
		for app in rank:
			if app.ranktime>0:
				self.response.out.write(app.rankscore/app.ranktime)
			else:
				self.response.out.write(0)
		self.response.out.write('''
		<img id = "starpic" src = "/static/img/star.jpg"></h3>
		<h3 class = "left">DHS Share</h3>
		<h3 class = "left">By: Pan Song<h3>
		<h3 class = "left">Description: </h3>
		<p>
		   Sharing of items that may not be useful to one anymore but may be useful to others e.g. books, textbooks. Owner of the item, if they really do not want it anymore, can add a price to the item and other students, if willing to own the item, can buy it.   </p>
		<h3 class = "left">Reviews</h3>
		''')
		
		
		reviews = db.Query(Review)
		reviews.filter('appname =', 'share')
		reviews.order("-date")
		for review in reviews:
			self.response.out.write('''<figure class = "blue">''')
			self.response.out.write('%s reviewed:' % review.author)
			self.response.out.write('<blockquote>%s</blockquote>' % cgi.escape(review.content))
			#if users.get_current_user().nickname() == review.author:
			#	self.response.out.write('''
			#		<form action = "/delete?app_name=share" method = "post">
			#		<input type = "submit" value = "Delete" name="username">
			#		</form>
			#	''')
			self.response.out.write('''</figure>''')
		self.response.out.write('''
			<form action = "/delete?app_name=share" method = "post">
			<input type = "submit" value = "Delete all your reviews!">
			</form>
		''')
			
			
		self.response.out.write('''
		
		<h3>Rank the App!</h3>
		<form action = "/rank?app_name=share" method = "post">
			<div>
			<select name="score">
			<option value="1">1</option>
			<option value="2">2</option>
			<option value="3">3</option>
			<option value="4">4</option>
			<option value="5">5</option>
			<option value="6">6</option>
			<option value="7">7</option>
			<option value="8">8</option>
			<option value="9">9</option>
			<option value="10">10</option>
			</div>
			<div><input type = "submit" value = "Rank!"></div>
		</form>
		
		<h3> Submit your own review!</h3>
		<form action="/review?app_name=share" method="post">
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

class Treasurer(webapp2.RequestHandler):
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
			<li><a href = "/contact" >Contact</a></li>
		</ul>
		</div>
		
		<div id = "content" class = "center blue">
		<a href = "/utilities"> <- Back</a><br /><br />
		<a href = "http://treasurer.dhs.sg"><img class = "screenshot" src = "/static/img/treasurer.jpg"></a>
		<h3 class = "left">''')
		
		rank = db.Query(NewApp)
		rank.filter('name =', 'treasurer')
		for app in rank:
			if app.ranktime>0:
				self.response.out.write(app.rankscore/app.ranktime)
			else:
				self.response.out.write(0)
		self.response.out.write('''
		<img id = "starpic" src = "/static/img/star.jpg"></h3>
		<h3 class = "left">Treasurer's Kit</h3>
		<h3 class = "left">By: Song Kai<h3>
		<h3 class = "left">Description: </h3>
		<p>
		   Keep track of all the INs and OUTs and gives the current amount of class fund. All the records are saved and for other students the app can also be used to track their own spending.   </p>
		<h3 class = "left">Reviews</h3>
		''')
		
		
		reviews = db.Query(Review)
		reviews.filter('appname =', 'treasurer')
		reviews.order("-date")
		for review in reviews:
			self.response.out.write('''<figure class = "blue">''')
			self.response.out.write('%s reviewed:' % review.author)
			self.response.out.write('<blockquote>%s</blockquote>' % cgi.escape(review.content))
			#if users.get_current_user().nickname() == review.author:
			#	self.response.out.write('''
			#		<form action = "/delete?app_name=treasurer" method = "post">
			#		<input type = "submit" value = "Delete" name="username">
			#		</form>
			#	''')
			self.response.out.write('''</figure>''')
		self.response.out.write('''
			<form action = "/delete?app_name=treasurer" method = "post">
			<input type = "submit" value = "Delete all your reviews!">
			</form>
		''')
			
			
		self.response.out.write('''
		
		<h3>Rank the App!</h3>
		<form action = "/rank?app_name=treasurer" method = "post">
			<div>
			<select name="score">
			<option value="1">1</option>
			<option value="2">2</option>
			<option value="3">3</option>
			<option value="4">4</option>
			<option value="5">5</option>
			<option value="6">6</option>
			<option value="7">7</option>
			<option value="8">8</option>
			<option value="9">9</option>
			<option value="10">10</option>
			</div>
			<div><input type = "submit" value = "Rank!"></div>
		</form>
		
		<h3> Submit your own review!</h3>
		<form action="/review?app_name=treasurer" method="post">
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

class Report(webapp2.RequestHandler):
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
			<li><a href = "/contact" >Contact</a></li>
		</ul>
		</div>
		
		<div id = "content" class = "center blue">
		<a href = "/utilities"> <- Back</a><br /><br />
		<a href = "http://report.dhs.sg"><img class = "screenshot" src = "/static/img/report.jpg"></a>
		<h3 class = "left">''')
		
		rank = db.Query(NewApp)
		rank.filter('name =', 'report')
		for app in rank:
			if app.ranktime>0:
				self.response.out.write(app.rankscore/app.ranktime)
			else:
				self.response.out.write(0)
		self.response.out.write('''
		<img id = "starpic" src = "/static/img/star.jpg"></h3>
		<h3 class = "left">DHS Report</h3>
		<h3 class = "left">By: Tan Jin Yi Ambrose<h3>
		<h3 class = "left">Description: </h3>
		<p>
		   Admin can mark errors with different statuses and users can report errors. Users will be directed to the area that they report to the most.   </p>
		<h3 class = "left">Reviews</h3>
		''')
		
		
		reviews = db.Query(Review)
		reviews.filter('appname =', 'report')
		reviews.order("-date")
		for review in reviews:
			self.response.out.write('''<figure class = "blue">''')
			self.response.out.write('%s reviewed:' % review.author)
			self.response.out.write('<blockquote>%s</blockquote>' % cgi.escape(review.content))
			#if users.get_current_user().nickname() == review.author:
			#	self.response.out.write('''
			#		<form action = "/delete?app_name=report" method = "post">
			#		<input type = "submit" value = "Delete" name="username">
			#		</form>
			#	''')
			self.response.out.write('''</figure>''')
		self.response.out.write('''
			<form action = "/delete?app_name=report" method = "post">
			<input type = "submit" value = "Delete all your reviews!">
			</form>
		''')
			
			
		self.response.out.write('''
		
		<h3>Rank the App!</h3>
		<form action = "/rank?app_name=report" method = "post">
			<div>
			<select name="score">
			<option value="1">1</option>
			<option value="2">2</option>
			<option value="3">3</option>
			<option value="4">4</option>
			<option value="5">5</option>
			<option value="6">6</option>
			<option value="7">7</option>
			<option value="8">8</option>
			<option value="9">9</option>
			<option value="10">10</option>
			</div>
			<div><input type = "submit" value = "Rank!"></div>
		</form>
		
		<h3> Submit your own review!</h3>
		<form action="/review?app_name=report" method="post">
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

class Responses(webapp2.RequestHandler):
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
			<li><a href = "/contact" >Contact</a></li>
		</ul>
		</div>
		
		<div id = "content" class = "center blue">
		<a href = "/utilities"> <- Back</a><br /><br />
		<a href = "http://respond.dhs.sg"><img class = "screenshot" src = "/static/img/response.jpg"></a>
		<h3 class = "left">''')
		
		rank = db.Query(NewApp)
		rank.filter('name =', 'response')
		for app in rank:
			if app.ranktime>0:
				self.response.out.write(app.rankscore/app.ranktime)
			else:
				self.response.out.write(0)
		self.response.out.write('''
		<img id = "starpic" src = "/static/img/star.jpg"></h3>
		<h3 class = "left">DHS Respond</h3>
		<h3 class = "left">By: Tan Yugin<h3>
		<h3 class = "left">Description: </h3>
		<p>
		   Suggestions and criticisms app which also displays responses and intended actions (if any) from school management for public viewing.  </p>
		<h3 class = "left">Reviews</h3>
		''')
		
		
		reviews = db.Query(Review)
		reviews.filter('appname =', 'response')
		reviews.order("-date")
		for review in reviews:
			self.response.out.write('''<figure class = "blue">''')
			self.response.out.write('%s reviewed:' % review.author)
			self.response.out.write('<blockquote>%s</blockquote>' % cgi.escape(review.content))
			#if users.get_current_user().nickname() == review.author:
			#	self.response.out.write('''
			#		<form action = "/delete?app_name=response" method = "post">
			#		<input type = "submit" value = "Delete" name="username">
			#		</form>
			#	''')
			self.response.out.write('''</figure>''')
		self.response.out.write('''
			<form action = "/delete?app_name=response" method = "post">
			<input type = "submit" value = "Delete all your reviews!">
			</form>
		''')
			
			
		self.response.out.write('''
		
		<h3>Rank the App!</h3>
		<form action = "/rank?app_name=response" method = "post">
			<div>
			<select name="score">
			<option value="1">1</option>
			<option value="2">2</option>
			<option value="3">3</option>
			<option value="4">4</option>
			<option value="5">5</option>
			<option value="6">6</option>
			<option value="7">7</option>
			<option value="8">8</option>
			<option value="9">9</option>
			<option value="10">10</option>
			</div>
			<div><input type = "submit" value = "Rank!"></div>
		</form>
		
		<h3> Submit your own review!</h3>
		<form action="/review?app_name=response" method="post">
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

class Gag(webapp2.RequestHandler):
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
			<li><a href = "/contact" >Contact</a></li>
		</ul>
		</div>
		
		<div id = "content" class = "center blue">
		<a href = "/leisure"> <- Back</a><br /><br />
		<a href = "http://gags.dhs.sg"><img class = "screenshot" src = "/static/img/gags.jpg"></a>
		<h3 class = "left">''')
		
		rank = db.Query(NewApp)
		rank.filter('name =', 'gags')
		for app in rank:
			if app.ranktime>0:
				self.response.out.write(app.rankscore/app.ranktime)
			else:
				self.response.out.write(0)
		self.response.out.write('''
		<img id = "starpic" src = "/static/img/star.jpg"></h3>
		<h3 class = "left">DHSGags</h3>
		<h3 class = "left">By: Ang Yong Loong<h3>
		<h3 class = "left">Description: </h3>
		<p>
		   Image hosting site for Dunmanians to showcase their artwork or comics or images created, for example, memes. There will be a comment and rating section for each post. To upload image, comment or rate, user have to sign in to their DHS accounts. Viewing does not require a log-in. Images can include inspiration post, jokes, world issues for discussion, news updates or problems faced, to be shared and discuss together as a school community, for example dirty toilets. Censorship will be exercised.  </p>
		<h3 class = "left">Reviews</h3>
		''')
		
		
		reviews = db.Query(Review)
		reviews.filter('appname =', 'gags')
		reviews.order("-date")
		for review in reviews:
			self.response.out.write('''<figure class = "blue">''')
			self.response.out.write('%s reviewed:' % review.author)
			self.response.out.write('<blockquote>%s</blockquote>' % cgi.escape(review.content))
			#if users.get_current_user().nickname() == review.author:
			#	self.response.out.write('''
			#		<form action = "/delete?app_name=gags" method = "post">
			#		<input type = "submit" value = "Delete" name="username">
			#		</form>
			#	''')
			self.response.out.write('''</figure>''')
		self.response.out.write('''
			<form action = "/delete?app_name=gags" method = "post">
			<input type = "submit" value = "Delete all your reviews!">
			</form>
		''')
			
			
		self.response.out.write('''
		
		<h3>Rank the App!</h3>
		<form action = "/rank?app_name=gags" method = "post">
			<div>
			<select name="score">
			<option value="1">1</option>
			<option value="2">2</option>
			<option value="3">3</option>
			<option value="4">4</option>
			<option value="5">5</option>
			<option value="6">6</option>
			<option value="7">7</option>
			<option value="8">8</option>
			<option value="9">9</option>
			<option value="10">10</option>
			</div>
			<div><input type = "submit" value = "Rank!"></div>
		</form>
		
		<h3> Submit your own review!</h3>
		<form action="/review?app_name=gags" method="post">
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

class Sendasmile(webapp2.RequestHandler):
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
			<li><a href = "/contact" >Contact</a></li>
		</ul>
		</div>
		
		<div id = "content" class = "center blue">
		<a href = "/leisure"> <- Back</a><br /><br />
		<a href = "http://sendasmile.dhs.sg"><img class = "screenshot" src = "/static/img/smile.jpg"></a>
		<h3 class = "left">''')
		
		rank = db.Query(NewApp)
		rank.filter('name =', 'smile')
		for app in rank:
			if app.ranktime>0:
				self.response.out.write(app.rankscore/app.ranktime)
			else:
				self.response.out.write(0)
		self.response.out.write('''
		<img id = "starpic" src = "/static/img/star.jpg"></h3>
		<h3 class = "left">Send A Smile</h3>
		<h3 class = "left">By: Gan Jing Ying<h3>
		<h3 class = "left">Description: </h3>
		<p>
		   An app that allows users to motivate each other by sending 'smiles' or virtual gifts. Users will be able to attach short messages, of 140 characters or less, to their gifts. They can also add specific users to their 'Favourites' list for easier reference.   </p>
		<h3 class = "left">Reviews</h3>
		''')
		
		
		reviews = db.Query(Review)
		reviews.filter('appname =', 'smile')
		reviews.order("-date")
		for review in reviews:
			self.response.out.write('''<figure class = "blue">''')
			self.response.out.write('%s reviewed:' % review.author)
			self.response.out.write('<blockquote>%s</blockquote>' % cgi.escape(review.content))
			#if users.get_current_user().nickname() == review.author:
			#	self.response.out.write('''
			#		<form action = "/delete?app_name=smile" method = "post">
			#		<input type = "submit" value = "Delete" name="username">
			#		</form>
			#	''')
			self.response.out.write('''</figure>''')
		self.response.out.write('''
			<form action = "/delete?app_name=smile" method = "post">
			<input type = "submit" value = "Delete all your reviews!">
			</form>
		''')
			
			
		self.response.out.write('''
		
		<h3>Rank the App!</h3>
		<form action = "/rank?app_name=smile" method = "post">
			<div>
			<select name="score">
			<option value="1">1</option>
			<option value="2">2</option>
			<option value="3">3</option>
			<option value="4">4</option>
			<option value="5">5</option>
			<option value="6">6</option>
			<option value="7">7</option>
			<option value="8">8</option>
			<option value="9">9</option>
			<option value="10">10</option>
			</div>
			<div><input type = "submit" value = "Rank!"></div>
		</form>
		
		<h3> Submit your own review!</h3>
		<form action="/review?app_name=smile" method="post">
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
	
class Jokes(webapp2.RequestHandler):
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
			<li><a href = "/contact" >Contact</a></li>
		</ul>
		</div>
		
		<div id = "content" class = "center blue">
		<a href = "/leisure"> <- Back</a><br /><br />
		<a href = "http://jokes.dhs.sg"><img class = "screenshot" src = "/static/img/jokes.jpg"></a>
		<h3 class = "left">''')
		
		rank = db.Query(NewApp)
		rank.filter('name =', 'jokes')
		for app in rank:
			if app.ranktime>0:
				self.response.out.write(app.rankscore/(1.5*app.ranktime))
			else:
				self.response.out.write(0)
		self.response.out.write('''
		<img id = "starpic" src = "/static/img/star.jpg"></h3>
		<h3 class = "left">DHS Jokes</h3>
		<h3 class = "left">By: Tan Di Sheng<h3>
		<h3 class = "left">Description: </h3>
		<p>
		   Users can read jokes on the app and insert their jokes to share with everyone. Slandering/Adult/Unsuitable jokes will be removed by moderator.  </p>
		<h3 class = "left">Reviews</h3>
		''')
		
		
		reviews = db.Query(Review)
		reviews.filter('appname =', 'jokes')
		reviews.order("-date")
		for review in reviews:
			self.response.out.write('''<figure class = "blue">''')
			self.response.out.write('%s reviewed:' % review.author)
			self.response.out.write('<blockquote>%s</blockquote>' % cgi.escape(review.content))
			#if users.get_current_user().nickname() == review.author:
			#	self.response.out.write('''
			#		<form action = "/delete?app_name=jokes" method = "post">
			#		<input type = "submit" value = "Delete" name="username">
			#		</form>
			#	''')
			self.response.out.write('''</figure>''')
		self.response.out.write('''
			<form action = "/delete?app_name=jokes" method = "post">
			<input type = "submit" value = "Delete all your reviews!">
			</form>
		''')
			
			
		self.response.out.write('''
		
		<h3>Rank the App!</h3>
		<form action = "/rank?app_name=jokes" method = "post">
			<div>
			<select name="score">
			<option value="1">1</option>
			<option value="2">2</option>
			<option value="3">3</option>
			<option value="4">4</option>
			<option value="5">5</option>
			<option value="6">6</option>
			<option value="7">7</option>
			<option value="8">8</option>
			<option value="9">9</option>
			<option value="10">10</option>
			</div>
			<div><input type = "submit" value = "Rank!"></div>
		</form>
		
		<h3> Submit your own review!</h3>
		<form action="/review?app_name=jokes" method="post">
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

class Know(webapp2.RequestHandler):
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
			<li><a href = "/contact" >Contact</a></li>
		</ul>
		</div>
		
		<div id = "content" class = "center blue">
		<a href = "/leisure"> <- Back</a><br /><br />
		<a href = "http://bond.dhs.sg"><img class = "screenshot" src = "/static/img/know.jpg"></a>
		<h3 class = "left">''')
		
		rank = db.Query(NewApp)
		rank.filter('name =', 'know')
		for app in rank:
			if app.ranktime>0:
				self.response.out.write(app.rankscore/app.ranktime)
			else:
				self.response.out.write(0)
		self.response.out.write('''
		<img id = "starpic" src = "/static/img/star.jpg"></h3>
		<h3 class = "left">DHS Get-to-know-each-other</h3>
		<h3 class = "left">By: Neo Wei Lu<h3>
		<h3 class = "left">Description: </h3>
		<p>
		   Users are able to search for anyone in the school apart from non-teaching stuff. The information given are limited.  </p>
		<h3 class = "left">Reviews</h3>
		''')
		
		
		reviews = db.Query(Review)
		reviews.filter('appname =', 'know')
		reviews.order("-date")
		for review in reviews:
			self.response.out.write('''<figure class = "blue">''')
			self.response.out.write('%s reviewed:' % review.author)
			self.response.out.write('<blockquote>%s</blockquote>' % cgi.escape(review.content))
			#if users.get_current_user().nickname() == review.author:
			#	self.response.out.write('''
			#		<form action = "/delete?app_name=know" method = "post">
			#		<input type = "submit" value = "Delete" name="username">
			#		</form>
			#	''')
			self.response.out.write('''</figure>''')
		self.response.out.write('''
			<form action = "/delete?app_name=know" method = "post">
			<input type = "submit" value = "Delete all your reviews!">
			</form>
		''')
			
			
		self.response.out.write('''
		
		<h3>Rank the App!</h3>
		<form action = "/rank?app_name=know" method = "post">
			<div>
			<select name="score">
			<option value="1">1</option>
			<option value="2">2</option>
			<option value="3">3</option>
			<option value="4">4</option>
			<option value="5">5</option>
			<option value="6">6</option>
			<option value="7">7</option>
			<option value="8">8</option>
			<option value="9">9</option>
			<option value="10">10</option>
			</div>
			<div><input type = "submit" value = "Rank!"></div>
		</form>
		
		<h3> Submit your own review!</h3>
		<form action="/review?app_name=know" method="post">
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
	
class Art(webapp2.RequestHandler):
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
			<li><a href = "/contact" >Contact</a></li>
		</ul>
		</div>
		
		<div id = "content" class = "center blue">
		<a href = "/leisure"> <- Back</a><br /><br />
		<a href = "http://artescape.dhs.sg"><img class = "screenshot" src = "/static/img/artspace.jpg"></a>
		<h3 class = "left">''')
		
		rank = db.Query(NewApp)
		rank.filter('name =', 'artspace')
		for app in rank:
			if app.ranktime>0:
				self.response.out.write(app.rankscore/app.ranktime)
			else:
				self.response.out.write(0)
		self.response.out.write('''
		<img id = "starpic" src = "/static/img/star.jpg"></h3>
		<h3 class = "left">Art Escape</h3>
		<h3 class = "left">By: Ng Yi Jun (Alan)<h3>
		<h3 class = "left">Description: </h3>
		<p>A space for dunmanians (AEP, SH Art, D'Art cca, or other Dunmanians) to share their artworks, post several pictures & descriptions, comments and likes. </p>
		<h3 class = "left">Reviews</h3>
		''')
		
		
		reviews = db.Query(Review)
		reviews.filter('appname =', 'artspace')
		reviews.order("-date")
		for review in reviews:
			self.response.out.write('''<figure class = "blue">''')
			self.response.out.write('%s reviewed:' % review.author)
			self.response.out.write('<blockquote>%s</blockquote>' % cgi.escape(review.content))
			#if users.get_current_user().nickname() == review.author:
			#	self.response.out.write('''
			#		<form action = "/delete?app_name=artspace" method = "post">
			#		<input type = "submit" value = "Delete" name="username">
			#		</form>
			#	''')
			self.response.out.write('''</figure>''')
		self.response.out.write('''
			<form action = "/delete?app_name=artspace" method = "post">
			<input type = "submit" value = "Delete all your reviews!">
			</form>
		''')
			
			
		self.response.out.write('''
		
		<h3>Rank the App!</h3>
		<form action = "/rank?app_name=artspace" method = "post">
			<div>
			<select name="score">
			<option value="1">1</option>
			<option value="2">2</option>
			<option value="3">3</option>
			<option value="4">4</option>
			<option value="5">5</option>
			<option value="6">6</option>
			<option value="7">7</option>
			<option value="8">8</option>
			<option value="9">9</option>
			<option value="10">10</option>
			</div>
			<div><input type = "submit" value = "Rank!"></div>
		</form>
		
		<h3> Submit your own review!</h3>
		<form action="/review?app_name=artspace" method="post">
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

class Crushes(webapp2.RequestHandler):
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
			<li><a href = "/contact" >Contact</a></li>
		</ul>
		</div>
		
		<div id = "content" class = "center blue">
		<a href = "/leisure"> <- Back</a><br /><br />
		<a href = "http://crushes.dhs.sg"><img class = "screenshot" src = "/static/img/crushes.jpg"></a>
		<h3 class = "left">''')
		
		rank = db.Query(NewApp)
		rank.filter('name =', 'crushes')
		for app in rank:
			if app.ranktime>0:
				self.response.out.write(app.rankscore/app.ranktime)
			else:
				self.response.out.write(0)
		self.response.out.write('''
		<img id = "starpic" src = "/static/img/star.jpg"></h3>
		<h3 class = "left">Crushes</h3>
		<h3 class = "left">By: Wu Chenmu<h3>
		<h3 class = "left">Description: </h3>
		<p>If you had a crush on someone but do not have the courage to confess, you can use this app to mark her/him as your favor(he or she will not know)...If that person, fortunately, is also an admirer of you and marked you, then...tada!</p>
		<h3 class = "left">Reviews</h3>
		''')
		
		
		reviews = db.Query(Review)
		reviews.filter('appname =', 'crushes')
		reviews.order("-date")
		for review in reviews:
			self.response.out.write('''<figure class = "blue">''')
			self.response.out.write('%s reviewed:' % review.author)
			self.response.out.write('<blockquote>%s</blockquote>' % cgi.escape(review.content))
			#if users.get_current_user().nickname() == review.author:
			#	self.response.out.write('''
			#		<form action = "/delete?app_name=crushes" method = "post">
			#		<input type = "submit" value = "Delete" name="username">
			#		</form>
			#	''')
			self.response.out.write('''</figure>''')
		self.response.out.write('''
			<form action = "/delete?app_name=crushes" method = "post">
			<input type = "submit" value = "Delete all your reviews!">
			</form>
		''')
			
			
		self.response.out.write('''
		
		<h3>Rank the App!</h3>
		<form action = "/rank?app_name=crushes" method = "post">
			<div>
			<select name="score">
			<option value="1">1</option>
			<option value="2">2</option>
			<option value="3">3</option>
			<option value="4">4</option>
			<option value="5">5</option>
			<option value="6">6</option>
			<option value="7">7</option>
			<option value="8">8</option>
			<option value="9">9</option>
			<option value="10">10</option>
			</div>
			<div><input type = "submit" value = "Rank!"></div>
		</form>
		
		<h3> Submit your own review!</h3>
		<form action="/review?app_name=crushes" method="post">
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

class Dhsjab(webapp2.RequestHandler):
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
			<li><a href = "/contact" >Contact</a></li>
		</ul>
		</div>
		
		<div id = "content" class = "center blue">
		<a href = "/cca"> <- Back</a><br /><br />
		<a href = "http://sjabps.dhs.sg"><img class = "screenshot" src = "/static/img/dhsjabps.jpg"></a>
		<h3 class = "left">''')
		
		rank = db.Query(NewApp)
		rank.filter('name =', 'dhsjabps')
		for app in rank:
			if app.ranktime>0:
				self.response.out.write(app.rankscore/app.ranktime)
			else:
				self.response.out.write(0)
		self.response.out.write('''
		<img id = "starpic" src = "/static/img/star.jpg"></h3>
		<h3 class = "left">DHSJAB Parade State</h3>
		<h3 class = "left">By: Chua Ming Yu<h3>
		<h3 class = "left">Description: </h3>
		<p>An app that allows users (target audience: SJAB people) to fill in the parade state more easily. Since the parade state is done weekly, and nearly the same information is filled in, the app allows the users to stay dry. The app also archives previous versions of parade states submitted on different training so that its easier for teachers to keep track of attendance.</p>
		<h3 class = "left">Reviews</h3>
		''')
		
		
		reviews = db.Query(Review)
		reviews.filter('appname =', 'dhsjabps')
		reviews.order("-date")
		for review in reviews:
			self.response.out.write('''<figure class = "blue">''')
			self.response.out.write('%s reviewed:' % review.author)
			self.response.out.write('<blockquote>%s</blockquote>' % cgi.escape(review.content))
			#if users.get_current_user().nickname() == review.author:
			#	self.response.out.write('''
			#		<form action = "/delete?app_name=dhsjabps" method = "post">
			#		<input type = "submit" value = "Delete" name="username">
			#		</form>
			#	''')
			self.response.out.write('''</figure>''')
		self.response.out.write('''
			<form action = "/delete?app_name=dhsjabps" method = "post">
			<input type = "submit" value = "Delete all your reviews!">
			</form>
		''')
			
			
		self.response.out.write('''
		
		<h3>Rank the App!</h3>
		<form action = "/rank?app_name=dhsjabps" method = "post">
			<div>
			<select name="score">
			<option value="1">1</option>
			<option value="2">2</option>
			<option value="3">3</option>
			<option value="4">4</option>
			<option value="5">5</option>
			<option value="6">6</option>
			<option value="7">7</option>
			<option value="8">8</option>
			<option value="9">9</option>
			<option value="10">10</option>
			</div>
			<div><input type = "submit" value = "Rank!"></div>
		</form>
		
		<h3> Submit your own review!</h3>
		<form action="/review?app_name=dhsjabps" method="post">
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

class Interact(webapp2.RequestHandler):
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
			<li><a href = "/contact" >Contact</a></li>
		</ul>
		</div>
		
		<div id = "content" class = "center blue">
		<a href = "/cca"> <- Back</a><br /><br />
		<a href = "http://interact.dhs.sg"><img class = "screenshot" src = "/static/img/interact.jpg"></a>
		<h3 class = "left">''')
		
		rank = db.Query(NewApp)
		rank.filter('name =', 'interact')
		for app in rank:
			if app.ranktime>0:
				self.response.out.write(app.rankscore/app.ranktime)
			else:
				self.response.out.write(0)
		self.response.out.write('''
		<img id = "starpic" src = "/static/img/star.jpg"></h3>
		<h3 class = "left">DHS CCA Updates</h3>
		<h3 class = "left">By: Thng Jing Xiong<h3>
		<h3 class = "left">Description: </h3>
		<p>Update the school on the latest friendlys/competitions any CCA is going to have. For example, basketball is going to have a friendly. The school will be updated on all these news and people who are free can come down to watch the matches. In this app, they can also indicate whether they are coming or not. And maybe they can post comments as well, for example to wish the team good luck and show their concern to the team. After the friendlys/competitions, the score will be posted online for everyone to see. People from different CCAs can interact and bond with each other through watching the competitions and through the comment box.</p>
		<h3 class = "left">Reviews</h3>
		''')
		
		
		reviews = db.Query(Review)
		reviews.filter('appname =', 'interact')
		reviews.order("-date")
		for review in reviews:
			self.response.out.write('''<figure class = "blue">''')
			self.response.out.write('%s reviewed:' % review.author)
			self.response.out.write('<blockquote>%s</blockquote>' % cgi.escape(review.content))
			#if users.get_current_user().nickname() == review.author:
			#	self.response.out.write('''
			#		<form action = "/delete?app_name=interact" method = "post">
			#		<input type = "submit" value = "Delete" name="username">
			#		</form>
			#	''')
			self.response.out.write('''</figure>''')
		self.response.out.write('''
			<form action = "/delete?app_name=interact" method = "post">
			<input type = "submit" value = "Delete all your reviews!">
			</form>
		''')
			
			
		self.response.out.write('''
		
		<h3>Rank the App!</h3>
		<form action = "/rank?app_name=interact" method = "post">
			<div>
			<select name="score">
			<option value="1">1</option>
			<option value="2">2</option>
			<option value="3">3</option>
			<option value="4">4</option>
			<option value="5">5</option>
			<option value="6">6</option>
			<option value="7">7</option>
			<option value="8">8</option>
			<option value="9">9</option>
			<option value="10">10</option>
			</div>
			<div><input type = "submit" value = "Rank!"></div>
		</form>
		
		<h3> Submit your own review!</h3>
		<form action="/review?app_name=interact" method="post">
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
	
class Submitreview(webapp2.RequestHandler):
	def post(self):
		#posted = False
		app_name = str(self.request.get('app_name'))
		username = users.get_current_user().nickname()
		#reviews = db.Query(Review)
		#for review in reviews:
		#	if review.author == username:
		#		posted=True
		#		review.content = self.request.get('content')
		#		review.put()
		#if posted==False:
		review = Review(parent=review_key(app_name))
		review.author = users.get_current_user().nickname()
		review.content = self.request.get('content')
		review.appname = app_name
		review.put()
		self.redirect('/' + app_name)
		
class Submitrank(webapp2.RequestHandler):
	def post(self):
		app_name = str(self.request.get('app_name'))
		score = int(self.request.get('score'))
		apps = db.Query(NewApp)
		apps.filter('name =', app_name)
		for app in apps:
			app.rankscore = app.rankscore + score
			app.ranktime = app.ranktime+1
			app.put()
		self.redirect('/' + app_name)
		
class Clear(webapp2.RequestHandler):
	def get(self):
		apps = db.Query(NewApp)
		for app in apps:
			app.delete()
		reviews = db.Query(Review)
		for review in reviews:
			review.delete()
	
class Delete(webapp2.RequestHandler):
	def post(self):
		appname = self.request.get('app_name')
		username = users.get_current_user().nickname()
		reviews = db.Query(Review)
		reviews.filter('author =', username)
		reviews.filter('appname =', appname)
		for review in reviews:
			review.delete()
		self.redirect('/' + appname)
	
class Addapp(webapp2.RequestHandler):
	def get(self):
		print "Hello. DIE INVADER!"
	
	
app = webapp2.WSGIApplication([('/', MainPage),
							   ('/about', About),
							   ('/leisure', Leisure),
							   ('/contact', Contact),
							   ('/utilities', Utilities),
							   ('/learning', Learning),
							   ('/cca', Cca),
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
							   ('/response', Responses),
							   ('/gags', Gag),
							   ('/smile', Sendasmile),
							   ('/jokes', Jokes),
							   ('/know', Know),
							   ('/artspace', Art),
							   ('/crushes', Crushes),
							   ('/dhsjabps', Dhsjab),
							   ('/interact', Interact),
							   ('/review', Submitreview),
							   ('/rank', Submitrank),
							   ('/clear', Clear),
							   ('/delete', Delete)
							   ]
							   ,
                               debug=True)