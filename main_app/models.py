from django.db import models
from django.utils.text import slugify
from datetime import date


class Church(models.Model):
    church_name = models.CharField(max_length=50)

    def __str__(self):
        return self.church_name

    class Meta:
        verbose_name_plural = "Churches"


class Ministers(models.Model):
    minister_name = models.CharField(max_length=50)

    def __str__(self):
        return self.minister_name

    class Meta:
        verbose_name_plural = "Ministers"

# class Role(models.Model):
#     church_role = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.church_role
#
#     class Meta:
#         verbose_name_plural = "Roles"


class Proofs(models.Model):
    proof = models.CharField(max_length=20)

    def __str__(self):
        return self.proof

    class Meta:
        verbose_name_plural = "Proofs"


class qualifyingConnections(models.Model):
    qualifying_connection = models.CharField(max_length=150)

    def __str__(self):
        return self.qualifying_connection


class Person(models.Model):
    wedding_id = models.IntegerField(blank=True)
    ROLE_CHOICES = (
        ('Groom', 'Groom'),
        ('Bride', 'Bride'),
    )
    role = models.CharField(max_length=6, choices=ROLE_CHOICES, blank=True)
    title = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, blank=True)
    phone = models.CharField(max_length=11, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    dob = models.DateField(blank=True)
    age_at_wedding = models.IntegerField(blank=True)
    proof = models.ForeignKey(Proofs, on_delete=models.CASCADE, related_name='proofOfId', blank=True)
    occupation = models.CharField(max_length=50, blank=True)
    STATUS_CHOICES = (
        ('Single', 'Sinlge'),
        ('PMD', 'Previous Marriage Dissolved'),
        ('Widowed', 'Widowed'),
        ('CPD', 'Civil Partnership Dissolved'),
    )
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, blank=True)
    nationality = models.CharField(max_length=20, blank=True)
    church = models.ForeignKey(Church, on_delete=models.CASCADE, related_name='church', blank=True)
    qualifying_connection = models.ForeignKey(qualifyingConnections, on_delete=models.CASCADE, related_name='qualConnect', blank=True)
    details = models.CharField(max_length=200,  blank=True)
    connected_by_marriage = models.BooleanField(default=False,  blank=True)
    if_yes_how = models.CharField(max_length=200, blank=True)
    father_name = models.CharField(max_length=50, blank=True)
    father_occupation = models.CharField(max_length=50, blank=True)
    # role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='role', default=1, blank=True)

    class Meta:
        verbose_name_plural = "People"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.first_name + ' ' + self.last_name)

        today = date.today()
        born = self.dob
        self.age_at_wedding = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        super(Person, self).save(*args, **kwargs)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


