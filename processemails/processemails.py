import imaplib
import email
mail=imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('jeromecukier@gmail.com','v4nd4lh34rt')
mail.select("inbox")
result,list=mail.uid('search',None,'(HEADER To "data-visualization-cartel@googlegroups.com")')

file=[]
seeds=[]
seedID=0
for uid in list[0]:
    result={}
    k,data=mail.uid('fetch',uid,'(RFC822)')
    raw_email=data[0][1]
    email_message=email.message_from_string(raw_email)
    result['From']=email.utils.parseaddr(m['From'])[1]
    result['Date']=email['Date']
    result['Subject']=email['Subject']
    result['Message-ID']=email['Message-ID']
    result['References']=[]
    for ref in email['References']:
        result['References']=ref
    if len(email['References'])==0:
        seed={}
        seed[email['Message-ID']]=seedID
        result['Thread']=seedID
        seedID=seedID+1
        seeds.append(seed)
        
    file.append(result)

for result in file:
    if(len(result['References'])>0):
        for ref in result['References']:
            if ref in seeds:
                result['Thread']=seeds[ref]
    
        
    
