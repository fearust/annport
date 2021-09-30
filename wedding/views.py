from django.shortcuts import render, get_object_or_404, redirect
from wedding.models import Mc
from taggit.models import Tag
from random import shuffle
from .forms import CastForm
from django.utils import timezone


def wedding_detail(request, mc_id):
    mc = get_object_or_404(Mc, pk=mc_id)
    tag_list = list(mc.tags.all())
    context = {'mc': mc, 'tag_list': tag_list}
    return render(request, 'wedding/mc_detail.html', context)


def wedding_list(request):
    mc_search_name = request.GET.get('mc_search_name', '')
    mc_search_tag = request.GET.get('mc_search_tag', '')
    mclist = Mc.objects.exclude(mcdisplay=False)
    if mc_search_name:
        mclist = mclist.filter(name__icontains=mc_search_name).distinct()
    if mc_search_tag:
        mc_search_tag_list = [tag.strip() for tag in mc_search_tag.split(',')]
        mclist = mclist.filter(tags__name__in=mc_search_tag_list).distinct()

    shuffle(mclist)
    mclist = mclist.order_by('-mcmain')
    all_tag_list = list(Tag.objects.all())

    context = {
        'mclist': mclist,
        'all_tag_list': all_tag_list,
        'mc_search_name': mc_search_name,
        'mc_search_tag': mc_search_tag
    }
    return render(request, 'wedding/mc_list.html', context)


def wedding_cast(request):
    if request.method == 'POST':
        castform = CastForm(request.POST)
        if castform.is_valid():
            castformquestion = castform.save(commit=False)
            castformquestion.create_date = timezone.now()
            castformquestion.save()
            return redirect('wedding:wedding_cast_success')
    elif request.method == 'GET':
        mc_cast_name = request.GET.get('mc_cast_name','')
        castform = CastForm()
        get_context = {
            'wish_mc': mc_cast_name,
            'castform': castform
        }
        return render(request, 'wedding/cast.html', get_context)
    else:
        castform = CastForm()
    context = {'castform': castform}
    return render(request, 'wedding/cast.html', context)

def wedding_cast_success(request):
    return render(request, 'wedding/cast_success.html')