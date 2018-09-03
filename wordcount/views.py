# -*- coding: utf-8 -*-
"""
Created on Sun Sep 02 13:52:55 2018

@author: ganes
"""

from django.http import HttpResponse
from django.shortcuts import render
import operator

def about(request):
    return render(request,'about.html')

def home(request):
    return HttpResponse("Hello Ganesh")

def homepage(request):
    return render(request,'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    fulltext_list = fulltext.split()
    wordcount= len(fulltext_list)
    worddict = dict  ( (i,fulltext_list.count(i)) for i in fulltext_list)
    print worddict
    return render(request,'count.html',{'fulltext':fulltext,'wordcount':wordcount, 'wordcounter': sorted(worddict.items(),key=operator.itemgetter(1),reverse=True)})