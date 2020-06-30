import webbrowser, os
def Get(str):
    if os.name == 'nt':
        chromePath = os.environ['WINDOWS_CHROME_PATH']
    else:
        chromePath = os.environ['MAC_CHROME_PATH']
    webbrowser.register(str, None, webbrowser.BackgroundBrowser(chromePath))
    return webbrowser.get(str)


