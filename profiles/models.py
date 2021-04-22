from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.html import mark_safe

class Profile(models.Model):
    #Account Info
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField('Foto', upload_to='profiles', blank=True, null=True)
    phone = models.CharField('Telefonnummer', max_length=20, blank=True, null=True)
    address = models.TextField('Adresse', blank=True, null=True)
    email = models.EmailField('E-Mail', blank=True, null=True)
    emergency = models.TextField('Notfallkontakt', max_length=200, blank=True, null=True)
    # Flying Info
    glider = models.CharField('Gleitschirm', max_length=64, blank=True, null=True)
    flights = models.IntegerField('Höhenflüge', default=0)
    # Schooling
    subscriptionType = models.CharField('Schulungspaket', null=True, blank=True, max_length=10, choices=[
        ('Basic', 'Basic'), 
        ('Premium', 'Premium'), 
        ],
    )
    subscriptionStart = models.DateField('Schulungsanfang', null=True, blank=True)
    subscriptionEnd = models.DateField('Schulungsende', null=True, blank=True)
    subscriptionInvoice = models.DateField('Rechnung gestellt Schulung', null=True, blank=True)
    materialInvoice = models.DateField('Rechnung gestellt Material', null=True, blank=True)
    serialnumberRegistered = models.BooleanField('Seriennummer Registriert', default=False)
    basicCourse = models.BooleanField('Grundkurs abgeschlossen', default=False)
    flightTest = models.BooleanField('Test vor dem ersten Höhenflug', default=False)
    shvSubscription = models.BooleanField('SHV Anmeldung', default=False)
    shvSticker = models.BooleanField('SHV Nummer aufgeklebt', default=False)
    conditionsSigned = models.BooleanField('AGBs unterzeichnet', default=False)
    regaPatron = models.BooleanField('Rega Gönner/in', default=False)
    theoryExam = models.BooleanField('Theorieprüfung', default=False)
    practiceExam = models.BooleanField('Praktische Prüfung', default=False)
    reserveTrainingValidUntil = models.DateField('Notschirmtraining Gültig bis', null=True, blank=True)
    reserveTrainingCompleted = models.DateField('Notschirmtraining absolviert am', null=True, blank=True)  
    teacherNotes = models.TextField('Fluglehrer Notizen', blank=True, null=True)
    # Premium Voucher
    gliderCheckRedeemed = models.BooleanField('Gleitschirm-Check', default=False)
    reservePackingRedeemed = models.BooleanField('Notschirmpackung', default=False)
    tandemFlightRedeemed = models.BooleanField('Tandem Gastflug (1 Jahr gültig)', default=False)
    theoryCourse1Redeemed = models.BooleanField('Theoriekurs 1 (1 Jahr gültig)', default=False)
    theoryCourse2Redeemed = models.BooleanField('Theoriekurs 2 (1 Jahr gültig)', default=False)
    # Material and Service
    materialOrder = models.TextField('Materialbestellung', blank=True, null=True)
    materialReturned = models.BooleanField('Theoriekurs 1 (1 Jahr gültig)', default=False)
    materialNotes = models.TextField('Fluglehrer Notizen', blank=True, null=True)
    lastReserveCheck = models.DateField('Letzter Notschirm Service', null=True, blank=True)
    nextReserveCheck = models.DateField('Nächster Notschirm Service', null=True, blank=True)
    lastGliderCheck = models.DateField('Letzter Gleitschirm Check', null=True, blank=True)
    nextGliderCheck = models.DateField('Nächster Gleitschirm Check', null=True, blank=True)
    # Progress Check
    ## STUFE 1: ÜBUNGSHANG
    stage1_1 = models.BooleanField('Auslegen', default=False)
    stage1_2 = models.BooleanField('Startvorbereitungen und 5-Punkte- Check', default=False)
    stage1_3 = models.BooleanField('3-Phasen-Start', default=False)
    stage1_4 = models.BooleanField('Aufzieh- und Laufübungen', default=False)
    stage1_5 = models.BooleanField('Slalomlauf', default=False)
    stage1_6 = models.BooleanField('Laufen mit abgebremstem Schirm', default=False)
    stage1_7 = models.BooleanField('Startabbruch (Entscheidungslinie)', default=False)
    stage1_8 = models.BooleanField('Flüge mit Richtungsänderungen', default=False)
    stage1_9 = models.BooleanField('Seitenwindstart (evtl. Simulation)', default=False)
    stage1_10 = models.BooleanField('Start mit schlecht ausgelegter Kalotte', default=False)
    stage1_11 = models.BooleanField('Start mit vorwärts & rückwärts Aufziehen', default=False)
    stage1_12 = models.BooleanField('Landetechnik und Landungen Einweisung mit Notlandeübungen Einweisung', default=False)
    stage1_13 = models.BooleanField('Rettungssystem', default=False)
    stage1_14 = models.BooleanField('90-180°- Kurven (Landeeinteilung) Entwirren', default=False)
    stage1_15 = models.BooleanField('Faltmethoden', default=False)
    stage1_16 = models.BooleanField('Theorietest vor dem 1. Höhenflug', default=False)
    stage1_17 = models.BooleanField('SHV-Nummer auf Schirm aufgeklebt', default=False)
    ## STUFE 2: HÖHENFLUG 1-20
    stage2_1 = models.BooleanField('Doppelsitzerflug als Passagier (fak.) Einweisung Notlandungen', default=False)
    stage2_2 = models.BooleanField('Start mit vorwärts & rückwärts Aufziehen', default=False)
    stage2_3 = models.BooleanField('Geländebeurteilung und Startplatzwahl', default=False)
    stage2_4 = models.BooleanField('Links- und rechtsdrehende Kreise', default=False)
    stage2_5 = models.BooleanField('Anwendung des Beschleunigungssystems', default=False)
    stage2_6 = models.BooleanField('Steuern mit Gewichtsverlagerung Nicken / Pendeln um die Querachse Ohren anlegen', default=False)
    stage2_7 = models.BooleanField('Landrevolte links/rechts', default=False)
    stage2_8 = models.BooleanField('Rollen', default=False)
    stage2_9 = models.BooleanField('Einseitiges Einklappen', default=False)
    stage2_10 = models.BooleanField('Enge Kreise', default=False)
    stage2_11 = models.BooleanField('Kreis links, kreis rechts (Acht)', default=False)
    stage2_12 = models.BooleanField('Einweisung Sackflug', default=False)
    stage2_13 = models.BooleanField('Erliegen des sicheren Geschwindigkeitsbereiches', default=False)
    ## STUFE 3: HÖHENFLUG 20-35
    stage3_1 = models.BooleanField('Schnelle Richtungswechsel', default=False)
    stage3_2 = models.BooleanField('Positiv- und Negativsteuerung Steuern mit Hinteren Traggurten B-Leinen-Stall (fak.)', default=False)
    stage3_3 = models.BooleanField('Einweisung Spirale', default=False)
    stage3_4 = models.BooleanField('Einweisung Rückenwindlandung Landung mit hinteren Traggurten Hanglandung', default=False)
    stage3_5 = models.BooleanField('Touch and Go (fak.) Ziellandungen', default=False)
    stage3_6 = models.BooleanField('Prüfungsprogramme', default=False)
    ## STUFE 4: HÖHENFLUG 35-50+
    stage4_1 = models.BooleanField('Hangsoaring', default=False)
    stage4_2 = models.BooleanField('Thermikflug', default=False)
    stage4_3 = models.BooleanField('Flug mit Instrumenten Starkwindstart (Cobra ect.)', default=False)
    stage4_4 = models.BooleanField('Aussenlandung Prüfungsvorbereitung', default=False)
    stage4_5 = models.BooleanField('Selbst. Luftraumbriefing', default=False)
    stage4_6 = models.BooleanField('Selbst. Fluggebietwahl', default=False)
    stage4_7 = models.BooleanField('Selbst. Wetterbriefing', default=False)
    stage4_8 = models.BooleanField('Notschirmwerfen/ SIKU (Fak.)', default=False)

    def __str__(self):
        return str(self.user)

#Automatische Erstellung vom User Profile bei User Erstellung (1-1 Beziehung)
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


def image_tag(self):
    return mark_safe('<img src="/directory/%s" width="150" height="150" />' % (self.image))
image_tag.short_description = 'Image'