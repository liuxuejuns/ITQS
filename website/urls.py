from django.urls import path
from django.urls import re_path as url

from . import views

app_name = 'website'
urlpatterns = [
    # path('componentInfo', views.component_info, name='componentInfo'),
    # path('view',views.view,name='view'),
    path('display/', views.display, name='display'),
    path('index/', views.index, name='index'),
    path('SuperAdminIndex/', views.SuperAdminIndex, name='SuperAdminIndex'),
    path(
        'index/get_user_authority/', views.get_user_authority, name='get_user_authority'
    ),
    path('index/todo_num/', views.index_todo_num, name='index_todo_num'),
    path('need_to_know/', views.need_to_know, name='need_to_know'),
    path('train/<int:bookid>/', views.train, name='train'),
    path(
        'train_skill_category/', views.train_skill_category, name='train_skill_category'
    ),
    path('train_book/', views.train_book, name='train_book'),
    path('train_records/', views.train_records, name='train_records'),
    path('practice/', views.practice, name='practice'),
    path('practice_records/', views.practice_records, name='practice_records'),
    path('pre_issue_paper/', views.pre_issue_paper, name='pre_issue_paper'),
    path('issue_paper/', views.issue_paper, name='issue_paper'),
    path('pre_exam/', views.pre_exam, name='pre_exam'),
    path('exam_notice/', views.exam_notice, name='exam_notice'),
    path('examing/', views.examing, name='examing'),
    path('exam_records/', views.exam_records, name='exam_records'),
    path('register/', views.register, name='register'),
    path('register/add_new_user', views.add_new_user, name='register/add_new_user'),
    path('login_index', views.login_index, name='login_index'),
    path('master', views.master, name='master'),
    path('technology', views.technology, name='technology'),
    path('plant', views.plant, name='plant'),
    path('questionbank', views.questionbank, name='questionbank'),
    path('trainingbank', views.trainingbank, name='trainingbank'),
    path('personal', views.personal, name='personal'),
    path('option', views.option, name='option'),
    path('bookPage', views.bookPage, name='bookPage'),
    path('skill_sort', views.skill_sort, name='skill_sort'),
    path('qBankSort', views.qBankSort, name='qBankSort'),
    # 超级管理员
    url(r'^get_super_all_user$', views.get_super_all_user),
    path(
        'get_super_all_site_plant/',
        views.get_super_all_site_plant,
        name='get_super_all_site_plant',
    ),
    path('add_plant/', views.add_plant, name='add_plant'),
    path('modify_plant/', views.modify_plant, name='modify_plant'),
    url(r'^del_plant$', views.del_plant),
    url(r'^add_book$', views.add_book),
    url(r'^bookPage$', views.bookPage),
    url(r'^del_book$', views.del_book),
    url(r'^modify_book$', views.modify_book),
    url(r'^get_all_bookpage$', views.get_all_bookpage),
    url(r'^del_BookPage$', views.del_BookPage),
    url(r'^modify_bookPage$', views.modify_bookPage),
    url(r'^add_choiceQuestion$', views.add_choiceQuestion),
    url(r'^del_choiceQuestion$', views.del_choiceQuestion),
    url(r'^del_choiceQuestion_by_book$', views.del_choiceQuestion_by_book),
    url(r'^get_options$', views.get_options),
    url(r'^get_bookName$', views.get_bookName),
    url(r'^get_choiceHistory$', views.get_choiceHistory),
    # url(r'^modify_choiceQuestion$',  views.modify_choiceQuestion),
    path('book_question_num/', views.book_question_num, name='book_question_num'),
    path('book/exist/', views.book_exist, name='book_exist'),
    # path('choiceQuestion/exist/', views.choiceQuestion_exist, name='choiceQuestion_exist'),
    # 带参数写法
    path('book/<int:bookid>/bookpage/', views.bookpage, name='bookpage'),
    path('api/book/<int:bookid>/bookpage/', views.bookpage_data, name='bookpage_data'),
    path('book/<int:bookid>/bookpage/add/', views.add_bookpage, name='add_bookpage'),
    path(
        'book/<int:bookid>/oprating_record/',
        views.book_oprating_record,
        name='book_oprating_record',
    ),
    path(
        'api/book/<int:bookid>/oprating_record/',
        views.book_oprating_record_data,
        name='book_oprating_record_data',
    ),
    path(
        'TrainingBank/<int:trainingBankID>/<str:trainingBankName>/book/',
        views.book,
        name='book',
    ),
    path(
        'api/TrainingBank/<int:trainingBankID>/book/', views.book_data, name='book_data'
    ),
    path(
        'pre_issue_paper/<int:ExamPaperID>/examieed/', views.examieed, name='examieed'
    ),
    path(
        'api/pre_issue_paper/<int:ExamPaperID>/examieed/',
        views.examieed_data,
        name='examieed_data',
    ),
    path('all_exam_books/', views.get_all_exam_books, name='all_exam_books'),
    path(
        'QuestionBank/<int:questionBankID>/<str:site>/<str:plant>/<str:name>/<str:isExercised>/choiceQuestion/',
        views.choiceQuestion,
        name='choiceQuestion',
    ),
    path(
        'api/QuestionBank/<int:questionBankID>/choiceQuestion/',
        views.choiceQuestion_data,
        name='choiceQuestion_data',
    ),
    # mwj now
    path(
        'QuestionBank/<int:questionBankID>/<str:name>/<str:isExercised>/choiceHistory/',
        views.choiceHistory,
        name='choiceHistory',
    ),
    path(
        'api/QuestionBank/<int:questionBankID>/<str:name>/<str:isExercised>/choiceHistory/',
        views.choiceHistory_data,
        name='choiceHistory_data',
    ),
    path(
        'choiceQuestion/<int:choiceQuestionID>/choiceHistory/',
        views.cqHistory,
        name='cqHistory',
    ),
    path(
        'api/choiceQuestion/<int:choiceQuestionID>/choiceHistory/',
        views.cqHistory_data,
        name='cqHistory_data',
    ),
    # 培训
    url(r'^get_train_skill_type$', views.get_train_skill_type),
    url(r'^get_train_book$', views.get_train_book),
    url(r'^get_train_pages$', views.get_train_pages),
    url(r'^add_train_record$', views.add_train_record),
    url(r'^get_train_record$', views.get_train_record),
    # 考核
    url(r'^get_exam_skill_type$', views.get_exam_skill_type),
    url(r'^judge_exam_site_plant$', views.judge_exam_site_plant),
    url(r'^auto_register$', views.auto_register),
    url(r'^get_all_issue$', views.get_all_issue),
    url(r'^to_issue_paper$', views.to_issue_paper),
    url(r'^get_all_exam$', views.get_all_exam),
    url(r'^make_paper$', views.make_paper),
    url(r'^get_paper$', views.get_paper),
    url(r'^update_exam_record$', views.update_exam_record),
    url(r'^get_exam_record$', views.get_exam_record),
    path(
        'ExamedPaper/<int:examedPaperID>/<str:name>/<int:examedCount>/examedChoiceQuestion/',
        views.examedChoiceQuestion_page,
        name='examedChoiceQuestion_page',
    ),
    path(
        'api/ExamedPaper/<int:examedPaperID>/<str:name>/examedChoiceQuestion/',
        views.examedChoiceQuestion_page_data,
        name='examedChoiceQuestion_page_data',
    ),
    url(r'^get_examed_options$', views.get_examed_options),
    # 训练
    url(r'^get_practice_record$', views.get_practice_record),
    url(r'^make_practice_paper$', views.make_practice_paper),
    path(
        'get_all_practice_books/',
        views.get_all_practice_books,
        name='get_all_practice_books',
    ),
    url(r'^get_user$', views.get_user),
    # 管理员界面修改用户
    url(r'^add_user$', views.add_user),
    url(r'^get_all_user$', views.get_all_user),
    url(r'^del_user$', views.del_user),
    url(r'^modify_user$', views.modify_user),
    # 管理员界面修改技能类型
    url(r'^add_technology$', views.add_technology),
    url(r'^get_all_technology$', views.get_all_technology),
    url(r'^del_technology$', views.del_technology),
    url(r'^modify_technology$', views.modify_technology),
    # 管理员界面修改厂别语言
    # url(r'^add_plant$', views.add_plant),
    # url(r'^get_all_plant$', views.get_all_plant),
    # url(r'^del_plant$', views.del_plant),
    # url(r'^modify_plant$', views.modify_plant),
    # 管理员界面修改题库与角色
    url(r'^add_questionbank$', views.add_questionbank),
    url(r'^get_all_questionbank$', views.get_all_questionbank),
    url(r'^del_questionbank$', views.del_questionbank),
    url(r'^modify_questionbank$', views.modify_questionbank),
    # 管理员界面修改教材库与角色
    url(r'^add_trainingbank$', views.add_trainingbank),
    url(r'^get_all_trainingbank$', views.get_all_trainingbank),
    url(r'^del_trainingbank$', views.del_trainingbank),
    url(r'^modify_trainingbank$', views.modify_trainingbank),
    # 管理员界面添加NG类型
    url(r'^add_option$', views.add_option),
    url(r'^get_all_option$', views.get_all_option),
    url(r'^del_option$', views.del_option),
    url(r'^del_issue_paper$', views.del_issue_paper),
]
