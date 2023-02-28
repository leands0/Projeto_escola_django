from rest_framework import viewsets
from escola.models import Aluno, Professor
from escola.serializer import AlunoSerializer, ProfessorSerializer

class AlunosViewSet(viewsets.ModelViewSet): 
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class ProfessoresViewSet(viewsets.ModelViewSet): 
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer