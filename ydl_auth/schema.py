from graphene_django import DjangoObjectType
import graphene

from django.contrib.auth.models import User
from ydl_auth.models import YDL_User, YDL_Student, YDL_Teacher

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

class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    all_ydl_users = graphene.List(YDL_UserType)
    all_ydl_students = graphene.List(YDL_StudentType)
    all_ydl_teachers = graphene.List(YDL_TeacherType)

    def resolve_all_users(self, info):
        return User.objects.all()

    def resolve_all_ydl_users(self, info):
        return YDL_User.objects.all()

    def resolve_all_ydl_students(self, info):
        return YDL_Student.objects.all()

    def resolve_all_students(self, info):
        return YDL_Teacher.objects.all()

schema = graphene.Schema(query=Query)