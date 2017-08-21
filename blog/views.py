from django.shortcuts import render, get_object_or_404, redirect
from .models import Eco
from django.db.models import Sum
import datetime

def post_list(request):
    #전체유저 카운트
    eco_aggre = Eco.objects.aggregate(Sum('ecocount'))
    eco=eco_aggre['ecocount__sum']

    #나의 카운트
    if request.user.is_anonymous():
        myeco=eco
    else:
        names = request.user
        eco_my_aggre = Eco.objects.filter(ecouser=names).aggregate(Sum('ecocount'))
        myeco = eco_my_aggre['ecocount__sum']

    # 30일안에 이용한  사람수
    ago = Eco.objects.values('ecouser').distinct().count()

    #폼버튼에 따라 더할지 뺄지
    if request.method == "POST":
        if request.POST.get('summary'):
            Eco.objects.create(ecouser=request.user, ecocount=-1)
            return redirect('post_list')
        elif request.POST.get('due_date'):
            Eco.objects.create(ecouser=request.user, ecocount=1)
            return redirect('post_list')
    return render(request, 'blog/post_list.html', {'eco': eco, 'myeco': myeco, 'ago':ago})


'''
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html',{'post': post})
'''


