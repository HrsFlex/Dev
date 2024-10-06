from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

import requests
from django.shortcuts import render

from dotenv import load_dotenv

from myproject.settings import GEMINI_API_KEY

def query_gemini_model(input_data):
    url = "https://api.gemini-model.com/v1/query"  # Make sure this is the correct API endpoint
    headers = {
        'Authorization': f"Bearer {GEMINI_API_KEY}",
        'Content-Type': 'application/json'
    }
    data = {
        'input': input_data,
        'mode': 'multimodal'
    }
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def ai_response_view(request):
    if request.method == "POST":
        input_data = request.POST.get("input_text")
        ai_response = query_gemini_model(input_data)
        if ai_response:
            return render(request, 'ai_response.html', {'response': ai_response})
        else:
            return render(request, 'error.html', {'error_message': "Failed to connect to Gemini API."})
    return render(request, 'ai_input.html')
def home(request):
    return render(request,'index2.html')
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
def service(request):
    return render(request,'service.html')
def detail(request):
    return render(request,'details.html')
def prediction(request):
    return render(request,'prediction.html')
def proof(request):
    return render(request,'proof.html')
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html');
def subscribe(request):
    return render(request,'aditional.html')