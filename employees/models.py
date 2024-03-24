from django.db import models

"""
Есть список сотрудников.
У каждого сотрудника может быть начальник.
Древо иерархий мостигает 5 уровней, 
где 1 - главный босс, 5 - корм подножий.

Задача: написать Django модель/модели котораы позволят 
эффективно хранить и манипулировать данными для этого списка.

Требования:
1. У всех кроме босса должен быть начальник.
2. Нижестоящие ранги не могут быть начальниками над вышестоящими.
3. При увольнении(удалении) начальника подчиненного, новым начальником становится начальник уволенного. 
3.5 Ранг сотрудника повышаеться до ранга уволенного.
3.9 При возникновении конфликтов интересов начальником становиться тот кто дольше работает.

3.? При увольнении боса, увольняються все. 
"""


def delete_employees():
    # print('--------------------------------------------------------------------')
    return None


#     if obj.rank == 1:
#         return models.CASCADE
#     else:


class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.SmallIntegerField()
    rank = models.SmallIntegerField()
    chief = models.ForeignKey('self',
                              on_delete=models.SET(delete_employees),
                              null=True, blank=True,
                              )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    changed_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.rank}'
