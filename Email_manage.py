from mailtm import Email
import re
import requests


def listener(message):
    raw = message.get('html') or message.get('text') or ''

    #transform the message (currently is a list) to a string
    content = raw if isinstance(raw, str) else str(raw)

    #list all links in the message
    urls = re.findall(r'(https?://[^\s"\']+)', content)
    for url in urls:
        #find the activation link
        if "activate.api.stardock.net" in url or "validation/validate" in url:
            print(f"Found activation link: {url}")
            #access the link
            resp = requests.get(url, allow_redirects=True)
            print("Status: ", resp.status_code)
            break


temp_email = Email()
#create a new random email
temp_email.register()
print("\nEmail Adress: " + str(temp_email.address))
temp_email.start(listener)
temp_email.stop()





