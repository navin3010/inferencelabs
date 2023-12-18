from ecom import models
from rest_framework import response, serializers

class IsExists:

    def category_title_is_exists(self, title: str):
        data = models.Categories.objects.filter(title=title)
        if data:
            raise serializers.ValidationError(
                    {
                        "result": False,
                        "msg": "Category already exists"
                    },
                    code="validation_error",
                )
        