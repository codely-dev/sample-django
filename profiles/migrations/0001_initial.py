# Generated by Django 3.1.6 on 2021-04-22 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='profiles', verbose_name='Foto')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefonnummer')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Adresse')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-Mail')),
                ('emergency', models.TextField(blank=True, max_length=200, null=True, verbose_name='Notfallkontakt')),
                ('glider', models.CharField(blank=True, max_length=64, null=True, verbose_name='Gleitschirm')),
                ('flights', models.IntegerField(default=0, verbose_name='Höhenflüge')),
                ('subscriptionType', models.CharField(blank=True, choices=[('Basic', 'Basic'), ('Premium', 'Premium')], max_length=10, null=True, verbose_name='Schulungspaket')),
                ('subscriptionStart', models.DateField(blank=True, null=True, verbose_name='Schulungsanfang')),
                ('subscriptionEnd', models.DateField(blank=True, null=True, verbose_name='Schulungsende')),
                ('subscriptionInvoice', models.DateField(blank=True, null=True, verbose_name='Rechnung gestellt Schulung')),
                ('materialInvoice', models.DateField(blank=True, null=True, verbose_name='Rechnung gestellt Material')),
                ('serialnumberRegistered', models.BooleanField(default=False, verbose_name='Seriennummer Registriert')),
                ('basicCourse', models.BooleanField(default=False, verbose_name='Grundkurs abgeschlossen')),
                ('flightTest', models.BooleanField(default=False, verbose_name='Test vor dem ersten Höhenflug')),
                ('shvSubscription', models.BooleanField(default=False, verbose_name='SHV Anmeldung')),
                ('shvSticker', models.BooleanField(default=False, verbose_name='SHV Nummer aufgeklebt')),
                ('conditionsSigned', models.BooleanField(default=False, verbose_name='AGBs unterzeichnet')),
                ('regaPatron', models.BooleanField(default=False, verbose_name='Rega Gönner/in')),
                ('theoryExam', models.BooleanField(default=False, verbose_name='Theorieprüfung')),
                ('practiceExam', models.BooleanField(default=False, verbose_name='Praktische Prüfung')),
                ('reserveTrainingValidUntil', models.DateField(blank=True, null=True, verbose_name='Notschirmtraining Gültig bis')),
                ('reserveTrainingCompleted', models.DateField(blank=True, null=True, verbose_name='Notschirmtraining absolviert am')),
                ('teacherNotes', models.TextField(blank=True, null=True, verbose_name='Fluglehrer Notizen')),
                ('gliderCheckRedeemed', models.BooleanField(default=False, verbose_name='Gleitschirm-Check')),
                ('reservePackingRedeemed', models.BooleanField(default=False, verbose_name='Notschirmpackung')),
                ('tandemFlightRedeemed', models.BooleanField(default=False, verbose_name='Tandem Gastflug (1 Jahr gültig)')),
                ('theoryCourse1Redeemed', models.BooleanField(default=False, verbose_name='Theoriekurs 1 (1 Jahr gültig)')),
                ('theoryCourse2Redeemed', models.BooleanField(default=False, verbose_name='Theoriekurs 2 (1 Jahr gültig)')),
                ('materialOrder', models.TextField(blank=True, null=True, verbose_name='Materialbestellung')),
                ('materialReturned', models.BooleanField(default=False, verbose_name='Theoriekurs 1 (1 Jahr gültig)')),
                ('materialNotes', models.TextField(blank=True, null=True, verbose_name='Fluglehrer Notizen')),
                ('lastReserveCheck', models.DateField(blank=True, null=True, verbose_name='Letzter Notschirm Service')),
                ('nextReserveCheck', models.DateField(blank=True, null=True, verbose_name='Nächster Notschirm Service')),
                ('lastGliderCheck', models.DateField(blank=True, null=True, verbose_name='Letzter Gleitschirm Check')),
                ('nextGliderCheck', models.DateField(blank=True, null=True, verbose_name='Nächster Gleitschirm Check')),
                ('stage1_1', models.BooleanField(default=False, verbose_name='Auslegen')),
                ('stage1_2', models.BooleanField(default=False, verbose_name='Startvorbereitungen und 5-Punkte- Check')),
                ('stage1_3', models.BooleanField(default=False, verbose_name='3-Phasen-Start')),
                ('stage1_4', models.BooleanField(default=False, verbose_name='Aufzieh- und Laufübungen')),
                ('stage1_5', models.BooleanField(default=False, verbose_name='Slalomlauf')),
                ('stage1_6', models.BooleanField(default=False, verbose_name='Laufen mit abgebremstem Schirm')),
                ('stage1_7', models.BooleanField(default=False, verbose_name='Startabbruch (Entscheidungslinie)')),
                ('stage1_8', models.BooleanField(default=False, verbose_name='Flüge mit Richtungsänderungen')),
                ('stage1_9', models.BooleanField(default=False, verbose_name='Seitenwindstart (evtl. Simulation)')),
                ('stage1_10', models.BooleanField(default=False, verbose_name='Start mit schlecht ausgelegter Kalotte')),
                ('stage1_11', models.BooleanField(default=False, verbose_name='Start mit vorwärts & rückwärts Aufziehen')),
                ('stage1_12', models.BooleanField(default=False, verbose_name='Landetechnik und Landungen Einweisung mit Notlandeübungen Einweisung')),
                ('stage1_13', models.BooleanField(default=False, verbose_name='Rettungssystem')),
                ('stage1_14', models.BooleanField(default=False, verbose_name='90-180°- Kurven (Landeeinteilung) Entwirren')),
                ('stage1_15', models.BooleanField(default=False, verbose_name='Faltmethoden')),
                ('stage1_16', models.BooleanField(default=False, verbose_name='Theorietest vor dem 1. Höhenflug')),
                ('stage1_17', models.BooleanField(default=False, verbose_name='SHV-Nummer auf Schirm aufgeklebt')),
                ('stage2_1', models.BooleanField(default=False, verbose_name='Doppelsitzerflug als Passagier (fak.) Einweisung Notlandungen')),
                ('stage2_2', models.BooleanField(default=False, verbose_name='Start mit vorwärts & rückwärts Aufziehen')),
                ('stage2_3', models.BooleanField(default=False, verbose_name='Geländebeurteilung und Startplatzwahl')),
                ('stage2_4', models.BooleanField(default=False, verbose_name='Links- und rechtsdrehende Kreise')),
                ('stage2_5', models.BooleanField(default=False, verbose_name='Anwendung des Beschleunigungssystems')),
                ('stage2_6', models.BooleanField(default=False, verbose_name='Steuern mit Gewichtsverlagerung Nicken / Pendeln um die Querachse Ohren anlegen')),
                ('stage2_7', models.BooleanField(default=False, verbose_name='Landrevolte links/rechts')),
                ('stage2_8', models.BooleanField(default=False, verbose_name='Rollen')),
                ('stage2_9', models.BooleanField(default=False, verbose_name='Einseitiges Einklappen')),
                ('stage2_10', models.BooleanField(default=False, verbose_name='Enge Kreise')),
                ('stage2_11', models.BooleanField(default=False, verbose_name='Kreis links, kreis rechts (Acht)')),
                ('stage2_12', models.BooleanField(default=False, verbose_name='Einweisung Sackflug')),
                ('stage2_13', models.BooleanField(default=False, verbose_name='Erliegen des sicheren Geschwindigkeitsbereiches')),
                ('stage3_1', models.BooleanField(default=False, verbose_name='Schnelle Richtungswechsel')),
                ('stage3_2', models.BooleanField(default=False, verbose_name='Positiv- und Negativsteuerung Steuern mit Hinteren Traggurten B-Leinen-Stall (fak.)')),
                ('stage3_3', models.BooleanField(default=False, verbose_name='Einweisung Spirale')),
                ('stage3_4', models.BooleanField(default=False, verbose_name='Einweisung Rückenwindlandung Landung mit hinteren Traggurten Hanglandung')),
                ('stage3_5', models.BooleanField(default=False, verbose_name='Touch and Go (fak.) Ziellandungen')),
                ('stage3_6', models.BooleanField(default=False, verbose_name='Prüfungsprogramme')),
                ('stage4_1', models.BooleanField(default=False, verbose_name='Hangsoaring')),
                ('stage4_2', models.BooleanField(default=False, verbose_name='Thermikflug')),
                ('stage4_3', models.BooleanField(default=False, verbose_name='Flug mit Instrumenten Starkwindstart (Cobra ect.)')),
                ('stage4_4', models.BooleanField(default=False, verbose_name='Aussenlandung Prüfungsvorbereitung')),
                ('stage4_5', models.BooleanField(default=False, verbose_name='Selbst. Luftraumbriefing')),
                ('stage4_6', models.BooleanField(default=False, verbose_name='Selbst. Fluggebietwahl')),
                ('stage4_7', models.BooleanField(default=False, verbose_name='Selbst. Wetterbriefing')),
                ('stage4_8', models.BooleanField(default=False, verbose_name='Notschirmwerfen/ SIKU (Fak.)')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
