from rest_framework import serializers
from .models import Cliente, CuentaAhorro, TipoCuenta, Transaccion

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class TipoCuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCuenta
        fields = '__all__'

class CuentaAhorroSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuentaAhorro
        fields = '__all__'

class TransaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaccion
        fields = '__all__'