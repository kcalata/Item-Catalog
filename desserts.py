from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User

engine = create_engine('sqlite:///itemcatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
user1 = User(name='Yummy Desserts', email='yummydesserts@gmail.com', picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png'')

session.add(user1)
session.commit()

category1 = Category(user_id=1, name='Cakes')

session.add(category1)
session.commit()

item1 = Item(user_id=1, name='Red Velvet Cake', description='Red velvet cake is traditionally a red, red-brown, mahogany, maroon, crimson or scarlet colored chocolate layer cake, layered with white cream cheese or ermine icing. Common modern red velvet cake is made with red dye; the red color was originally due to non-Dutched, anthocyanin-rich cocoa.', category=category1)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name='Molten Chocolate Cake', description='A petit gateau, or chocolate fondant, is a dessert composed of a small chocolate cake with crunchy rind and mellow filling that is conventionally served hot with vanilla ice cream on a plate. In French, the terms for the chocolate cake are "gateau fondant au chocolat" or simply "fondant au chocolat".', category=category1)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name='Carrot Cake', description='Carrot cake is a cake that contains carrots mixed into the batter.', category=category1)

session.add(item3)
session.commit()

category2 = Category(user_id=1, name='Cookies')

session.add(category2)
session.commit()

item1 = Item(user_id=1, name='Chocolate Chip Cookie', description='A chocolate chip cookie is a drop cookie that originated in the United States and features chocolate chips or chocolate morsels as its distinguishing ingredient. Circa 1938, Ruth Graves Wakefield added chopped up bits from a Nestle semi-sweet chocolate bar into a cookie.', category=category2)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name='Peanut Butter Cookie', description='A peanut butter cookie is a type of cookie that is distinguished for having peanut butter as a principal ingredient. The cookie generally originated in the United States, its development dating back to the 1910s. If crunchy peanut butter is used, the resulting cookie may contain peanut fragments.', category=category2)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name='Shortbread', description='Shortbread is a traditional Scottish biscuit usually made from one part white sugar, two parts butter, and three parts oat flour. Other ingredients like ground rice or cornflour are sometimes added to alter the texture.', category=category2)

session.add(item3)
session.commit()

category3 = Category(user_id=1, name='Doughnuts')

session.add(category3)
session.commit()

item1 = Item(user_id=1, name='Old Fashioned Doughnut', description='The old-fashioned doughnut is a variety of cake doughnut prepared in the shape of a ring with tapered edges around it. Cake doughnuts originated in the United States circa 1829. Primary ingredients in the old-fashioned doughnut include flour, sugar, eggs, sour cream or buttermilk and leavener. It is typically deep fried, may have a crunchier or crisper texture compared to other styles of cake doughnuts, and typically has cracks and pores on its surface. After being fried, it may be glazed, dusted with sugar, or served plain.', category=category3)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name='Berliner', description='A Berliner Pfannkuchen (referred to as Berliner for short) is a traditional German pastry similar to a doughnut with no central hole, made from sweet yeast dough fried in fat or oil, with a marmalade or jam filling and usually icing, powdered sugar or conventional sugar on top. They are sometimes made with chocolate, champagne, custard, mocha, or advocaat filling, or with no filling at all.', category=category3)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name='Jelly Doughnut', description="A jelly (or jam) doughnut is a doughnut filled with jelly filling. Varieties include the German Berliner, Australia, Britain and Nigeria's jam doughnuts, sufganiyot from Israel, and the jelly-filled doughnuts sold in the United States and Canada. Japanese anpan are similar to the Berliner, except they contain red bean paste. Krafne from Eastern Europe also include a jelly-filled variety. In Italy, bomboloni are popular. Austria also has a jelly doughnut known as krapfen that is typically filled with apricot jam and topped with powdered sugar. The Polish paczki is also similar to a jelly doughnut.", category=category3)

session.add(item3)
session.commit()

category4 = Category(user_id=1, name='Pastries')

session.add(category4)
session.commit()

item1 = Item(user_id=1, name='Macaron', description='A macaron or French macaroon is a sweet meringue-based confection made with egg white, icing sugar, granulated sugar, almond powder or ground almond, and food coloring. There is some variation in whether the term macaron or macaroon is used, and the related coconut macaroon is often confused with the macaron.', category=category4)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name='Croissant', description='A croissant is a buttery, flaky, viennoiserie pastry of Austrian origin, named for its historical crescent shape. Croissants and other viennoiserie are made of a layered yeast-leavened dough.', category=category4)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name='Cannoli', description='Cannoli are Italian pastries that originated on the island of Sicily and are today a staple of Sicilian cuisine as well as Italian-American cuisine. Cannoli consist of tube-shaped shells of fried pastry dough, filled with a sweet, creamy filling usually containing ricotta.', category=category4)

session.add(item3)
session.commit()

category5 = Category(user_id=1, name='Pies')

session.add(category5)
session.commit()

item1 = Item(user_id=1, name='Apple Pie', description='An apple pie or apple tart is a pie or a tart, in which the principal filling ingredient is apple. It is, on occasion, served with whipped cream or ice cream on top, or with cheddar cheese.', category=category5)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name='Sweet Potato Pie', description='Sweet potato pie is a traditional dessert, originating in the Southern United States. It is often served during the American holiday season, especially at Thanksgiving and Christmas in place of pumpkin pie, which is more traditional in other regions of the United States.', category=category5)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name='Pumpkin Pie', description='Pumpkin pie is a dessert pie with a spiced, pumpkin-based custard filling. The pumpkin is a symbol of harvest time, and pumpkin pie is often eaten during the fall and early winter. In the United States and Canada, it is usually prepared for Thanksgiving, and other occasions when pumpkin is in season.', category=category5)

session.add(item3)
session.commit()

category6 = Category(user_id=1, name='Puddings')

session.add(category6)
session.commit()

item1 = Item(user_id=1, name='Rice Pudding', description='Rice pudding is a dish made from rice mixed with water or milk and other ingredients such as cinnamon and raisins. Variants are used for either desserts or dinners. When used as a dessert, it is commonly combined with a sweetener such as sugar.', category=category6)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name='Christmas Pudding', description='Christmas pudding is a type of pudding traditionally served as part of the Christmas dinner in the UK, Ireland and in other countries where it has been brought by British immigrants.', category=category6)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name='Bread Pudding', description="Bread pudding is a bread-based dessert popular in many countries' cuisines, made with stale bread and milk or cream, generally containing eggs, a form of fat such as oil, butter or suet, and depending on whether the pudding is sweet or savory, a variety of other ingredients.", category=category6)

session.add(item3)
session.commit()


print 'added desserts!'
