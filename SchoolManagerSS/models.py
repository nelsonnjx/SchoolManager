from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField('Nombre y Apellido', max_length=70, help_text='Nombre y Apellidos del Estudiante')
    cedula = models.IntegerField('Cedula', primary_key=True, help_text='Cedula del Estudiante')
    fechaNacimiento = models.DateField('Fecha de Nacimiento', help_text='Fecha de Nacimiento del Estudiante')
    lugarNacimiento = models.CharField('Lugar de Nacimiento', help_text='Lugar de Nacimiento del Estudiante',
                                       max_length=70)
    MASCULINO = 'GM'
    FEMENINO = 'GF'
    GENDER_CHOICES = [
        (MASCULINO, 'Masculino'),
        (FEMENINO, 'Femenino'),
        ]
    gender = models.CharField('Sexo', choices=GENDER_CHOICES, help_text='Genero o Sexo del Estudiante')
    edad = models.IntegerField('Edad', help_text='Edad del Estudiante')
    direccion = models.TextField('Dirección', help_text='Dirección del Estudiante')
    INICIAL = 'IN'
    NIVEL1 = 'N1'
    NIVEL2 = 'N2'
    NIVEL3 = 'N3'
    GRADO1 = 'G1'
    GRADO2 = 'G2'
    GRADO3 = 'G3'
    GRADO4 = 'G4'
    GRADO5 = 'G5'
    GRADO6 = 'G6'
    GRADO_CHOICES = [
        (INICIAL, 'Inicial'),
        (NIVEL1, 'Kinder Garden Nivel 1'),
        (NIVEL2, 'Kinder Garden Nivel 2'),
        (NIVEL3, 'Kinder Garden Nivel 3'),
        (GRADO1, '1er Grado'),
        (GRADO2, '2do Grado'),
        (GRADO3, '3er Grado'),
        (GRADO4, '4to Grado'),
        (GRADO5, '5to Grado'),
        (GRADO6, '6to Grado'),
    ]
    ultimoGrado = models.CharField('Último Grado Cursado', choices=GRADO_CHOICES, max_length=22,
                                   help_text='Último Grado Cursado Aprobado')
    lugarUltimo = models.CharField('Lugar de Último Grado Cursado', max_length=70,
                                   help_text='Lugar Donde Cursó Último Grado Aprobado')
    a_oUltimo = models.IntegerField('Año Último Grado Cursado', help_text='Año Donde Cursó Último Grado Aprobado')
    seccionesCursadas = models.ManyToManyField('Seccion_Abierta', related_name='Cursadas', blank=True)
    nombrePadre = models.CharField('Nombre y Apellido del Padre', max_length=70, blank=True)
    cedulaPadre = models.IntegerField('Cedula del Padre', blank=True)
    tlfPadre = models.CharField('Teléfono del Padre', max_length=12, blank=True)
    nombreMadre = models.CharField('Nombre y Apellido de la Madre', max_length=70, blank=True)
    cedulaMadre = models.IntegerField('Cedula de la Madre', blank=True)
    tlfMadre = models.CharField('Teléfono de la Madre', max_length=12, blank=True)
    Inscripcion = models.ForeignKey('Seccion_Abierta', related_name='Inscrito', blank=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-nombre']

class Docente(models.Model):

    nombre = models.CharField('Nombre y Apellido', max_length=70)
    cedula = models.IntegerField('Cedula', primary_key=True)
    direccion = models.TextField('Dirección')
    titulacion = models.CharField('Titulación o Nivel de Estudios', max_length=70)
    FIJO = 'FJ'
    PROVISIONAL = 'PR'
    DEPORTE = 'DE'
    SUPLENTE = 'SU'
    OTRO = 'OT'
    TIPO_CHOICES = [
        (FIJO, 'Fijo / Contratado'),
        (PROVISIONAL, 'Provisional'),
        (DEPORTE, 'Deporte'),
        (SUPLENTE, 'Suplente'),
        (OTRO, 'Otro'),
    ]
    tipo = models.CharField('Tipo', choices=TIPO_CHOICES, max_length=18)
    telefono1 = models.CharField('Teléfono Fijo', max_length=12, blank=True)
    telefono2 = models.CharField('Teléfono Móvil', max_length=12, blank=True)
    telefono3 = models.CharField('Otro Teléfono', max_length=12, blank=True)
    email = models.EmailField('Correo Electrónico', blank=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-nombre']

class Seccion(models.Model):
    INICIAL = 'IN'
    NIVEL1 = 'N1'
    NIVEL2 = 'N2'
    NIVEL3 = 'N3'
    GRADO1 = 'G1'
    GRADO2 = 'G2'
    GRADO3 = 'G3'
    GRADO4 = 'G4'
    GRADO5 = 'G5'
    GRADO6 = 'G6'
    GRADO_CHOICES = [
        (INICIAL, 'Inicial'),
        (NIVEL1, 'Kinder Garden Nivel 1'),
        (NIVEL2, 'Kinder Garden Nivel 2'),
        (NIVEL3, 'Kinder Garden Nivel 3'),
        (GRADO1, '1er Grado'),
        (GRADO2, '2do Grado'),
        (GRADO3, '3er Grado'),
        (GRADO4, '4to Grado'),
        (GRADO5, '5to Grado'),
        (GRADO6, '6to Grado'),
    ]
    grado = models.CharField('Grado o Nivel', max_length=22, choices=GRADO_CHOICES)
    Codigo = models.IntegerField('Código')
    Descripcion = models.TextField('Descripcion General', blank=True)

    def __str__(self):
        return self.title

class Periodo(models.Model):
    a_o = models.IntegerField('Año')
    fechaInicial = models.DateField('Fecha Inicial')
    fechaCulminacion = models.DateField('Fecha de Culminación')
    totalEstudiantes = models.IntegerField('Total Estudiantes Inscritos')

    def __str__(self):
        return self.title

class Seccion_Abierta(models.Model):
    aula = models.CharField('Aula', max_length=15)
    periodo = models.ForeignKey('Periodo')
    docente = models.ForeignKey('Docente')
    seccion = models.ForeignKey('Seccion')

    def __str__(self):
        return self.title

