import sys
import nltk
import csv
from prettytable import PrettyTable

CSV_FILE = sys.argv[1]

# Handle any known abbreviations,
# strip off common suffixes, etc.

transforms = [
    ('\xe9', 'e'),
    ('\xf9', 'u'),
    ('\xef', 'i'),
    ('\xe8', 'e'),
    ('\xe7', 'c'),
    (', Inc.', ''),
    (', Inc', ''),
    (', LLC', ''),
    (', LLP', ''),
    ('Organisation for Economic Co-operation and Development (OECD)', 'OECD'),
    ('Organisation for Economic Co-Operation and Development', 'OECD'),
    ('Organisation for Economic Co-operation & Development (OECD)', 'OECD'),
    ('Organisation for Economic Co-operation and Development', 'OECD'),
    ('Organisation for Economic Co-operation and Development, OECD Publishing', 'OECD'),
    ('Organisation for Economic Cooperation and Development (OECD)', 'OECD'),
    ('OECD Publishing', 'OECD'),
    ('OECD, Economics Department', 'OECD'),
    ('EDF - Electricite de France', 'EDF'),
    ('DELOITTE', 'Deloitte'),
    ('Societe GENERALE', 'Societe Generale'),
    ('Sopra Consulting', 'Sopra Group'),
    ('Wolfram Alpha', 'Wolfram|Alpha') 
    ]

csvReader = csv.DictReader(open(CSV_FILE), delimiter=',', quotechar='"')
contacts = [row for row in csvReader]
companies = [c['Company'].strip() for c in contacts if c['Company'].strip() != '']

for i in range(len(companies)):
    for transform in transforms:
        companies[i] = companies[i].replace(*transform)

pt = PrettyTable(fields=['Company', 'Freq'])
pt.set_field_align('Company', 'l')
fdist = nltk.FreqDist(companies)
[pt.add_row([company, freq]) for (company, freq) in fdist.items() if freq>0]

        

pt.printt()
