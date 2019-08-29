from graphene_django import DjangoObjectType
import graphene

from django.contrib.auth.models import User as DjangoUser

class User(DjangoObjectType):
    class Meta:
        model = DjangoUser

class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(self, info):
        return DjangoUser.objects.all()

schema = graphene.Schema(query=Query)