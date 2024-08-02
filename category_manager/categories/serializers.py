from rest_framework import serializers
from .models import Category, CategorySimilarity
from django.contrib.auth.models import User


'''
The validated_data.pop('xxx_name', None) line is used to remove the xxx_name field 
from the validated_data dictionary before passing it to the create or update methods of 
the parent class. This is necessary because the parent_name field is not an actual field 
in the Category model; it is a custom field used only for input purposes to allow setting the parent category by name.
'''

# Serializer for Category model
class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()  # Custom field to get children categories
    parent_name = serializers.CharField(write_only=True, required=False)  # Custom field to handle parent by name

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'image', 'parent', 'parent_name', 'children']

    def get_children(self, obj):
        # Recursive serialization for children categories
        children = obj.get_children()
        return CategorySerializer(children, many=True).data

    def validate(self, data):
        # Validate and set parent category by name
        parent_name = data.get('parent_name')
        if parent_name:
            try:
                parent = Category.objects.get(name=parent_name)
                data['parent'] = parent
            except Category.DoesNotExist:
                raise serializers.ValidationError(f"Parent category with name '{parent_name}' does not exist.")
        return data

    def create(self, validated_data):
        # Remove parent_name from validated data before creating
        validated_data.pop('parent_name', None)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Remove parent_name from validated data before updating
        validated_data.pop('parent_name', None)
        return super().update(instance, validated_data)


class CategorySimilaritySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategorySimilarity
        fields = '__all__'

    def validate(self, data):
        if data['category_a'] == data['category_b']:
            raise serializers.ValidationError("Category A and Category B cannot be the same.")

        if CategorySimilarity.objects.filter(category_a=data['category_a'], category_b=data['category_b']).exists() or \
                CategorySimilarity.objects.filter(category_a=data['category_b'],
                                                  category_b=data['category_a']).exists():
            raise serializers.ValidationError("The combination of Category A and Category B must be unique.")

        return data


class CategoryWithSimilaritiesSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    similarities = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'image', 'parent', 'children', 'similarities']

    def get_children(self, obj):
        children = obj.get_children()
        return CategoryWithSimilaritiesSerializer(children, many=True).data

    def get_similarities(self, obj):
        similarities = CategorySimilarity.objects.filter(category_a=obj)
        return CategorySimilaritySerializer(similarities, many=True).data


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', ''),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user


class CategoryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class CategorySimilaritySerializer(serializers.ModelSerializer):
    category_a_name = serializers.CharField(source='category_a.name', read_only=True)
    category_b_name = serializers.CharField(source='category_b.name', read_only=True)

    class Meta:
        model = CategorySimilarity
        fields = ['category_a_name', 'category_b_name']

class CategorySimilarityCreateUpdateSerializer(serializers.ModelSerializer):
    category_a_name = serializers.CharField(write_only=True)
    category_b_name = serializers.CharField(write_only=True)

    class Meta:
        model = CategorySimilarity
        fields = ['category_a_name', 'category_b_name']

    def validate(self, data):
        category_a_name = data.get('category_a_name')
        category_b_name = data.get('category_b_name')

        try:
            category_a = Category.objects.get(name=category_a_name)
        except Category.DoesNotExist:
            raise serializers.ValidationError(f"Category A with name '{category_a_name}' does not exist.")

        try:
            category_b = Category.objects.get(name=category_b_name)
        except Category.DoesNotExist:
            raise serializers.ValidationError(f"Category B with name '{category_b_name}' does not exist.")

        if category_a == category_b:
            raise serializers.ValidationError("Category A and Category B cannot be the same.")

        data['category_a'] = category_a
        data['category_b'] = category_b
        return data

    def create(self, validated_data):
        validated_data.pop('category_a_name')
        validated_data.pop('category_b_name')
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop('category_a_name')
        validated_data.pop('category_b_name')
        return super().update(instance, validated_data)
