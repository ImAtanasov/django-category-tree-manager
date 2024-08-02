from django.shortcuts import render
from .models import Category, CategorySimilarity
from .serializers import CategorySerializer, CategorySimilaritySerializer, CategoryNameSerializer, \
    CategorySimilarityCreateUpdateSerializer
from django.core.cache import cache
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
import logging

logger = logging.getLogger(__name__)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class CategorySimilarityViewSet(viewsets.ModelViewSet):
    queryset = CategorySimilarity.objects.all()
    serializer_class = CategorySimilaritySerializer


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UpdateCategoryByNameView(APIView):
    def put(self, request, name):
        logger.info(f"Received PUT request with name: {name}")
        category = get_object_or_404(Category, name=name)
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteCategoryByNameView(APIView):
    def delete(self, request, name):
        logger.info(f"Received DELETE request with name: {name}")
        category = get_object_or_404(Category, name=name)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GetCategoryByNameView(APIView):
    def get(self, request, name):
        logger.info(f"Received GET request with name: {name}")
        category = get_object_or_404(Category, name=name)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


class GetCategoriesByParentNameView(APIView):
    def get(self, request, parent_name):
        logger.info(f"Received GET request with parent name: {parent_name}")
        parent = get_object_or_404(Category, name=parent_name)
        categories = Category.objects.filter(parent=parent)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class GetAllCategoriesView(APIView):
    def get(self, request):
        logger.info("Received GET request for all categories")
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class GetCategoriesByLevelView(APIView):
    def get(self, request, level):
        logger.info(f"Received GET request with level: {level}")
        categories = Category.objects.filter(level=level)
        serializer = CategoryNameSerializer(categories, many=True)
        return Response(serializer.data)


class CreateCategorySimilarityView(APIView):
    def post(self, request):
        logger.info("Received POST request to create similarity")
        serializer = CategorySimilarityCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateCategorySimilarityByNameView(APIView):
    def put(self, request, name):
        logger.info(f"Received PUT request for similarity with category name: {name}")
        category = get_object_or_404(Category, name=name)
        similarity = get_object_or_404(CategorySimilarity, category_a=category)
        serializer = CategorySimilarityCreateUpdateSerializer(similarity, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteCategorySimilarityByNameView(APIView):
    def delete(self, request, name):
        logger.info(f"Received DELETE request for similarity with category name: {name}")
        category = get_object_or_404(Category, name=name)
        similarity = get_object_or_404(CategorySimilarity, category_a=category)
        similarity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GetCategorySimilarityByNameView(APIView):
    def get(self, request, name):
        logger.info(f"Received GET request for similarity with category name: {name}")
        category = get_object_or_404(Category, name=name)
        similarities = CategorySimilarity.objects.filter(category_a=category) | CategorySimilarity.objects.filter(category_b=category)
        serializer = CategorySimilaritySerializer(similarities, many=True)
        return Response(serializer.data)


class GetAllCategorySimilaritiesView(APIView):
    def get(self, request):
        logger.info("Received GET request for all category similarities")
        similarities = CategorySimilarity.objects.all()
        serializer = CategorySimilaritySerializer(similarities, many=True)
        return Response(serializer.data)


def category_list(request):
    categories = cache.get('category_list')
    if not categories:
        categories = Category.objects.filter(parent=None).select_related('parent').prefetch_related('children')
        cache.set('category_list', categories, 60 * 2)  # Cache for 15 minutes
    return render(request, 'category_list.html', {'categories': categories})


def category_similarities_list(request):
    categories_similarities = CategorySimilarity.objects.filter()  # Get all root categories
    return render(request, 'category_similarities_list.html', {'categories_similarities': categories_similarities})
