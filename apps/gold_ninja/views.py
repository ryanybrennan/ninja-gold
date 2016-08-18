from django.shortcuts import render, HttpResponse, redirect
import random
# Create your views here.
def index(request):
    try:
		request.session['your_gold']
    except KeyError:
		request.session['your_gold']=0
    try:
		request.session['activities']
    except KeyError:
        request.session['activities'] = []
    return render(request, 'gold_ninja/index.html')
def process(request):
    gold_dict={ 'farm': random.randint(10,20),
    'cave': random.randint(5,10),
    'house': random.randint(2,5),
    'casino': random.randint(-50, 50)}

    if "farm" in request.POST:
        building = 'farm'
    elif "cave" in request.POST:
        building = 'cave'
    elif "house" in request.POST:
        building = 'house'
    elif "casino" in request.POST:
        building = 'casino'
    request.session['your_gold'] += gold_dict[building]
    if gold_dict[building] > 0:
        request.session['activities'].append("<span class='green'>Entered a {} and gained {} golds!</span>".format(building, gold_dict[building]))
    else:
        request.session['activities'].append("<span class='red'>Entered a {} and lost {} golds!</span>".format(building, gold_dict[building]))
    return redirect('/')
def reset(request):
    request.session.clear()
    return redirect('/')
