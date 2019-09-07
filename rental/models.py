from django.conf import settings
from django.db import models
import pendulum

class FriendQuerySet(models.QuerySet):
    def with_overdue(self):
        return self.annotate(
            ann_overdue=models.Case(
                models.When(
                    borrowed__when__lte=pendulum.now().subtract(months=2),
                    then=True),
                default=models.Value(False),
                output_field=models.BooleanField()
            )
        )

class OwnedModel(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE)
    
    class Meta:
        abstract = True

class Friend(OwnedModel):
    name = models.CharField(max_length=100)

    objects = FriendQuerySet.as_manager()

    def has_overdue(self):
        if hasattr(self, 'ann_overdue'): # in case we deal with annotated object
            return self.ann_overdue
        return self.borrowed_set.filter(
            returned__isnull=True, when=pendulum.now().subtract(months=2)
        ).exists()

    def __str__(self):
        return self.name

class Belonging(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Borrowed(models.Model):
    what = models.ForeignKey(Belonging, on_delete=models.CASCADE)
    to_who = models.ForeignKey(Friend, on_delete=models.CASCADE)
    when = models.DateTimeField(auto_now_add=True)
    returned = models.DateTimeField(null=True, blank=True)
    