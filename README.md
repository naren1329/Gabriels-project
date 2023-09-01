# Gabriels-project
# Gabriels-project

**STEPS TO RUN A PROJECT**

_Step-1_
Download the project as ZIP file and extract and open VS-CODE and open downloaded project folder.
find SQL QURIES.docx from the folder and paste quries in MYSQL-Workbench and execute(for database,table creation and inserting records)

(FYI)
i have used longblob data type for both images and link path** / you can also use nvarchar data type for specifying as link of image  
For Mysql:
  **Save required Project Images in (C:\ProgramData\MySQL\MySQL Server 8.0\Uploads) path.
  *If doubts in Image insertion (refer SQL QURIES.docx)

_STEP-2_
IN VS Code,
Open project folder, in settings.py:
*In Database - 'default': {'ENGINE': 'django.db.backends.mysql',
                              'NAME': ' <your DB_name>',
                              'USER':'<your username> ',
                              'PASSWORD':'<your password> ',
                              'HOST':'<'your localhost'> ',
                              'PORT':'<your portnumber>'}
 In Command Promt:
  *pip install pymysql (for accepting an Database datas from existing table)  

_STEP -3_
*py manage.py runserver - To run a project  

