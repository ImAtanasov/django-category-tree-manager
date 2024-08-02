from django.test import TestCase
from .models import Category, CategorySimilarity


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category", description="A test category")

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Test Category")
        self.assertEqual(self.category.description, "A test category")


class CategorySimilarityModelTest(TestCase):
    def setUp(self):
        self.category1 = Category.objects.create(name="Category 1", description="First category")
        self.category2 = Category.objects.create(name="Category 2", description="Second category")
        self.similarity = CategorySimilarity.objects.create(category_a=self.category1, category_b=self.category2)

    def test_similarity_creation(self):
        self.assertEqual(self.similarity.category_a, self.category1)
        self.assertEqual(self.similarity.category_b, self.category2)
