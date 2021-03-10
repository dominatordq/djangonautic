- In the Django Tutorial folder in a command line on Windows, run the command:
  djangonautic\Scripts\activate.bat.
  This will run Django/Python in a virtual environment
- Run command:
  py -m pip install Django (if needed)
- jangonautic is the project folder
- To run server, cd into jangonautic and run command:
  python manage.py runserver
- To create a new app within the app, run command:
  python manage.py startapp <app name here>
- To migrate files, cd to jangonautic and run command:
  python manage.py migrate
- To create custom migration file, in jangonautic run command:
  python manage.py makemigrations
- To open an interactive shell, run command:
  python manage.py shell
  - To interact with a model or database in the shell, type:
    ex) from articles.models import Article
  - To see all rows/objects in the table, type:
    Article.objects.all()
  - Or just a specific object:
    Article.objects.all()[n]
  - To create a new article, type:
    article = Article()
  - To edit variables in this object, type:
    article.<variable name> = "..."
  - To save this object to the database, type:
    article.save()
