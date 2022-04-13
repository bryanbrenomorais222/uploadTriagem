from django.contrib import admin

# Our created models
from .models import Allergy
from .models import AllergyGroup
from .models import AllergyReaction
from .models import AllergyReactionGroup
from .models import AppointmentDoctor
from .models import AppointmentNurse
from .models import BloodPressureRange
from .models import Comorbidity
from .models import ComorbidityGroup
from .models import Doctor
from .models import HeartRate
from .models import HomeUseMedication
from .models import HomeUseMedicationGroup
from .models import ImcClassification
from .models import MotorResponseLevel
from .models import Nurse
from .models import OcularOpeningLevel
from .models import OtherAssociatedFactor
from .models import OximetryRange
from .models import PainClassification
from .models import Period
from .models import PeripheralCapillaryBloodGlucose
from .models import Patient
from .models import PreviousSurgery
from .models import PreviousSurgeryGroup
from .models import PupilEvaluationLevel
from .models import RespiratoryFrequency
from .models import ScreeningFlowchart
from .models import ScreeningProtocol
from .models import Symptom
from .models import SymptomGroup
from .models import TemperatureRange
from .models import VerbalResponseLevel
from .models import vaccineRegistration
from .models import vaccination


# Registering the models with the admin module
admin.site.register(Allergy)
admin.site.register(AllergyGroup)
admin.site.register(AllergyReaction)
admin.site.register(AllergyReactionGroup)
admin.site.register(AppointmentDoctor)
admin.site.register(AppointmentNurse)
admin.site.register(BloodPressureRange)
admin.site.register(Comorbidity)
admin.site.register(ComorbidityGroup)
admin.site.register(Doctor)
admin.site.register(HeartRate)
admin.site.register(HomeUseMedication)
admin.site.register(HomeUseMedicationGroup)
admin.site.register(ImcClassification)
admin.site.register(MotorResponseLevel)
admin.site.register(Nurse)
admin.site.register(OcularOpeningLevel)
admin.site.register(OtherAssociatedFactor)
admin.site.register(OximetryRange)
admin.site.register(PainClassification)
admin.site.register(Period)
admin.site.register(PeripheralCapillaryBloodGlucose)
admin.site.register(Patient)
admin.site.register(PreviousSurgery)
admin.site.register(PreviousSurgeryGroup)
admin.site.register(PupilEvaluationLevel)
admin.site.register(RespiratoryFrequency)
admin.site.register(ScreeningFlowchart)
admin.site.register(ScreeningProtocol)
admin.site.register(Symptom)
admin.site.register(SymptomGroup)
admin.site.register(TemperatureRange)
admin.site.register(VerbalResponseLevel)
admin.site.register(vaccineRegistration)
admin.site.register(vaccination)