from django.urls import path
from . import views
app_name = "evaluate"

urlpatterns = [
    path('branchmanager/', views.branchmanagerPage, name="branchmanagerpage"),
    path('appraisalspecialist/', views.appraisalspecialistPage, name="appraisalspecialistpage"),
    path("vieworderdetail/<int:id>", views.vieworderDetail, name="vieworderdetail"),
    path("getpdf/<int:id>", views.getPdf, name="getpdf"),
    path("evaluateform/<int:id>", views.evaluateForm, name="evaluateform"),
]