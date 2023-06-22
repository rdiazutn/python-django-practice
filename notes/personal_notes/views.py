from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from .models import PersonalNote
from .serializers import PersonalNoteSerializer


# Create your views here.
class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.none()
    
    def get_queryset(self):
        user = self.request.user
        
        if user.is_anonymous:
            return PersonalNote.objects.none()
        else:
            print(user)
            return PersonalNote.objects.filter(user=user)
    
    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(user=self.request.user)
    
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
    
    def perform_destroy(self, instance):
        if instance.user == self.request.user:
            instance.delete()
        else:
            raise PermissionDenied("You can not delete this note.")