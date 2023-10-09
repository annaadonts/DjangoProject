from django.shortcuts import render
from django.http import JsonResponse
from .your_python_script import run_python_script  # Qo pythoni script@ import ara

def index(request):
    return render(request, 'index.html')

def run_script(request):
    if request.method == 'POST':
        input_data = request.POST.get('input_data')

        #Kanchi Pythoni scriptd dataov
        result = run_python_script(input_data)

        # Veradardzru result@ vorpes JSON
        return JsonResponse({'result': result})
    else:
        return JsonResponse({'error': 'Invalid request method'})
