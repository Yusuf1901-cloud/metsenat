from django.db import models
from django.utils import timezone

ENTITY_TYPE = [
    ('PHY', 'PHYSICAL ENTITY'),
    ('LEG', 'LEGAL ENTITY'),
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
        return self.fio


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
    phone_num = models.CharField(max_length=13)
    otm = models.ForeignKey(University, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=StudyType.choices, default=StudyType.BACHELOR)
    created = models.DateTimeField(auto_now_add=True)
    cont_amount = models.IntegerField()

    class Meta:
        ordering = ['-cont_amount']

    def __str__(self):
        return self.fio


class SponsorShip(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='sponsorship')
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='sponsorship')
    dist_amount = models.IntegerField()

    class Meta:
        ordering = ['-dist_amount']

    def __str__(self):
        return f"{self.id} \'id\' li donate"


class Dashboard(models.Model):
    paid_amount = models.IntegerField()
    required_amount = models.IntegerField()
    asked_amount = models.IntegerField()

    def __str__(self):
        return f""