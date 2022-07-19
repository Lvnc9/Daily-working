#! python3.10.4
# Start
# Creating the mailing list
# Modules
from collections import defaultdict
from someday import send_email
import datetime
import time

# Base mailing list class
class MailingList:
    """ Manage groups of email addresses for sending e-mails """
    
    def __init__(self, data_file):
        self.data_file = data_file
        self.email_map = defaultdict(set)
    
    def add_to_group(self, email, group):
        self.email_map[email].add(group)
    
    def email_in_groups(self, *groups):
        """ using set structure for not having
        duplicated groups! """
        
        groups = set(groups)
        emails = set()
        
        for e, g in self.email_map.items():
            if g & groups:
                emails.add(e)
        return emails

    def send_mailing(self, subject:str, message:str,
        from_addr, *groups, headers=None):
        start_time = datetime.datetime.now()
        emails = self.email_in_groups(*groups)
        send_email(subject, message, from_addr, *emails,
            headers=headers)
        return f"Spended time: {datetime.datetime.now()}"

    def save(self):
        with open(self.data_file, 'w') as file:
            for email, group in self.email_map.items():
                file.write(f"{email}, {','.join(group)} \n")
    
    def load(self):
        self.email_map = defaultdict(set)
        try:
            with open(self.data_file, 'r') as file:
                for line in file:
                    email, groups = line.strip().split(' ')
                    groups = set(groups.split(','))
                    self.email_map[email] = groups
        except IOError:
            pass
    
    def __enter__(self):
        self.load()
        return self
    
    def __exit__(self, type, value, tb):
        self.save()

    
# End