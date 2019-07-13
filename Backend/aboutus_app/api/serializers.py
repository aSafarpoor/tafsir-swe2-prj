from rest_framework.serializers import ModelSerializer

from aboutus_app.models import aboutus,contactus,news

# class CreateSerializer(ModelSerializer):
#     class Meta:
#         model=aboutus
#         fields='__all__'
# class EditSerializer(ModelSerializer):
#     class Meta:
#         model=aboutus
#         fields='__all__'
        

class ListSerializer(ModelSerializer):
    class Meta:
        model=aboutus
        fields='__all__'


class contactSerializer(ModelSerializer):
    class Meta:
        model=contactus
        fields='__all__'

class newsSerializer(ModelSerializer):
    class Meta:
        model=news
        fields='__all__'


# class CreateSerializer(ModelSerializer):
#     # picture=Base64ImageField()
    
#     class Meta:
#         model=aboutus
#         fields= ('title','explanation','file')
#     def create(self, validated_data):
#         # print("helloooo")
#         title=validated_data.pop('title')
#         explanation=validated_data.pop('explanation')
#         try:
#             file=validated_data.pop('file')
#             return aboutus.objects.create(title=title,explanation=explanation,file=file)
#         except:
#             return aboutus.objects.create(title=title,explanation=explanation)


# class EditSerializer(ModelSerializer):
#     # picture=Base64ImageField()
    
#     class Meta:
#         model=aboutus
#         fields= ('title','explanation','file')

#     def create(self, validated_data):
#         # print("helloooo")
#         title=validated_data.pop('title')
#         id=validated_data.pop("id")
#         explanation=validated_data.pop('explanation')
#         try:
#             file=validated_data.pop('file')

#             is_exist=aboutus.objects.filter(id=id).is_exist()
#             if(is_exist):
#                 obj=aboutus.objects.filter(id=id)[0]
#                 obj.title=title
#                 obj.explanation=explanation
#                 obj.file=file
#                 return obj
#             else:
#                 return null
#         except:
#             file=validated_data.pop('file')

#             is_exist=aboutus.objects.filter(id=id).is_exist()
#             if(is_exist):
#                 obj=aboutus.objects.filter(id=id)[0]
#                 obj.title=title
#                 obj.explanation=explanation
#                 return obj
#             else:
#                 return null