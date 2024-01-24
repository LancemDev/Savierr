from sms import SMS as sms

apiKey = ""
username = ""
recepients = ["+2547xxxxxxxx", "+2547xxxxxxxx"]

# the logic to send the messages
sms = sms(username, apiKey)
sms.send("Hello, World!", recepients)