from .models import MajorCategory, MinorCategory, Product
from rest_framework import permissions, status, response
from rest_framework.decorators import api_view, permission_classes

# A custom permission you are either the owner or all you can do is read only
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def getRoutes(request):
    routes = [
    # get all major categories
     'items/category/',
    # get all minor categories under a major category
     'items/category/<str:categoryname>',
    #  get all the items under a minor category
     'items/category/<str:categoryname>'
    ]
    return response.Response(routes, status=status.HTTP_200_OK)

# All major categories
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def majorCategories(request):
    categories = MajorCategory.objects.all()
    return response.Response([category.serialize() for category in categories], status=status.HTTP_200_OK)

# Minor categories from a Major Category using related name
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def specificMinorCategory(request, category):
    try:
           category = MajorCategory.objects.get(name = category.title())
    except MinorCategory.DoesNotExist:
        return response.Response("This category does not exist", status=status.HTTP_404_NOT_FOUND)
    
    categories = category.minorcategory.all()
    return response.Response([category.serialize() for category in categories], status=status.HTTP_200_OK)


# Items from a minor category using related name
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def getCategoryItems(request, majorcategory, minorcategory):
    try:
        # get the major category passed from the major category
        category = MajorCategory.objects.get(name = majorcategory.title())
        # Each major category has sub minor categories
        # get the minor category under the major gotten above
        category = category.minorcategory.get(name = minorcategory.title())
    except MinorCategory.DoesNotExist or MinorCategory.DoesNotExist:
        return response.Response("This category does not exist", status=status.HTTP_404_NOT_FOUND)
    
    items = category.categoryItems.all()
    return response.Response([item.serialize() for item in items], status=status.HTTP_200_OK)


@permission_classes([permissions.AllowAny])
@api_view(['GET'])
def getItemForDisplay(request, id):
    try:
        product = Product.objects.get(pk = id)
        return response.Response(product.serialize(), status=status.HTTP_200_OK)
    except Product.DoesNotExist:
        return response.Response("Item not found", status=status.HTTP_404_NOT_FOUND)


@permission_classes([permissions.IsAuthenticated, IsOwnerOrReadOnly])
@api_view(['PUT', 'DELETE'])
def getItemForUpdateOrDelete(request, method, id):
    try:
        product = Product.objects.get(pk = id)
    except Product.DoesNotExist:
        return response.Response("Item not found", status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        product = product(request.data)
        product.save()

    elif request.method == 'DELETE':
        product.delete()