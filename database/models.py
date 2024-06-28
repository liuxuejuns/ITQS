from django.db import models
import django.utils.timezone as timezone

# Create your models here.
class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    Site =  models.CharField(max_length=10)
    PlantName = models.CharField(max_length=10)
    StaffID = models.CharField(max_length=20)
    StaffName = models.CharField(max_length=30)
    Role = models.CharField(max_length=10, null=True, blank=True)
    Department = models.CharField(max_length=10, null=True, blank=True)
    Password = models.CharField(max_length=20)
    Email = models.CharField(max_length=50, null=True, blank=True)
    Language = models.CharField(max_length=20)
    Supervisor = models.IntegerField(null=True, blank=True)
    IsActivated = models.BooleanField(default=False)  # False: Un-activated; True: activated

    class Meta:
        db_table = 'User'

    def __str__(self):
        return 'ID%s: StaffID(%s),StaffName(%s)' % (self.UserID, self.StaffID, self.StaffName)

class Plant(models.Model):
    PlantID = models.AutoField(primary_key=True)
    Site =  models.CharField(max_length=10)
    ShortName = models.CharField(max_length=10)
    Language = models.CharField(max_length=20)

    class Meta:
        db_table = 'Plant'

    def __str__(self):
        return 'ID%s: ShortName(%s) Site(%s) Language(%s)' % (self.PlantID, self.ShortName, self.Site, self.Language)

class Technology(models.Model):
    TechnologyID = models.AutoField(primary_key=True)
    Site =  models.CharField(max_length=10)
    PlantName = models.CharField(max_length=10)
    Name = models.CharField(max_length=30)
    Description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'Technology'
    
    def __str__(self):
        return 'ID%s: Name(%s)' % (self.TechnologyID, self.Name)

class ChoiceQuestionHistory(models.Model):
    ChoiceQuestionHistoryID = models.BigAutoField(primary_key=True)
    ChoiceQuestionID = models.IntegerField()
    Reason = models.TextField()
    Operation = models.CharField(max_length=10)
    StaffID = models.CharField(max_length=20)
    StaffName = models.CharField(max_length=30)
    CreateDate = models.DateTimeField()

    class Meta:
        db_table = 'ChoiceQuestionHistory'

    def __str__(self):
        return 'ID%s: ChoiceQuestion(%s)' % (self.ChoiceQuestionHistoryID, self.ChoiceQuestionID)

class QuestionOption(models.Model):
    QuestionOptionID = models.BigAutoField(primary_key=True)
    ChoiceQuestionID = models.IntegerField()
    Option = models.CharField(max_length=50)
    IsAnswer = models.BooleanField(default=True)

    class Meta:
        db_table = 'QuestionOption'

    def __str__(self):
        return 'ID%s: ChoiceQuestionID(%s) Option(%s) IsAnswer(%s)' % (self.QuestionOptionID, self.ChoiceQuestionID, self.Option, self.IsAnswer)

class ChoiceQuestion(models.Model):
    ChoiceQuestionID = models.AutoField(primary_key=True)
    QuestionBankID = models.IntegerField()
    BookID = models.IntegerField(null=True)
    Subject = models.CharField(max_length=100, null=True, blank=True)
    Type = models.CharField(max_length=10,default='Single')
    Content = models.TextField()
    CreatorID = models.CharField(max_length=20)
    CreatorName = models.CharField(max_length=30)
    UpdateDate = models.DateTimeField()
    CreateDate = models.DateTimeField()

    class Meta:
        db_table = 'ChoiceQuestion'
    
    def __str__(self):
        return 'ID%s: QuestionBankID(%s)' % (self.ChoiceQuestionID, self.QuestionBankID)

class QuestionBank(models.Model):
    QuestionBankID = models.AutoField(primary_key=True)
    Site = models.CharField(max_length = 10)
    Plant = models.CharField(max_length = 10)
    Name = models.CharField(max_length=30)
    IsExercised = models.BooleanField(default=False)
    ExamQuestionMaker = models.CharField(max_length=512, null=True, blank=True)
    ExamPaperPublisher = models.CharField(max_length=512, null=True, blank=True)
    Description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'QuestionBank'
    
    def __str__(self):
        return 'ID%s: Name(%s)' % (self.QuestionBankID, self.Name)

class ExamedPaper(models.Model):
    ExamedPaperID = models.AutoField(primary_key=True)
    ExamPaperID = models.IntegerField(null=True)
    Site = models.CharField(max_length = 10)
    Plant = models.CharField(max_length = 10)
    Name = models.CharField(max_length=100, null=True)
    QuestionBankID = models.IntegerField()
    QuestionBankName = models.CharField(max_length=30)
    IsExercised = models.BooleanField(default=False)
    QuestionNumber = models.SmallIntegerField()
    PassQuestionNumber = models.SmallIntegerField()
    QuestionLimitTime = models.SmallIntegerField()
    ExamTime = models.SmallIntegerField()
    OptionAnsMinNumber = models.SmallIntegerField()
    NewQuestionBeforeDays = models.SmallIntegerField(default=0)
    NewQuestionPercent = models.SmallIntegerField()
    Deadline = models.DateTimeField()
    ExamMaxCount = models.SmallIntegerField()
    ExamineeStaffID = models.CharField(max_length=20)
    ExamineeStaffName = models.CharField(max_length=30)
    ExamedCount = models.SmallIntegerField(default=0)
    PassedQuestionNumber = models.SmallIntegerField()
    IsPassed = models.BooleanField(default=False)
    CreateDate = models.DateTimeField()

    class Meta:
        db_table = 'ExamedPaperID'
    
    def __str__(self):
        return 'ID%s: QuestionBankName(%s)' % (self.ExamedPaperID, self.QuestionBankName)

class ExamedChoiceQuestion(models.Model):
    ExamedChoiceQuestionID = models.AutoField(primary_key=True)
    ChoiceQuestionID = models.IntegerField(default=0)
    ExamedPaperID = models.IntegerField()
    Subject = models.CharField(max_length=100, null=True, blank=True)
    Type = models.CharField(max_length=10, default='Single')
    Content = models.TextField()

    class Meta:
        db_table = 'ExamedChoiceQuestion'

    def __str__(self):
        return 'ID%s: ExamedPaperID(%s)' % (self.ExamedChoiceQuestionID, self.ExamedPaperID)

class ExamedQuestionOption(models.Model):
    ExamedQuestionOptionID = models.BigAutoField(primary_key=True)
    ExamedChoiceQuestionID = models.IntegerField()
    Option = models.CharField(max_length=50)
    IsAnswer = models.BooleanField()
    IsMarked = models.BooleanField(default=False)

    class Meta:
        db_table = 'ExamedQuestionOption'
    
    def __str__(self):
        return 'ID%s: ExamedChoiceQuestionID(%s)' % (self.ExamedQuestionOptionID, self.ExamedChoiceQuestionID)

class Option(models.Model):
    OptionID = models.AutoField(primary_key=True)
    Site =  models.CharField(max_length=10)
    PlantName = models.CharField(max_length=10)
    Name = models.CharField(max_length=50)

    class Meta:
        db_table = 'Option'

    def __str__(self):
        return 'ID%s: Name(%s)' % (self.OptionID, self.Name)

class Examinee(models.Model):
    ExamineeID = models.AutoField(primary_key=True)
    ExamPaperID = models.IntegerField()
    StaffID = models.CharField(max_length=20)
    StaffName = models.CharField(max_length=30)
    ExamedCount = models.SmallIntegerField(default=0)
    ProductLine = models.CharField(max_length=30, default="")
    IsPassed = models.BooleanField(default=False)
    CreateDate = models.DateTimeField()

    class Meta:
        db_table = 'Examinee'

    def __str__(self):
        return 'ID%s: ExamPaperID(%s) StaffID(%s)' % (self.ExamineeID, self.ExamPaperID, self.StaffID)

class ExamPaper(models.Model):
    ExamPaperID = models.AutoField(primary_key=True)
    Site = models.CharField(max_length = 10)
    Plant = models.CharField(max_length = 10)
    Name = models.CharField(max_length=100, null=True)
    QuestionBankID = models.IntegerField()
    QuestionBankName = models.CharField(max_length=30)
    IsExercised = models.BooleanField(default=False)
    BookID = models.IntegerField(default=0)
    Deadline = models.DateTimeField(default=timezone.now)
    ExamMaxCount = models.SmallIntegerField(default=0)
    QuestionNumber = models.SmallIntegerField()
    PassQuestionNumber = models.SmallIntegerField()
    QuestionLimitTime = models.SmallIntegerField()
    ExamTime = models.SmallIntegerField()
    OptionAnsCategorys = models.CharField(max_length=512, default="")
    OptionAnsMinNumber = models.SmallIntegerField()
    NewQuestionBeforeDays = models.SmallIntegerField(default=0)
    NewQuestionPercent = models.SmallIntegerField()
    CreatorID = models.CharField(max_length=20, default="")
    CreatorName = models.CharField(max_length=30, default="")
    CreateDate = models.DateTimeField()

    class Meta:
        db_table = 'ExamPaper'

    def __str__(self):
        return 'ID%s: QuestionBankID(%s) QuestionBankName(%s)' % (self.ExamPaperID, self.QuestionBankID, self.QuestionBankName)

class TrainingBank(models.Model):
    TrainingBankID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30)
    Site = models.CharField(max_length = 10)
    Plant = models.CharField(max_length = 10)
    TrainingMaterialMaker = models.CharField(max_length=512, null=True, blank=True)
    Trainer = models.CharField(max_length=512, null=True, blank=True)
    Description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'TrainingBank'

    def __str__(self):
        return 'ID%s: Name(%s) Trainer(%s)' % (self.TrainingBankID, self.Name, self.Trainer)

class Book(models.Model):
    BookID = models.AutoField(primary_key=True)
    Site = models.CharField(max_length = 10)
    Plant = models.CharField(max_length = 10)
    TrainingBankID = models.IntegerField()
    TrainingBankName = models.CharField(max_length=30)
    Name = models.CharField(max_length=100)
    MinTime = models.SmallIntegerField()
    CreatorID = models.CharField(max_length=20)
    CreatorName = models.CharField(max_length=30)
    UpdateDate = models.DateTimeField()
    CreateDate = models.DateTimeField()

    class Meta:
        db_table = 'Book'

    def __str__(self):
        return 'ID%s: TrainingBankID(%s) Name(%s)' % (self.BookID, self.TrainingBankID, self.Name)

class TrainingRecord(models.Model):
    TrainingRecordID = models.AutoField(primary_key=True)
    Site = models.CharField(max_length = 10)
    Plant = models.CharField(max_length = 10)
    BookID = models.IntegerField()
    BookName = models.CharField(max_length=100)
    BookMinTime = models.SmallIntegerField()
    TrainingBankName = models.CharField(max_length=30)
    StaffID = models.CharField(max_length=20)
    StaffName = models.CharField(max_length=30)
    TrainingTime = models.SmallIntegerField()
    IsPassed = models.BooleanField(default=False)
    CreateDate = models.DateTimeField()

    class Meta:
        db_table = 'TrainingRecord'

    def __str__(self):
        return 'ID%s: BookID(%s) StaffID(%s)' % (self.TrainingRecordID, self.BookID, self.StaffID)

class BookHistory(models.Model):
    BookHistoryID = models.AutoField(primary_key=True)
    BookID = models.IntegerField()
    Reason = models.TextField()
    Operation = models.CharField(max_length=10)
    StaffID = models.CharField(max_length=20)
    StaffName = models.CharField(max_length=30)
    CreateDate = models.DateTimeField()

    class Meta:
        db_table = 'BookHistory'

    def __str__(self):
        return 'ID%s: BookID(%s) StaffID(%s)' % (self.BookHistoryID, self.BookID, self.StaffID)

class BookPage(models.Model):
    BookPageID = models.BigAutoField(primary_key=True)
    BookID = models.IntegerField()
    Name = models.CharField(max_length=100)
    Content = models.TextField()
    AudioPathFile = models.CharField(max_length=512, null=True, blank=True)
    MinTime = models.SmallIntegerField()
    Sequence = models.SmallIntegerField(default=0)
    CreatorID = models.CharField(max_length=20)
    CreatorName = models.CharField(max_length=30)
    UpdateDate = models.DateTimeField()
    CreateDate = models.DateTimeField()

    class Meta:
        db_table = 'BookPage'

    def __str__(self):
        return 'ID%s: BookID(%s) Name(%s)' % (self.BookPageID, self.BookID, self.Name)

class BookPageHistory(models.Model):
    BookPageHistoryID = models.BigAutoField(primary_key=True)
    BookID = models.IntegerField()
    BookPageID = models.IntegerField()
    Reason = models.TextField()
    Operation = models.CharField(max_length=10)
    StaffID = models.CharField(max_length=20)
    StaffName = models.CharField(max_length=30)
    CreateDate = models.DateTimeField()

    class Meta:
        db_table = 'BookPageHistory'

    def __str__(self):
        return 'ID%s: BookID(%s) StaffID(%s)' % (self.BookPageHistoryID, self.BookID, self.StaffID)