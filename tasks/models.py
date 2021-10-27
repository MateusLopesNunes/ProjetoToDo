from django.db import models

class Task(models.Model):

    STATUS = (
        ('doing', 'Doing'),
        ('done', 'Done'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(
        max_length=5,
        choices=STATUS,
    )
    created_at = models.DateTimeField(auto_now_add=True) #sempre que adcionar vai salvar a data da modificação
    updated_at = models.DateTimeField(auto_now=True) #sempre que atualizar vai salvar a data da modificação

    def __str__(self):
        return self.title