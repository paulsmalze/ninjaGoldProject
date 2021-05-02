from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    return render(request, 'index.html')
    
def process_money(request):
    if request.method == 'POST':
        myGold = request.session['gold']
        location = request.POST['location']
        if location == 'farm':
            #Earn 10-20 Gold
            goldThisTurn = round(random.random() * 10 + 10)
            #Add gold This Turn to my Gold
            myGold += goldThisTurn 
            #if its the first time my Gold will be 0 from above
            request.session['gold'] = myGold
    return redirect("/")