from django.contrib import admin
from .models import Post
from .models import User
from .models import Image
from .models import Comment
from .models import Report

admin.site.register(Post)
admin.site.register(User)
admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(Report)