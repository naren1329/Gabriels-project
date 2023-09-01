from django.shortcuts import render
#import models for fetching data from DB table 
from .models import UserDetails
# this module is decode the code in user format
import base64

#Main function
def profile(request,letter=None):
    #List contain alphabets for searching records
    my_data = ['ALL','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    #List for Primary phone number
    pri_ph =[]
    #List for Secondary phone number
    sec_ph = []
    #list for Images
    link=[]
    s=request.GET.get('searchbutton')
    
    #It gets all records in the DB table
    records=UserDetails.objects.all()

    #This IF statements for searching elements form SearchBox
    if s != None:
        if s != "":
            if records != []:
                records=records.filter(user_name__icontains=s)

    #This IF statements for searching elements via Letters            
    if letter:
        if letter != 'ALL':
            records=records.filter(user_name__istartswith=letter)
        else:
            records=records.all()

    #This Loop for Checking whether the image is Binaryfile or httpslink or Noimage
    for item in records:
        if item.userprofile:
            if 'https' in str(item.userprofile):
                i=str(item.userprofile).replace("b","")
                i=i.replace("'","")
                link.append(i)
            else:
                #Here i have used Base64 Encoding to convert binary data to jpg file
                item.userprofile=base64.b64encode(item.userprofile).decode('utf-8')
                link.append("")   
        else:
            binary=open("C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/dimage.jpg","rb")
            item.userprofile=base64.b64encode(binary.read()).decode('utf-8')
            link.append("") 

        #Splitting a Phone number and stored in to specified list     
        split=item.user_phno.split(',')
        if len(split)>1:
            pri_ph.append(split[0])
            sec_ph.append(split[1])
        else:
            pri_ph.append(split[0])
            sec_ph.append('none')

    #Joining a fourlists(my_data,pri_phno,sec_phno,link) in single variable
    join=zip(records,pri_ph,sec_ph,link)    

    #Rendering a HTML page        
    return render(request,'homepage.html',{"records":join,"My_data":my_data})


