import mysql.connector as mysql

connection = mysql.connect(host='localhost', user='root', database='mmorpg_db', password='caca12j')

cursor = connection.cursor()

query = "SELECT * FROM users"
cursor.execute(query)
results = cursor.fetchall()

cursor.execute(
    "INSERT INTO users(user_id, name, email, password, registry_date, role) VALUES(%s, %s, %s, %s, %s, %s)",
    (1, "Erik", "erik@uniat.com", "ola", "2024-12-10", "admin")
)
connection.commit()

def login(cursor):
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    query = "SELECT user_id, email, role FROM users WHERE email = %s AND password = %s"
    cursor.execute(query, (email, password))
    result = cursor.fetchone()
    if result:
        print(f"Login successful! Welcome {email}.")
        return result  # Returns user_id, email, and role
    else:
        print("Login failed. Please try again.")
        return None

# CRUD para la tabla users
def create_user(connection, cursor):
    name = input("Enter your name: \n")
    email = input("Enter your email: \n")
    password = input("Enter your password: \n")
    registry_date = input("Enter the registry date (YYYY-MM-DD): \n")

    query = "INSERT INTO users(name, email, password, registry_date) VALUES(%s, %s, %s, %s)"
    cursor.execute(query, (name, email, password, registry_date))
    connection.commit()
    print("User created successfully.")

def read_users(cursor):
    query = "SELECT * FROM users"
    cursor.execute(query)
    results = cursor.fetchall()
    print("Users:")
    for row in results:
        print(row)

def update_user(connection, cursor):
    user_id = int(input("Enter the user ID to update: \n"))
    name = input("Enter the new name (leave blank to skip): \n") or None
    email = input("Enter the new email (leave blank to skip): \n") or None
    password = input("Enter the new password (leave blank to skip): \n") or None

    fields = []
    values = []
    if name:
        fields.append("name = %s")
        values.append(name)
    if email:
        fields.append("email = %s")
        values.append(email)
    if password:
        fields.append("password = %s")
        values.append(password)

    if fields:
        query = f"UPDATE users SET {', '.join(fields)} WHERE user_id = %s"
        values.append(user_id)
        cursor.execute(query, values)
        connection.commit()
        print("User updated successfully.")

def delete_user(connection, cursor):
    user_id = int(input("Enter the user ID to delete: \n"))
    query = "DELETE FROM users WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    connection.commit()
    print("User deleted successfully.")

# CRUD para la tabla characters
def create_character(connection, cursor):
    name = input("Enter the character's name: \n")
    level = input("Enter the character's level: \n") or "1"
    experience = input("Enter the character's experience points: \n") or "0"
    race = input("Enter the character's race: \n")
    class_type = input("Enter the character's class: \n")
    user_id = int(input("Enter the user ID to associate with this character: \n"))

    query = "INSERT INTO characters(name, level, experience, race, class, user_id) VALUES(%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (name, level, experience, race, class_type, user_id))
    connection.commit()
    print("Character created successfully.")

def read_characters(cursor):
    query = "SELECT * FROM characters"
    cursor.execute(query)
    results = cursor.fetchall()
    print("Characters:")
    for row in results:
        print(row)

def update_character(connection, cursor):
    character_id = int(input("Enter the character ID to update: \n"))
    name = input("Enter the new character name (leave blank to skip): \n") or None
    level = input("Enter the new level (leave blank to skip): \n") or None
    experience = input("Enter the new experience points (leave blank to skip): \n") or None
    race = input("Enter the new race (leave blank to skip): \n") or None
    class_type = input("Enter the new class (leave blank to skip): \n") or None

    fields = []
    values = []
    if name:
        fields.append("name = %s")
        values.append(name)
    if level:
        fields.append("level = %s")
        values.append(int(level))
    if experience:
        fields.append("experience = %s")
        values.append(int(experience))
    if race:
        fields.append("race = %s")
        values.append(race)
    if class_type:
        fields.append("class = %s")
        values.append(class_type)

    if fields:
        query = f"UPDATE characters SET {', '.join(fields)} WHERE character_id = %s"
        values.append(character_id)
        cursor.execute(query, values)
        connection.commit()
        print("Character updated successfully.")

def delete_character(connection, cursor):
    character_id = int(input("Enter the character ID to delete: \n"))
    query = "DELETE FROM characters WHERE character_id = %s"
    cursor.execute(query, (character_id,))
    connection.commit()
    print("Character deleted successfully.")

# CRUD para la tabla inventory
def create_inventory_item(connection, cursor):
    character_id = int(input("Enter the character ID: \n"))
    item_id = int(input("Enter the item ID: \n"))
    quantity = int(input("Enter the quantity of the item: \n"))
    obtained_date = input("Enter the obtained date (YYYY-MM-DD): \n")

    query = "INSERT INTO inventory(character_id, item_id, quantity, obtained_date) VALUES(%s, %s, %s, %s)"
    cursor.execute(query, (character_id, item_id, quantity, obtained_date))
    connection.commit()
    print("Inventory item created successfully.")

def read_inventory(cursor):
    query = "SELECT * FROM inventory"
    cursor.execute(query)
    results = cursor.fetchall()
    print("Inventory:")
    for row in results:
        print(row)

def update_inventory_item(connection, cursor):
    inventory_id = int(input("Enter the inventory ID to update: \n"))
    quantity = input("Enter the new quantity (leave blank to skip): \n") or None
    obtained_date = input("Enter the new obtained date (leave blank to skip): \n") or None

    fields = []
    values = []
    if quantity:
        fields.append("quantity = %s")
        values.append(int(quantity))
    if obtained_date:
        fields.append("obtained_date = %s")
        values.append(obtained_date)

    if fields:
        query = f"UPDATE inventory SET {', '.join(fields)} WHERE inventory_id = %s"
        values.append(inventory_id)
        cursor.execute(query, values)
        connection.commit()
        print("Inventory item updated successfully.")

def delete_inventory_item(connection, cursor):
    inventory_id = int(input("Enter the inventory ID to delete: \n"))
    query = "DELETE FROM inventory WHERE inventory_id = %s"
    cursor.execute(query, (inventory_id,))
    connection.commit()
    print("Inventory item deleted successfully.")

    # CRUD para la tabla achievements
def create_achievement(connection, cursor):
    name = input("Enter the achievement name: \n")
    description = input("Enter the achievement description: \n")
    points = int(input("Enter the achievement points: \n"))

    query = "INSERT INTO achievements(name, description, points) VALUES(%s, %s, %s)"
    cursor.execute(query, (name, description, points))
    connection.commit()
    print("Achievement created successfully.")

def read_achievements(cursor):
    query = "SELECT * FROM achievements"
    cursor.execute(query)
    results = cursor.fetchall()
    print("Achievements:")
    for row in results:
        print(row)

def update_achievement(connection, cursor):
    achievement_id = int(input("Enter the achievement ID to update: \n"))
    name = input("Enter the new achievement name (leave blank to skip): \n") or None
    description = input("Enter the new description (leave blank to skip): \n") or None
    points = input("Enter the new points (leave blank to skip): \n") or None

    fields = []
    values = []
    if name:
        fields.append("name = %s")
        values.append(name)
    if description:
        fields.append("description = %s")
        values.append(description)
    if points:
        fields.append("points = %s")
        values.append(int(points))

    if fields:
        query = f"UPDATE achievements SET {', '.join(fields)} WHERE achievement_id = %s"
        values.append(achievement_id)
        cursor.execute(query, values)
        connection.commit()
        print("Achievement updated successfully.")

def delete_achievement(connection, cursor):
    achievement_id = int(input("Enter the achievement ID to delete: \n"))
    query = "DELETE FROM achievements WHERE achievement_id = %s"
    cursor.execute(query, (achievement_id,))
    connection.commit()
    print("Achievement deleted successfully.")

# CRUD para la tabla crafting
def create_crafting(connection, cursor):
    crafted_item_id = int(input("Enter the crafted item ID: \n"))
    recipe = input("Enter the crafting recipe: \n")

    query = "INSERT INTO crafting(crafted_item_id, recipe) VALUES(%s, %s)"
    cursor.execute(query, (crafted_item_id, recipe))
    connection.commit()
    print("Crafting entry created successfully.")

def read_crafting(cursor):
    query = "SELECT * FROM crafting"
    cursor.execute(query)
    results = cursor.fetchall()
    print("Crafting entries:")
    for row in results:
        print(row)

def update_crafting(connection, cursor):
    crafting_id = int(input("Enter the crafting ID to update: \n"))
    crafted_item_id = input("Enter the new crafted item ID (leave blank to skip): \n") or None
    recipe = input("Enter the new recipe (leave blank to skip): \n") or None

    fields = []
    values = []
    if crafted_item_id:
        fields.append("crafted_item_id = %s")
        values.append(int(crafted_item_id))
    if recipe:
        fields.append("recipe = %s")
        values.append(recipe)

    if fields:
        query = f"UPDATE crafting SET {', '.join(fields)} WHERE crafting_id = %s"
        values.append(crafting_id)
        cursor.execute(query, values)
        connection.commit()
        print("Crafting entry updated successfully.")

def delete_crafting(connection, cursor):
    crafting_id = int(input("Enter the crafting ID to delete: \n"))
    query = "DELETE FROM crafting WHERE crafting_id = %s"
    cursor.execute(query, (crafting_id,))
    connection.commit()
    print("Crafting entry deleted successfully.")

# CRUD para la tabla enchantments
def create_enchantment(connection, cursor):
    name = input("Enter the enchantment name: \n")
    description = input("Enter the enchantment description: \n")
    level_required = int(input("Enter the level required for the enchantment: \n"))
    effect = input("Enter the enchantment effect: \n")
    item_id = int(input("Enter the associated item ID: \n"))

    query = "INSERT INTO enchantments(name, description, level_required, effect, item_id) VALUES(%s, %s, %s, %s, %s)"
    cursor.execute(query, (name, description, level_required, effect, item_id))
    connection.commit()
    print("Enchantment created successfully.")

def read_enchantments(cursor):
    query = "SELECT * FROM enchantments"
    cursor.execute(query)
    results = cursor.fetchall()
    print("Enchantments:")
    for row in results:
        print(row)

def update_enchantment(connection, cursor):
    enchantment_id = int(input("Enter the enchantment ID to update: \n"))
    name = input("Enter the new enchantment name (leave blank to skip): \n") or None
    description = input("Enter the new description (leave blank to skip): \n") or None
    level_required = input("Enter the new level required (leave blank to skip): \n") or None
    effect = input("Enter the new effect (leave blank to skip): \n") or None
    item_id = input("Enter the new associated item ID (leave blank to skip): \n") or None

    fields = []
    values = []
    if name:
        fields.append("name = %s")
        values.append(name)
    if description:
        fields.append("description = %s")
        values.append(description)
    if level_required:
        fields.append("level_required = %s")
        values.append(int(level_required))
    if effect:
        fields.append("effect = %s")
        values.append(effect)
    if item_id:
        fields.append("item_id = %s")
        values.append(int(item_id))

    if fields:
        query = f"UPDATE enchantments SET {', '.join(fields)} WHERE enchantment_id = %s"
        values.append(enchantment_id)
        cursor.execute(query, values)
        connection.commit()
        print("Enchantment updated successfully.")

def delete_enchantment(connection, cursor):
    enchantment_id = int(input("Enter the enchantment ID to delete: \n"))
    query = "DELETE FROM enchantments WHERE enchantment_id = %s"
    cursor.execute(query, (enchantment_id,))
    connection.commit()
    print("Enchantment deleted successfully.")

    # CRUD para la tabla enemies
def create_enemy(connection, cursor):
    name = input("Enter the enemy's name: \n")
    level = int(input("Enter the enemy's level: \n"))
    experience_reward = int(input("Enter the experience reward for defeating the enemy: \n"))
    zone_id = int(input("Enter the zone ID where the enemy is located: \n"))

    query = "INSERT INTO enemies(name, level, experience_reward, zone_id) VALUES(%s, %s, %s, %s)"
    cursor.execute(query, (name, level, experience_reward, zone_id))
    connection.commit()
    print("Enemy created successfully.")

def read_enemies(cursor):
    query = "SELECT * FROM enemies"
    cursor.execute(query)
    results = cursor.fetchall()
    print("Enemies:")
    for row in results:
        print(row)

def update_enemy(connection, cursor):
    enemy_id = int(input("Enter the enemy ID to update: \n"))
    name = input("Enter the new enemy name (leave blank to skip): \n") or None
    level = input("Enter the new enemy level (leave blank to skip): \n") or None
    experience_reward = input("Enter the new experience reward (leave blank to skip): \n") or None
    zone_id = input("Enter the new zone ID (leave blank to skip): \n") or None

    fields = []
    values = []
    if name:
        fields.append("name = %s")
        values.append(name)
    if level:
        fields.append("level = %s")
        values.append(int(level))
    if experience_reward:
        fields.append("experience_reward = %s")
        values.append(int(experience_reward))
    if zone_id:
        fields.append("zone_id = %s")
        values.append(int(zone_id))

    if fields:
        query = f"UPDATE enemies SET {', '.join(fields)} WHERE enemy_id = %s"
        values.append(enemy_id)
        cursor.execute(query, values)
        connection.commit()
        print("Enemy updated successfully.")

def delete_enemy(connection, cursor):
    enemy_id = int(input("Enter the enemy ID to delete: \n"))
    query = "DELETE FROM enemies WHERE enemy_id = %s"
    cursor.execute(query, (enemy_id,))
    connection.commit()
    print("Enemy deleted successfully.")

# CRUD para la tabla events
def create_event(connection, cursor):
    name = input("Enter the event name: \n")
    description = input("Enter the event description: \n")
    start_date = input("Enter the event start date (YYYY-MM-DD): \n")
    end_date = input("Enter the event end date (YYYY-MM-DD): \n")

    query = "INSERT INTO events(name, description, start_date, end_date) VALUES(%s, %s, %s, %s)"
    cursor.execute(query, (name, description, start_date, end_date))
    connection.commit()
    print("Event created successfully.")

def read_events(cursor):
    query = "SELECT * FROM events"
    cursor.execute(query)
    results = cursor.fetchall()
    print("Events:")
    for row in results:
        print(row)

def update_event(connection, cursor):
    event_id = int(input("Enter the event ID to update: \n"))
    name = input("Enter the new event name (leave blank to skip): \n") or None
    description = input("Enter the new event description (leave blank to skip): \n") or None
    start_date = input("Enter the new start date (leave blank to skip): \n") or None
    end_date = input("Enter the new end date (leave blank to skip): \n") or None

    fields = []
    values = []
    if name:
        fields.append("name = %s")
        values.append(name)
    if description:
        fields.append("description = %s")
        values.append(description)
    if start_date:
        fields.append("start_date = %s")
        values.append(start_date)
    if end_date:
        fields.append("end_date = %s")
        values.append(end_date)

    if fields:
        query = f"UPDATE events SET {', '.join(fields)} WHERE event_id = %s"
        values.append(event_id)
        cursor.execute(query, values)
        connection.commit()
        print("Event updated successfully.")

def delete_event(connection, cursor):
    event_id = int(input("Enter the event ID to delete: \n"))
    query = "DELETE FROM events WHERE event_id = %s"
    cursor.execute(query, (event_id,))
    connection.commit()
    print("Event deleted successfully.")

# CRUD para la tabla friends_list
def create_friendship(connection, cursor):
    user_id = int(input("Enter your user ID: \n"))
    friend_user_id = int(input("Enter the friend's user ID: \n"))
    friendship_status = input("Enter the friendship status (pending, accepted, blocked): \n")

    query = "INSERT INTO friends_list(user_id, friend_user_id, friendship_status) VALUES(%s, %s, %s)"
    cursor.execute(query, (user_id, friend_user_id, friendship_status))
    connection.commit()
    print("Friendship created successfully.")

def read_friendships(cursor):
    query = "SELECT * FROM friends_list"
    cursor.execute(query)
    results = cursor.fetchall()
    print("Friendships:")
    for row in results:
        print(row)

def update_friendship(connection, cursor):
    friend_list_id = int(input("Enter the friendship ID to update: \n"))
    friendship_status = input("Enter the new friendship status (pending, accepted, blocked): \n")

    query = "UPDATE friends_list SET friendship_status = %s WHERE friend_list_id = %s"
    cursor.execute(query, (friendship_status, friend_list_id))
    connection.commit()
    print("Friendship updated successfully.")

def delete_friendship(connection, cursor):
    friend_list_id = int(input("Enter the friendship ID to delete: \n"))
    query = "DELETE FROM friends_list WHERE friend_list_id = %s"
    cursor.execute(query, (friend_list_id,))
    connection.commit()
    print("Friendship deleted successfully.")

    # CRUD para la tabla guild
def create_guild(connection, cursor):
    name = input("Enter the guild name: \n")
    leader_id = int(input("Enter the leader's user ID: \n"))

    query = "INSERT INTO guild(name, leader_id) VALUES(%s, %s)"
    cursor.execute(query, (name, leader_id))
    connection.commit()
    print("Guild created successfully.")

def read_guilds(cursor):
    query = "SELECT * FROM guild"
    cursor.execute(query)
    results = cursor.fetchall()
    print("Guilds:")
    for row in results:
        print(row)

def update_guild(connection, cursor):
    guild_id = int(input("Enter the guild ID to update: \n"))
    name = input("Enter the new guild name (leave blank to skip): \n") or None
    leader_id = input("Enter the new leader's user ID (leave blank to skip): \n") or None

    fields = []
    values = []
    if name:
        fields.append("name = %s")
        values.append(name)
    if leader_id:
        fields.append("leader_id = %s")
        values.append(int(leader_id))

    if fields:
        query = f"UPDATE guild SET {', '.join(fields)} WHERE guild_id = %s"
        values.append(guild_id)
        cursor.execute(query, values)
        connection.commit()
        print("Guild updated successfully.")

def delete_guild(connection, cursor):
    guild_id = int(input("Enter the guild ID to delete: \n"))
    query = "DELETE FROM guild WHERE guild_id = %s"
    cursor.execute(query, (guild_id,))
    connection.commit()
    print("Guild deleted successfully.")

# CRUD para la tabla houses
def create_house(connection, cursor):
    name = input("Enter the house name: \n")
    character_id = int(input("Enter the character ID associated with the house: \n"))

    query = "INSERT INTO houses(name, character_id) VALUES(%s, %s)"
    cursor.execute(query, (name, character_id))
    connection.commit()
    print("House created successfully.")

def read_houses(cursor):
    query = "SELECT * FROM houses"
    cursor.execute(query)
    results = cursor.fetchall()
    print("Houses:")
    for row in results:
        print(row)

def update_house(connection, cursor):
    house_id = int(input("Enter the house ID to update: \n"))
    name = input("Enter the new house name (leave blank to skip): \n") or None
    character_id = input("Enter the new character ID (leave blank to skip): \n") or None

    fields = []
    values = []
    if name:
        fields.append("name = %s")
        values.append(name)
    if character_id:
        fields.append("character_id = %s")
        values.append(int(character_id))

    if fields:
        query = f"UPDATE houses SET {', '.join(fields)} WHERE house_id = %s"
        values.append(house_id)
        cursor.execute(query, values)
        connection.commit()
        print("House updated successfully.")

def delete_house(connection, cursor):
    house_id = int(input("Enter the house ID to delete: \n"))
    query = "DELETE FROM houses WHERE house_id = %s"
    cursor.execute(query, (house_id,))
    connection.commit()
    print("House deleted successfully.")

# CRUD para la tabla items
def create_item(connection, cursor):
    name = input("Enter the item name: \n")
    item_type = input("Enter the item type (consumable, weapon, equipment): \n")
    rarity = input("Enter the item rarity (common, rare, epic, legendary): \n")
    price = int(input("Enter the item price: \n"))

    query = "INSERT INTO items(name, type, rarity, price) VALUES(%s, %s, %s, %s)"
    cursor.execute(query, (name, item_type, rarity, price))
    connection.commit()
    print("Item created successfully.")

def read_items(cursor):
    query = "SELECT * FROM items"
    cursor.execute(query)
    results = cursor.fetchall()
    print("Items:")
    for row in results:
        print(row)

def update_item(connection, cursor):
    item_id = int(input("Enter the item ID to update: \n"))
    name = input("Enter the new item name (leave blank to skip): \n") or None
    item_type = input("Enter the new item type (leave blank to skip): \n") or None
    rarity = input("Enter the new rarity (leave blank to skip): \n") or None
    price = input("Enter the new price (leave blank to skip): \n") or None

    fields = []
    values = []
    if name:
        fields.append("name = %s")
        values.append(name)
    if item_type:
        fields.append("type = %s")
        values.append(item_type)
    if rarity:
        fields.append("rarity = %s")
        values.append(rarity)
    if price:
        fields.append("price = %s")
        values.append(int(price))

    if fields:
        query = f"UPDATE items SET {', '.join(fields)} WHERE item_id = %s"
        values.append(item_id)
        cursor.execute(query, values)
        connection.commit()
        print("Item updated successfully.")

def delete_item(connection, cursor):
    item_id = int(input("Enter the item ID to delete: \n"))
    query = "DELETE FROM items WHERE item_id = %s"
    cursor.execute(query, (item_id,))
    connection.commit()
    print("Item deleted successfully.")

    # CRUD para la tabla maps
def create_map(connection, cursor):
    name = input("Enter the map name: \n")
    description = input("Enter the map description: \n")

    query = "INSERT INTO maps(name, description) VALUES(%s, %s)"
    cursor.execute(query, (name, description))
    connection.commit()
    print("Map created successfully.")

def read_maps(cursor):
    query = "SELECT * FROM maps"
    cursor.execute(query)
    results = cursor.fetchall()
    print("Maps:")
    for row in results:
        print(row)

def update_map(connection, cursor):
    map_id = int(input("Enter the map ID to update: \n"))
    name = input("Enter the new map name (leave blank to skip): \n") or None
    description = input("Enter the new description (leave blank to skip): \n") or None

    fields = []
    values = []
    if name:
        fields.append("name = %s")
        values.append(name)
    if description:
        fields.append("description = %s")
        values.append(description)

    if fields:
        query = f"UPDATE maps SET {', '.join(fields)} WHERE map_id = %s"
        values.append(map_id)
        cursor.execute(query, values)
        connection.commit()
        print("Map updated successfully.")

def delete_map(connection, cursor):
    map_id = int(input("Enter the map ID to delete: \n"))
    query = "DELETE FROM maps WHERE map_id = %s"
    cursor.execute(query, (map_id,))
    connection.commit()
    print("Map deleted successfully.")

# CRUD para la tabla npc
def create_npc(connection, cursor):
    name = input("Enter the NPC name: \n")
    role = input("Enter the NPC role: \n")
    zone_id = int(input("Enter the zone ID where the NPC is located: \n"))

    query = "INSERT INTO npc(name, role, zone_id) VALUES(%s, %s, %s)"
    cursor.execute(query, (name, role, zone_id))
    connection.commit()
    print("NPC created successfully.")

def read_npcs(cursor):
    query = "SELECT * FROM npc"
    cursor.execute(query)
    results = cursor.fetchall()
    print("NPCs:")
    for row in results:
        print(row)

def update_npc(connection, cursor):
    npc_id = int(input("Enter the NPC ID to update: \n"))
    name = input("Enter the new NPC name (leave blank to skip): \n") or None
    role = input("Enter the new NPC role (leave blank to skip): \n") or None
    zone_id = input("Enter the new zone ID (leave blank to skip): \n") or None

    fields = []
    values = []
    if name:
        fields.append("name = %s")
        values.append(name)
    if role:
        fields.append("role = %s")
        values.append(role)
    if zone_id:
        fields.append("zone_id = %s")
        values.append(int(zone_id))

    if fields:
        query = f"UPDATE npc SET {', '.join(fields)} WHERE npc_id = %s"
        values.append(npc_id)
        cursor.execute(query, values)
        connection.commit()
        print("NPC updated successfully.")

def delete_npc(connection, cursor):
    npc_id = int(input("Enter the NPC ID to delete: \n"))
    query = "DELETE FROM npc WHERE npc_id = %s"
    cursor.execute(query, (npc_id,))
    connection.commit()
    print("NPC deleted successfully.")

# CRUD para la tabla pets
def create_pet(connection, cursor):
    name = input("Enter the pet name: \n")
    pet_type = input("Enter the pet type: \n")
    character_id = int(input("Enter the character ID associated with this pet: \n"))

    query = "INSERT INTO pets(name, type, character_id) VALUES(%s, %s, %s)"
    cursor.execute(query, (name, pet_type, character_id))
    connection.commit()
    print("Pet created successfully.")

def read_pets(cursor):
    query = "SELECT * FROM pets"
    cursor.execute(query)
    results = cursor.fetchall()
    print("Pets:")
    for row in results:
        print(row)

def update_pet(connection, cursor):
    pet_id = int(input("Enter the pet ID to update: \n"))
    name = input("Enter the new pet name (leave blank to skip): \n") or None
    pet_type = input("Enter the new pet type (leave blank to skip): \n") or None
    character_id = input("Enter the new character ID (leave blank to skip): \n") or None

    fields = []
    values = []
    if name:
        fields.append("name = %s")
        values.append(name)
    if pet_type:
        fields.append("type = %s")
        values.append(pet_type)
    if character_id:
        fields.append("character_id = %s")
        values.append(int(character_id))

    if fields:
        query = f"UPDATE pets SET {', '.join(fields)} WHERE pet_id = %s"
        values.append(pet_id)
        cursor.execute(query, values)
        connection.commit()
        print("Pet updated successfully.")

def delete_pet(connection, cursor):
    pet_id = int(input("Enter the pet ID to delete: \n"))
    query = "DELETE FROM pets WHERE pet_id = %s"
    cursor.execute(query, (pet_id,))
    connection.commit()
    print("Pet deleted successfully.")

    # CRUD para la tabla purchase_history
def create_purchase(connection, cursor):
    user_id = int(input("Enter the user ID: \n"))
    item_id = int(input("Enter the item ID: \n"))
    purchase_date = input("Enter the purchase date (YYYY-MM-DD HH:MM:SS): \n")
    quantity = int(input("Enter the quantity purchased: \n"))
    total_price = int(input("Enter the total price: \n"))

    query = "INSERT INTO purchase_history(user_id, item_id, purchase_date, quantity, total_price) VALUES(%s, %s, %s, %s, %s)"
    cursor.execute(query, (user_id, item_id, purchase_date, quantity, total_price))
    connection.commit()
    print("Purchase recorded successfully.")

def read_purchase_history(cursor):
    query = "SELECT * FROM purchase_history"
    cursor.execute(query)
    results = cursor.fetchall()
    print("Purchase History:")
    for row in results:
        print(row)

def update_purchase(connection, cursor):
    purchase_id = int(input("Enter the purchase ID to update: \n"))
    quantity = input("Enter the new quantity (leave blank to skip): \n") or None
    total_price = input("Enter the new total price (leave blank to skip): \n") or None

    fields = []
    values = []
    if quantity:
        fields.append("quantity = %s")
        values.append(int(quantity))
    if total_price:
        fields.append("total_price = %s")
        values.append(int(total_price))

    if fields:
        query = f"UPDATE purchase_history SET {', '.join(fields)} WHERE purchase_id = %s"
        values.append(purchase_id)
        cursor.execute(query, values)
        connection.commit()
        print("Purchase updated successfully.")

def delete_purchase(connection, cursor):
    purchase_id = int(input("Enter the purchase ID to delete: \n"))
    query = "DELETE FROM purchase_history WHERE purchase_id = %s"
    cursor.execute(query, (purchase_id,))
    connection.commit()
    print("Purchase deleted successfully.")

# CRUD para la tabla quests
def create_quest(connection, cursor):
    name = input("Enter the quest name: \n")
    description = input("Enter the quest description: \n")
    reward_item_id = int(input("Enter the reward item ID: \n"))
    reward_xp = int(input("Enter the reward experience points: \n"))

    query = "INSERT INTO quests(name, description, reward_item_id, reward_xp) VALUES(%s, %s, %s, %s)"
    cursor.execute(query, (name, description, reward_item_id, reward_xp))
    connection.commit()
    print("Quest created successfully.")

def read_quests(cursor):
    query = "SELECT * FROM quests"
    cursor.execute(query)
    results = cursor.fetchall()
    print("Quests:")
    for row in results:
        print(row)

def update_quest(connection, cursor):
    quest_id = int(input("Enter the quest ID to update: \n"))
    name = input("Enter the new quest name (leave blank to skip): \n") or None
    description = input("Enter the new description (leave blank to skip): \n") or None
    reward_item_id = input("Enter the new reward item ID (leave blank to skip): \n") or None
    reward_xp = input("Enter the new reward experience points (leave blank to skip): \n") or None

    fields = []
    values = []
    if name:
        fields.append("name = %s")
        values.append(name)
    if description:
        fields.append("description = %s")
        values.append(description)
    if reward_item_id:
        fields.append("reward_item_id = %s")
        values.append(int(reward_item_id))
    if reward_xp:
        fields.append("reward_xp = %s")
        values.append(int(reward_xp))

    if fields:
        query = f"UPDATE quests SET {', '.join(fields)} WHERE quest_id = %s"
        values.append(quest_id)
        cursor.execute(query, values)
        connection.commit()
        print("Quest updated successfully.")

def delete_quest(connection, cursor):
    quest_id = int(input("Enter the quest ID to delete: \n"))
    query = "DELETE FROM quests WHERE quest_id = %s"
    cursor.execute(query, (quest_id,))
    connection.commit()
    print("Quest deleted successfully.")

# CRUD para la tabla rankings
def create_ranking(connection, cursor):
    user_id = int(input("Enter the user ID: \n"))
    score = int(input("Enter the ranking score: \n"))

    query = "INSERT INTO rankings(user_id, score) VALUES(%s, %s)"
    cursor.execute(query, (user_id, score))
    connection.commit()
    print("Ranking entry created successfully.")

def read_rankings(cursor):
    query = "SELECT * FROM rankings"
    cursor.execute(query)
    results = cursor.fetchall()
    print("Rankings:")
    for row in results:
        print(row)

def update_ranking(connection, cursor):
    ranking_id = int(input("Enter the ranking ID to update: \n"))
    score = input("Enter the new score (leave blank to skip): \n") or None

    if score:
        query = "UPDATE rankings SET score = %s WHERE ranking_id = %s"
        cursor.execute(query, (int(score), ranking_id))
        connection.commit()
        print("Ranking updated successfully.")

def delete_ranking(connection, cursor):
    ranking_id = int(input("Enter the ranking ID to delete: \n"))
    query = "DELETE FROM rankings WHERE ranking_id = %s"
    cursor.execute(query, (ranking_id,))
    connection.commit()
    print("Ranking deleted successfully.")

    # CRUD para la tabla relationships
def create_relationship(connection, cursor):
    user1_id = int(input("Enter the first user ID: \n"))
    user2_id = int(input("Enter the second user ID: \n"))
    relationship_type = input("Enter the relationship type (friend/enemy): \n")

    query = "INSERT INTO relationships(user1_id, user2_id, type) VALUES(%s, %s, %s)"
    cursor.execute(query, (user1_id, user2_id, relationship_type))
    connection.commit()
    print("Relationship created successfully.")

def read_relationships(cursor):
    query = "SELECT * FROM relationships"
    cursor.execute(query)
    results = cursor.fetchall()
    print("Relationships:")
    for row in results:
        print(row)

def update_relationship(connection, cursor):
    relationship_id = int(input("Enter the relationship ID to update: \n"))
    relationship_type = input("Enter the new relationship type (friend/enemy): \n")

    query = "UPDATE relationships SET type = %s WHERE relationship_id = %s"
    cursor.execute(query, (relationship_type, relationship_id))
    connection.commit()
    print("Relationship updated successfully.")

def delete_relationship(connection, cursor):
    relationship_id = int(input("Enter the relationship ID to delete: \n"))
    query = "DELETE FROM relationships WHERE relationship_id = %s"
    cursor.execute(query, (relationship_id,))
    connection.commit()
    print("Relationship deleted successfully.")

# CRUD para la tabla servers
def create_server(connection, cursor):
    name = input("Enter the server name: \n")
    location = input("Enter the server location: \n")

    query = "INSERT INTO servers(name, location) VALUES(%s, %s)"
    cursor.execute(query, (name, location))
    connection.commit()
    print("Server created successfully.")

def read_servers(cursor):
    query = "SELECT * FROM servers"
    cursor.execute(query)
    results = cursor.fetchall()
    print("Servers:")
    for row in results:
        print(row)

def update_server(connection, cursor):
    server_id = int(input("Enter the server ID to update: \n"))
    name = input("Enter the new server name (leave blank to skip): \n") or None
    location = input("Enter the new server location (leave blank to skip): \n") or None

    fields = []
    values = []
    if name:
        fields.append("name = %s")
        values.append(name)
    if location:
        fields.append("location = %s")
        values.append(location)

    if fields:
        query = f"UPDATE servers SET {', '.join(fields)} WHERE server_id = %s"
        values.append(server_id)
        cursor.execute(query, values)
        connection.commit()
        print("Server updated successfully.")

def delete_server(connection, cursor):
    server_id = int(input("Enter the server ID to delete: \n"))
    query = "DELETE FROM servers WHERE server_id = %s"
    cursor.execute(query, (server_id,))
    connection.commit()
    print("Server deleted successfully.")

# CRUD para la tabla shop
def create_shop(connection, cursor):
    name = input("Enter the shop name: \n")
    zone_id = int(input("Enter the zone ID where the shop is located: \n"))

    query = "INSERT INTO shop(name, zone_id) VALUES(%s, %s)"
    cursor.execute(query, (name, zone_id))
    connection.commit()
    print("Shop created successfully.")

def read_shops(cursor):
    query = "SELECT * FROM shop"
    cursor.execute(query)
    results = cursor.fetchall()
    print("Shops:")
    for row in results:
        print(row)

def update_shop(connection, cursor):
    shop_id = int(input("Enter the shop ID to update: \n"))
    name = input("Enter the new shop name (leave blank to skip): \n") or None
    zone_id = input("Enter the new zone ID (leave blank to skip): \n") or None

    fields = []
    values = []
    if name:
        fields.append("name = %s")
        values.append(name)
    if zone_id:
        fields.append("zone_id = %s")
        values.append(int(zone_id))

    if fields:
        query = f"UPDATE shop SET {', '.join(fields)} WHERE shop_id = %s"
        values.append(shop_id)
        cursor.execute(query, values)
        connection.commit()
        print("Shop updated successfully.")

def delete_shop(connection, cursor):
    shop_id = int(input("Enter the shop ID to delete: \n"))
    query = "DELETE FROM shop WHERE shop_id = %s"
    cursor.execute(query, (shop_id,))
    connection.commit()
    print("Shop deleted successfully.")

    # CRUD para la tabla skills
def create_skill(connection, cursor):
    name = input("Enter the skill name: \n")
    description = input("Enter the skill description: \n")
    required_level = int(input("Enter the required level for the skill: \n"))
    cooldown = int(input("Enter the cooldown time (in seconds): \n"))
    character_id = int(input("Enter the character ID associated with this skill: \n"))

    query = "INSERT INTO skills(name, description, required_level, cooldown, character_id) VALUES(%s, %s, %s, %s, %s)"
    cursor.execute(query, (name, description, required_level, cooldown, character_id))
    connection.commit()
    print("Skill created successfully.")

def read_skills(cursor):
    query = "SELECT * FROM skills"
    cursor.execute(query)
    results = cursor.fetchall()
    print("Skills:")
    for row in results:
        print(row)

def update_skill(connection, cursor):
    skill_id = int(input("Enter the skill ID to update: \n"))
    name = input("Enter the new skill name (leave blank to skip): \n") or None
    description = input("Enter the new description (leave blank to skip): \n") or None
    required_level = input("Enter the new required level (leave blank to skip): \n") or None
    cooldown = input("Enter the new cooldown time (leave blank to skip): \n") or None

    fields = []
    values = []
    if name:
        fields.append("name = %s")
        values.append(name)
    if description:
        fields.append("description = %s")
        values.append(description)
    if required_level:
        fields.append("required_level = %s")
        values.append(int(required_level))
    if cooldown:
        fields.append("cooldown = %s")
        values.append(int(cooldown))

    if fields:
        query = f"UPDATE skills SET {', '.join(fields)} WHERE skill_id = %s"
        values.append(skill_id)
        cursor.execute(query, values)
        connection.commit()
        print("Skill updated successfully.")

def delete_skill(connection, cursor):
    skill_id = int(input("Enter the skill ID to delete: \n"))
    query = "DELETE FROM skills WHERE skill_id = %s"
    cursor.execute(query, (skill_id,))
    connection.commit()
    print("Skill deleted successfully.")

# CRUD para la tabla skins
def create_skin(connection, cursor):
    name = input("Enter the skin name: \n")
    description = input("Enter the skin description: \n")
    price = int(input("Enter the price of the skin: \n"))

    query = "INSERT INTO skins(name, description, price) VALUES(%s, %s, %s)"
    cursor.execute(query, (name, description, price))
    connection.commit()
    print("Skin created successfully.")

def read_skins(cursor):
    query = "SELECT * FROM skins"
    cursor.execute(query)
    results = cursor.fetchall()
    print("Skins:")
    for row in results:
        print(row)

def update_skin(connection, cursor):
    skins_id = int(input("Enter the skin ID to update: \n"))
    name = input("Enter the new skin name (leave blank to skip): \n") or None
    description = input("Enter the new description (leave blank to skip): \n") or None
    price = input("Enter the new price (leave blank to skip): \n") or None

    fields = []
    values = []
    if name:
        fields.append("name = %s")
        values.append(name)
    if description:
        fields.append("description = %s")
        values.append(description)
    if price:
        fields.append("price = %s")
        values.append(int(price))

    if fields:
        query = f"UPDATE skins SET {', '.join(fields)} WHERE skins_id = %s"
        values.append(skins_id)
        cursor.execute(query, values)
        connection.commit()
        print("Skin updated successfully.")

def delete_skin(connection, cursor):
    skins_id = int(input("Enter the skin ID to delete: \n"))
    query = "DELETE FROM skins WHERE skins_id = %s"
    cursor.execute(query, (skins_id,))
    connection.commit()
    print("Skin deleted successfully.")

# CRUD para la tabla stats
def create_stat(connection, cursor):
    character_id = int(input("Enter the character ID: \n"))
    stat_name = input("Enter the stat name: \n")
    value = int(input("Enter the stat value: \n"))

    query = "INSERT INTO stats(character_id, stat_name, value) VALUES(%s, %s, %s)"
    cursor.execute(query, (character_id, stat_name, value))
    connection.commit()
    print("Stat created successfully.")

def read_stats(cursor):
    query = "SELECT * FROM stats"
    cursor.execute(query)
    results = cursor.fetchall()
    print("Stats:")
    for row in results:
        print(row)

def update_stat(connection, cursor):
    stat_id = int(input("Enter the stat ID to update: \n"))
    stat_name = input("Enter the new stat name (leave blank to skip): \n") or None
    value = input("Enter the new stat value (leave blank to skip): \n") or None

    fields = []
    values = []
    if stat_name:
        fields.append("stat_name = %s")
        values.append(stat_name)
    if value:
        fields.append("value = %s")
        values.append(int(value))

    if fields:
        query = f"UPDATE stats SET {', '.join(fields)} WHERE stat_id = %s"
        values.append(stat_id)
        cursor.execute(query, values)
        connection.commit()
        print("Stat updated successfully.")

def delete_stat(connection, cursor):
    stat_id = int(input("Enter the stat ID to delete: \n"))
    query = "DELETE FROM stats WHERE stat_id = %s"
    cursor.execute(query, (stat_id,))
    connection.commit()
    print("Stat deleted successfully.")

    # CRUD para la tabla trades
def create_trade(connection, cursor):
    user1_id = int(input("Enter the ID of the first user: \n"))
    user2_id = int(input("Enter the ID of the second user: \n"))
    offered_item_id = int(input("Enter the ID of the item offered: \n"))
    received_item_id = int(input("Enter the ID of the item received: \n"))

    query = "INSERT INTO trades(user1_id, user2_id, offered_item_id, received_item_id) VALUES(%s, %s, %s, %s)"
    cursor.execute(query, (user1_id, user2_id, offered_item_id, received_item_id))
    connection.commit()
    print("Trade created successfully.")

def read_trades(cursor):
    query = "SELECT * FROM trades"
    cursor.execute(query)
    results = cursor.fetchall()
    print("Trades:")
    for row in results:
        print(row)

def update_trade(connection, cursor):
    trade_id = int(input("Enter the trade ID to update: \n"))
    offered_item_id = input("Enter the new offered item ID (leave blank to skip): \n") or None
    received_item_id = input("Enter the new received item ID (leave blank to skip): \n") or None

    fields = []
    values = []
    if offered_item_id:
        fields.append("offered_item_id = %s")
        values.append(int(offered_item_id))
    if received_item_id:
        fields.append("received_item_id = %s")
        values.append(int(received_item_id))

    if fields:
        query = f"UPDATE trades SET {', '.join(fields)} WHERE trade_id = %s"
        values.append(trade_id)
        cursor.execute(query, values)
        connection.commit()
        print("Trade updated successfully.")

def delete_trade(connection, cursor):
    trade_id = int(input("Enter the trade ID to delete: \n"))
    query = "DELETE FROM trades WHERE trade_id = %s"
    cursor.execute(query, (trade_id,))
    connection.commit()
    print("Trade deleted successfully.")

# CRUD para la tabla zones
def create_zone(connection, cursor):
    name = input("Enter the zone name: \n")
    map_id = int(input("Enter the map ID associated with this zone: \n"))

    query = "INSERT INTO zones(name, map_id) VALUES(%s, %s)"
    cursor.execute(query, (name, map_id))
    connection.commit()
    print("Zone created successfully.")

def read_zones(cursor):
    query = "SELECT * FROM zones"
    cursor.execute(query)
    results = cursor.fetchall()
    print("Zones:")
    for row in results:
        print(row)

def update_zone(connection, cursor):
    zone_id = int(input("Enter the zone ID to update: \n"))
    name = input("Enter the new zone name (leave blank to skip): \n") or None
    map_id = input("Enter the new map ID (leave blank to skip): \n") or None

    fields = []
    values = []
    if name:
        fields.append("name = %s")
        values.append(name)
    if map_id:
        fields.append("map_id = %s")
        values.append(int(map_id))

    if fields:
        query = f"UPDATE zones SET {', '.join(fields)} WHERE zone_id = %s"
        values.append(zone_id)
        cursor.execute(query, values)
        connection.commit()
        print("Zone updated successfully.")

def delete_zone(connection, cursor):
    zone_id = int(input("Enter the zone ID to delete: \n"))
    query = "DELETE FROM zones WHERE zone_id = %s"
    cursor.execute(query, (zone_id,))
    connection.commit()
    print("Zone deleted successfully.")