import os
import time




############
#  Globals #
############
wrong_tries=0

user_name1=""" __      __  ___   _       ___    ___    __  __   ___       __  __   ___        ___     _     _   _   ___ 
 \ \    / / | __| | |     / __|  / _ \  |  \/  | | __|     |  \/  | | _ \      / __|   /_\   | | | | | _ \ 
  \ \/\/ /  | _|  | |__  | (__  | (_) | | |\/| | | _|      | |\/| | |   /  _  | (_ |  / _ \  | |_| | |   /
   \_/\_/   |___| |____|  \___|  \___/  |_|  |_| |___|     |_|  |_| |_|_\ (_)  \___| /_/ \_\  \___/  |_|_\ """

user_name2="""
██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    ███╗   ███╗██████╗     ██████╗  █████╗ ██╗   ██╗██████╗ 
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    ████╗ ████║██╔══██╗   ██╔════╝ ██╔══██╗██║   ██║██╔══██╗
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗      ██╔████╔██║██████╔╝   ██║  ███╗███████║██║   ██║██████╔╝
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝      ██║╚██╔╝██║██╔══██╗   ██║   ██║██╔══██║██║   ██║██╔══██╗
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗    ██║ ╚═╝ ██║██║  ██║██╗╚██████╔╝██║  ██║╚██████╔╝██║  ██║
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝
                                                                                                                          """
print(user_name2)
print()
print("""************* Starting HelpBro Service *************""")
time.sleep(3)

def run_server():
    try:
        os.system(f"echo starting server protocol")
        os.system(f"python manage.py runserver")
        os.system(f"echo ===========================================")
    except:
        os.system("echo couldn't fullflill ur request. see error details for more info.")

def create_django_project():
   param1 = input("enter your project name: ")
   os.system(f"echo Building your django project: {param1}.")
   try:
       os.system(f"django-admin startproject {param1}")
       os.system(f"echo Successfully built your project: {param1}.")
       os.system(f"echo ===========================================")
   except:
       os.system("echo couldn't fullflill ur request.")


def create_django_app():
    param1 = input("enter your app name: ")
    os.system(f"echo Building your django app : {param1}.")
    try:
        os.system(f"python manage.py startapp {param1}")
        os.system(f"echo Successfully built your django app: {param1}.")
        os.system(f"echo ===========================================")
    except:
        os.system("echo couldn't fullflill ur request.")



def make_migrations():
    try:
        os.system(f"echo making migrations and pushing updates")
        os.system(f"python manage.py makemigrations")
        os.system(f"echo ===========================================")
    except:
        os.system("echo couldn't fullflill ur request. see error details for more info.")

def migrate():
    try:
        os.system(f"echo Migrating....")
        os.system(f"python manage.py migrate")
        os.system(f"echo ===========================================")
    except:
        os.system("echo couldn't fullflill ur request. see error details for more info.")



def create_a_super_user():
    try:
        os.system(f"")
        os.system(f"echo Careful, you're going to create a super_user")
        os.system(f"python manage.py createsuperuser")
        os.system(f"echo ===========================================")
    except:
        os.system("echo couldn't fullflill ur request. see error details for more info.")






def perform_choice_operation(choice):
    global wrong_tries
    if(choice==1):
        run_server()
    elif(choice==2):
        create_django_project()
    elif(choice==3):
        create_django_app()
    elif(choice==4):
        make_migrations()
    elif(choice==5):
        migrate()
    elif(choice==6):
        create_a_super_user()
    elif(choice==0):
        exit()
    else:
        wrong_tries=wrong_tries+1
        if(wrong_tries%5==0):
            print("dude, take a coffee break, u've entered a wrong choice again T_T, you've been batteling for hrs ig.")
        else:
            print("Wrong pick! for coffee's sake enter a valid choice Dev.")




while True:
    print("")
    print("1) Start Server")
    print("2) Make a Django-Project")
    print("3) Make a django-app")
    print("4) Make Migrations files ready for migration.")
    print("5) Migrate/Sync Databses. :)")
    print("6) Create a Super-User")
    print("7) Create a user")
    print("0) Exit")
    print("")
    try:
        choice=int(input("wish: "))
        perform_choice_operation(choice)
    except (ValueError):
        print(f"ummmm, i think you've entered a string, you can stick to numbers as choices!")
        print(f"my developer didn't really want devs to type a lot, they do that a lot already.")
        print(f"save yourself some time, use numbers! -snehc.")























































###########################################################
#                                                         #
# baby lang version needs to be added to the below code.  #
#                                                         #
###########################################################

########################uncomment from here.
# import os
#
#
# #os.system()
#
#
#
# def create_django_project():
#     param1 = input("enter your project name: ")
#     os.system(f"echo Building your django project: {param1}.")
#     try:
#         os.system(f"django-admin startproject {param1}")
#         os.system(f"echo Successfully built your project: {param1}.")
#         os.system(f"echo ===========================================")
#     except:
#         os.system("echo couldn't fullflill ur request.")
#
#
# create_a_django_project_commands={
#     "create a django project":"django-admin startproject",
#     "build a django project":"django-admin startproject",
#     "make a django project":"django-admin startproject",
#     "create django project":"django-admin startproject",
# }
#
#
#
#
#
# def create_django_app():
#     param1 = input("enter your app name: ")
#     os.system(f"echo Building your django app : {param1}.")
#     try:
#         os.system(f"python manage.py startapp {param1}")
#         os.system(f"echo Successfully built your django app: {param1}.")
#         os.system(f"echo ===========================================")
#     except:
#         os.system("echo couldn't fullflill ur request.")
#
#
# create_a_django_app_commands={
#     "create a django app":"python manage.py startapp",
#     "build a django app":"python manage.py startapp",
#     "make a django app":"python manage.py startapp",
#     "create django app":"python manage.py startapp",
# }
#
#
#
#
#
#
#
# def run_server():
#     try:
#         os.system(f"echo starting server protocol")
#         os.system(f"python manage.py runserver")
#         os.system(f"echo ===========================================")
#     except:
#         os.system("echo couldn't fullflill ur request. see error details for more info.")
#
#
# run_server_commands={
#     "start server":"python manage.py runserver",
#     "start server":"python manage.py runserver",
#     "run server":"python manage.py runserver",
#     "runserver":"python manage.py runserver",
#     "host project":"python manage.py runserver",
#     "go live":"python manage.py runserver",
#     "host live":"python manage.py runserver",
#     "golive":"python manage.py runserver",
#     "hostlive":"python manage.py runserver",
#     "live server":"python manage.py runserver",
#     "host server":"python manage.py runserver",
#     "liveserver":"python manage.py runserver",
#     "hostserver":"python manage.py runserver",
#     "start django server":"python manage.py runserver",
# }
#
#
#
#
#
#
#
#
#
# def make_migrations():
#     try:
#         os.system(f"echo making migrations and pushing updates")
#         os.system(f"python manage.py makemigrations")
#         os.system(f"echo ===========================================")
#     except:
#         os.system("echo couldn't fullflill ur request. see error details for more info.")
#
#
# make_migrations_commands={
#
#     "make migrations":"python manage.py make migrations",
#     "make migration":"python manage.py make migrations",
#     "make_migrations":"python manage.py make migrations",
#     "update database":"python manage.py make migrations",
#     "update_database":"python manage.py make migrations",
#     "sync database":"python manage.py make migrations",
#     "sync_database":"python manage.py make migrations",
#     "sync databases": "python manage.py make migrations",
#     "sync_databases": "python manage.py make migrations",
#     "update database schema": "python manage.py make migrations",
#     "update_database_schema": "python manage.py make migrations",
#     "push updates": "python manage.py make migrations",
#     "push_updates": "python manage.py make migrations",
#     "update models": "python manage.py make migrations",
#     "update_models": "python manage.py make migrations",
# }
#
#
#
#
#
#
#
#
#
#
# all_commands=[create_a_django_project_commands,create_a_django_app_commands,run_server_commands,make_migrations_commands]
#
#
# input_command=input("enter helpro command: ")
#
# for commands in all_commands:
#     for command in commands:
#         if(command==input_command):
#             if(commands[input_command]=="django-admin startproject"):
#                 create_django_project()
#             if (commands[input_command] == "python manage.py startapp"):
#                 create_django_app()
#             if (commands[input_command] == "python manage.py runserver"):
#                 #print(commands[input_command])
#                 run_server()
#
#             if (commands[input_command] == "python manage.py make migrations"):
#                 #print(commands[input_command])
#                 make_migrations()
#
#
#
#end of comments of the old code.