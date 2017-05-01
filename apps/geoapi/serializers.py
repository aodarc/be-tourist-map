from rest_framework_gis.serializers import GeoModelSerializer

from apps.marker.models import Marker


class MarkerSerializer(GeoModelSerializer):
    class Meta:
        model = Marker
        geo_field = "position"
        fields = ('title', 'type', 'position', 'description', 'main_img', 'address',)
        extra_kwargs = {
            'address': {'required': False},
            'main_img': {'required': False}
        }

    # TODO Upload image

    def get_main_img(self):
        return self.main_img.image.url

    # def create(self, validated_data):
    #     pass
    #
    # def update(self, instance, validated_data):
    #     pass
