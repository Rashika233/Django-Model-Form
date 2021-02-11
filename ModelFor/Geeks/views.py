'''from django.shortcuts import render

# Create your views here.

from .forms import GeeksForm 

def home_view(request): 
	form = GeeksForm()
	if request.method == 'POST':
		print(request.POST)
		form = GeeksForm(request.POST)
		if form.is_valid():
			form.save()

	# create object of form 
	
	# check if form data is valid 
	context={
		'form' : form
	} 
	return render(request, "home.html", context) 
'''

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import GeeksModel
from .serializers import GeeksSerializer
from .forms import GeeksForm


def home(request):
    tmpl_vars = {'form': PostForm()}
    return render(request, 'talk/index.html', tmpl_vars)


@api_view(['GET'])
def post_collection(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = GeeksSerializer(posts, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def post_element(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = GeeksSerializer(post)
        return Response(serializer.data)