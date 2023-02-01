from .models import SponsorShip, Dashboard, Student
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum


@receiver(post_save, sender=SponsorShip)
def update_dashboard(sender, instance, *args, **kwargs):
    dashboard = Dashboard.objects.first()
    asked_amount = Student.objects.all().aggregate(Sum('cont_amount')).get('cont_amount__sum'),
    paid_amount = SponsorShip.objects.all().aggregate(Sum('dist_amount')).get('dist_amount__sum')
    required_amount = asked_amount - paid_amount

    if dashboard:
        Dashboard.objects.create(
            asked_amount=asked_amount,
            paid_amount=paid_amount,
            required_amount=required_amount
        )
    else:
        dashboard.required_amount = required_amount
        dashboard.asked_amount = asked_amount
        dashboard.paid_amount = paid_amount
