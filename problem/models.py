from django.db import models

class Data(models.Model):
    STATUS_CHOICES = (
        ('s', 'Sample'),
        ('d', 'Test'),
        ('r', "Removed"),
    )

    input = models.TextField('Input')
    output = models.TextField('Output')
    explanation = models.TextField('Explanation')

    def __str__(self):
        return str(self.id)


class Problem(models.Model):
    STATUS_CHOICES = (
        ('r', 'Removed'),
        ('a', 'Available'),
    )

    id = models.IntegerField('#', primary_key=True)
    title = models.CharField('Title', max_length=70)
    submissions = models.IntegerField('Submissions', default=0)
    status = models.CharField('Status', max_length=1, choices=STATUS_CHOICES)
    likes = models.PositiveIntegerField('Likes', default=0)

    time_limit = models.IntegerField('Time Limit (ms)', default=1000)
    memory_limit = models.IntegerField('Memory Limit (MB)', default=512)
    program_limit = models.IntegerField('Program Limit (KB)', default=128)
    description = models.TextField('Description')
    input = models.TextField('Input')
    output = models.TextField('Output')
    samples = models.ManyToManyField(Data, 'Samples')

    def __str__(self):
        return str(self.id) + ' - ' + self.title

    class Meta:
        ordering = ['-id']

# TODO: There is a redirect issue when saving Data through Problem