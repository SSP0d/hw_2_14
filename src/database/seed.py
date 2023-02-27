from random import randint

from faker import Faker
from sqlalchemy.orm import Session

from src.database.connect import SessionLocal
from src.database.models import Contact, User
from src.schemas import ContactModel, UserModel

fake = Faker()
database = SessionLocal()


def create_contacts(body: ContactModel, db: Session = database):
    contact = Contact(**body.dict())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


def create_users(body: UserModel, db: Session = database):
    user = User(**body.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


if __name__ == '__main__':

    for _ in range(10):
        random_user = UserModel(
            username=fake.first_name(),
            email=fake.email(),
            password=fake.password()
        )
        create_users(body=random_user, db=database)

    for _ in range(100):
        random_contact = ContactModel(
            name=fake.first_name(),
            surname=fake.last_name(),
            email=fake.email(),
            phone=fake.msisdn(),
            birthday=fake.date(),
            additionally=fake.paragraph(nb_sentences=2),
            user_id=randint(1, 10)
        )
        create_contacts(body=random_contact, db=database)
