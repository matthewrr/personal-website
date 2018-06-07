{"filter":false,"title":"models.py","tooltip":"/blog/models.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":18,"column":25},"action":"insert","lines":["from django.db import models","from django.utils import timezone","","","class Post(models.Model):","    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)","    title = models.CharField(max_length=200)","    text = models.TextField()","    created_date = models.DateTimeField(","            default=timezone.now)","    published_date = models.DateTimeField(","            blank=True, null=True)","","    def publish(self):","        self.published_date = timezone.now()","        self.save()","","    def __str__(self):","        return self.title"],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":18,"column":25},"end":{"row":18,"column":25},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1528392911913,"hash":"fbdba2bb1ae2459e55ed4a0023770228d8ab4561"}