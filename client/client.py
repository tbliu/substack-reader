import imaplib
import email
import json
from flask import Flask

app = Flask(__name__)

@app.route("/")
def getEmails():
    imap_host = 'imap.gmail.com'
    imap_user = ''
    imap_pass = ''

    # connect to host using SSL
    imap = imaplib.IMAP4_SSL(imap_host)

    # login to server
    imap.login(imap_user, imap_pass)

    imap.select('Inbox')

    t, data = imap.search(None, 'FROM', '"substack"')
    if t != 'OK':
        raise Exception('Could not search mailbox')

    messages = []

    for num in data[0].split():
        t, data = imap.fetch(num, '(RFC822)')
        if t != 'OK':
            raise Exception("Could not retrieve email with uid %d"%int(num))
        raw_message = data[0][1].decode('utf-8')
        parsed_message = email.message_from_string(raw_message)
        serializable_message = parsed_message.__dict__['_headers']
        messages.append(serializable_message)

        encoded_messages = json.dumps(messages)
        print(encoded_messages)
        imap.close()
        return encoded_messages

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
