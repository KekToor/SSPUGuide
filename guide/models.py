from django.db import models

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
        return self.name


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
        ordering = ['name']

    def __str__(self):
        return self.name.name








