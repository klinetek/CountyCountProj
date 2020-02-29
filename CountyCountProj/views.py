from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddicitonary = {}
    for word in wordlist:
        if word in worddicitonary:
            #Increase
            worddicitonary[word] += 1
        else:
            #add to dictionary
            worddicitonary[word] = 1
    sortedWords = sorted(worddicitonary.items(), key = operator.itemgetter(1), reverse=True)

    return render(request, 'count.html' , {'fulltext':fulltext, 'count':len(wordlist), 'sortedWords':sortedWords})

def about(request):
    return render(request, 'about.html')
