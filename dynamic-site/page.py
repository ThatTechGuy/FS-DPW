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
    <title>MasterFile</title>

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
    <nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <a class="navbar-brand" href="">MasterFile</a>
        </div>
      </div>
    </nav>
'''
        self.html['footer'] = '''
    <footer class="footer">
      <div class="container">
        <p class="text-muted center-text">&copy; 2015 MasterFile by Rick Martin</p>
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
        output = ''
        self.build_hook()
        for html in self.html:
            output += html
        return output.format(**self.build)

    def build_hook(self):
        print "build_hook is not available in this module"

#Inherit from default page and add new HTML keys to dictionary
class LandingPage(DefaultPage):
    def __init__(self, pages):
        DefaultPage.__init__(self)
        self.pages = pages
        self.html['section'] = '''

'''

    def build_hook(self):
        pass

#Inherit from default page and add new HTML keys to dictionary
class OperationPage(DefaultPage):
    def __init__(self, build):
        DefaultPage.__init__(self)
        self.build = build
        self.html['section'] = '''
    <section>
      <div class="container">
        <div class="page-header clearfix">
          <h1 class="pull-left">Open Business Record</h1>
        </div>
        <div class="jumbotron clearfix">
          <div class="col-sm-6">
           <h3>{name} </br><small>Registrant: {contact}</small></h3>

           </br>
           <h4><strong>Contact:</strong> {contact}</h4>
           <h4><strong>Number:</strong> {number}</h4>
          </div>
         <div class="col-sm-6">
           <h4 class="text-right">Cashing Eligibility: <span class="label {color}">{eligible}</span></h4>
           <ul class="list-group">
             {files}
           </ul>
         </div>
        </div>
      </div>
    </section>
'''

    def build_hook(self):
        pass
