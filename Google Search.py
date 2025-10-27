import webbrowser

user_term = input("Enter a word to search in Google: ").replace(" ", "+")

webbrowser.open_new_tab(f"https://www.google.com/search?q={user_term}" )