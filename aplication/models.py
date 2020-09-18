from django.db import models

class Usuario(models.Model):
    email = models.EmailField(max_length=15)
    senha = models.Charfiel(max_length=255)
    dt_nascimento = models.DateField()

class Perfil(models.Model):
    nome = models.CharFIeld(max_length=30)
    usuario = models.(on_delete=models.CASCADE)
    contados = models.ForeingKey("self")

    def get_timeline(self):
        return Postagem.objects.filter(perfil=self)

class Postagem(models.Model):
    texto = models.TextField()
    data = models.DateField()
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)

class Comentario(models.Model):
    texto = models.TextField()
    data = models.DateField(auto_now_add=True)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)

class Reacao(models.Model):
    TIPO_REACAO = [
        ('Curti', 'Curti'),
        ('Amei', 'Amaei'),
        ('Kkk', 'Kkk'),
        ('Uau', 'Uau'),
        ('Triste', 'Triste'),
        ('Raiva', 'Raiva'),
    ]

    tipo = models.CharField(choices=TIPO_REACAO,default=TIPO_REACAO[0][1],max_length=15)
    data = models.DateField()
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE, related_name='reacoes')
    profile = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='reacoes')
    peso = models.IntegerField(default=1)

