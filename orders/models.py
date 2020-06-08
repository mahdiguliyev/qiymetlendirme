from django.db import models
from evaluate.models import SubCategory,EvaluationCompany
from django.core.files.storage import FileSystemStorage
from ckeditor.fields import RichTextField

class CustomerCompany(models.Model):
    company_name            = models.CharField(max_length=255, unique =True)
    company_boss            = models.CharField(max_length=255)
    company_specialist      = models.CharField(max_length=255)
    company_created_date    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name

class Order(models.Model):
    company_name            = models.ForeignKey(CustomerCompany, on_delete=models.CASCADE, verbose_name = "Sifarişçi təşkilat",related_name="orders")
    order_name              = models.CharField(max_length=255, verbose_name="Sifarişin adı")
    subcategory_name        = models.ForeignKey(SubCategory, on_delete=models.DO_NOTHING, verbose_name = "Kateqoriya",related_name="subcategories")
    order_law_decision      = models.CharField(max_length=255, verbose_name="Rayon məhkəməsinin qərarı")
    order_deptor            = models.CharField(max_length=255, verbose_name="Borclu")
    order_claimant          = models.CharField(max_length=255, verbose_name="Tələbkar")
    order_information       = RichTextField(verbose_name="Əmlak haqqında məlumat")
    order_document          = models.FileField(verbose_name="Əmlakın texniki sənədlərini daxil edin", upload_to="order_documents/%Y/")
    order_keep_date_location= models.CharField(max_length=255, verbose_name="Saxlanma yeri və tarix")
    order_mobile            = models.CharField(max_length=13, verbose_name="Sifarişçinin mobil nömrəsi")
    price_one               = models.FloatField(verbose_name="Qiymət 1", null=True)
    eva_company_one         = models.ForeignKey(EvaluationCompany, on_delete=models.DO_NOTHING, verbose_name = "Qiymətləndirici təşkilat 1",related_name="evacompanyone", null=True)
    price_two               = models.FloatField(verbose_name="Qiymət 2", null=True)
    eva_company_two         = models.ForeignKey(EvaluationCompany, on_delete=models.DO_NOTHING, verbose_name = "Qiymətləndirici təşkilat 2",related_name="evacompanytwo", null=True)
    price_three             = models.FloatField(verbose_name="Qiymət 3", null=True)
    eva_company_three       = models.ForeignKey(EvaluationCompany, on_delete=models.DO_NOTHING, verbose_name = "Qiymətləndirici təşkilat 3",related_name="evacompanythree", null=True)
    choosen_price           = models.FloatField(verbose_name="Seçilmiş qiymət", null=True)
    is_choosed              = models.BooleanField(default=False)
    is_send                 = models.BooleanField(default=False)
    is_done                 = models.BooleanField(default=False)
    order_created_date      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_name

    class Meta:
        ordering = ['-order_created_date']

