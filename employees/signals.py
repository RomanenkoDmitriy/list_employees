from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from employees.models import *


@receiver(pre_save, sender=Employee)
def pre_save_employee(sender, instance: Employee, **kwargs):
    if instance.rank < 1:
        raise ValueError('Employee rank < 1')

    if not 1 <= instance.rank <= 5:
        raise ValueError('Wrong "rank" value from 1 to 5')

    if instance.rank == 1:
        if instance.chief:
            raise ValueError("Can't be the boss")
    else:
        if not instance.chief:
            raise ValueError("Can't be an empty field")

    if instance.rank < instance.chief.rank:
        raise ValueError('Supervisor addition error')




@receiver(pre_delete, sender=Employee)
def employee_delete(sender, instance: Employee, **kwargs):

    if instance.rank == 1:
        print('-----------------------', sender.objects.all())
        for obj in sender.objects.all():
            if obj.id != instance.id:
                obj.delete()

    else:
        subordinates = list(instance.employee_set.order_by('changed_at', 'created_at'))

        if subordinates:
            sub = subordinates.pop(0)
            sub.rank = instance.rank
            sub.chief = instance.chief
            sub.save()
        if subordinates:
            for subordinate in subordinates:
                subordinate.chief = sub
                subordinate.save()

