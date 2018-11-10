from django.db import models
from django.contrib.auth.models import User

class Organizations(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='Наименование')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'


class Categories(models.Model):
    name = models.CharField(verbose_name='Наименование', null=False, blank=False, max_length=255)
    parent = models.ForeignKey('Categories', on_delete=models.PROTECT, verbose_name='Категория выше')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class ServiceTypes(models.Model):
    name = models.CharField(verbose_name='Наименование', null=False, blank=False, max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип услуги'
        verbose_name_plural = 'Типы услуг'


class WeekDays(models.Model):
    name = models.CharField(verbose_name='Наименование', null=False, blank=False, max_length=255)
    order_number = models.IntegerField(verbose_name='Очередь', null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'День недели'
        verbose_name_plural = 'Дни недели'


class TimeOffs(models.Model):
    week_day = models.ForeignKey(WeekDays, null=True, blank=False, on_delete=models.PROTECT,
                                    verbose_name='День недели')
    begin_time = models.TimeField(verbose_name='Время начало', null=True, blank=False)
    end_time = models.TimeField(verbose_name='Время конца', null=True, blank=False)
    exact_day = models.DateField(verbose_name='Точная дата', null=True, blank=False)

    def __str__(self):
        time =  self.week_day+' '+self.begin_time+'-'+self.end_time

        if(self.exact_day is not None):
            time += ' в ' + self.exact_day

        return time

    class Meta:
        verbose_name = 'Время отдыха'
        verbose_name_plural = 'Времена отдыхов'


class Services(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.PROTECT, null=False, blank=False,
                                 verbose_name=Categories._meta.verbose_name)
    organization = models.ForeignKey(Organizations, on_delete=models.PROTECT, null=False, blank=False,
                                     verbose_name=Organizations._meta.verbose_name)
    def __str__(self):
        return self.category.name + "  " + self.organization.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'



class ServiceNodes(models.Model):
    service = models.ForeignKey(Services, on_delete=models.PROTECT, blank=False,null=False, verbose_name=Services._meta.verbose_name)
    service_type = models.ForeignKey(ServiceTypes, on_delete=models.PROTECT, blank=False,null=False, verbose_name=ServiceTypes._meta.verbose_name)
    name = models.CharField(verbose_name='Наименование', null=False, blank=False, max_length=255)
    time_off = models.ForeignKey(TimeOffs,on_delete=models.PROTECT,blank=False,null=False,verbose_name=TimeOffs._meta.verbose_name)
    servicer = models.ForeignKey(User,verbose_name='Обслуживающий',blank=True,null=True,on_delete=models.PROTECT)

    def __str__(self):
        return self.name + ": " + self.service_type.name

    class Meta:
        verbose_name = 'Обслуживающий'
        verbose_name_plural = 'Обслуживающие'


class Schedules(models.Model):
    begin_time = models.TimeField(verbose_name='Время начало', null=False, blank=False)
    end_time = models.TimeField(verbose_name='Время конца', null=False, blank=False)
    exact_day = models.DateField(verbose_name='День', null=False, blank=False)
    client = models.ForeignKey(User, verbose_name='Клиент', blank=False, null=False, on_delete=models.PROTECT)
    service_node = models.ForeignKey(ServiceNodes, on_delete=models.PROTECT, blank=False, null=False, verbose_name=ServiceNodes._meta.verbose_name)

    def __str__(self):
        time =  self.client.name + ": " + self.service_node.name + " "+ self.begin_time+'-'+self.end_time
        return time

    class Meta:
        verbose_name = 'Время бронирования'
        verbose_name_plural = 'Времена бронирований'

class Roles(models.Model):
    name = models.CharField(verbose_name='Наименование', null=False, blank=False, max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'


class UserRoles(models.Model):
    user = models.ForeignKey(User, verbose_name=User._meta.verbose_name, null=False, blank=False, on_delete=models.PROTECT)
    role = models.ForeignKey(Roles, verbose_name=Roles._meta.verbose_name, null=False, blank=False, on_delete=models.PROTECT)

    def __str__(self):
        return self.user + " : " + self.role.name

    class Meta:
        verbose_name = 'Роли пользователя'
        verbose_name_plural = 'Роли пользователей'