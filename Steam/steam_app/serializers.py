from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import UserProfile, Game, Achievement, Clan

class UserProfileSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='UserProfile-detail')
    user = CharField(read_only=True)
    class Meta:
        model = UserProfile
        fields = ('uri','user', 'steam_id','nickname', 'real_name', 'city','stateOrProvince',
        'country','url_profile', 'friends')


