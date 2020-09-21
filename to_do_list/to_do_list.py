from datetime import datetime, timedelta
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today())

    def __str__(self):
        return self.task


class OrmConnection:
    def __init__(self, db_name):
        self.engine = create_engine(f'sqlite:///{db_name}?check_same_thread=False')
        Base.metadata.create_all(self.engine)

        self.session = sessionmaker(bind=self.engine)()

    def get_session(self):
        return self.session


class ToDoList:
    def __init__(self, session):
        self.session = session
        self.methods = {'1': self._show_today_tasks,
                        '2': self._show_week_tasks,
                        '3': self._show_all_tasks,
                        '4': self._missed_task,
                        '5': self._add_task,
                        '6': self._delete_task,
                        '0': self._exit}

        self.running = True

    def menu(self):
        while self.running:
            self.show()
            user_input = input()
            self._handle_input(user_input)

    @staticmethod
    def show():
        print("1) Today's tasks")
        print("2) Week's tasks")
        print("3) All tasks")
        print("4) Missed tasks")
        print("5) Add task")
        print("6) Delete task")
        print("0) Exit")

    def _handle_input(self, user_input):
        if user_input not in self.methods.keys():
            raise KeyError(f"Action {user_input} not allowed!")

        return self.methods[user_input]()

    def _show_today_tasks(self):
        today = datetime.today()

        tasks = self.session.query(Task).filter(Task.deadline == today.date()).all()
        date = today.strftime("%d %b")

        print(f'\nToday {date}:')
        if tasks:
            for idx, task in enumerate(tasks, 1):
                print(f'{idx}. {task}')
            print()
        else:
            print('\nNothing to do!\n')

    def _show_week_tasks(self):
        today = datetime.today().date()

        week_days = []
        for i in range(7):
            days = today + timedelta(days=i)
            week_days.append(days)

        for date in week_days:
            i_date = date.strftime("%A %d %b")
            print(f'{i_date}:')
            tasks = self.session.query(Task).filter(Task.deadline == date).order_by(Task.deadline).all()
            if tasks:
                for idx, task in enumerate(tasks, 1):
                    print(f'{idx}. {task}')
                print()
            else:
                print('Nothing to do!\n')

    def _show_all_tasks(self):
        tasks = self.session.query(Task).order_by(Task.deadline).all()

        print("All tasks:")
        for idx, task in enumerate(tasks, 1):
            date = tasks[idx - 1].deadline.strftime("%d %b")
            print(f'{idx}. {task}. {date}')
        print()

    def _missed_task(self):
        today = datetime.today().date()
        tasks = self.session.query(Task).filter(Task.deadline < today).order_by(Task.deadline).all()

        print("\nMissed tasks:")
        if tasks:
            for idx, task in enumerate(tasks, 1):
                date = tasks[idx - 1].deadline.strftime("%d %b")
                print(f'{idx}. {task}. {date}')
            print()
        else:
            print("Nothing is missed!\n")

    def _delete_task(self):
        today = datetime.today().date()
        tasks = self.session.query(Task).filter(Task.deadline < today).order_by(Task.deadline).all()

        print("\nChoose the number of the task you want to delete:")
        if tasks:
            for idx, task in enumerate(tasks, 1):
                date = tasks[idx - 1].deadline.strftime("%d %b")
                print(f'{idx}. {task}. {date}')
            idx = int(input()) - 1
            self.session.delete(tasks[idx])
            self.session.commit()
            print()
        else:
            print("Nothing to delete\n")

    def _add_task(self):
        task = input('\nEnter task\n')
        deadline = [int(i) for i in input('Enter deadline\n').split("-")]

        self.session.add(Task(task=task, deadline=datetime(*deadline)))
        self.session.commit()

        print('The task has been added!\n')

    def _exit(self):
        print('\nBye!')
        self.running = False


todo_list = ToDoList(OrmConnection(db_name='todo.db').get_session())
todo_list.menu()
