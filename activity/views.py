from django.utils.timezone import now, timedelta
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.permissions import IsMember
from library.models import Book
from activity.models import Borrow, BORROW_DAYS_CHOICES
from activity.serializers import BorrowSerializer




# borrow view sets
class BorrowBookView(APIView):
    permission_classes = [IsMember]

    def post(self, request, pk):
        try:
            book = Book.objects.get(pk = pk)
        except Book.DoesNotExist:
            return Response({'error': 'Book not found'}, status=404)

        # Check if there are available copies of the book
        if book.quantity <= 0:
            return Response({'error': 'Book is not available'}, status=400)

        # Check if the user has already borrowed this book and has not returned it
        if Borrow.objects.filter(
            borrowed_by_user = request.user, borrowed_book = book, is_returned = False
        ).exists():
            return Response({'error': 'You have already borrowed this book and have not returned it yet'}, status=400)

        # Check if the user has reached the borrow limit
        if Borrow.objects.filter(borrowed_by_user = request.user, is_returned = False).count() >= 5:
            return Response({'error': 'Borrow limit reached'}, status=400)


        # Retrieve the `borrow_for` value from the request, defaulting to 3 days if not provided
        borrow_for_duration = int(request.data.get('borrow_for', 3))

        if borrow_for_duration not in dict(BORROW_DAYS_CHOICES).keys():
            return Response({'error': 'Invalid borrow duration'}, status=400)

        # Calculate the return deadline
        calculated_return_deadline = now().date() + timedelta(days = borrow_for_duration)

        # Create a new Borrow record
        Borrow.objects.create(
            borrowed_by_user = request.user,
            borrowed_book = book,
            borrow_for = borrow_for_duration,
            return_deadline = calculated_return_deadline,
        )


        book.quantity -= 1
        book.save()

        return Response({'success': 'Book borrowed successfully'})
    



# View to get all borrowed books for the current user
class BorrowedBooksView(APIView):
    permission_classes = [IsMember]

    def get(self, request):
        borrowed_books = Borrow.objects.filter(borrowed_by_user=request.user).select_related('borrowed_book')
        serializer = BorrowSerializer(borrowed_books, many=True)  # Serialize the borrowed books
        return Response(serializer.data)
    



# return view sets
class ReturnBookView(APIView):
    permission_classes = [IsMember]

    def post(self, request, pk):
        borrowed_book_data = Borrow.objects.filter(
            borrowed_by_user = request.user, borrowed_book__id = pk, is_returned = False
        ).first()

        if not borrowed_book_data:
            return Response({'error': 'No active borrowing found'}, status=400)

        overdue_days = (now().date() - borrowed_book_data.return_deadline).days
        fine = max(0, overdue_days * 5)  # Fine: assumed 5 BDT per day

        borrowed_book_data.is_returned = True
        borrowed_book_data.save()

        target_book = borrowed_book_data.borrowed_book
        target_book.quantity += 1

        target_book.save()

        return Response({'success': 'Book returned successfully', 'fine': fine})

