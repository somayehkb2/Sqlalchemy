from sqlalchemy import create_engine, Column, INTEGER, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine('sqlite:///StudentData_Tap.db', echo=False)
engine.connect()


Base = declarative_base()


class Student(Base):
    __tablename__ = 'studentinfo'

    id = Column(INTEGER, primary_key=True)
    name = Column(String, nullable=False)
    score = Column(Float)


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
sessionLocal = Session()

###############################################

def create_student(name, score):
    student = Student(name=name, score=score)
    sessionLocal.add(student)
    sessionLocal.commit()
    print(f"دانش‌آموز اضافه شد: {student.name} - نمره: {student.score} (id={student.id})")


def read_students():
    students = sessionLocal.query(Student).all()
    if not students:
        print("هیچ دانش‌آموزی وجود ندارد.")
        return
    print("\n📋 لیست دانش‌آموزان:")
    for s in students:
        print(f"  id={s.id} | name={s.name} | score={s.score}")
    print()


def update_student(student_id, new_name=None, new_score=None):
    student = sessionLocal.query(Student).filter_by(id=student_id).first()
    if student is None:
        print(f" دانش‌آموزی با id={student_id} پیدا نشد.")
        return
    if new_name is not None:
        student.name = new_name
    if new_score is not None:
        student.score = new_score
    sessionLocal.commit()
    print(f"دانش‌آموز id={student_id} به‌روزرسانی شد , name={student.name}, score={student.score}")


def delete_student(student_id):
    student = sessionLocal.query(Student).filter_by(id=student_id).first()
    if student is None:
        print(f"دانش‌آموزی با id={student_id} پیدا نشد.")
        return
    sessionLocal.delete(student)
    sessionLocal.commit()
    print(f"دانش‌آموز id={student_id} حذف شد.")

###############################################

if __name__ == "__main__":
    
    create_student('Ali', 18.5)
    create_student('Somayeh', 19.0)
    create_student('Zahra', 15.75)
    create_student('Arman', 18.25)
    create_student('Reza', 18.0)
    create_student('Sara', 17.5)
    create_student('Omid', 16.0)

    
    read_students()

    
    update_student(1, new_name='Ali Salehi', new_score=20.0)
    read_students()

    
    delete_student(2)
    read_students()


sessionLocal.close()