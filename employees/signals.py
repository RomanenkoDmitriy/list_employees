from django.db.models.signals import post_save, pre_delete, post_delete
from django.dispatch import receiver
from employees.models import *


@receiver(pre_delete, sender=Employee)
def employee_delete(sender, instance: Employee, **kwargs):

    if instance.rank == 1:
        sender.objects.all().delete()

    else:
        subordinates = list(instance.employee_set.order_by('changed_at', 'created_at'))

        sub = subordinates.pop(0)
        sub.rank = instance.rank
        sub.chief = instance.chief
        sub.save()

        for subordinate in subordinates:
            subordinate.chief = sub
            subordinate.save()

