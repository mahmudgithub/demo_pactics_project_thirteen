from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('app1.urls'), name='home'),
    path('cost/', include('app1.urls'), name='cost'),
    #path('add-expense/', views.add_expense, name='add-expense'),

]