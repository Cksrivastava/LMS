from django import forms
from .models import Book, User, BookIssue, Membership

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'serial_no']

class IssueBookForm(forms.ModelForm):
    class Meta:
        model = BookIssue
        fields = ['book', 'user', 'issue_date', 'return_date']

class ReturnBookForm(forms.ModelForm):
    class Meta:
        model = BookIssue
        fields = ['book', 'user', 'issue_date', 'return_date']

class AddMembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ['start_date', 'end_date', 'status']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']