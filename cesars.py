from pattern.web   import Twitter, Google, plaintext
from pattern.table import Table
t = Table()
for nomme, categorie in (("l'arnacoeur", "film"), ("le nom des gens", "film"), ("the ghost writer", "film"), ("tourn�e", "film"), ("des hommes et des dieux", "film"), ("gainsbourg, vie h�roique", "film"), ("mammuth", "film")):
    for tweet in Twitter().search(nomme):
        s = plaintext(tweet.description)        
        t.append([nomme, film, tweet.date, s])