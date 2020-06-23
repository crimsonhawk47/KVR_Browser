import webbrowser, os, RegisterChrome
BHandle = RegisterChrome.Get('chrome')
site = 'https://www.kvraudio.com/forum/'
print(os.environ['MAC_CHROME_PATH'])
BHandle.open(site)
webbrowser.open(site)