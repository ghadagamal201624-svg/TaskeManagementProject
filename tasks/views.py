from django.shortcuts import render
from todo_lists.models import TodoLists

def todo_list_view(request):
    # بنجيب كل القوائم الخاصة بالمستخدم اللي عامل تسجيل دخول حالياً
    # لو لسه مش عاملين نظام تسجيل دخول، هنعرض كل القوائم مؤقتاً
    lists = TodoLists.objects.all() 
    return render(request, 'tasks/todo_list.html', {'lists': lists})