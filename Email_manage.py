from mailtm import Email
import re
import requests
import threading

#verify if the activation link is found to end the process
done = threading.Event()

def listener(message):
    raw = message.get('html') or message.get('text') or ''

    #transforms the message (currently is a list) to a string
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
            #enable closing the process
            done.set()
            return


temp_email = Email()
#create a new random email
temp_email.register()
print("\nEmail Adress: " + str(temp_email.address))
temp_email.start(listener)
#flag to wait until the activation link is found
done.wait()
#close the email
temp_email.stop()






