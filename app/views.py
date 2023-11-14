from django.shortcuts import render
from joblib import load
# import numpy as np

# Create your views here.
def predict_price(request):


    if request.method == "POST":
        bhk = int(request.POST.get('bhk'))
        area = int(request.POST.get('area'))

        model = load("app/mumbai.pkl")
        white = model.predict([[bhk,area]])[0]
        black=white/2
        total=black+white

        total=int(total/10000)
        total=total*10000

        if(total<10000000):
            total=total/100000
            total=round(total,2)
            new=f"{total}L"
        else:
            total=total/10000000
            total=round(total,2)
            new=f"{total}Cr"


        return render(request, 'index.html', {'predicted_price': new})

    return render(request, 'index.html')