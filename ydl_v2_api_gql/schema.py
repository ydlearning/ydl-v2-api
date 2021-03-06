import ydl_auth.schema
import graphql_jwt
import graphene

from graphene_django.debug import DjangoDebug

class Mutation(ydl_auth.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

class Query(
    ydl_auth.schema.Query,
    graphene.ObjectType
):
    debug = graphene.Field(DjangoDebug, name="_debug")

schema = graphene.Schema(query=Query, mutation=Mutation)