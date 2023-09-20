from django.shortcuts import render
import requests
# Create your views here.

def chatgpt(request):
        if request.method == 'POST':
            matn = request.POST.get('user_input')
            url = "https://chatgpt-api8.p.rapidapi.com/"

            payload = [
            {
                "content": f"{matn}",
                "role": "user",
            }
            ]
            headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": "1992518991msh95bfaa0aa166399p145a69jsnec193c0fb4f3",
            "X-RapidAPI-Host": "chatgpt-api8.p.rapidapi.com",
            }

            response = requests.post(url, json=payload, headers=headers)
            result = response.json()['text']
            context = {
                'result': result
            }
            return render(request, 'chatgpt.html',context=context)
        return render(request, 'chatgpt.html')
            
            
        
    