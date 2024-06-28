from django.contrib import admin

# Register your models here.
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('UserID','StaffID','StaffName','Role','Department','Password','Email','Language','Supervisor','IsActivated')
    search_fields = ('StaffID','StaffName',)
    ordering = ('StaffID',)

class PlantAdmin(admin.ModelAdmin):
    list_display = ('PlantID','ShortName','Language')
    search_fields = ('ShortName','Language',)
    ordering = ('ShortName',)

class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('TechnologyID','Name','Description')
    search_fields = ('Name','Description',)
    ordering = ('Name',)

class ChoiceQuestionHistoryAdmin(admin.ModelAdmin):
    list_display = (
        'ChoiceQuestionHistoryID',
        'ChoiceQuestionID',
        'Reason',
        'Operation',
        'StaffID',
        'StaffName',
        'CreateDate'
        )
    search_fields = ('ChoiceQuestionID','StaffID',)
    ordering = ('ChoiceQuestionID',)

class QuestionOptionAdmin(admin.ModelAdmin):
    list_display = ('QuestionOptionID','ChoiceQuestionID','Option','IsAnswer')
    search_fields = ('QuestionOptionID','ChoiceQuestionID',)
    ordering = ('QuestionOptionID',)

class ChoiceQuestionAdmin(admin.ModelAdmin):
    list_display = (
        'ChoiceQuestionID',
        'QuestionBankID',
        'BookID',
        'Subject',
        'Type',
        'CreatorID',
        'CreatorName',
        'UpdateDate',
        'CreateDate',
    )
    search_fields = ('CreatorID','QuestionBankID','BookID',)
    ordering = ('ChoiceQuestionID',)

class QuestionBankAdmin(admin.ModelAdmin):
    list_display = ('QuestionBankID','Name','IsExercised','ExamQuestionMaker','ExamPaperPublisher','Description')
    search_fields = ('QuestionBankID','Name',)
    ordering = ('QuestionBankID',)

class ExamedPaperAdmin(admin.ModelAdmin):
    list_display = (
        'ExamedPaperID',
        'ExamPaperID',
        'Name',
        'QuestionBankID',
        'IsExercised',
        'QuestionNumber',
        'PassQuestionNumber',
        'QuestionLimitTime',
        'ExamineeStaffID',
        'ExamineeStaffName',
        'PassedQuestionNumber',
        'IsPassed'
        )
    search_fields = ('ExamedPaperID','ExamPaperID','QuestionBankID','Name')
    ordering = ('ExamedPaperID',)

class ExamedChoiceQuestionAdmin(admin.ModelAdmin):
    list_display = ('ExamedChoiceQuestionID', 'ChoiceQuestionID', 'ExamedPaperID','Subject','Type','Content')
    search_fields = ('ExamedPaperID',)
    ordering = ('ExamedPaperID',)

class ExamedQuestionOptionAdmin(admin.ModelAdmin):
    list_display = ('ExamedQuestionOptionID','ExamedChoiceQuestionID','Option','IsAnswer','IsMarked')
    search_fields = ('ExamedQuestionOptionID','ExamedChoiceQuestionID',)
    ordering = ('ExamedQuestionOptionID',)

class OptionAdmin(admin.ModelAdmin):
    list_display = ('OptionID','Name')
    search_fields = ('OptionID','Name',)
    ordering = ('OptionID',)

class ExamineeAdmin(admin.ModelAdmin):
    list_display = ('ExamineeID','ExamPaperID','StaffID','StaffName','ExamedCount','ProductLine', 'IsPassed', 'CreateDate')
    search_fields = ('ExamineeID','StaffID','ExamPaperID')
    ordering = ('ExamPaperID','StaffID',)

class ExamPaperAdmin(admin.ModelAdmin):
    list_display = ('ExamPaperID','Name','QuestionBankID', 'BookID','Deadline', 'ExamMaxCount','QuestionNumber','PassQuestionNumber','IsExercised', 'QuestionLimitTime', 'OptionAnsCategorys', 'OptionAnsMinNumber', 'CreatorID', 'CreatorName')
    search_fields = ('ExamPaperID','QuestionBankID','Name',)
    ordering = ('QuestionBankID',)

class TrainingBankAdmin(admin.ModelAdmin):
    list_display = ('TrainingBankID','Name','TrainingMaterialMaker','Trainer','Description')
    search_fields = ('TrainingBankID','Name',)
    ordering = ('TrainingBankID',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('BookID','TrainingBankID','TrainingBankName','Name','MinTime','CreatorID','CreatorName','UpdateDate','CreateDate')
    search_fields = ('BookID','TrainingBankID',)
    ordering = ('BookID',)

class TrainingRecordAdmin(admin.ModelAdmin):
    list_display = ('TrainingRecordID','BookID','BookName','BookMinTime','TrainingBankName','StaffID','StaffName','TrainingTime','IsPassed','CreateDate')
    search_fields = ('TrainingRecordID','BookID',)
    ordering = ('TrainingRecordID',)

class BookHistoryAdmin(admin.ModelAdmin):
    list_display = ('BookHistoryID','BookID','Reason','Operation','StaffID','StaffName','CreateDate')
    search_fields = ('BookHistoryID','BookID',)
    ordering = ('BookID',)

class BookPageAdmin(admin.ModelAdmin):
    list_display = ('BookPageID','BookID','Name','Content','AudioPathFile','MinTime','Sequence','CreatorID','CreatorName','UpdateDate','CreateDate')
    search_fields = ('BookPageID','BookID',)
    ordering = ('BookID',)

class BookPageHistoryAdmin(admin.ModelAdmin):
    list_display = ('BookPageHistoryID','BookID','BookPageID','Reason','Operation','StaffID','StaffName','CreateDate')
    search_fields = ('BookPageHistoryID','BookID',)
    ordering = ('BookID',)

admin.site.register(User, UserAdmin)
admin.site.register(Plant, PlantAdmin)
admin.site.register(Technology, TechnologyAdmin)
admin.site.register(ChoiceQuestionHistory, ChoiceQuestionHistoryAdmin)
admin.site.register(QuestionOption, QuestionOptionAdmin)
admin.site.register(ChoiceQuestion, ChoiceQuestionAdmin)
admin.site.register(QuestionBank, QuestionBankAdmin)
admin.site.register(ExamedPaper, ExamedPaperAdmin)
admin.site.register(ExamedChoiceQuestion, ExamedChoiceQuestionAdmin)
admin.site.register(ExamedQuestionOption, ExamedQuestionOptionAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(Examinee, ExamineeAdmin)
admin.site.register(ExamPaper, ExamPaperAdmin)
admin.site.register(TrainingBank, TrainingBankAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(TrainingRecord, TrainingRecordAdmin)
admin.site.register(BookHistory, BookHistoryAdmin)
admin.site.register(BookPage, BookPageAdmin)
admin.site.register(BookPageHistory, BookPageHistoryAdmin)
