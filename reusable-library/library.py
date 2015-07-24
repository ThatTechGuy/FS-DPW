class Record(object):
    def __init__(self):
        self.__record = {}

    @property
    def record(self):
        return self.__record

    @record.setter
    def record(self,form):
        self.__record = form
        self.check_eligibility()
        self.list_item()

    def check_eligibility(self):
        if all (k in self.__record for k in ("sun","art","wcs","irs","loa")):
            self.__record['eligible'] = ["text-success","All Checks"]
        elif all (k in self.__record for k in ("sun","wcs","loa")):
            if self.__record['type'] == "DBA":
                self.__record['eligible'] = "All Checks"
                self.__record['color'] = self.bootstrap_color("green")
            else:
                self.__record['eligible'] = "DBA Under $1k"
                self.__record['color'] = self.bootstrap_color("green")
        elif "sun" in self.__record:
            self.__record['eligible'] = "DBA Under $1k"
            self.__record['color'] = self.bootstrap_color("yellow")
        else:
            self.__record['eligible'] = "Personal Only"
            self.__record['color'] = self.bootstrap_color("red")

    def list_item(self):
        self.__record['files'] = ""
        if 'sun' in self.__record:
            self.__record['files'] += '''
            <li class="list-group-item">Sunbiz Registration</li>
            '''
        if 'art' in self.__record:
            self.__record['files'] += '''
            <li class="list-group-item">Articles of Incorporation</li>
            '''
        if 'wcs' in self.__record:
            self.__record['files'] += '''
            <li class="list-group-item">Workman's Comp Search</li>
            '''
        if 'irs' in self.__record:
            self.__record['files'] += '''
            <li class="list-group-item">IRS Letter w/ Tax ID</li>
            '''
        if 'loa' in self.__record:
            self.__record['files'] += '''
            <li class="list-group-item">Letter of Authority</li>
            '''

    def bootstrap_color(self,color):
        if color == "green":
            return "label-success"
        if color == "yellow":
            return "label-warning"
        if color == "red":
            return "label-danger"
