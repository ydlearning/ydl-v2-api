from graphene_django import DjangoObjectType
from graphene_django.rest_framework.mutation import SerializerMutation
import graphene

from graphql_jwt.decorators import login_required, superuser_required

from django.contrib.auth.models import User
from ydl_auth.models import YDL_User, YDL_Student, YDL_Teacher
from ydl_auth.serializers import UserSerializer

class UserType(DjangoObjectType):
    class Meta:
        model = User

class YDL_UserType(DjangoObjectType):
    class Meta:
        model = YDL_User

class YDL_StudentType(DjangoObjectType):
    class Meta:
        model = YDL_Student

class YDL_TeacherType(DjangoObjectType):
    class Meta:
        model = YDL_Teacher

class UserMutation(SerializerMutation):
    class Meta:
        serializer_class = UserSerializer
        model_operations = ["create", "update"]

# example for a graphql only implementation for a Mutation.
# But it would be necessary to also validate the input so a serializer is
# much more convenient

# class UserMutation(graphene.Mutation):
#     class Arguments:
#         username = graphene.String(required=True)
#         email = graphene.String(required=True)
#         password = graphene.String(required=True)

#     user = graphene.Field(UserType)

#     def mutate(self, info, username, email, password):
#         user = User.objects.create(
#                 username=username,
#                 email=email
#             )
#         user.set_password(password)
#         user.save()
        
#         return UserMutation(user=user)

class Mutation(graphene.ObjectType):
    create_user = UserMutation.Field()
    update_user = UserMutation.Field()

class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    all_ydl_users = graphene.List(YDL_UserType)
    all_ydl_students = graphene.List(YDL_StudentType)
    all_ydl_teachers = graphene.List(YDL_TeacherType)

    @superuser_required
    def resolve_all_users(self, info):
        return User.objects.all()

    @login_required
    def resolve_all_ydl_users(self, info):
        return YDL_User.objects.all()
    
    @login_required
    def resolve_all_ydl_students(self, info):
        return YDL_Student.objects.all()
    
    @login_required
    def resolve_all_students(self, info):
        return YDL_Teacher.objects.all()