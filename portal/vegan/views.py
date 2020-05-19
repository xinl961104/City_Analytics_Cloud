import pandas as pd
from django.http import JsonResponse, HttpResponseRedirect, response, HttpResponse
from .forms import featureSelectionForm
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect
from cloudant import CouchDB


def home(request):
    if request.method == 'POST':
        featureform = featureSelectionForm(request.POST)
        # Get user input from feature date range selection form
        if featureform.is_valid():
            f = featureform.cleaned_data['features']
            # if the end date is earlier than start date, return the error message

            # CouchDB authentication
            username = 'admin'
            password = 'password'
            url = 'http://172.26.132.199:5984/'
            client = CouchDB(username, password, url=url, connect=True)
            db_processed = client['processed_data']
            view_processed = db_processed.get_design_document('ddoc001').get_view('mapreduce')
            view1 = view_processed.custom_result(group=True)
            senti_by_region = {'code': [], 'senti_scores': [], 'tweet_count': []}
            with view1 as view1:
                for row in view1:
                    senti_by_region['code'].append(int(row['key']))
                    senti_by_region['senti_scores'].append(round(row['value']['sum'] / row['value']['count'], 3))
                    senti_by_region['tweet_count'].append(row['value']['count'])
            senti_by_region = pd.DataFrame(senti_by_region)

            db_edu = client['aurin_edu']
            view = db_edu.get_design_document('ddoc001').get_view('mapreduce')
            view_edu = view.custom_result(group=False)
            edu_table = {'code': [], 'tertiary_pop': []}
            with view_edu as view_edu:
                for row in view_edu:
                    edu_table['code'].append(int(row['key']))
                    edu_table['tertiary_pop'].append(int(row['value']))
            edu_table = pd.DataFrame(edu_table)

            code_name = {'code': [206, 207, 208, 209, 210, 211, 212, 213, 214],
                         'region_name': ['Melbourne - Inner', 'Melbourne - Inner East', 'Melbourne - Inner South',
                                         'Melbourne - North East', 'Melbourne - North West', 'Melbourne - Outer East',
                                         'Melbourne - South East', 'Melbourne - West', 'Mornington Peninsula']}
            region_label = code_name['region_name']

            code_name = pd.DataFrame(code_name)
            edu_table = edu_table.merge(code_name, left_on='code', right_on='code')
            edu_twitter = edu_table.merge(senti_by_region, left_on='code', right_on='code')
            # print(edu_twitter)
            # print(region_label)
            tertiary_list = [edu_twitter.iloc[0, 1],edu_twitter.iloc[1, 1], edu_twitter.iloc[2, 1],
                             edu_twitter.iloc[3, 1],edu_twitter.iloc[4, 1], edu_twitter.iloc[5, 1],
                             edu_twitter.iloc[6, 1],edu_twitter.iloc[7, 1], edu_twitter.iloc[8, 1]]
            print(tertiary_list)

            senti_list = [edu_twitter.iloc[0, 3],edu_twitter.iloc[1, 3], edu_twitter.iloc[2, 3],
                             edu_twitter.iloc[3, 3],edu_twitter.iloc[4, 3], edu_twitter.iloc[5, 3],
                             edu_twitter.iloc[6, 3],edu_twitter.iloc[7, 3], edu_twitter.iloc[8, 3]]
            print(senti_list)
            tweet_count = [edu_twitter.iloc[0, 4], edu_twitter.iloc[1, 4], edu_twitter.iloc[2, 4],
                          edu_twitter.iloc[3, 4], edu_twitter.iloc[4, 4], edu_twitter.iloc[5, 4],
                          edu_twitter.iloc[6, 4], edu_twitter.iloc[7, 4], edu_twitter.iloc[8, 4]]
            print(tweet_count)
            args = {'featureform': featureform, 'tertiary_list': tertiary_list, 'senti_list': senti_list, 'tweet_count': tweet_count, 'region_label': region_label}
            return render(request, 'vegan/home.html', args)

    featureform = featureSelectionForm()
    return render(request, 'vegan/home.html', {'featureform': featureform})


def income(request):
    if request.method == 'POST':
        featureform = featureSelectionForm(request.POST)
        # Get user input from feature date range selection form
        if featureform.is_valid():
            f = featureform.cleaned_data['features']
            # if the end date is earlier than start date, return the error message

            # CouchDB authentication
            # print(f)
            username = 'admin'
            password = 'password'
            url = 'http://172.26.132.199:5984/'
            client = CouchDB(username, password, url=url, connect=True)
            db_processed = client['processed_data']
            view_processed = db_processed.get_design_document('ddoc001').get_view('mapreduce')
            view1 = view_processed.custom_result(group=True)
            senti_by_region = {'code': [], 'senti_scores': [], 'tweet_count': []}
            with view1 as view1:
                for row in view1:
                    senti_by_region['code'].append(int(row['key']))
                    senti_by_region['senti_scores'].append(round(row['value']['sum'] / row['value']['count'], 3))
                    senti_by_region['tweet_count'].append(row['value']['count'])
            senti_by_region = pd.DataFrame(senti_by_region)

            db_income = client['aurin_income']
            view = db_income.get_design_document('ddoc001').get_view('mapreduce')
            view_income = view.custom_result(group=False)
            income_table = {'code': [], 'avg_income': []}
            with view_income as view_income:
                for row in view_income:
                    income_table['code'].append(int(row['key']))
                    income_table['avg_income'].append(int(row['value']))
            income_table = pd.DataFrame(income_table)

            code_name = {'code': [206, 207, 208, 209, 210, 211, 212, 213, 214],
                         'region_name': ['Melbourne - Inner', 'Melbourne - Inner East', 'Melbourne - Inner South',
                                         'Melbourne - North East', 'Melbourne - North West', 'Melbourne - Outer East',
                                         'Melbourne - South East', 'Melbourne - West', 'Mornington Peninsula']}
            code_name = pd.DataFrame(code_name)
            income_table = income_table.merge(code_name, left_on='code', right_on='code')
            income_twitter = income_table.merge(senti_by_region, left_on='code', right_on='code')
            # print(income_twitter)
            print(income_twitter.iloc[1, 4])
            return render(request, 'vegan/income.html')

    featureform = featureSelectionForm()

    return render(request, 'vegan/income.html', {'featureform': featureform})


def donation(request):
    if request.method == 'POST':
        featureform = featureSelectionForm(request.POST)
        # Get user input from feature date range selection form
        if featureform.is_valid():
            f = featureform.cleaned_data['features']
            # if the end date is earlier than start date, return the error message

            # CouchDB authentication
            print(f)
            username = 'admin'
            password = 'password'
            url = 'http://172.26.132.199:5984/'
            client = CouchDB(username, password, url=url, connect=True)
            db_processed = client['processed_data']
            view_processed = db_processed.get_design_document('ddoc001').get_view('mapreduce')
            view1 = view_processed.custom_result(group=True)
            senti_by_region = {'code': [], 'senti_scores': [], 'tweet_count': []}
            with view1 as view1:
                for row in view1:
                    senti_by_region['code'].append(int(row['key']))
                    senti_by_region['senti_scores'].append(round(row['value']['sum'] / row['value']['count'], 3))
                    senti_by_region['tweet_count'].append(row['value']['count'])
            senti_by_region = pd.DataFrame(senti_by_region)

            db_donation = client['aurin_donation']
            view = db_donation.get_design_document('ddoc001').get_view('mapreduce')
            view_income = view.custom_result(group=False)
            donation_table = {'code': [], 'donation_med': []}
            with view_income as view_income:
                for row in view_income:
                    donation_table['code'].append(int(row['key']))
                    donation_table['donation_med'].append(int(row['value']))
            donation_table = pd.DataFrame(donation_table)

            code_name = {'code': [206, 207, 208, 209, 210, 211, 212, 213, 214],
                         'region_name': ['Melbourne - Inner', 'Melbourne - Inner East', 'Melbourne - Inner South',
                                         'Melbourne - North East', 'Melbourne - North West', 'Melbourne - Outer East',
                                         'Melbourne - South East', 'Melbourne - West', 'Mornington Peninsula']}
            code_name = pd.DataFrame(code_name)
            donation_table = donation_table.merge(code_name, left_on='code', right_on='code')
            donation_twitter = donation_table.merge(senti_by_region, left_on='code', right_on='code')
            print(donation_twitter)
            return render(request, 'vegan/donation.html')

    featureform = featureSelectionForm()

    return render(request, 'vegan/donation.html', {'featureform': featureform})


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
