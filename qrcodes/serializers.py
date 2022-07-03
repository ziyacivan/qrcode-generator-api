import os
from core.settings import BASE_DIR
from rest_framework.serializers import ModelSerializer
from qrcodes.models import QRCode

class QRCodeSerializer(ModelSerializer):
    class Meta:
        model = QRCode
        exclude = ('id', 'file_name', 'owner')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['file'] = os.path.join(BASE_DIR, 'qrcodes', 'images', instance.file_name)
        return data