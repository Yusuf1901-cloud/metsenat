from .models import SponsorShip, Dashboard, Student
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum


@receiver(post_save, sender=SponsorShip)
def update_dashboard(sender, instance: SponsorShip, *args, **kwargs):
    dashboard = Dashboard.objects.first()
    dist_amount = instance.dist_amount
    asked_amount = Student.objects.all().aggregate(asked=Sum('cont_amount')).get('asked')
    paid_amount = SponsorShip.objects.all().aggregate(paid=Sum('dist_amount')).get('paid') + dist_amount
    required_amount = asked_amount - paid_amount

    if dashboard is None:
        Dashboard.objects.create(
            asked_amount=asked_amount,
            paid_amount=paid_amount,
            required_amount=required_amount
        )
    else:
        dashboard.required_amount = required_amount
        dashboard.asked_amount = asked_amount
        dashboard.paid_amount = paid_amount
