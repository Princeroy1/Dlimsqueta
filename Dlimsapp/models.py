
from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
class Client(models.Model):
    def validate_image(image):
        pass
    #   file_size = image.file.size
    #   limit_kb = 150
    #   limit_mb = 8
    #   if file_size > limit_kb * 1024:
    #     raise ValidationError("Max size of file is %s KB" )
     
    id=models.AutoField(primary_key=True)
    pic = models.ImageField(upload_to='media', height_field=None, width_field=None,validators=[validate_image])
    cnic=models.CharField(max_length=13,unique=True)
    Licence_number=models.CharField(max_length=20)
    Driver_name=models.CharField(max_length=120)
    Father_name=models.CharField(max_length=120)
    Allowed_Vehcial=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    city=models.CharField(max_length=120)
    issue_date=models.DateField()
    valid_from=models.DateField()
    valid_to=models.DateField()

    