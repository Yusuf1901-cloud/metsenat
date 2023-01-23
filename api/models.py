from django.db import models
from django.utils import timezone

ENTITY_TYPE = [
    ('PHY', 'PHYSICAL ENTITY'),
    ('LEG', 'LEGAL ENTITY')
]


class Application(models.Model):
    class STATUS(models.TextChoices):
        NEW = 'NW', 'New'
        BEING_MODERATED = 'BM', 'Being Moderated'
        APPROVED = 'AP', 'Approved'
        REJECTED = 'RJ', 'Rejected'

    fio = models.CharField(max_length=250)
    phone_num = models.CharField(max_length=13)
    donate_amount = models.IntegerField()
    entity_type = models.CharField(max_length=3, choices=ENTITY_TYPE, default='PHY')
    firm_name = models.CharField(max_length=250, null=True, blank=True)
    status = models.CharField(max_length=2, choices=STATUS.choices, default=STATUS.NEW)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        self.fio


class University(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Student(models.Model):

    class StudyType(models.TextChoices):
        BACHELOR = "BK", 'Bachelor'
        MASTER = "MS", 'Master'
        Doctor = "DK", 'Doctor'

    fio = models.CharField(max_length=250)
    otm = models.ForeignKey(University, on_delete=models.CASCADE)

