from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.request import QueryDict
from django.http.response import HttpResponse
from .brow_motion import BrownianMotion
from .forms import BrownianForm

@csrf_exempt
def index(request):
    if request.method == "POST":
        dict = QueryDict(request.body)

        choice = dict['choice']
        context = {}

        mu = float(dict['mu'])
        sigma = float(dict['sigma'])
        T = float(dict['t'])
        n_ = int(dict['n'])
        no_of_paths = int(dict['no_of_paths'])
        S_0 = float(dict['s_0'])

        # return HttpResponse(n_)

        if choice == "bm":
            brow_motion = BrownianMotion(mu, sigma, T, n_, 1, no_of_paths, S_0)
            context = brow_motion.generate_brownian()
        else:
            brow_motion = BrownianMotion(mu, sigma, T, n_, 2, no_of_paths, S_0)
            context = brow_motion.generate_geo_brownian()

        context['image'] = f"data:image/png;base64, {context['image']}"; 

        return render(request, 'graph.html', context)
    else:
        brownianForm = BrownianForm(request.POST)
        return render(request, 'form.html', {"form": brownianForm})