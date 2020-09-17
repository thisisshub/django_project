import django_filters
from .models import Notes_Model, Syllabus_Model

class NotesFilter(django_filters.FilterSet):
    """Filter notes."""

    class Meta:
        """Filter branch choice and semester to find notes."""
        
        model = Notes_Model
        fields = ['branch_choice', 'file_semester']

class SyllabusFilter(django_filters.FilterSet):
    """Filter syllabus."""
    
    class Meta:

        model = Syllabus_Model
        filter_fields = ()
        fields = ['branch_choice', 'file_semester']