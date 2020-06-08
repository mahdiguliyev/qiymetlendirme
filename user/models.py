from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, fin, username, sirname, email, is_active=True, is_company_user=False, is_customer_user=False, is_admin=False, is_staff=False, is_icra_company=False, is_e_mahkama=False, password=None):
        if not fin:
            raise ValueError("İstifadəçi FİN kodunu daxil etməlidir!")
        if not password:
            raise ValueError("İstifadəçi parolunu daxil etməlidir!")
        if not username:
            raise ValueError("İstifadəçi adını daxil etməlidir!")
        if not sirname:
            raise ValueError("İstifadəçi familiyasını daxil etməlidir!")
        if not email:
            raise ValueError("İstifadəçi email adresini daxil etməlidir!")
        user_obj = self.model(
            fin = fin
        )
        user_obj.set_password(password)
        user_obj.username = username
        user_obj.sirname = sirname
        user_obj.email = email
        user_obj.active = is_active
        user_obj.company_user = is_company_user
        user_obj.customer_user = is_customer_user
        user_obj.admin = is_admin
        user_obj.staff = is_staff
        user_obj.icra_company = is_icra_company
        user_obj.e_mahkama = is_e_mahkama
        user_obj.save(using=self._db)
        return user_obj
    
    def create_company_user(self, fin, username, sirname, email, password=None):
        user = self.create_user(
            fin,
            username,
            sirname,
            email,
            password=password,
            is_company_user=True
        )
        return user
    
    def create_customer_user(self, fin, username, sirname, email, password=None):
        user = self.create_user(
            fin,
            username,
            sirname,
            email,
            password=password,
            is_customer_user=True
        )
        return user
    
    def create_superuser(self, fin, username, sirname, email, password=None):
        user = self.create_user(
            fin,
            username,
            sirname,
            email,
            password=password,
            is_company_user=True,
            is_customer_user=True,
            is_admin=True,
            is_staff=True,
            is_icra_company=True,
            is_e_mahkama=True
        )
        return user

class User(AbstractBaseUser):
    fin           = models.CharField(max_length = 7, unique = True)
    username      = models.CharField(max_length=55)
    sirname       = models.CharField(max_length=55)
    email         = models.EmailField(max_length=255, unique = True)
    active        = models.BooleanField(default=True) # can login
    company_user  = models.BooleanField(default=False)
    customer_user = models.BooleanField(default=False)
    admin         = models.BooleanField(default=False)
    staff         = models.BooleanField(default=False)
    icra_company  = models.BooleanField(default=False)
    e_mahkama     = models.BooleanField(default=False)
    timestamp     = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'fin'
    REQUIRED_FIELDS = ['username','sirname','email']

    objects = UserManager()

    def __str__(self):
        return self.fin
    
    def get_full_name(self):
        return self.username + " " + self.sirname

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label): 
        return True
    @property
    def is_company_user(self):
        return self.company_user

    @property
    def is_customer_user(self):
        return self.customer_user
    
    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_icra_company(self):
        return self.icra_company
    
    @property
    def is_e_mahkama(self):
        return self.e_mahkama

