


1.-  Procesamiento de formularios y abreviacion de codigo

2.-  Crear nuestro Modelo


class Persona(models.Model):
    id = models.BigAutoField
    nombre = models.CharField(max_length=100)
    edad = models.SmallIntegerField()
    comuna = models.CharField(max_length=40)

3. - 
