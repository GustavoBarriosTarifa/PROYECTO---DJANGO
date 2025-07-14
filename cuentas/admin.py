from django.contrib import admin
from .models import Cliente, CuentaAhorro, TipoCuenta, Transaccion

admin.site.register(Cliente)
admin.site.register(CuentaAhorro)
admin.site.register(TipoCuenta)
admin.site.register(Transaccion)