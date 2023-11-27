from django.http import HttpResponse
from django.shortcuts import render,redirect
from miniprojectapp.models import academictable,culturaltable,eventstable,nsstable,placementstable,sportstable,rightmsgtable
import datetime
from django.utils import timezone





def homepage(request):
   
   
  
    return render(request,'home.html')


def academic(request):
    
    

    academicdata={"academicdata":academictable.objects.all().order_by('-id'),
                   'rightdata':rightmsgtable.objects.all().order_by('-id')
                   }
                
    
    if request.method=="POST"and request.FILES['file']:
        try:
            n1=request.POST.get('title')
            n2=request.POST.get('description')
            file=request.FILES['file']
            type=request.POST.get('type')
          
            if type=='image':
                type=True
            else:
                type=False
            
            
            en=academictable(title=n1,description=n2,image=file,type=type)
            en.save()
        except:
            pass

    if request.method=="GET":
        try:
            name=request.GET['rightmg']
            if name=='':
                pass
            else:
                data=rightmsgtable(name=name)
                data.save()
            
          
        except:
            pass
    
   
    return render(request,'academic.html',academicdata)








def cultural(request):
    academicdata={"academicdata":culturaltable.objects.all().order_by('-id'),
                   'rightdata':rightmsgtable.objects.all().order_by('-id')
                
                  }
    
    if request.method=="POST"and request.FILES['cfile']:
        try:
            n1=request.POST.get('ctitle')
            n2=request.POST.get('cdescription')
            file=request.FILES['cfile']
            type=request.POST.get('ctype')
           
        
            if type=='image':
                type=True
            else:
                type=False
            
            en=culturaltable(title=n1,description=n2,image=file,type=type)
            en.save()
        except:
            pass

    if request.method=="GET":
        try:
            name=request.GET['rightmg']
            if name=='':
                pass
            else:
                data=rightmsgtable(name=name)
                data.save()
         
        except:
            pass

    
    
    return render(request,'cultural.html',academicdata)






def events(request):
    current_date = timezone.now().strftime("%Y-%m-%d")
   
    
    academicdata={"academicdata":eventstable.objects.all().order_by('-id'),
                   'rightdata':rightmsgtable.objects.all().order_by('-id'),
                   
                    
    
    'current_date': current_date,
                  }
    
    if request.method=="POST"and request.FILES['efile']:
        try:
            n1=request.POST.get('etitle')
            n2=request.POST.get('edescription')
            file=request.FILES['efile']
            edate=request.POST.get('edate')
            type=request.POST.get('etype')
 
            print(type)
            if type=='image':
                type=True
            else:
                type=False
            
            en=eventstable(title=n1,description=n2,image=file,date=edate,type=type)
            en.save()
        except:
            pass

    if request.method=="GET":
        try:
            name=request.GET['rightmg']
            if name=='':
                pass
            else:
                data=rightmsgtable(name=name)
                data.save()
            
        except:
            pass



   
    

    
    
    
    return render(request,'events.html',academicdata)







def nss(request):
    current_date = timezone.now().strftime("%Y-%m-%d")
    academicdata={"academicdata":nsstable.objects.all().order_by('-id'),
                'rightdata':rightmsgtable.objects.all().order_by('-id'),
                'current_date': current_date,

                  }
    
    if request.method=="POST"and request.FILES['nfile']:
        try:
            n1=request.POST.get('ntitle')
            n2=request.POST.get('ndescription')
            file=request.FILES['nfile']
            ndate=request.POST.get('ndate')
            type=request.POST.get('ntype')

           
            if type=='image':
                type=True
            else:
                type=False
            
            en=nsstable(title=n1,description=n2,image=file,date=ndate,type=type)
            en.save()
        except:
            pass

    if request.method=="GET":
        try:
            name=request.GET['rightmg']
            if name=='':
                pass
            else:
                data=rightmsgtable(name=name)
                data.save()
            
        except:
            pass
    return render(request,'nss.html',academicdata)







def placements(request):
    academicdata={"academicdata":placementstable.objects.all().order_by('-id'),
                'rightdata':rightmsgtable.objects.all().order_by('-id')

                  }
    
    if request.method=="POST"and request.FILES['pfile']:
        try:
            n1=request.POST.get('ptitle')
            n2=request.POST.get('pdescription')
            file=request.FILES['pfile']
            type=request.POST.get('ptype')

           
        
            if type=='image':
                type=True
            else:
                type=False
            
            en=placementstable(title=n1,description=n2,image=file,type=type)
            en.save()
        except:
            pass

    if request.method=="GET":
        try:
            name=request.GET['rightmg']
            if name=='':
                pass
            else:
                data=rightmsgtable(name=name)
                data.save()
            
          
        except:
            pass
    
    return render(request,'placements.html',academicdata)







def sports(request):

    academicdata={"academicdata":sportstable.objects.all().order_by('-id'),
                   'rightdata':rightmsgtable.objects.all().order_by('-id')
               
                  }
    
    if request.method=="POST"and request.FILES['sfile']:
        try:
            n1=request.POST.get('stitle')
            n2=request.POST.get('sdescription')
            file=request.FILES['sfile']
            type=request.POST.get('stype')

            
            if type=='image':
                type=True
            else:
                type=False
            
            en=sportstable(title=n1,description=n2,image=file,type=type)
            en.save()
        except:
            pass

    if request.method=="GET":
        try:
            name=request.GET['rightmg']
            if name=='':
                pass
            else:
                data=rightmsgtable(name=name)
                data.save()
            
           
        except:
            pass



 
    return render(request,'sports.html',academicdata)







