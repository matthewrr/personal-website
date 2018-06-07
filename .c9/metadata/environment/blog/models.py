{"filter":false,"title":"models.py","tooltip":"/blog/models.py","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["from django.db import models","","# Create your models here.",""],"id":2},{"start":{"row":0,"column":0},"end":{"row":18,"column":25},"action":"insert","lines":["from django.db import models","from django.utils import timezone","","","class Post(models.Model):","    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)","    title = models.CharField(max_length=200)","    text = models.TextField()","    created_date = models.DateTimeField(","            default=timezone.now)","    published_date = models.DateTimeField(","            blank=True, null=True)","","    def publish(self):","        self.published_date = timezone.now()","        self.save()","","    def __str__(self):","        return self.title"]}],[{"start":{"row":1,"column":33},"end":{"row":2,"column":0},"action":"remove","lines":["",""],"id":3}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":1,"column":33},"end":{"row":1,"column":33},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1528395824512,"hash":"2f329f9793da9a9358022876c4e00b3068b0acd7"}