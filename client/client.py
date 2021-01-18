import imaplib
import pprint

imap_host = 'imap.gmail.com'

# TODO: Get the username and password from front-end. Maybe allow multiple log-ins
imap_user = ""
imap_pass = ""

# connect to host using SSL
imap = imaplib.IMAP4_SSL(imap_host)

# login to server
imap.login(imap_user, imap_pass)

imap.select('Inbox')

tmp, data = imap.search(None, 'FROM', '"substack"')
mailboxes = imap.list()
print(mailboxes)
for num in data[0].split():
    tmp, data = imap.fetch(num, '(RFC822)')
    # pprint.pprint(data[0][1])
    print('Message %s\n%s\n' % (num, data[0][1]))
    break
imap.close()
