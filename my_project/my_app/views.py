from django.shortcuts import render, redirect
from .forms import PublisherForm
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
 

def publisher_dashboard(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.cleaned_data['category']
            title = form.cleaned_data['title']
            image = form.cleaned_data['image']
            price = form.cleaned_data['price']
            description = form.cleaned_data['description']

            model_class = {
                'popular':Popular,
                'new_arrivals':New_Arrivals,
                'lifestyles':Lifestyles,
                'entertainment':Entertainment,
                'sport':Sport,
                'holiday':Holiday,
                'fitness':Fitness,
                'competitive_exam':Competitive_Exam,
                'health':Health,
                'newspaper': Newspaper,
                'magazine': Magazine,
                'business': Business,
                'fashion': Fashion,
                'technology': Technology,
                'comic': Comic,
                'autocar': Autocar,
                
            }.get(category)

            if model_class:
                model_class.objects.create(
                    title=title,
                    image=image,
                    price=price,
                    description=description
                )
            
            return redirect('publisher_dashboard')

    else:
        form = PublisherForm()

    return render(request, 'publisher_dashboard.html', {'form': form})


def user_dashboard(request):
    category = request.GET.get('category', 'all')

    categorized_items = {
        "popular": list(Popular.objects.all()),
        "new_arrivals": list(New_Arrivals.objects.all()),
        "business": list(Business.objects.all()),
        "newspaper": list(Newspaper.objects.all()),
        "magazine": list(Magazine.objects.all()),
        "lifestyles": list(Lifestyles.objects.all()),
        "entertainment": list(Entertainment.objects.all()),
        "fashion": list(Fashion.objects.all()),
        "technology": list(Technology.objects.all()),
        "comic": list(Comic.objects.all()),
        "autocar": list(Autocar.objects.all()),
        "sport": list(Sport.objects.all()),
        "holiday": list(Holiday.objects.all()),
        "health": list(Health.objects.all()),
        "fitness": list(Fitness.objects.all()),
        "competitive_exam": list(Competitive_Exam.objects.all()),
    }

    # Add a category field to each item to use in the template
    for cat, items in categorized_items.items():
        for item in items:
            item.category_name = cat  # Assign category name to each item

    if category != 'all':
        items = categorized_items.get(category, [])
        categorized_items = {category: items}  
    else:
        items = sum(categorized_items.values(), [])

    return render(request, 'user_dashboard.html', {'categorized_items': categorized_items, 'category': category, 'items': items})

# Mapping category names to their respective models
MODEL_CLASS = {
    'popular': Popular,
    'new_arrivals': New_Arrivals,
    'lifestyles': Lifestyles,
    'entertainment': Entertainment,
    'sport': Sport,
    'holiday': Holiday,
    'fitness': Fitness,
    'competitive_exam': Competitive_Exam,
    'health': Health,
    'newspaper': Newspaper,
    'magazine': Magazine,
    'business': Business,
    'fashion': Fashion,
    'technology': Technology,
    'comic': Comic,
    'autocar': Autocar,
}

def view_all(request):
    category = request.GET.get('category', None)

    if category in MODEL_CLASS:
        model = MODEL_CLASS[category]  # Get the correct model
        items = model.objects.all()  # Fetch all items from that model
    else:
        items = []  # If category not found, return an empty list

    return render(request, 'viewall.html', {'items': items, 'category': category})


def item_detail(request, category, item_id):
    model_mapping = {
        'popular': Popular,
        'new_arrivals': New_Arrivals,
        'lifestyles': Lifestyles,
        'entertainment': Entertainment,
        'sport': Sport,
        'holiday': Holiday,
        'fitness': Fitness,
        'competitive_exam': Competitive_Exam,
        'health': Health,
        'newspaper': Newspaper,
        'magazine': Magazine,
        'business': Business,
        'fashion': Fashion,
        'technology': Technology,
        'comic': Comic,
        'autocar': Autocar,
    }

    model = model_mapping.get(category)
    if not model:
        return render(request, '404.html')  

    item = get_object_or_404(model, id=item_id)
    recent_visits = request.session.get('recent_visits', [])
    visit_entry = {'category': category, 'id': item_id}
    recent_visits = [entry for entry in recent_visits if entry != visit_entry]
    recent_visits.insert(0, visit_entry)
    recent_visits = recent_visits[:5]
    request.session['recent_visits'] = recent_visits
    request.session.modified = True

    recent_items = []
    for entry in recent_visits:
        model = model_mapping.get(entry['category'])
        if model:
            item_instance = model.objects.get(id=entry['id'])
            recent_items.append({
                'id': item_instance.id,
                'title': item_instance.title,
                'image': item_instance.image,
                'date': item_instance.date,
                'readers_count': item_instance.readers_count,
                'category': entry['category']  # Pass category separately
            })
    return render(request, 'item_detail.html', {'item': item, 'recent_items': recent_items})



