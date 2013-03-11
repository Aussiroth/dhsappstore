import webapp2
import cgi

class MainPage(webapp2.RequestHandler):
  def get(self):
	  self.response.out.write('''
	  
	<!DOCTYPE html>
	<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
	<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
	<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
	<!--[if gt IE 8]><!--> <html class="no-js"> <!--<![endif]-->
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <title>D'App Store</title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width">

        <!-- Place favicon.ico and apple-touch-icon.png in the root directory -->
		<link rel="icon" href = "/static/favicon.ico">
        <link rel="stylesheet" href="stylesheets/normalize.css">
        <link rel="stylesheet" href="static/stylesheets/main.css">
        <script src="js/vendor/modernizr-2.6.2.min.js"></script>
    </head>
    <body>
        <!--[if lt IE 7]>
            <p class="chromeframe">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> or <a href="http://www.google.com/chromeframe/?redirect=true">activate Google Chrome Frame</a> to improve your experience.</p>
        <![endif]-->

        <!-- Add your site or application content here -->
        
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
		
		<div id = "content" class = "blue">
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
			<p>&copy DHS Computing class 2013</p>
		</div>
		
        <script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.min.js"></script>
        <script>window.jQuery || document.write('<script src="js/vendor/jquery-1.9.0.min.js"><\/script>')</script>
        <script src="js/plugins.js"></script>
        <script src="js/main.js"></script>

        <!-- Google Analytics: change UA-XXXXX-X to be your site's ID. -->
        <script>
            var _gaq=[['_setAccount','UA-XXXXX-X'],['_trackPageview']];
            (function(d,t){var g=d.createElement(t),s=d.getElementsByTagName(t)[0];
            g.src=('https:'==location.protocol?'//ssl':'//www')+'.google-analytics.com/ga.js';
            s.parentNode.insertBefore(g,s)}(document,'script'));
        </script>
    </body>
</html>


	  
	  
	  ''')
	  
class About(webapp2.RequestHandler):	  
	def get(self):
	  self.response.out.write('''
	  <!DOCTYPE html>
	<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
	<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
	<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
	<!--[if gt IE 8]><!--> <html class="no-js"> <!--<![endif]-->
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <title>D'App Store</title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width">

        <!-- Place favicon.ico and apple-touch-icon.png in the root directory -->
		<link rel="icon" href = "/../static/favicon.ico">
        <link rel="stylesheet" href="/../stylesheets/normalize.css">
        <link rel="stylesheet" href="/../static/stylesheets/main.css">
        <script src="js/vendor/modernizr-2.6.2.min.js"></script>
    </head>
    <body>
        <!--[if lt IE 7]>
            <p class="chromeframe">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> or <a href="http://www.google.com/chromeframe/?redirect=true">activate Google Chrome Frame</a> to improve your experience.</p>
        <![endif]-->

        <!-- Add your site or application content here -->
        
		<header class = "center blue">
			<h1> <a class = "black" href = "/..">D'APP STORE</a></h1>
		</header>
		
		<!-- Navigational sidebar -->
		
		<div id = "sidebar" class = "center blue">
		<ul>
			<li><a href = "/..">Home</a></li>
			<li><a href = "/../learning" >Learning</a></li>
			<li><a href = "/../utilities" >Utilities</a></li>
			<li><a href = "/../leisure" >Leisure</a></li>
			<li><a href = "/../cca" >CCA</a></li>
			<li><a href = "/../contact" >Contact</a></li>
		</ul>
		</div>
		
		<div id = "content" class = "blue">
			<h2>About This App</h2>
			
			<p>This app was made to help organise, access and learn more about the different apps created by computing students.</p>
			
			<p>In this app, you can help to rank the apps with a score through an easy drop-down selection list.</p>
			
			<p>Later modifications include reviews so people will better know what to expect out of the app, as well as possibly reporting functions to allow a centralised area to send bug reports to the app creators.</p>			
			
			<p>You can select a catagory though the left navigational menu to view certain types of apps.</p>
			
			<p>The front page randomly showcases an app to help all the different apps on this site to gain popularity. It can also help introduce you to a new app you haven't tried out before!</p>
			
			<p>Click on the banner at the top or the home in the navigational menu to return to the front page of this app! </p>
			
			<p>This "App Store" was done by Alvin Yan. All the apps that are linked to by this "App Store" are productions of other computing students.</p>
			
		</div>
		
	</body>
	</html>
	  ''')

	  
app = webapp2.WSGIApplication([('/', MainPage), ('/about', About)],
                              debug=True)