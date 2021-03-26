from tortoise.fields import TextField, UUIDField
from tortoise.models import Model


class Text(Model):
    id = UUIDField(pk=True)
    value = TextField()

    def __str__(self):
        return self.value
