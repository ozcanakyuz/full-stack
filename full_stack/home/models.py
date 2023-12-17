from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ModelForm 
from django.utils.safestring import mark_safe


class Setting(models.Model):
    STATUS = (('True', 'True'),('False', 'False'),)
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    address = models.CharField(blank=True, max_length=100)
    phone = models.CharField(blank=True, max_length=15)
    fax = models.CharField(blank=True, max_length=15)
    email = models.CharField(blank=True, max_length=50)
    smtpserver = models.CharField(blank=True, max_length=50)
    smtpemail = models.CharField(blank=True, max_length=50)
    smtppassword = models.CharField(blank=True, max_length=10)
    smtpport = models.CharField(blank=True, max_length=5)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(blank=True, max_length=50)
    instagram = models.CharField(blank=True, max_length=50)
    twitter = models.CharField(blank=True, max_length=50)
    youtube = models.CharField(blank=True, max_length=50)
    aboutus = RichTextUploadingField()  #! models.TextField()
    contact = RichTextUploadingField() #! RichTextUploadingField()
    references = RichTextUploadingField()
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

#! ------------------- USER FORM ---------------------
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=50)
    image = models.ImageField(blank=True, upload_to='images/users/')
    def __str__(self):
        return self.user.username
    def user_name(self):
        return self.user.first_name + ' ' + self.user.last_name + ' [' + self.user.username + '] '

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'address', 'city', 'country', 'image']

#! POST FORM 
class Post(models.Model):
    STATUS = (('New', 'New'),('True', 'True'),('False', 'False'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=5, choices=STATUS, default='New')
    # status = models.BooleanField(choices=STATUS, default=False)
    image = models.ImageField(upload_to='images/')
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title
    
    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" width="50" height="50" />' % self.image.url)
        return None
    image_tag.short_description = 'Image Preview'

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
        #! image = forms.ImageField(required=True, validators=[validate_image_file_extension])

class Images(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title
    
    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" width="50" height="50" />' % self.image.url)
        return None
    image_tag.short_description = 'Image Preview'



class Comment(models.Model):
    STATUS = (('New', 'New'),('True', 'True'),('False', 'False'))
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=250,blank=False)
    ip = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=5, choices=STATUS, default='New')
   # status = models.BooleanField(choices=STATUS, default=False)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment

class ReplyComment(models.Model):
    STATUS = (('New', 'New'),('True', 'True'),('False', 'False'))
    comment=models.ForeignKey(Comment,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    repcomment = models.CharField(max_length=250,blank=False)
    ip = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=5, choices=STATUS, default='New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.repcomment

class ReplyCommentForm(ModelForm):
    class Meta:
        model = ReplyComment
        fields = ['repcomment']