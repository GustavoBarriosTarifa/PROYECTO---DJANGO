from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Cliente, CuentaAhorro, TipoCuenta, Transaccion
from .serializers import ClienteSerializer, CuentaAhorroSerializer, TipoCuentaSerializer, TransaccionSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class TipoCuentaViewSet(viewsets.ModelViewSet):
    queryset = TipoCuenta.objects.all()
    serializer_class = TipoCuentaSerializer

class CuentaAhorroViewSet(viewsets.ModelViewSet):
    queryset = CuentaAhorro.objects.all()
    serializer_class = CuentaAhorroSerializer

class TransaccionViewSet(viewsets.ModelViewSet):
    queryset = Transaccion.objects.all()
    serializer_class = TransaccionSerializer

@api_view(['POST'])
def realizar_deposito(request):
    try:
        numero_cuenta = request.data.get('numero_cuenta')
        monto = request.data.get('monto')
        
        if not numero_cuenta or not monto:
            return Response({'error': 'Número de cuenta y monto son requeridos.'}, status=status.HTTP_400_BAD_REQUEST)
        
        monto = float(monto)
        if monto <= 0:
            return Response({'error': 'El monto del depósito debe ser positivo.'}, status=status.HTTP_400_BAD_REQUEST)

        cuenta = CuentaAhorro.objects.get(numero_cuenta=numero_cuenta)
        cuenta.saldo += monto
        cuenta.save()

        Transaccion.objects.create(cuenta=cuenta, tipo='Deposito', monto=monto)
        
        serializer = CuentaAhorroSerializer(cuenta)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except CuentaAhorro.DoesNotExist:
        return Response({'error': 'Cuenta no encontrada.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)