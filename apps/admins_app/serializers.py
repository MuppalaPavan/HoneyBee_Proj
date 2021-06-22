from rest_framework.serializers import ModelSerializer, CharField, ImageField, Serializer, DictField, ListField, \
    SerializerMethodField
from .models import AdminUser, Function, Skill

class AdminLoginSerializer(ModelSerializer):
    admin_role = CharField(default='super_admin')

    class Meta:
        model = AdminUser
        fields = ('email', 'password', 'admin_role')


class AdminUserDetailSerializer(ModelSerializer):

    class Meta:
        model = AdminUser
        exclude = ('active', 'created', 'modified', 'password')


class ChangePasswordSerializer(ModelSerializer):
    old_password = CharField(required=True)
    new_password = CharField(required=True)

    class Meta:
        model = AdminUser
        fields = ('old_password', 'new_password',)



class FunctionSerializer(ModelSerializer):
    name = CharField(source='tag_name')

    class Meta:
        model = Function
        fields = ('id', 'name')


class SkillSerializer(ModelSerializer):
    name = CharField(source='tag_name')

    class Meta:
        model = Skill
        fields = ('id', 'name', 'function')


class SkillListingSerializer(ModelSerializer):
    name = CharField(source='tag_name')
    function = CharField(source='function.tag_name')

    class Meta:
        model = Skill
        fields = ('id', 'name', 'function')


class AdminProfileUpdateSerializer(ModelSerializer):

    class Meta:
        model = AdminUser
        fields = ('profile_pic', 'description', 'phone', 'first_name', 'last_name', 'country_code',)