from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    job_title_animated_text = models.TextField(default="Vision Engineer, From Lahore Pakistan")
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=25, blank=True)
    post = models.CharField(max_length=100)  
    location = models.CharField(max_length=100)  
    linkedin = models.URLField(max_length=100)
    github = models.URLField(max_length=100)
    facebook = models.URLField(max_length=100)
    instagram = models.URLField(max_length=100)
    bg_video = models.FileField(upload_to='videos/', null=True, verbose_name="")

    class Meta:
        verbose_name_plural = "Person"

    def save(self, *args, **kwargs):
        if not self.pk and Person.objects.exists():
            return
        super(Person, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Skills(models.Model):
    title = models.CharField(max_length=100)
    percentage = models.IntegerField()
    icon = models.ImageField(upload_to='icons/', null=True, verbose_name="")

    class Meta:
        verbose_name_plural = "Skills"

    def __str__(self):
        return self.title
    
class About(models.Model):
    title = models.CharField(max_length=100)
    description_1 = models.TextField()
    description_2 = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', null=True, verbose_name="")

    class Meta:
        verbose_name_plural = "About"

    def save(self, *args, **kwargs):
        if not self.pk and About.objects.exists():
            return
        super(About, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
# Capabilities 2 of 1 
class Capabilities_Headings(models.Model):
    main_title = models.CharField(max_length=200,blank=True)
    sub_title = models.CharField(max_length=250,blank=True)

    class Meta:
        verbose_name_plural = "Capabilities Headings"
    
    def save(self, *args, **kwargs):
        if not self.pk and Capabilities_Headings.objects.exists():
            return
        super(Capabilities_Headings, self).save(*args, **kwargs)

    def __str__(self):
        return self.main_title
    
# Capabilities 2 of 2 
class Capabilities(models.Model):
    hedings = models.ForeignKey(Capabilities_Headings, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='capabilities_icons/', null=True, verbose_name="")

    class Meta:
        verbose_name_plural = "Capabilities"

    def __str__(self):
        return self.title

# Education 2 of 1  
class Education_Headings(models.Model):
    main_title = models.CharField(max_length=200,blank=True)
    sub_title = models.CharField(max_length=250,blank=True)

    class Meta:
        verbose_name_plural = "Education Headings"
    
    def save(self, *args, **kwargs):
        if not self.pk and Education_Headings.objects.exists():
            return
        super(Education_Headings, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.main_title
    
# Education 2 of 2
class Education(models.Model):
    headings = models.ForeignKey(Education_Headings, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    institute = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    start_year = models.IntegerField()  
    end_year = models.IntegerField() 

    class Meta:
        verbose_name_plural = "Education"

    def __str__(self):
        return self.title

# Exprience 1 of 1
class Experience(models.Model):
    headings = models.ForeignKey(Education_Headings, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    institute = models.CharField(max_length=255, blank=True)
    intro_description = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    start_year = models.IntegerField()  
    end_year = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Experience"
    
    def __str__(self):
        return self.title
    
# Projects 1 of 1
class Projects_Headings(models.Model):
    main_title = models.CharField(max_length=200,blank=True)
    sub_title = models.CharField(max_length=250,blank=True)

    class Meta:
        verbose_name_plural = "Projects Headings"
    
    def save(self, *args, **kwargs):
        if not self.pk and Projects_Headings.objects.exists():
            return
        super(Projects_Headings, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.main_title

class Projects(models.Model):
    category_options = [('Programming Task', 'Programming Task'), ('Graphics Task', 'Graphics Task'), ('Other', 'Other')]
    category = models.CharField(max_length=40, choices=category_options)
    thumbnail = models.ImageField(upload_to='project_thumbnails/', null=True, verbose_name="")
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title

class Project_Media(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='media_project')
    media = models.FileField(upload_to='project_media/', null=True, verbose_name="")
    pic_description = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name_plural = "Project Media"

    def __str__(self):
        return f"{self.media} for {self.project}"

class Certificates_Headings(models.Model):
    main_title = models.CharField(max_length=200,blank=True)
    sub_title = models.CharField(max_length=250,blank=True)

    class Meta:
        verbose_name_plural = "Certificates Headings"
    
    def save(self, *args, **kwargs):
        if not self.pk and Certificates_Headings.objects.exists():
            return
        super(Certificates_Headings, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.main_title
    
class Certificates(models.Model):
    headings = models.ForeignKey(Certificates_Headings, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    modal_caption = models.CharField(max_length=255, blank=True)
    verify = models.URLField(max_length=200)
    certificate = models.FileField(upload_to='certificates/', null=True, verbose_name="")

    class Meta:
        verbose_name_plural = "Certificates"

    def __str__(self):
        return self.title
    
class Hire_Button_Picture(models.Model):
    text = models.CharField(max_length=200)
    button_text = models.CharField(max_length=50)
    image = models.ImageField(upload_to='hire_button/', null=True, verbose_name="")

    class Meta:
        verbose_name_plural = "Hire Button Picture"

    def save(self, *args, **kwargs):
        if not self.pk and Hire_Button_Picture.objects.exists():
            return
        super(Hire_Button_Picture, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.image} for {self.text}"
    
class Contct_heading_Info(models.Model):
    main_title = models.CharField(max_length=200,blank=True)
    sub_title = models.CharField(max_length=250,blank=True)

    class Meta:
        verbose_name_plural = "Contact Headings"
    
    def save(self, *args, **kwargs):
        if not self.pk and Contct_heading_Info.objects.exists():
            return
        super(Contct_heading_Info, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.main_title
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Contact"

    def __str__(self):
        return self.name
    
class Blog_Heading_Info(models.Model):
    main_heading = models.CharField(max_length=200)
    sub_title = models.TextField()
    thumbnail = models.ImageField(upload_to='blog_thumbnails/', null=True, verbose_name="")

    def save(self, *args, **kwargs):
        if not self.pk and Blog_Heading_Info.objects.exists():
            return
        super(Blog_Heading_Info, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Blog Heading Info"

    def __str__(self):
        return self.main_heading
    
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=100,default="Ahmad Bilal Bhatti")
    platform = models.CharField(max_length=100,default="Medium")
    url = models.URLField(max_length=250)
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Blogs"

    def __str__(self):
        return self.title