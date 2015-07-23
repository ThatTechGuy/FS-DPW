class DefaultPage(object):
    def __init__(self):
        self.header = '''
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
        self.section = '''
    <section>
      <div class="container">
        <div class="page-header clearfix">
          <h1 class="pull-left">Record New Business</h1>
        </div>
        <div class="jumbotron">
          <form class="form-horizontal" method="GET">
            <div class="form-group">
              <label for="name" class="col-sm-2 control-label">Business Name</label>
              <div class="col-sm-10">
                <input type="text" class="form-control" id="name" name="name" placeholder="John Doe's Lawn Care" />
              </div>
            </div>
            <div class="form-group">
              <label for="type" class="col-sm-2 control-label">Business Type</label>
              <div class="col-sm-10">
                <select class="form-control" id="type" name="type">
                  <option value="DBA">Doing Business As (DBA)</option>
                  <option value="LLC">Limited Liability Company (LLC)</option>
                  <option value="INC">Incorporated Company (INC)</option>
                </select>
              </div>
            </div>
            <div class="form-group">
              <label for="contact" class="col-sm-2 control-label">Contact Name</label>
              <div class="col-sm-10">
                <input type="text" class="form-control" id="contact" name="contact" placeholder="John Doe" />
              </div>
            </div>
            <div class="form-group">
              <label for="number" class="col-sm-2 control-label">Contact Number</label>
              <div class="col-sm-10">
                <input type="tel" class="form-control" id="number" name="number" placeholder="1234567890" />
              </div>
            </div>
            <div class="form-group">
              <label for="files" class="col-sm-2 control-label">Files Available</label>
              <div class="col-sm-10">
                <label class="checkbox-inline">
                  <input type="checkbox" id="sunbiz" name="files[sun]" value="1"> Sunbiz Registration
                </label>
                <label class="checkbox-inline">
                  <input type="checkbox" id="articles" name="files[art]" value="1"> Articles of Incorporation
                </label>
                <label class="checkbox-inline">
                  <input type="checkbox" id="workcomp" name="files[wcs]" value="1"> Workman's Comp Search
                </label>
                <label class="checkbox-inline">
                  <input type="checkbox" id="irsletter" name="files[irs]" value="1"> IRS Letter w/ Tax ID
                </label>
                <label class="checkbox-inline">
                  <input type="checkbox" id="custloa" name="files['loa']" value="1"> Letter of Authority
                </label>
              </div>
            </div>
            <input type="submit" class="btn btn-primary btn-block" value="Save Business Record" />
          </form>
        </div>
      </div>
    </section>
'''
        self.footer = '''
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

    def load(self):
        return self.header + self.section + self.footer
