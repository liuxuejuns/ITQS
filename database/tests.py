from django.test import TestCase

# Create your tests here.

from database.models import Book
from database.models import BookHistory
from database.models import BookPage
from database.models import BookPageHistory
from database.models import TrainingRecord, QuestionOption,ChoiceQuestionHistory
from database.models import User, Technology, Plant, QuestionBank, TrainingBank, ChoiceQuestion,Examinee,ExamPaper,ExamedPaper,ExamedChoiceQuestion,ExamedQuestionOption,Option,Examinee
from database.models import Option
from django.db.models import Count

book_obj_list = Book.objects.all()

for book_obj in book_obj_list:
    exam_paper_obj_list = ExamPaper.objects.filter(BookID=book_obj.BookID)
    if exam_paper_obj_list.exists():
        choice_question_obj_list = ChoiceQuestion.objects.filter(BookID=book_obj.BookID)
        question_option_obj_list = QuestionOption.objects.filter(ChoiceQuestionID__in=choice_question_obj_list, IsAnswer=True).values('Option').annotate(Count=Count('QuestionOptionID')).values('Option', 'Count')
        question_option_list = list(question_option_obj_list)
        if len(question_option_list) == 0:
            continue
        for exam_paper_obj in exam_paper_obj_list:
            option_list = []
            for question_option in question_option_list:
                if question_option['Count'] <= exam_paper_obj.OptionAnsMinNumber:
                    option_list.append(question_option['Option'])
            print(str(exam_paper_obj.ExamPaperID) + ":" +','.join(option_list))
            ExamPaper.objects.filter(ExamPaperID=exam_paper_obj.ExamPaperID).update(OptionAnsCategorys=','.join(option_list))


passed_exam_paper_obj_list = []
unpassed_exam_paper_obj_list = []
exam_paper_obj_list = ExamPaper.objects.filter(CreatorID=staff_id).order_by('Deadline')
for exam_paper_obj in exam_paper_obj_list:
    examinee_obj_list = Examinee.objects.filter(ExamPaperID=exam_paper_obj.ExamPaperID, IsPassed=False)
    if examinee_obj_list.exists():
        unpassed_exam_paper_obj_list.append(exam_paper_obj)
    else:
        passed_exam_paper_obj_list.append(exam_paper_obj)
exam_paper_obj_list[i]['Passed'] = True

exam_paper_obj_list = unpassed_exam_paper_obj_list + passed_exam_paper_obj_list