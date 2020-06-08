from django.db import models
from user.models import User
from ckeditor.fields import RichTextField
from django.core.validators import MinLengthValidator

class Category(models.Model):
    category_name             = models.CharField(max_length=255, unique =True)

    def __str__(self):
        return self.category_name

class SubCategory(models.Model):
    category_name  =     models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name = "Kateqoriya",related_name="categories")
    subcategory_name =   models.CharField(max_length=255, unique =True)

    def __str__(self):
        return self.subcategory_name

class EvaluationCompany(models.Model):
    evacompany_name         = models.CharField(max_length=255, unique =True)
    
    def __str__(self):
        return self.evacompany_name

class Worker(models.Model):
    company_name        = models.ForeignKey(EvaluationCompany, on_delete=models.CASCADE, verbose_name = "Qiymətləndirici təşkilat",related_name="workers")
    user                = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = "İstifadəçi",related_name="users",null=True)
    worker_name         = models.CharField(max_length=55,verbose_name="Adı")
    worker_sirname      = models.CharField(max_length=55,verbose_name="Familiya")
    worker_fin          = models.CharField(max_length=7,validators=[MinLengthValidator(7)],verbose_name="Fin")
    is_bm               = models.BooleanField(default=False)
    is_as               = models.BooleanField(default=False)
    worker_created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.worker_fin

class EvaluationOrder(models.Model):
    company_name            = models.ManyToManyField(EvaluationCompany, verbose_name = "Qiymətləndirici təşkilat",related_name="orders")
    order_name              = models.CharField(max_length=255, verbose_name="Sifarişin adı")
    subcategory_name        = models.ForeignKey(SubCategory, on_delete=models.DO_NOTHING, verbose_name = "Kateqoriya",related_name="subcategories_evaluationorder")
    order_law_decision      = models.CharField(max_length=255, verbose_name="Rayon məhkəməsinin qərarı")
    order_deptor            = models.CharField(max_length=255, verbose_name="Borclu")
    order_claimant          = models.CharField(max_length=255, verbose_name="Tələbkar")
    order_information       = RichTextField(verbose_name="Əmlak haqqında məlumat")
    order_document          = models.FileField(verbose_name="Əmlakın texniki sənədlərini daxil edin", upload_to="order_documents/%Y/")
    order_keep_date_location= models.CharField(max_length=255, verbose_name="Saxlanma yeri və tarix")
    order_mobile            = models.CharField(max_length=13, verbose_name="Sifarişçinin mobil nömrəsi")
    is_done                 = models.BooleanField(default=False)
    order_created_date      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_name

class Apartment(models.Model):
    subcategory_name =              models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name = "Alt Kateqoriya",related_name="subcategories_apartment")
    order_number =                  models.CharField(max_length=255, verbose_name="Sifariş nömrəsi")
    building_floor =                models.IntegerField(verbose_name="Binanın mərtəbəliliyi")
    located_floor =                 models.IntegerField(verbose_name="Yerləşdiyi mərtəbə")
    room_number =                   models.IntegerField(verbose_name="Otaqların sayı")
    total_area =                    models.CharField(max_length=50, verbose_name="Ümumi sahəsi")
    residential_area =              models.CharField(max_length=50, verbose_name="Yaşayış sahəsi")
    auxiliary_area =                models.CharField(max_length=50, verbose_name="Köməkçi sahə")
    balcony =                       models.BooleanField(verbose_name="Eyvan")
    sunitary_junction =             models.BooleanField(verbose_name="Sanitar qovşağı")
    height =                        models.CharField(max_length=50, verbose_name="Hündürlüyü")
    project =                       models.CharField(max_length=255, verbose_name="Layihə")
    blocks_number =                 models.IntegerField(verbose_name="Blokların sayı")
    interior_exterior_walls =       models.CharField(max_length=255, verbose_name="Daxili və xarici divarları")
    floor =                         models.CharField(max_length=255, verbose_name="Döşəməsi")
    ceiling =                       models.CharField(max_length=255, verbose_name="Tavan")
    window =                        models.CharField(max_length=255, verbose_name="Pəncərə")
    interior_door =                 models.CharField(max_length=255, verbose_name="Daxili qapı")
    interior_decoration =           models.CharField(max_length=255, verbose_name="Daxili bəzək işləri")
    entry_door =                    models.CharField(max_length=255, verbose_name="Giriş qapısı")
    sanitary_equioment =            models.CharField(max_length=255, verbose_name="Sanitar texniki təchizat (o cümlədən su, qaz, elektrik)")
    general_condition =             models.CharField(max_length=255, verbose_name="Ümumi vəziyyəti")
    price =                         models.FloatField(verbose_name="Qiymət")
    created_date =                  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_number

class PrivateHouse(models.Model):
    subcategory_name =              models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name = "Alt Kateqoriya",related_name="subcategories_privatehouse")
    order_number =                  models.CharField(max_length=255, verbose_name="Sifariş nömrəsi")
    building_floor =                models.IntegerField(verbose_name="Fərdi-yaşayış evinin mərtəbəliliyi")
    room_number =                   models.IntegerField(verbose_name="Otaqların sayı")
    total_area =                    models.CharField(max_length=50, verbose_name="Ümumi sahəsi")
    residential_area =              models.CharField(max_length=50, verbose_name="Yaşayış sahəsi")
    auxiliary_area =                models.CharField(max_length=50, verbose_name="Köməkçi sahə")
    land_area =                     models.CharField(max_length=255, verbose_name="Torpaq sahəsi")
    interior_exterior_walls =       models.CharField(max_length=255, verbose_name="Daxili və xarici divarları")
    floor =                         models.CharField(max_length=255, verbose_name="Döşəməsi")
    ceiling =                       models.CharField(max_length=255, verbose_name="Tavan")
    window =                        models.CharField(max_length=255, verbose_name="Pəncərə")
    interior_door =                 models.CharField(max_length=255, verbose_name="Daxili qapı")
    interior_decoration =           models.CharField(max_length=255, verbose_name="Daxili bəzək işləri")
    entry_door =                    models.CharField(max_length=255, verbose_name="Giriş qapısı")
    sanitary_equioment =            models.CharField(max_length=255, verbose_name="Sanitar texniki təchizat (o cümlədən su, qaz, elektrik)")
    roof =                          models.CharField(max_length=255, verbose_name="Dam örtüyü")
    general_condition =             models.CharField(max_length=255, verbose_name="Ümumi vəziyyəti")
    price =                         models.FloatField(verbose_name="Qiymət")
    created_date =                  models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.order_number

class EnterpriseComplex(models.Model):
    subcategory_name =              models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name = "Alt Kateqoriya",related_name="subcategories_enterprisecomplex")
    order_number =                  models.CharField(max_length=255, verbose_name="Sifariş nömrəsi")
    building_floor =                models.IntegerField(verbose_name="Mərtəbəliliyi")
    room_number =                   models.IntegerField(verbose_name="Otaqların sayı")
    total_area =                    models.CharField(max_length=50, verbose_name="Ümumi sahəsi")
    residential_area =              models.CharField(max_length=50, verbose_name="Yaşayış sahəsi")
    auxiliary_area =                models.CharField(max_length=50, verbose_name="Köməkçi sahə")
    interior_exterior_walls =       models.CharField(max_length=255, verbose_name="Daxili və xarici divarları")
    floor =                         models.CharField(max_length=255, verbose_name="Döşəməsi")
    ceiling =                       models.CharField(max_length=255, verbose_name="Tavan")
    window =                        models.CharField(max_length=255, verbose_name="Pəncərə")
    interior_door =                 models.CharField(max_length=255, verbose_name="Daxili qapı")
    interior_decoration =           models.CharField(max_length=255, verbose_name="Daxili bəzək işləri")
    entry_door =                    models.CharField(max_length=255, verbose_name="Giriş qapısı")
    sanitary_equioment =            models.CharField(max_length=255, verbose_name="Sanitar texniki təchizat (o cümlədən su, qaz, elektrik)")
    roof =                          models.CharField(max_length=255, verbose_name="Dam örtüyü")
    general_condition =             models.CharField(max_length=255, verbose_name="Ümumi vəziyyəti")
    price =                         models.FloatField(verbose_name="Qiymət")
    created_date =                  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_number

class NonResidentialBuilding(models.Model):
    subcategory_name =              models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name = "Alt Kateqoriya",related_name="subcategories_nonresidentialbuilding")
    order_number =                  models.CharField(max_length=255, verbose_name="Sifariş nömrəsi")
    building_floor =                models.IntegerField(verbose_name="Mərtəbəliliyi")
    total_area =                    models.CharField(max_length=50, verbose_name="Ümumi sahəsi")
    residential_area =              models.CharField(max_length=50, verbose_name="Yaşayış sahəsi")
    auxiliary_area =                models.CharField(max_length=50, verbose_name="Köməkçi sahə")
    land_area =                     models.CharField(max_length=255, verbose_name="Torpaq sahəsi")
    interior_exterior_walls =       models.CharField(max_length=255, verbose_name="Daxili və xarici divarları")
    floor =                         models.CharField(max_length=255, verbose_name="Döşəməsi")
    ceiling =                       models.CharField(max_length=255, verbose_name="Tavan")
    window =                        models.CharField(max_length=255, verbose_name="Pəncərə")
    interior_door =                 models.CharField(max_length=255, verbose_name="Daxili qapı")
    interior_decoration =           models.CharField(max_length=255, verbose_name="Daxili bəzək işləri")
    entry_door =                    models.CharField(max_length=255, verbose_name="Giriş qapısı")
    sanitary_equioment =            models.CharField(max_length=255, verbose_name="Sanitar texniki təchizat (o cümlədən su, qaz, elektrik)")
    general_condition =             models.CharField(max_length=255, verbose_name="Ümumi vəziyyəti")
    price =                         models.FloatField(verbose_name="Qiymət")
    created_date =                  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_number

class NonResidentialArea(models.Model):
    subcategory_name =              models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name = "Alt Kateqoriya",related_name="subcategories_nonresidentialarea")
    order_number =                  models.CharField(max_length=255, verbose_name="Sifariş nömrəsi")
    building_floor =                models.IntegerField(verbose_name="Mərtəbəliliyi")
    room_number =                   models.IntegerField(verbose_name="Otaqların sayı")
    total_area =                    models.CharField(max_length=50, verbose_name="Ümumi sahəsi")
    residential_area =              models.CharField(max_length=50, verbose_name="Yaşayış sahəsi")
    auxiliary_area =                models.CharField(max_length=50, verbose_name="Köməkçi sahə")
    interior_exterior_walls =       models.CharField(max_length=255, verbose_name="Daxili və xarici divarları")
    floor =                         models.CharField(max_length=255, verbose_name="Döşəməsi")
    ceiling =                       models.CharField(max_length=255, verbose_name="Tavan")
    window =                        models.CharField(max_length=255, verbose_name="Pəncərə")
    interior_door =                 models.CharField(max_length=255, verbose_name="Daxili qapı")
    interior_decoration =           models.CharField(max_length=255, verbose_name="Daxili bəzək işləri")
    entry_door =                    models.CharField(max_length=255, verbose_name="Giriş qapısı")
    sanitary_equioment =            models.CharField(max_length=255, verbose_name="Sanitar texniki təchizat (o cümlədən su, qaz, elektrik)")
    roof =                          models.CharField(max_length=255, verbose_name="Dam örtüyü")
    general_condition =             models.CharField(max_length=255, verbose_name="Ümumi vəziyyəti")
    price =                         models.FloatField(verbose_name="Qiymət")
    created_date =                  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_number

class LandPlot(models.Model):
    subcategory_name =              models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name = "Alt Kateqoriya",related_name="subcategories_landplot")
    order_number =                  models.CharField(max_length=255, verbose_name="Sifariş nömrəsi")
    located_area =                  models.CharField(max_length=255, verbose_name="Yerləşdiyi ərazi")
    land_area =                     models.CharField(max_length=255, verbose_name="Torpaq sahəsi")
    land_purpose =                  models.CharField(max_length=255, verbose_name="Torpağın təyinatı")
    price =                         models.FloatField(verbose_name="Qiymət")
    created_date =                  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_number

class OtherRealState(models.Model):
    subcategory_name =              models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name = "Alt Kateqoriya",related_name="subcategories_otherrealestate")
    order_number =                  models.CharField(max_length=255, verbose_name="Sifariş nömrəsi")
    technical_indicators =          RichTextField(verbose_name="Texniki göstəriciləri")
    technical_characteristics =     RichTextField(verbose_name="Texniki xarakterizələri")
    price =                         models.FloatField(verbose_name="Qiymət")
    created_date =                  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_number

