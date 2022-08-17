from django.shortcuts import render
from .models import Headline
from  .getnews.getnews  import get_business, get_news, get_indin, get_sports, get_world, get_politics, get_entertainment, get_miscellaneous, get_startup, get_technology, get_hindibusiness, get_hindientertainment, get_hindiindin, get_hindimiscellaneous, get_hindinews, get_hindipolitics, get_hindisports, get_hindistartup, get_hinditechnology, get_hindiworld
import random


def shownews(request):

    get_news()

    headlines = Headline.objects.order_by('?')
    preview = []
    right, left = 3, 3

    for head in headlines:
        if head.leaning == 'right' and right > 0 and head.img:
            preview.append(head)
            right -= 1
        elif head.leaning == 'left' and left > 0 and head.img:
            preview.append(head)
            left -= 1

    random.shuffle(preview)
    

    context = {
        'headline_list': headlines,
        'preview': preview,
        'num_headlines': len(headlines) #for debugging purposes
    }
    
    return render(request, 'news/news.html', context=context)


def shownews1(request):

    get_business()

    headlines = Headline.objects.order_by('?')
    preview = []
    right, left = 3, 3

    for head in headlines:
        if head.leaning == 'right' and right > 0 and head.img:
            preview.append(head)
            right -= 1
        elif head.leaning == 'left' and left > 0 and head.img:
            preview.append(head)
            left -= 1

    random.shuffle(preview)
    

    context = {
        'headline_list': headlines,
        'preview': preview,
        'num_headlines': len(headlines) #for debugging purposes
    }
    
    return render(request, 'news/news.html', context=context)

def shownews2(request):

    get_indin()

    headlines = Headline.objects.order_by('?')
    preview = []
    right, left = 3, 3

    for head in headlines:
        if head.leaning == 'right' and right > 0 and head.img:
            preview.append(head)
            right -= 1
        elif head.leaning == 'left' and left > 0 and head.img:
            preview.append(head)
            left -= 1

    random.shuffle(preview)
    

    context = {
        'headline_list': headlines,
        'preview': preview,
        'num_headlines': len(headlines) #for debugging purposes
    }
    
    return render(request, 'news/news.html', context=context)

def shownews3(request):

    get_sports()

    headlines = Headline.objects.order_by('?')
    preview = []
    right, left = 3, 3

    for head in headlines:
        if head.leaning == 'right' and right > 0 and head.img:
            preview.append(head)
            right -= 1
        elif head.leaning == 'left' and left > 0 and head.img:
            preview.append(head)
            left -= 1

    random.shuffle(preview)
    

    context = {
        'headline_list': headlines,
        'preview': preview,
        'num_headlines': len(headlines) #for debugging purposes
    }
    
    return render(request, 'news/news.html', context=context)


def shownews4(request):

    get_world()

    headlines = Headline.objects.order_by('?')
    preview = []
    right, left = 3, 3

    for head in headlines:
        if head.leaning == 'right' and right > 0 and head.img:
            preview.append(head)
            right -= 1
        elif head.leaning == 'left' and left > 0 and head.img:
            preview.append(head)
            left -= 1

    random.shuffle(preview)
    

    context = {
        'headline_list': headlines,
        'preview': preview,
        'num_headlines': len(headlines) #for debugging purposes
    }
    
    return render(request, 'news/news.html', context=context)


# get_business, get_news, get_indin, get_sports, get_world, get_politics, get_entertainment, get_miscellaneous, get_startup, get_technology

def shownews5(request):

    get_politics()

    headlines = Headline.objects.order_by('?')
    preview = []
    right, left = 3, 3

    for head in headlines:
        if head.leaning == 'right' and right > 0 and head.img:
            preview.append(head)
            right -= 1
        elif head.leaning == 'left' and left > 0 and head.img:
            preview.append(head)
            left -= 1

    random.shuffle(preview)
    

    context = {
        'headline_list': headlines,
        'preview': preview,
        'num_headlines': len(headlines) #for debugging purposes
    }
    
    return render(request, 'news/news.html', context=context)


def shownews6(request):

    get_entertainment()

    headlines = Headline.objects.order_by('?')
    preview = []
    right, left = 3, 3

    for head in headlines:
        if head.leaning == 'right' and right > 0 and head.img:
            preview.append(head)
            right -= 1
        elif head.leaning == 'left' and left > 0 and head.img:
            preview.append(head)
            left -= 1

    random.shuffle(preview)
    

    context = {
        'headline_list': headlines,
        'preview': preview,
        'num_headlines': len(headlines) #for debugging purposes
    }
    
    return render(request, 'news/news.html', context=context)


def shownews7(request):

    get_miscellaneous()

    headlines = Headline.objects.order_by('?')
    preview = []
    right, left = 3, 3

    for head in headlines:
        if head.leaning == 'right' and right > 0 and head.img:
            preview.append(head)
            right -= 1
        elif head.leaning == 'left' and left > 0 and head.img:
            preview.append(head)
            left -= 1

    random.shuffle(preview)
    

    context = {
        'headline_list': headlines,
        'preview': preview,
        'num_headlines': len(headlines) #for debugging purposes
    }
    
    return render(request, 'news/news.html', context=context)


def shownews8(request):

    get_startup()

    headlines = Headline.objects.order_by('?')
    preview = []
    right, left = 3, 3

    for head in headlines:
        if head.leaning == 'right' and right > 0 and head.img:
            preview.append(head)
            right -= 1
        elif head.leaning == 'left' and left > 0 and head.img:
            preview.append(head)
            left -= 1

    random.shuffle(preview)
    

    context = {
        'headline_list': headlines,
        'preview': preview,
        'num_headlines': len(headlines) #for debugging purposes
    }
    
    return render(request, 'news/news.html', context=context)


def shownews9(request):

    get_technology()

    headlines = Headline.objects.order_by('?')
    preview = []
    right, left = 3, 3

    for head in headlines:
        if head.leaning == 'right' and right > 0 and head.img:
            preview.append(head)
            right -= 1
        elif head.leaning == 'left' and left > 0 and head.img:
            preview.append(head)
            left -= 1

    random.shuffle(preview)
    

    context = {
        'headline_list': headlines,
        'preview': preview,
        'num_headlines': len(headlines) #for debugging purposes
    }
    
    return render(request, 'news/news.html', context=context)




def shownewshindi0(request):

    get_hindinews()

    headlines = Headline.objects.order_by('?')
    preview = []
    right, left = 3, 3

    for head in headlines:
        if head.leaning == 'right' and right > 0 and head.img:
            preview.append(head)
            right -= 1
        elif head.leaning == 'left' and left > 0 and head.img:
            preview.append(head)
            left -= 1

    random.shuffle(preview)
    

    context = {
        'headline_list': headlines,
        'preview': preview,
        'num_headlines': len(headlines) #for debugging purposes
    }
    
    return render(request, 'hindinews/news.html', context=context)


def shownewshindi1(request):

    get_hindibusiness()

    headlines = Headline.objects.order_by('?')
    preview = []
    right, left = 3, 3

    for head in headlines:
        if head.leaning == 'right' and right > 0 and head.img:
            preview.append(head)
            right -= 1
        elif head.leaning == 'left' and left > 0 and head.img:
            preview.append(head)
            left -= 1

    random.shuffle(preview)
    

    context = {
        'headline_list': headlines,
        'preview': preview,
        'num_headlines': len(headlines) #for debugging purposes
    }
    
    return render(request, 'hindinews/news.html', context=context)

def shownewshindi2(request):

    get_hindiindin()

    headlines = Headline.objects.order_by('?')
    preview = []
    right, left = 3, 3

    for head in headlines:
        if head.leaning == 'right' and right > 0 and head.img:
            preview.append(head)
            right -= 1
        elif head.leaning == 'left' and left > 0 and head.img:
            preview.append(head)
            left -= 1

    random.shuffle(preview)
    

    context = {
        'headline_list': headlines,
        'preview': preview,
        'num_headlines': len(headlines) #for debugging purposes
    }
    
    return render(request, 'hindinews/news.html', context=context)

def shownewshindi3(request):

    get_hindisports()

    headlines = Headline.objects.order_by('?')
    preview = []
    right, left = 3, 3

    for head in headlines:
        if head.leaning == 'right' and right > 0 and head.img:
            preview.append(head)
            right -= 1
        elif head.leaning == 'left' and left > 0 and head.img:
            preview.append(head)
            left -= 1

    random.shuffle(preview)
    

    context = {
        'headline_list': headlines,
        'preview': preview,
        'num_headlines': len(headlines) #for debugging purposes
    }
    
    return render(request, 'hindinews/news.html', context=context)


def shownewshindi4(request):

    get_hindiworld()

    headlines = Headline.objects.order_by('?')
    preview = []
    right, left = 3, 3

    for head in headlines:
        if head.leaning == 'right' and right > 0 and head.img:
            preview.append(head)
            right -= 1
        elif head.leaning == 'left' and left > 0 and head.img:
            preview.append(head)
            left -= 1

    random.shuffle(preview)
    

    context = {
        'headline_list': headlines,
        'preview': preview,
        'num_headlines': len(headlines) #for debugging purposes
    }
    
    return render(request, 'hindinews/news.html', context=context)



def shownewshindi5(request):

    get_hindipolitics()

    headlines = Headline.objects.order_by('?')
    preview = []
    right, left = 3, 3

    for head in headlines:
        if head.leaning == 'right' and right > 0 and head.img:
            preview.append(head)
            right -= 1
        elif head.leaning == 'left' and left > 0 and head.img:
            preview.append(head)
            left -= 1

    random.shuffle(preview)
    

    context = {
        'headline_list': headlines,
        'preview': preview,
        'num_headlines': len(headlines) #for debugging purposes
    }
    
    return render(request, 'hindinews/news.html', context=context)


def shownewshindi6(request):

    get_hindientertainment()

    headlines = Headline.objects.order_by('?')
    preview = []
    right, left = 3, 3

    for head in headlines:
        if head.leaning == 'right' and right > 0 and head.img:
            preview.append(head)
            right -= 1
        elif head.leaning == 'left' and left > 0 and head.img:
            preview.append(head)
            left -= 1

    random.shuffle(preview)
    

    context = {
        'headline_list': headlines,
        'preview': preview,
        'num_headlines': len(headlines) #for debugging purposes
    }
    
    return render(request, 'hindinews/news.html', context=context)



def shownewshindi7(request):

    get_hindimiscellaneous()

    headlines = Headline.objects.order_by('?')
    preview = []
    right, left = 3, 3

    for head in headlines:
        if head.leaning == 'right' and right > 0 and head.img:
            preview.append(head)
            right -= 1
        elif head.leaning == 'left' and left > 0 and head.img:
            preview.append(head)
            left -= 1

    random.shuffle(preview)
    

    context = {
        'headline_list': headlines,
        'preview': preview,
        'num_headlines': len(headlines) #for debugging purposes
    }
    
    return render(request, 'hindinews/news.html', context=context)


def shownewshindi8(request):

    get_hindistartup()

    headlines = Headline.objects.order_by('?')
    preview = []
    right, left = 3, 3

    for head in headlines:
        if head.leaning == 'right' and right > 0 and head.img:
            preview.append(head)
            right -= 1
        elif head.leaning == 'left' and left > 0 and head.img:
            preview.append(head)
            left -= 1

    random.shuffle(preview)
    

    context = {
        'headline_list': headlines,
        'preview': preview,
        'num_headlines': len(headlines) #for debugging purposes
    }
    
    return render(request, 'hindinews/news.html', context=context)


def shownewshindi9(request):

    get_hinditechnology()

    headlines = Headline.objects.order_by('?')
    preview = []
    right, left = 3, 3

    for head in headlines:
        if head.leaning == 'right' and right > 0 and head.img:
            preview.append(head)
            right -= 1
        elif head.leaning == 'left' and left > 0 and head.img:
            preview.append(head)
            left -= 1

    random.shuffle(preview)
    

    context = {
        'headline_list': headlines,
        'preview': preview,
        'num_headlines': len(headlines) #for debugging purposes
    }
    
    return render(request, 'hindinews/news.html', context=context)