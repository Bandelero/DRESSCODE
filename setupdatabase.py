from app import db,data_import

db.create_all()

user1 = data_import('abc@gmail.com', 'Test', 'Test2')
user2 = data_import('def@gmail.com', 'Test3', 'Test4')

print(user1.id)
print(user2.id)

db.session.add_all([user1,user2])

db.session.commit()

print(user1.id)
print(user2.id)