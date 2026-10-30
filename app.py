from sqlalchemy import create_engine, Column, INTEGER, Float, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///StudentData.db', echo=True)
engine.connect()

Base = declarative_base()

class Student(Base):
    __tablename__ = 'studentinfo'

    id = Column(INTEGER, primary_key=True)
    name = Column(String, nullable=False)
    score = Column(Float)


Base.metadata.create_all(engine)
###################################################

session = sessionmaker(bind=engine)
sessionlocal = session()
# ###################################################

# stud1 = Student(name='Ali', score=18.5)
# stud2 = Student(name='Somayeh', score=19.0)
# stud3 = Student(name='Zahra', score=15.75)
# stud4 = Student(name='Arman', score=18.25)
# stud5 = Student(name='Reza', score=18.0)
# stud6 = Student(name='Sara', score=17.5)
# stud7 = Student(name='Omid', score=16.0)

# sessionlocal.add_all([stud1, stud2, stud3, stud4, stud5, stud6, stud7])
# sessionlocal.commit()
####################################################

# students_obj = sessionlocal.query(Student).all()   # list of student object
# for item in students_obj:
#     print(item.id)
#     print(item.name)
#     print(item.score)
#     print('--'*30)

######################################################

# stud1 = sessionlocal.query(Student).filter_by(id = 1).first()   # object
# print(stud1.name)
# print(stud1.score)

################################

# stud_sara = sessionlocal.query(Student).filter_by(name = 'Sara').all()
# for item in stud_sara:
#     print(item.id)
#     print(item.name)
#     print(item.score)
#     print('--'*30)

##############################################

# stud_temp = sessionlocal.query(Student).filter(Student.score > 17).all()
# for item in stud_temp:
#     print(item.name)
#     print(item.score)
#     print('--'*30)

#########################

# stud_temp = sessionlocal.query(Student).filter(Student.name.like('S%')).all()
# for item in stud_temp:
#     print(item.name)
#     print(item.score)
#     print('--'*30)

#######################################################

# stud_temp = sessionlocal.query(Student).filter(Student.name.like('Ali%')).first()

# stud_temp.name = 'Ali Akbari'
# stud_temp.score = 20.0
# sessionlocal.commit()

#######################################################

stud_temp = sessionlocal.query(Student).filter_by(id = 2).first()

if stud_temp != None:
    sessionlocal.delete(stud_temp)
    sessionlocal.commit()