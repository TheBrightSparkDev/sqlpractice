from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# creating the variables

class Programmer(base):
    __tablename__ = "Programmer"
    Id = Column(Integer, primary_key=True)
    First_name = Column(String)
    Last_name = Column(String)
    Gender = Column(String)
    Nationality = Column(String)
    Famous_for = Column(String)

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# ada_lovelace = Programmer(
#     First_name="Ada",
#     Last_name="Lovelace",
#     Gender="F",
#     Nationality="British",
#     Famous_for="First programmer"
# )

alan_turing = Programmer(
    First_name="Alan",
    Last_name="Turing",
    Gender="M",
    Nationality="British",
    Famous_for="Modern Computing"
)

grace_hopper = Programmer(
    First_name="Grace",
    Last_name="Hopper",
    Gender="F",
    Nationality="American",
    Famous_for="COBOL language"
)

margaret_hamilton = Programmer(
    First_name="Margaret",
    Last_name="Hamilton",
    Gender="F",
    Nationality="American",
    Famous_for="Apollo 11"
)

bill_gates = Programmer(
    First_name="Bill",
    Last_name="Gates",
    Gender="M",
    Nationality="American",
    Famous_for="Microsoft"
)

tim_berners_lee = Programmer(
    First_name="Tim",
    Last_name="Berners-Lee",
    Gender="M",
    Nationality="British",
    Famous_for="World Wide Web"
)

daniel_harries = Programmer(
    First_name="Daniel",
    Last_name="Harries",
    Gender="M",
    Nationality="British",
    Famous_for="Nothing"
)
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(daniel_harries)
# Programmers = session.query(Programmer)

# programmer = session.query(Programmer).filter_by(Id=11).first()
# programmer.Famous_for = "loudest fart"

# People = session.query(Programmer)
# for person in People:
#     if person.Gender == "F":
#         person.Gender = "Female"
#     elif person.Gender == "M":
#         person.Gender = "Male"
#     else:
#         Print("Gender not defined")
#     session.commit()

# deleting a single record
# fname = input("Enter the first name:")
# lname = input("Enter the last name:")
# programmer = session.query(Programmer).filter_by(
#     First_name=fname,
#     Last_name=lname).first()
# defensive programming
# if Programmer is not None:
#     print("Programmer found: " + programmer.First_name + " " + programmer.Last_name)
#     confirmation = input("Are you sure you want to remove this? y/n:")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted")
#     else:
#         print("Programmer not deleted")
# else:
#     print("No records found")

# delete multiple/all records
# programmers = session.query(Programmer)
# for programmer in programmers:
#     session.delete(programmer)
#     session.commit()

programmers = session.query(Programmer)
for Programmer in programmers:
    print(
        Programmer.Id,
        Programmer.First_name,
        Programmer.Last_name,
        Programmer.Gender,
        Programmer.Nationality,
        Programmer.Famous_for,
        sep=(" | ")
        )
