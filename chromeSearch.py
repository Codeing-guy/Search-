import webbrowser ,sys ,pyperclip
sys.argv
if len(sys.argv)>1:
    search=' '.join(sys.argv[1:])
else:
    search=pyperclip.paste()


webbrowser.open('https://www.google.com/search?q='+search)
