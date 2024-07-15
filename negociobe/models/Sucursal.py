from django.db import models

class Sucursal(models.Model):
    idsucursal = models.AutoField(primary_key=True)
    numero = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    idnegocio = models.ForeignKey('negociobe.Negocio', on_delete=models.DO_NOTHING, db_column='idnegocio')
    flagescentral = models.BooleanField(blank=True, null=True)
    localizacionx = models.DecimalField(max_digits=12, decimal_places=9, blank=True, null=True)
    localizaciony = models.DecimalField(max_digits=12, decimal_places=9, blank=True, null=True)

    class Meta:
        db_table = 'gen_sucursal'