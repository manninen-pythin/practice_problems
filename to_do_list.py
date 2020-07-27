from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///todo.db?check_same_thread=False')

Base = declarative_base()


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


class DisplayTasks:
    def __init__(self, choice):
        self.choice = choice
        if self.choice == '1':
            DisplayTasks.today(self)
        elif self.choice == '2':
            DisplayTasks.week(self)
        elif self.choice == '3':
            DisplayTasks.all(self)
        elif self.choice == '4':
            DisplayTasks.missed(self)

    def today(self):
        today = datetime.today().date()
        rows = session.query(Task).filter(Task.deadline == today).all()
        print(f"Today {today.day} {today.strftime('%b')}:")
        if not rows:
            print('Nothing to do!\n')
        else:
            for row in rows:
                print(row)

    def week(self):
        today = datetime.today()
        i = 0
        days_of_week = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday',
                        4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
        while i != 7:
            day = today + timedelta(days=i)
            print(f"{days_of_week.get(day.weekday())} {day.day} {day.strftime('%b')}")
            rows = session.query(Task).filter(Task.deadline == day.date()).all()
            if not rows:
                print('Nothing to do!\n')
            else:
                j = 1
                for row in rows:
                    print(f'{j}. {row}')
                    j += 1
                print()
            i += 1

    def all(self):
        rows = session.query(Task).order_by(Task.deadline).all()
        dates = session.query(Task.deadline).order_by(Task.deadline).all()
        if not rows:
            print('No tasks!\n')
        else:
            print('All tasks:')
            i = 1
            j = 0
            for row in rows:
                date = dates[j][0]
                print(f"{i}. {row}. {date.strftime('%#d %b')}")
                i += 1
                j += 1
            print()

    def missed(self):
        today = datetime.today()
        rows = session.query(Task).filter(Task.deadline
                                          < today.date()).order_by(Task.deadline).all()
        dates = session.query(Task.deadline).filter(Task.deadline
                                                    < today.date()).order_by(Task.deadline).all()
        if not rows:
            print('Nothing is missed!\n')
        else:
            print('Missed tasks:')
            i = 1
            j = 0
            for row in rows:
                date = dates[j][0]
                print(f"{i}. {row}. {date.strftime('%#d %b')}")
                i += 1
                j += 1
            print()


class EnterTask:
    def __init__(self):
        self.new_task = input('Enter task: \n')
        self.deadline = input('Enter deadline: \n')
        EnterTask.add_task(self)

    def add_task(self):
        new_row = Task(task=self.new_task,
                       deadline=datetime.strptime(self.deadline, '%Y-%m-%d').date())
        session.add(new_row)
        session.commit()
        print('The task has been added!\n')


class DeleteTasks:
    def __init__(self):
        self.rows = session.query(Task).order_by(Task.deadline).all()
        self.dates = session.query(Task.deadline).order_by(Task.deadline).all()
        self.IDs = session.query(Task.id).order_by(Task.deadline).all()
        if not self.rows:
            print('Nothing to delete!\n')
        else:
            print('Chose the number of the task you want to delete:')
            i = 1
            j = 0
            for row in self.rows:
                date = self.dates[j][0]
                print(f"{i}. {row}. {date.strftime('%#d %b')}")
                i += 1
                j += 1
            choice = int(input()) - 1
            self.task = self.IDs[choice][0]
        DeleteTasks.delete_task(self)

    def delete_task(self):
        session.query(Task).filter(Task.id == self.task).delete()
        session.commit()

def menu():
    print('1) Today\'s tasks\n'
          '2) Week\'s tasks\n'
          '3) All tasks\n'
          '4) Missed tasks\n'
          '5) Add task\n'
          '6) Delete Task\n'
          '0) Exit')
    select = input()
    print()
    if select == '0':
        print('Bye!')
        quit()
    DisplayTasks(select)
    if select == '5':
        EnterTask()
    elif select == '6':
        DeleteTasks()
    menu()


menu()
