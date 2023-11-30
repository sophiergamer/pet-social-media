from app import app
from models import User, Pet, AdoptionApplication, Ownership, db

User1 = User(username="John", email="<EMAIL1>", password_hash="<PASSWORD>", zipcode=123456)
User2 = User(username="Jane", email="<EMAIL2>", password_hash="<PASSWORD>", zipcode = 123456)
User3 = User(username="Mary", email="<EMAIL3>", password_hash="<PASSWORD>", zipcode=123456)
User4 = User(username="Mike", email="<EMAIL4>", password_hash="<PASSWORD>", zipcode=123456)


Pet1 = Pet(name="Doggo", photo="doggo.jpg", description="This is a dog", size="Medium", age=2, gender="Male", type="Dog", is_adoptable=True)
Pet2 = Pet(name="Puppy", photo="puppy.jpg", description="This is a puppy", size="Medium", age=4, gender="Male", type="Dog", is_adoptable=False)
Pet3 = Pet(name="Kitty", photo="kitty.jpg", description="This is a kitty", size="Medium", age=1, gender="Male", type="Cat", is_adoptable=False)
Pet4 = Pet(name="Bird", photo="bird.jpg", description="This is a bird", size="Medium", age=1, gender="Male", type="Bird", is_adoptable=False)
Pet5 = Pet(name="Fish", photo="fish.jpg", description="This is a fish", size="Medium", age=3, gender="Male", type="Fish", is_adoptable=False)
Pet6 = Pet(name="Cat", photo="cat.jpg", description="This is a cat", size="Medium", age=6, gender="Male", type="Cat", is_adoptable=False)
Pet7 = Pet(name="Dog", photo="dog.jpg", description="This is a dog", size="Medium", age=2, gender="Male", type="Dog", is_adoptable=False)

def create_pets():
    all_pets = [Pet1, Pet2, Pet3, Pet4, Pet5, Pet6, Pet7]
    return all_pets

def create_users():
    all_users = [User1, User2, User3, User4]
    return all_users

def create_ownerships():
    all_ownerships = [Ownership(pet_id=1, user_id=1), Ownership(pet_id=3, user_id=2), Ownership(pet_id=4, user_id=3), Ownership(pet_id=4, user_id=4), Ownership(pet_id=6, user_id=2), Ownership(pet_id=7, user_id=3)]
    return all_ownerships

def test_create_adoption_application():
    new_adoption_application = AdoptionApplication(
        pet_id=1,
        user_id=1,
        HasHadPetBefore=False,
        TypeOfHousing = 'House',
    )
    return new_adoption_application

with app.app_context():
    # Remove all existing data from the database.
    Pet.query.delete()
    User.query.delete()
    Ownership.query.delete()
    AdoptionApplication.query.delete()
    db.session.commit()

    # Start creating the database.
    pets = create_pets()
    users = create_users()
    ownerships = create_ownerships()
    adoption_applications = test_create_adoption_application()

    # Add all to the database.
    db.session.add_all(ownerships)
    db.session.add_all(pets)
    db.session.add_all(users)
    db.session.add(adoption_applications)

    db.session.commit()