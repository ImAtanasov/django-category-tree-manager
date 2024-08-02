"""
URL configuration for category_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, CategorySimilarityViewSet, category_list, category_similarities_list, \
    UserCreateView, UpdateCategoryByNameView, DeleteCategoryByNameView, GetCategoryByNameView, \
    GetCategoriesByParentNameView, GetAllCategoriesView, GetCategoriesByLevelView, GetAllCategorySimilaritiesView, \
    GetCategorySimilarityByNameView, DeleteCategorySimilarityByNameView, UpdateCategorySimilarityByNameView, \
    CreateCategorySimilarityView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'similarities', CategorySimilarityViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # UI lists
    path('category-list/', category_list, name='category_list'),
    path('category-similarities-list/', category_similarities_list, name='category_similarities_list'),
    # Potential authentication
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserCreateView.as_view(), name='user_register'),
    # Categories endpoints
    path('updatebyname/<str:name>/', UpdateCategoryByNameView.as_view(), name='update-category-by-name'),
    path('deletebyname/<str:name>/', DeleteCategoryByNameView.as_view(), name='delete-category-by-name'),
    path('getbyname/<str:name>/', GetCategoryByNameView.as_view(), name='get-category-by-name'),
    path('getbyparentname/<str:parent_name>/', GetCategoriesByParentNameView.as_view(),
         name='get-categories-by-parent-name'),
    path('getallcategories/', GetAllCategoriesView.as_view(), name='get-all-categories'),
    path('getbylevel/<int:level>/', GetCategoriesByLevelView.as_view(), name='get-categories-by-level'),
    # Similarities endpoints
    path('updatebya/<str:name>/', UpdateCategorySimilarityByNameView.as_view(), name='update-similarity-by-name'),
    path('deletebya/<str:name>/', DeleteCategorySimilarityByNameView.as_view(), name='delete-similarity-by-name'),
    path('getbya/<str:name>/', GetCategorySimilarityByNameView.as_view(), name='get-similarity-by-name'),
    path('getallsimilarities/', GetAllCategorySimilaritiesView.as_view(), name='get-all-similarities'),
    path('create/', CreateCategorySimilarityView.as_view(), name='create-similarity'),
]
