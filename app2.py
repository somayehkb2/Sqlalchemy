from sqlalchemy import create_engine, Column, INTEGER, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine('sqlite:///StudentCourse2.db', echo=False)
engine.connect()

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(String)

  
    courses = relationship('Course', back_populates='student')


class Course(Base):
    __tablename__ = 'courses'

    id = Column(INTEGER, primary_key=True)
    title = Column(String)
    unit = Column(INTEGER)
    student_id = Column(INTEGER, ForeignKey('students.id'))

   
    student = relationship('Student', back_populates='courses')

Base.metadata.create_all(engine)
#############################################

Session = sessionmaker(bind=engine)
sessionLocal = Session()
#############################################

# ---------- افزودن داده‌های نمونه ----------
# student1 = Student(name='Sara Zamani')
# student2 = Student(name='Nima Akbari')
# sessionLocal.add_all([student1, student2])
# sessionLocal.commit()

# course1 = Course(id=1, title='Python', unit=3, student_id=1)
# course2 = Course(id=2, title='Database', unit=4, student_id=1)
# course3 = Course(id=3, title='Network', unit=3, student_id=2)
# sessionLocal.add_all([course1, course2, course3])
# sessionLocal.commit()

#############################################


student1 = sessionLocal.query(Student).filter_by(id=1).first()

print(f"Student: {student1.name}")
for course in student1.courses:
    print(course.title, '-', course.unit, 'units')
    print('--' * 30)

# #############################################


course1 = sessionLocal.query(Course).filter_by(id=1).first()

print(f"Course: {course1.title}")
print("Student:", course1.student.name)