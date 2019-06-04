from rest_framework.serializers import ModelSerializer
from image_file_test.models import image_file as imfi
from drf_extra_fields.fields import Base64ImageField

class CreateMember(ModelSerializer):
    class Meta:
        model = imfi
        fields = '__all__'


class MyImageModelSerializer(ModelSerializer):
    # picture=Base64ImageField()
    
    class Meta:
        model=imfi
        fields= ('name','picture')
    def create(self, validated_data):
        # print("helloooo")
        name=validated_data.pop('name')
        try:
            picture=validated_data.pop('picture')
            return imfi.objects.create(name=name,picture=picture)
        except:
            return imfi.objects.create(name=name)

        