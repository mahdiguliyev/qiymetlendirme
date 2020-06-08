from django.contrib import admin
from .models import EvaluationCompany,Worker,EvaluationOrder,Category,SubCategory,Apartment,PrivateHouse,EnterpriseComplex,NonResidentialBuilding,NonResidentialArea,LandPlot,OtherRealState


admin.site.register(EvaluationCompany)
admin.site.register(Worker)
admin.site.register(EvaluationOrder)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Apartment)
admin.site.register(PrivateHouse)
admin.site.register(EnterpriseComplex)
admin.site.register(NonResidentialBuilding)
admin.site.register(NonResidentialArea)
admin.site.register(LandPlot)
admin.site.register(OtherRealState)
