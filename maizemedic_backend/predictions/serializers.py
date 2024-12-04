from rest_framework import serializers 

#not used now

class PredictionSerializer(serializers.Serializer):
    predicted_class = serializers.CharField(read_only=True)
    symptoms = serializers.CharField(read_only=True)
    prevention = serializers.CharField(read_only=True)
    treatment = serializers.CharField(read_only=True)
