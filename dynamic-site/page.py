class DefaultPage(object):
    def __init__(self):
        self.html = {}
        self.build = {}
        #Create HTML dictionary and section out keys with all base HTML
        self.html['header'] = '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>OperationCommand</title>

    <!-- Bootstrap -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.min.css">

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  <body style="padding-top:50px">
'''
        self.html['navbar'] = '''
    <nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <a class="navbar-brand" href="/">OperationCommand</a>
        </div>
      </div>
    </nav>
'''
        self.html['footer'] = '''
    <footer class="footer">
      <div class="container">
        <p class="text-muted center-text">&copy; 2015 OperationCommand by Rick Martin</p>
      </div>
    </footer>

    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
  </body>
</html>
'''

    #Combine all HTML in dictionary regardless of how many and format with passed dictionary
    def load(self):
        self.build_hook()
        output = self.html['header'] + self.html['navbar'] + self.html['section'] + self.html['footer']
        return output.format(**self.build)

    def build_hook(self):
        print "build_hook is not available in this module"

#Inherit from default page and add new HTML keys to dictionary
class LandingPage(DefaultPage):
    def __init__(self, pages):
        DefaultPage.__init__(self)
        self.pages = pages
        self.html['navbar'] = '''
<nav class="navbar navbar-inverse navbar-fixed-top">
  <div class="container">
    <div class="navbar-header">
      <a class="navbar-brand" href="">OperationCommand</a>
    </div>
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav">
        {links}
      </ul>
    </div>
  </div>
</nav>
'''
        self.html['section'] = '''
    <section>
      <div class="container">
        <div class="page-header clearfix">
          <h1 class="pull-left">Operation Campaign Briefing</h1>
        </div>
        <div class="jumbotron clearfix">
          <div class="row">
            <div class="col-md-6">
              <h1><em>Control</em> Team</br>
              <small>Leader: <strong>Confidential</strong></small></h1>
              <h2>Base of Operations: <em>Undisclosed</em></h2>
              <p>This campaign is being lead by the most elite group of indivduals forming the best teams our organization has to offer. In the main navigation you will find links to each mission briefing for your team, let there be no mistake, it's all riding on this.</p>
            </div>
            <div class="col-md-6">
              <img class="img-thumbnail" width="100%" src="/image/control.png" />
            </div>
          </div>
        </div>
      </div>
    </section>
'''

    #Loop through pages given and create links in nav only available on homepage
    def build_hook(self):
        self.build['links'] = ""
        for page in self.pages:
            self.build['links'] += "<li><a href='/?op=%s'>%s</a></li>" % (page,page)

#Inherit from default page and add new HTML keys to dictionary
class OperationPage(DefaultPage):
    def __init__(self, build):
        DefaultPage.__init__(self)
        self.build = build
        self.html['section'] = '''
    <section>
      <div class="container">
        <div class="page-header clearfix">
          <h1 class="pull-left">Operation <em>"{name}"</em> Briefing</h1>
        </div>
        <div class="jumbotron clearfix">
          <div class="row">
            <div class="col-md-6">
              <h1><em>{squad}</em> Squad</br>
              <small>Leader: <strong>{leader}</strong></small></h1>
              <h2>Insertion Point: <em>{local}</em></h2>
              <p>{brief}</p>
            </div>
            <div class="col-md-6">
              <img class="img-thumbnail" width="100%" src="{image}" />
            </div>
          </div>
        </div>
      </div>
    </section>
'''
