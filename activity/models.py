from django.db import models
from accounts.models import CustomUser
from library.models import Book


BORROW_DAYS_CHOICES = [
        (1, '1 days'),
        (3, '3 days'),
        (5, '5 days'),
        (7, '7 days'),
        (10, '10 days'),
        (15, '15 days'),
        (30, '30 days'),
    ]



# Create your models here.
class Borrow(models.Model):
    borrowed_by_user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    borrowed_book = models.ForeignKey(Book, on_delete = models.CASCADE)

    borrowed_date = models.DateField(auto_now_add = True)
    borrow_for = models.PositiveSmallIntegerField(choices = BORROW_DAYS_CHOICES, default = 3)
    return_deadline = models.DateField()

    is_returned = models.BooleanField(default = False)

    fine = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)  # Fine field


    def __str__(self):
        return f"{self.borrowed_by_user.username} borrowed {self.borrowed_book.title}"

