from django.db import models
from django.core.mail import send_mail
from lastwill.settings import DEFAULT_FROM_EMAIL, DEFAULT_TO_EMAIL

class Sentence(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    contract_name = models.CharField(max_length=200)
    message = models.TextField()

    def save(self, *args, **kwargs):
        new_obj = not self.id
        super().save(*args, **kwargs)
        if new_obj:
            send_mail(
                '{} {} {}'.format(self.contract_name, self.username, self.email),
                self.message,
                DEFAULT_FROM_EMAIL,
                [DEFAULT_TO_EMAIL],
                fail_silently=True,
            )

