  
from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'subscriptionStart', 'subscriptionEnd',)
    fieldsets = (
        ('Accountinfo', {
            'classes': ('collapse',),
            'fields': ('user', 'image', 'phone', 'address', 'email', 'emergency')
        }),
        ('Fluginfo', {
            'classes': ('collapse',),
            'fields': ('glider', 'flights')
        }),
        ('Schulung', {
            'classes': ('collapse',),
            'fields': ('subscriptionType', 'subscriptionStart', 'subscriptionEnd', 'subscriptionInvoice',
                        'materialInvoice', 'serialnumberRegistered', 'basicCourse', 'flightTest', 'shvSubscription',
                        'shvSticker', 'conditionsSigned', 'regaPatron', 'theoryExam', 'practiceExam',
                        'reserveTrainingValidUntil', 'reserveTrainingCompleted', 'teacherNotes')
        }),
        ('Premium Paket Gutscheine', {
            'classes': ('collapse',),
            'fields': ('gliderCheckRedeemed', 'reservePackingRedeemed', 'tandemFlightRedeemed',
                        'theoryCourse1Redeemed', 'theoryCourse2Redeemed')
        }),
        ('Material & Service', {
            'classes': ('collapse',),
            'fields': ('materialOrder', 'materialReturned', 'materialNotes', 'lastReserveCheck',
                        'nextReserveCheck', 'lastGliderCheck', 'nextGliderCheck')
        }),
        ('Progress Check - Übungshang', {
            'classes': ('collapse',),
            'fields': ('stage1_1', 'stage1_2', 'stage1_3', 'stage1_4', 'stage1_5', 'stage1_6', 'stage1_7',
                        'stage1_8', 'stage1_9', 'stage1_10', 'stage1_11', 'stage1_12', 'stage1_13',
                        'stage1_14', 'stage1_15', 'stage1_16', 'stage1_17')
        }),
        ('Progress Check - Flug 1-20', {
            'classes': ('collapse',),
            'fields': ('stage2_1', 'stage2_2', 'stage2_3', 'stage2_4', 'stage2_5', 'stage2_6', 'stage2_7',
                        'stage2_8', 'stage2_9', 'stage2_10', 'stage2_11', 'stage2_12', 'stage2_13')
        }),
        ('Progress Check - Flug 20-35', {
            'classes': ('collapse',),
            'fields': ('stage3_1', 'stage3_2', 'stage3_3', 'stage3_4', 'stage3_5', 'stage3_6')
        }),
        ('Progress Check - Flug 35-50+', {
            'classes': ('collapse',),
            'fields': ('stage4_1', 'stage4_2', 'stage4_3', 'stage4_4', 'stage4_5', 'stage4_6', 'stage4_7', 'stage4_8')
        }),
    )

admin.site.register(Profile, ProfileAdmin)