from django.db.models import *

from accounts.models import Profile


class MembersGroup(Model):
    person = ForeignKey(Profile, on_delete=CASCADE)
    member = CharField(max_length=50, default="My duty",
                       null=False, blank=False, unique=True)

    def __str__(self):
        return self.member


class Task(Model):
    member = ForeignKey(MembersGroup, to_field='member', on_delete=CASCADE)
    title = CharField(max_length=250, null=False, blank=False)
    date = DateField(null=True, blank=True)
    time = DateField(null=True, blank=True)
    complete = BooleanField(default=False)
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class TaskBody(Model):
    task = OneToOneField(Task, on_delete=CASCADE)
    body = TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.body
