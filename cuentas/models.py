from django.db import models
from django.core.exceptions import ValidationError

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=10, unique=True)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def clean(self):
        if not self.dni.isdigit() or len(self.dni) != 10:
            raise ValidationError({'dni': 'El DNI debe contener exactamente 10 dígitos numéricos.'})
        if '@' not in self.email or '.' not in self.email:
            raise ValidationError({'email': 'El formato del email es inválido.'})
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class TipoCuenta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    tasa_interes_anual = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    def __str__(self):
        return self.nombre

class CuentaAhorro(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo_cuenta = models.ForeignKey(TipoCuenta, on_delete=models.CASCADE)
    numero_cuenta = models.CharField(max_length=20, unique=True)
    saldo = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    fecha_apertura = models.DateField(auto_now_add=True)
    activa = models.BooleanField(default=True)

    def clean(self):
        if self.saldo < 0:
            raise ValidationError({'saldo': 'El saldo inicial no puede ser negativo.'})

    def __str__(self):
        return self.numero_cuenta

class Transaccion(models.Model):
    cuenta = models.ForeignKey(CuentaAhorro, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=[('Deposito', 'Depósito'), ('Retiro', 'Retiro')])
    monto = models.DecimalField(max_digits=15, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.monto <= 0:
            raise ValidationError({'monto': 'El monto de la transacción debe ser positivo.'})

    def __str__(self):
        return f'{self.tipo} de {self.monto} en {self.cuenta.numero_cuenta}'