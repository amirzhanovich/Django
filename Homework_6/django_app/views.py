from django.shortcuts import render
import json

def home(request):
    return render(request, template_name='home.html', context={})

def pricing(request):

    json_file_path = 'static/prices.json'
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    print(data)

    old_data = data["data"]
    print(type(old_data), old_data)
    new_data = sorted(old_data, key=lambda x: x["name"])

    for i in new_data:
        print(i)

    return render(request, template_name='pricing.html', context={'new_data': new_data})

def login(request):
    return render(request, template_name='login.html', context={})

def signup(request):
    return render(request, template_name='signup.html', context={})

def details(request):
    return render(request, template_name='details.html', context={})
