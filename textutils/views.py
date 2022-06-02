# I have created this file - Himmu

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyzer(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newline = request.POST.get('newline','off')
    spaceremover = request.POST.get('spaceremover','off')
    
    if removepunc == 'on':
        punctuations = '''!"#$%&'()* +,-./:;<=>?@[\]^_`{|}~'''
        analyzed_txt = ''
        for char in djtext:
            if char not in punctuations:
                analyzed_txt = analyzed_txt + char
        params = {'purpose':'Removed Punctuations','Analyzed':analyzed_txt}
        djtext = analyzed_txt

    if fullcaps == 'on':
        analyzed_txt = ''
        for char in djtext:
            analyzed_txt = analyzed_txt + char.upper()
        params = {'purpose':'UPPER CASE','Analyzed':analyzed_txt}
        djtext = analyzed_txt

    if newline == 'on':
        analyzed_txt = ''
        for char in djtext:
            if char != '\n' and char!='\r':
                analyzed_txt = analyzed_txt + char
        params = {'purpose':'New Line Remover','Analyzed':analyzed_txt}
        djtext = analyzed_txt

    if spaceremover == 'on':
        analyzed_txt = ''
        for index,char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed_txt = analyzed_txt + char
        params = {'purpose':'Space Remover','Analyzed':analyzed_txt}
        djtext = analyzed_txt

    if spaceremover != 'on' and newline != 'on' and fullcaps != 'on' and  removepunc != 'on' :
        return HttpResponse('Please Select atleast one option!')
        
    return render(request, 'analyzed.html', params)
