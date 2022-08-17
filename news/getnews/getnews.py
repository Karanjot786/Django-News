from .news_sites.getcbs import getcbs, indin, world, sports, business, politics, technology, startup, entertainment, miscellaneous
from .news_sites.gethindi import hindi_getcbs, hindi_indin, hindi_world, hindi_sports, hindi_business, hindi_politics, hindi_technology, hindi_startup, hindi_entertainment, hindi_miscellaneous
from ..models import Headline


def get_news():
    STORIES = 25
    SITES = 1
    per_site = STORIES // SITES

    Headline.objects.all().delete()
    getcbs(per_site)


def get_business():
    STORIES = 25
    SITES = 1
    per_site = STORIES // SITES

    Headline.objects.all().delete()
    business(per_site)

def get_indin():
    STORIES = 25
    SITES = 1
    per_site = STORIES // SITES

    Headline.objects.all().delete()
    indin(per_site)

def get_sports():
    STORIES = 25
    SITES = 1
    per_site = STORIES // SITES

    Headline.objects.all().delete()
    sports(per_site)

def get_world():
    STORIES = 25
    SITES = 1
    per_site = STORIES // SITES

    Headline.objects.all().delete()
    world(per_site)

def get_politics():
    STORIES = 25
    SITES = 1
    per_site = STORIES // SITES

    Headline.objects.all().delete()
    politics(per_site)

def get_technology():
    STORIES = 25
    SITES = 1
    per_site = STORIES // SITES

    Headline.objects.all().delete()
    technology(per_site)

def get_startup():
    STORIES = 25
    SITES = 1
    per_site = STORIES // SITES

    Headline.objects.all().delete()
    startup(per_site)

def get_entertainment():
    STORIES = 25
    SITES = 1
    per_site = STORIES // SITES

    Headline.objects.all().delete()
    entertainment(per_site)

def get_miscellaneous():
    STORIES = 25
    SITES = 1
    per_site = STORIES // SITES

    Headline.objects.all().delete()
    miscellaneous(per_site)
    



# hindi News



def get_hindinews():
    STORIES = 25
    SITES = 1
    per_site = STORIES // SITES

    Headline.objects.all().delete()
    hindi_getcbs(per_site)


def get_hindibusiness():
    STORIES = 25
    SITES = 1
    per_site = STORIES // SITES

    Headline.objects.all().delete()
    hindi_business(per_site)

def get_hindiindin():
    STORIES = 25
    SITES = 1
    per_site = STORIES // SITES

    Headline.objects.all().delete()
    hindi_indin(per_site)

def get_hindisports():
    STORIES = 25
    SITES = 1
    per_site = STORIES // SITES

    Headline.objects.all().delete()
    hindi_sports(per_site)

def get_hindiworld():
    STORIES = 25
    SITES = 1
    per_site = STORIES // SITES

    Headline.objects.all().delete()
    hindi_world(per_site)

def get_hindipolitics():
    STORIES = 25
    SITES = 1
    per_site = STORIES // SITES

    Headline.objects.all().delete()
    hindi_politics(per_site)

def get_hinditechnology():
    STORIES = 25
    SITES = 1
    per_site = STORIES // SITES

    Headline.objects.all().delete()
    hindi_technology(per_site)

def get_hindistartup():
    STORIES = 25
    SITES = 1
    per_site = STORIES // SITES

    Headline.objects.all().delete()
    startup(per_site)

def get_hindientertainment():
    STORIES = 25
    SITES = 1
    per_site = STORIES // SITES

    Headline.objects.all().delete()
    hindi_entertainment(per_site)

def get_hindimiscellaneous():
    STORIES = 25
    SITES = 1
    per_site = STORIES // SITES

    Headline.objects.all().delete()
    hindi_miscellaneous(per_site)
    