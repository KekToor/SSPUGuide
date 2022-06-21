from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

def code_path(instance, filename):
    return 'media' + '/codes/' + str(instance.id) + '/' + filename

def sit_path(instance, filename):
    return 'media' + '/sit/' + str(instance.id) + '/' + filename


MGR = 'Mgr.'
ING = 'Ing.'
RNDR = 'RNDr.'
NONE = '_'

TITLES = [
    (MGR, 'Mgr.'),
    (ING, 'Ing.'),
    (RNDR, 'RNDr.'),
    (NONE, '_')
]


class Teacher(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Teacher Name', help_text='Zadejte jméno učitele')
    titul = models.CharField(max_length=7, default='_', choices=TITLES, verbose_name='Teacher \'s Title', help_text='Zadejte titul učitele')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.titul} {self.name}'


class SubjectInfo(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Subject Name', help_text='Zadejte jméno předmětu')
    short = models.CharField(max_length=5, unique=True, verbose_name='Subject Short', help_text='Zadejte jeho zkratku')
    desc = models.TextField(verbose_name='Subject Description', help_text='Popište předmět')
    teachers = models.ManyToManyField(Teacher, help_text='Zvolte učitele předmětu')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.ForeignKey(SubjectInfo, on_delete=models.CASCADE)
    classroom = models.CharField(max_length=10, help_text='Zadejte Název Učebny', verbose_name='Classroom Name')

    class Meta:
        ordering = ['name__name']

    def __str__(self):
        return self.name.name


class Lang(models.Model):
    name = models.CharField(max_length=100, verbose_name='Název jazyka', help_text='Název jazyka')
    desc = models.TextField(verbose_name='Popis jazyka', help_text='Popište programovací jazyk')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Code(models.Model):
    name = models.CharField(max_length=100, verbose_name='Obsah kódu', help_text='Krátce popište, co je cílem kódu')
    desc = models.TextField(verbose_name='Popis kódu', help_text='Stručně popište, jak bude kód fungovat')
    alignment = models.ForeignKey(SubjectInfo, on_delete=models.CASCADE)
    lang = models.ManyToManyField(Lang, help_text='Vyberte název jazyka')
    difficulty = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(10)],
                                     verbose_name='Obtížnost kódu (1-10)', help_text='Zadejte obtížnost kódu v hodnotách od 1 do 10')
    code = models.FileField(upload_to=code_path, null=True, verbose_name='Zdrojový kód')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.lang.all()[0]} - {self.name}'


class Sit(models.Model):
    name = models.CharField(max_length=100, verbose_name='Obsah kódu', help_text='Krátce popište, co je cílem kódu')
    desc = models.TextField(verbose_name='Popis kódu', help_text='Stručně popište, jak bude kód fungovat')
    shortdesc = models.TextField(verbose_name='Stručný popis kódu', help_text='Stručně popište, jak bude kód fungovat')
    difficulty = models.IntegerField(blank=True, null=True,
                                    validators=[MinValueValidator(1), MaxValueValidator(10)],
                                    verbose_name='Obtížnost kódu (1-10)',
                                    help_text='Zadejte obtížnost kódu v hodnotách od 1 do 10')
    sit = models.FileField(upload_to=sit_path, null=True, verbose_name='Zdrojový kód')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'







