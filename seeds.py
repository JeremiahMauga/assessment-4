from craigs_list_application.models import Category, Post

blades = Category(category_name='Blades', category_description='Double-edged or single-edged, slicing is all the same!')
blades.save()

bludgeons = Category(category_name='Bludgeon', category_description='Blunt force trauma at it`s finest!')
bludgeons.save()

post_1 = Post(category_type=blades, post_title="Zwiehander for cheap!", post_content="A two-handed doubled edged sword, for taking out those pesky horse legs!")
post_1.save()

post_2 = Post(category_type=blades, post_title="Longsword-GOOD CONDITION", post_content="Classic longsword. Only used once. Great condition with original hilt and leather. Only serious inquiries please.")
post_2.save()

post_3 = Post(category_type=bludgeons, post_title="Maul for Sale", post_content="Extremely dense and heavy maul. Probably about 400lbs, maybe. Selling to buy a larger maul.")
post_3.save()

post_4 = Post(category_type=bludgeons, post_title="Legendary Mace", post_content="Expensive and definitely not a scam! Become the hero you always wanted to be! NO REFUNDS.")
post_4.save()




