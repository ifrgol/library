from django.db import models
from authors.models import Author
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Book(models.Model):
    name = models.CharField(max_length=100)
    author_name = models.ForeignKey(Author, to_field="name", on_delete=models.CASCADE, null=True)
    pages = models.IntegerField()
    publication_date = models.DateField()
    genre = models.CharField(max_length=200, default="none")
    owner = models.ForeignKey('auth.User', related_name='books', on_delete=models.CASCADE, default='')
    # highlight = models.TextField(default='')


def save(self, *args, **kwargs):
    """
    Use the `pygments` library to create a highlighted HTML representation of the code snippet.
    """
    lexer = get_lexer_by_name(self.language)
    linenos = 'table' if self.linenos else False
    options = {'title': self.title} if self.title else {}
    formatter = HtmlFormatter(style=self.style, linenos=linenos,
                              full=True, **options)
    self.highlighted = highlight(self.code, lexer, formatter)
    super().save(*args, **kwargs)

