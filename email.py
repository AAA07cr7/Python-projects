import pandas as pd
import datetime
import smtplib 
GMAILID='anmolagrawal853@gmail.com'
GMAILPASS='anmol@1234'
def sendemail(to,sub,msg):
    print(f"Email is sent to {to} with subject {sub} and message is {msg}")
    s=smtplib.SMTP_SSL('smtp.gmail.com',465)
    
    s.login(GMAILID,GMAILPASS)
    s.sendmail(GMAILID,to,f"subject: {sub}/n/n message {msg}")
    s.quit()
    
if __name__ == "__main__":
    
    df=pd.read_excel("birthh.xlsx")
    today=datetime.datetime.now().strftime("%d-%m")
    yearnow=datetime.datetime.now().strftime("%y")
    writeind=[]
   # print(type(today))
    for index, item in  df.iterrows():
        print(index,item['birth'])
        bday=item['birth'].strftime("%d-%m")
        print(bday)
        if(today==bday) and yearnow not in str(item['year']):
            sendemail(item['Email'],"Happy birthday",item['wishes'])
            writeind.append(index)
    print(writeind)
    if(len(writeind)!=0):
        for i in writeind:
            yr=df.loc[i,'year']
            print(yr)
            df.loc[i,'year']=str(yr)+','+ str(yearnow)
            df.to_excel('birthh.xlsx')
