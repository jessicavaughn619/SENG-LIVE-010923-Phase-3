
# 3. ✅ CRUD Practice

# To run the file, run `python3 debug.py` in the app directory

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import (Base, Pet)

if __name__ == '__main__':
    
    #3.1 ✅ Uncomment below to create the engine.
    engine = create_engine('sqlite:///pet_app.db')
    Base.metadata.create_all(engine)
    
    #3.2 ✅ Uncomment below to create sessions and bind to the engine.
    Session = sessionmaker(bind=engine)
    session = Session()

    #3.3 ✅ Create
    
        # Create a pet and save it to the database with 'session.add' and 'session.commit'

    # Olivia = Pet(name="Olivia", species="dog", breed="terrier", temperament="stiff", owner_id=1)
    # session.add(Olivia)
    # session.commit()

        # Create multiple pets and bulk save them with  'session.bulk_save_objects' and 'session.commit'

    # Molly = Pet(name="Molly", species="dog", breed="chihuahua", temperament="flexible", owner_id=1)
    # Brandy = Pet(name="Brandy", species="dog", breed="husky", temperament="playful", owner_id=2)
    # Bruce = Pet(name="Bruce", species="cat", breed="domestic shorthair", temperament="lovable", owner_id=1)
    # session.bulk_save_objects([Molly, Brandy, Bruce])
    # session.commit()


            # Note: Bulk save will not contain the id

        # Verify results by checking the db 

    #3.4 ✅ Read
        
        # Retrieve all pets with session.query

    # all_pets = session.query(Pet)
    # print([pet for pet in all_pets])

        # Print the pets 

        # Get all of the pet names and print them with session.query
    
    # names = session.query(Pet.name)
    # print([name for name in names])

# OR

    # print([name for name in session.query(Pet.name)])

        # Get all the pet names and print them in order with session.query and order_by
    
    # ordered_names = [name for name in session.query(Pet.name).order_by(Pet.name)]
    # print(ordered_names)

        # Get the first pet with session.query and first
    
    # first_pet = session.query(Pet).first()
    # print(first_pet)

        # Filter pet by temperament with session.query and filter 
    
    # filtered_pets = session.query(Pet).filter(Pet.temperament.like('%playful%'))
    # print([record for record in filtered_pets])

    #3.5 ✅ Update 
        
        # Update the first pet's name and print the updated pet info

    # first = session.query(Pet).first()
    # first.name = "Boots"
    # session.commit()

        # Update all the pets' temperaments to 'cool' and print the pets 
    
    # all_pets = session.query(Pet)
    # all_pets.update({Pet.temperament: 'cool'})
    # session.commit()
    # print([pet for pet in all_pets])

    #3.6 ✅ Delete
        
        # Delete one item by querying the first pet, deleting it and committing
    # first_pet = session.query(Pet).first()
    # first_pet.delete(first_pet)
    # session.commit()

        # Delete all the pets with session.query and .delete
    
    # pets = session.query(Pet)
    # pets.delete()
    # session.commit()
  
    # optional Break point for debugging and testing
    import ipdb; ipdb.set_trace()