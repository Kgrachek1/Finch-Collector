from django.shortcuts import render

finches = [
{'name':'Evening Grosbeak' , 'description':'Heavily Built with large bills and short tails', 'age':4}
    ]
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finch_index(request):
    return render(request, 'finches/index.html', {
       'finches': finches
        })