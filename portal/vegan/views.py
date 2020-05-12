from django.http import JsonResponse, HttpResponseRedirect, response, HttpResponse
from .forms import featureSelectionForm
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect


def home(request):
    if request.method == 'POST':
        featureform = featureSelectionForm(request.POST)
        # Get user input from feature date range selection form
        if featureform.is_valid():
            f = featureform.cleaned_data['features']
            # if the end date is earlier than start date, return the error message

    featureform = featureSelectionForm()
    return render(request, 'vegan/home.html', {'featureform': featureform})


def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data)  # http response


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        labels = ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"]
        default_items = [34, 14, 12, 32, 12, 90]
        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)
