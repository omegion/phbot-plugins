import json
import os
import random
import struct
from threading import Timer

import QtBind
import phBotChat
from phBot import *

pName = 'xControl'
pVersion = '1.4.0'
pUrl = 'https://raw.githubusercontent.com/JellyBitz/phBot-xPlugins/master/xControl.py'

# ______________________________ Initializing ______________________________ #

# Globals
inGame = None
followActivated = False
followPlayer = ''
followDistance = 0

# Graphic user interface
gui = QtBind.init(__name__, pName)
lblxControl01 = QtBind.createLabel(gui,
                                   'Manage your partys easily using the ingame chat.\nThe Leader(s) is the character that write chat commands.\nIf you character have Leader(s) into the leader list, this will follow his orders.\n\n* UPPERCASE is required to use the command, all his data is separated by spaces.\n* #Variable (required) #Variable? (optional)\n Supported commands :\n - START : Start bot\n - STOP : Stop bot\n - TRACE #Player? : Start trace to leader or another character\n - NOTRACE : Stop trace\n - SETAREA #PosX? #PosY? #Region? : Set training area.\n - SETRADIUS #Radius? : Set training radius.\n - SIT : Sit or Stand up, depends\n - CAPE #Type? : Use PVP Cape\n - ZERK : Use berserker mode if is available\n - RETURN : Use some "Return Scroll" from your inventory\n - TP #A #B : Use teleport from location A to B\n - INJECT #Opcode #Encrypted? #Data? : Inject packet\n - CHAT #Type #Message : Send any message type',
                                   21, 11)
lblxControl02 = QtBind.createLabel(gui,
                                   ' - MOVEON #Radius? : Set a random movement\n - FOLLOW #Player? #Distance? : Trace a party player using distance\n - NOFOLLOW : Stop following\n - PROFILE #Name? : Loads a profile by his name\n - JUMP : Generate knockback visual effect\n - DC : Disconnect from game\n - MOUNT #PetType? : Mount horse by default\n - DISMOUNT #PetType? : Dismount horse by default\n - GETOUT : Left party\n - RECALL #Town : Set recall on city portal\n - SETSCRIPT #Path : Change script path for training area',
                                   345, 101)

tbxLeaders = QtBind.createLineEdit(gui, "", 511, 11, 100, 20)
lstLeaders = QtBind.createList(gui, 511, 32, 176, 48)
btnAddLeader = QtBind.createButton(gui, 'btnAddLeader_clicked', "    Add    ", 612, 10)
btnRemLeader = QtBind.createButton(gui, 'btnRemLeader_clicked', "     Remove     ", 560, 79)


# ______________________________ Methods ______________________________ #

# Return xControl folder path
def getPath():
    return get_config_dir() + pName + "\\"


# Return character configs path (JSON)
def getConfig():
    return getPath() + inGame['server'] + "_" + inGame['name'] + ".json"


# Check if character is ingame
def isJoined():
    global inGame
    inGame = get_character_data()
    if not (inGame and "name" in inGame and inGame["name"]):
        inGame = None
    return inGame


# Load default configs
def loadDefaultConfig():
    # Clear data
    QtBind.clear(gui, lstLeaders)


# Loads all config previously saved
def loadConfigs():
    loadDefaultConfig()
    if isJoined():
        # Check config exists to load
        if os.path.exists(getConfig()):
            data = {}
            with open(getConfig(), "r") as f:
                data = json.load(f)
            if "Leaders" in data:
                for nickname in data["Leaders"]:
                    QtBind.append(gui, lstLeaders, nickname)


# Add leader to the list
def btnAddLeader_clicked():
    if inGame:
        player = QtBind.text(gui, tbxLeaders)
        # Player nickname it's not empty
        if player and not lstLeaders_exist(player):
            # Init dictionary
            data = {}
            # Load config if exist
            if os.path.exists(getConfig()):
                with open(getConfig(), 'r') as f:
                    data = json.load(f)
            # Add new leader
            if not "Leaders" in data:
                data['Leaders'] = []
            data['Leaders'].append(player)
            # Replace configs
            with open(getConfig(), "w") as f:
                f.write(json.dumps(data, indent=4, sort_keys=True))
            QtBind.append(gui, lstLeaders, player)
            QtBind.setText(gui, tbxLeaders, "")
            log('Plugin: Leader added [' + player + ']')


# Remove leader selected from list
def btnRemLeader_clicked():
    if inGame:
        selectedItem = QtBind.text(gui, lstLeaders)
        if selectedItem:
            if os.path.exists(getConfig()):
                data = {"Leaders": []}
                with open(getConfig(), 'r') as f:
                    data = json.load(f)
                try:
                    # remove leader nickname from file if exists
                    data["Leaders"].remove(selectedItem)
                    with open(getConfig(), "w") as f:
                        f.write(json.dumps(data, indent=4, sort_keys=True))
                except:
                    pass  # just ignore file if doesn't exist
            QtBind.remove(gui, lstLeaders, selectedItem)
            log('Plugin: Leader removed [' + selectedItem + ']')


# Return True if nickname exist at the leader list
def lstLeaders_exist(nickname):
    nickname = nickname.lower()
    players = QtBind.getItems(gui, lstLeaders)
    for i in range(len(players)):
        if players[i].lower() == nickname:
            return True
    return False


# Inject teleport packet, using the source and destination name
def inject_teleport(source, destination):
    t = get_teleport_data(source, destination)
    if t:
        npcs = get_npcs()
        for key, npc in npcs.items():
            if npc['name'] == source or npc['servername'] == source:
                log("Plugin: Selecting teleporter [" + source + "]")
                # Teleport found, select it
                inject_joymax(0x7045, struct.pack('<I', key), False)
                # Start a timer to teleport in 2.0 seconds
                Timer(2.0, inject_joymax, (0x705A, struct.pack('<IBI', key, 2, t[1]), False)).start()
                Timer(2.0, log, ("Plugin: Teleporting to [" + destination + "]")).start()
                return
        log('Plugin: NPC not found. Wrong NPC name or servername')
    else:
        log('Plugin: Teleport data not found. Wrong teleport name or servername')


# Send message, Ex. "All Hello World!" or "private JellyBitz Hi!"
def handleChatCommand(msg):
    # Try to split message
    args = msg.split(' ', 1)
    # Check if the format is correct and is not empty
    if len(args) != 2 or not args[0] or not args[1]:
        return
    # Split correctly the message
    t = args[0].lower()
    if t == 'private' or t == 'note':
        # then check message is not empty
        argsExtra = args[1].split(' ', 1)
        if len(argsExtra) != 2 or not argsExtra[0] or not argsExtra[1]:
            return
        args.pop(1)
        args += argsExtra
    # Check message type
    sent = False
    if t == "all":
        sent = phBotChat.All(args[1])
    elif t == "private":
        sent = phBotChat.Private(args[1], args[2])
    elif t == "party":
        sent = phBotChat.Party(args[1])
    elif t == "guild":
        sent = phBotChat.Guild(args[1])
    elif t == "union":
        sent = phBotChat.Union(args[1])
    elif t == "note":
        sent = phBotChat.Note(args[1], args[2])
    elif t == "stall":
        sent = phBotChat.Stall(args[1])
    elif t == "global":
        sent = phBotChat.Global(args[1])
    if sent:
        log('Plugin: Message "' + t + '" sent successfully!')


# Move to a random position from the actual position using a maximum radius
def randomMovement(radiusMax=10):
    # Generating a random new point
    pX = random.uniform(-radiusMax, radiusMax)
    pY = random.uniform(-radiusMax, radiusMax)
    # Mixing with the actual position
    p = get_position()
    pX = pX + p["x"]
    pY = pY + p["y"]
    # Moving to new position
    move_to(pX, pY, p["z"])
    log("Plugin: Random movement to (X:%.1f,Y:%.1f)" % (pX, pY))


# Follow a player using distance. Return success
def start_follow(player, distance):
    if party_player(player):
        global followActivated, followPlayer, followDistance
        followPlayer = player
        followDistance = distance
        followActivated = True
        return True
    return False


# Return True if the player is in the party
def party_player(player):
    players = get_party()
    if players:
        for p in players:
            if players[p]['name'] == player:
                return True
    return False


# Return point [X,Y] if player is in the party and near, otherwise return None
def near_party_player(player):
    players = get_party()
    if players:
        for p in players:
            if players[p]['name'] == player and players[p]['player_id'] > 0:
                return players[p]
    return None


# Calc the distance from point A to B
def GetDistance(ax, ay, bx, by):
    return ((bx - ax) ** 2 + (by - ay) ** 2) ** 0.5


# Stop follow player
def stop_follow():
    global followActivated, followPlayer, followDistance
    result = followActivated
    # stop
    followActivated = False
    followPlayer = ""
    followDistance = 0
    return result


# Try to summon a vehicle
def MountHorse():
    items = get_inventory()['items']
    for slot, item in enumerate(items):
        if item:
            sn = item['servername']
            # Search some kind vehicle by servername
            if '_C_' in sn:
                packet = struct.pack('B', slot)
                packet += struct.pack('H', 4588 + (1 if sn.endswith('_SCROLL') else 0))  # Silk scroll
                inject_joymax(0x704C, packet, True)
                return True
    log('Plugin: Horse not found at your inventory')
    return False


# Try to mount pet by type, return success
def MountPet(petType):
    # just in case
    if petType == 'pick':
        return False
    elif petType == 'horse':
        return MountHorse()
    # get all summoned pets
    pets = get_pets()
    if pets:
        for uid, pet in pets.items():
            if pet['type'] == petType:
                p = b'\x01'  # mount flag
                p += struct.pack('I', uid)
                inject_joymax(0x70CB, p, False)
                return True
    return False


# Try to dismount pet by type, return success
def DismountPet(petType):
    petType = petType.lower()
    # just in case
    if petType == 'pick':
        return False
    # get all summoned pets
    pets = get_pets()
    if pets:
        for uid, pet in pets.items():
            if pet['type'] == petType:
                p = b'\x00'
                p += struct.pack('I', uid)
                inject_joymax(0x70CB, p, False)
                return True
    return False


# Gets the NPC unique ID if the specified name is found near
def GetNPCUniqueID(name):
    NPCs = get_npcs()
    if NPCs:
        name = name.lower()
        for UniqueID, NPC in NPCs.items():
            NPCName = NPC['name'].lower()
            if name == NPCName:
                return UniqueID
    return 0


# ______________________________ Events ______________________________ #

# Called when the bot successfully connects to the game server
def connected():
    global inGame
    inGame = None


# Called when the character enters the game world
def joined_game():
    loadConfigs()


# All chat messages received are sent to this function
def handle_chat(t, player, msg):
    # Check player at leader list or a Discord message
    if player and lstLeaders_exist(player) or t == 4:
        # Parsing message command
        if msg == "START":
            start_bot()
            log("Plugin: Bot started")
        elif msg == "STOP":
            stop_bot()
            log("Plugin: Bot stopped")
        elif msg.startswith("TRACE"):
            # deletes empty spaces on right
            msg = msg.rstrip()
            if msg == "TRACE":
                if start_trace(player):
                    log("Plugin: Starting trace to [" + player + "]")
            else:
                msg = msg[5:].split()[0]
                if start_trace(msg):
                    log("Plugin: Starting trace to [" + msg + "]")
        elif msg == "NOTRACE":
            stop_trace()
            log("Plugin: Trace stopped")
        elif msg.startswith("SETAREA"):
            # deletes empty spaces on right
            msg = msg.rstrip()
            if msg == "SETAREA":
                p = get_position()
                set_training_position(p['region'], p['x'], p['y'])
                log("Plugin: Training area set to current position (X:%.1f,Y:%.1f)" % (p['x'], p['y']))
            else:
                try:
                    # check arguments
                    p = msg[7:].split()
                    x = float(p[0])
                    y = float(p[1])
                    # auto calculated if is not specified
                    region = int(p[2]) if len(p) >= 3 else 0
                    set_training_position(region, x, y, 0.0)
                    log("Plugin: Training area set to (X:%.1f,Y:%.1f)" % (x, y))
                except:
                    log("Plugin: Wrong training area coordinates!")
        elif msg.startswith("SETRADIUS"):
            # deletes empty spaces on right
            msg = msg.rstrip()
            if msg == "SETRADIUS":
                # set default radius
                radius = 35
                set_training_radius(radius)
                log("Plugin: Training radius reseted to " + str(radius) + " m.")
            else:
                try:
                    # split and parse movement radius
                    radius = int(float(msg[9:].split()[0]))
                    # to absolute
                    radius = (radius if radius > 0 else radius * -1)
                    set_training_radius(radius)
                    log("Plugin: Training radius set to " + str(radius) + " m.")
                except:
                    log("Plugin: Wrong training radius value!")
        elif msg.startswith('SETSCRIPT'):
            # deletes empty spaces on right
            msg = msg.rstrip()
            if msg == 'SETSCRIPT':
                # reset script
                set_training_script('')
                log('Plugin: Training script path has been reseted')
            else:
                # change script to the path specified
                set_training_script(msg[9:])
                log('Plugin: Training script path has been changed')
        elif msg == "SIT":
            log("Plugin: Sit/Stand")
            inject_joymax(0x704F, b'\x04', False)
        elif msg == "JUMP":
            # Just a funny emote lol
            log("Plugin: Jumping!")
            inject_joymax(0x3091, b'\x0c', False)
        elif msg.startswith("CAPE"):
            # deletes empty spaces on right
            msg = msg.rstrip()
            if msg == "CAPE":
                log("Plugin: Using PVP Cape by default (Yellow)")
                inject_joymax(0x7516, b'\x05', False)
            else:
                # get cape type normalized
                cape = msg[4:].split()[0].lower()
                if cape == "off":
                    log("Plugin: Removing PVP Cape")
                    inject_joymax(0x7516, b'\x00', False)
                elif cape == "red":
                    log("Plugin: Using PVP Cape (Red)")
                    inject_joymax(0x7516, b'\x01', False)
                elif cape == "gray":
                    log("Plugin: Using PVP Cape (Gray)")
                    inject_joymax(0x7516, b'\x02', False)
                elif cape == "blue":
                    log("Plugin: Using PVP Cape (Blue)")
                    inject_joymax(0x7516, b'\x03', False)
                elif cape == "white":
                    log("Plugin: Using PVP Cape (White)")
                    inject_joymax(0x7516, b'\x04', False)
                elif cape == "yellow":
                    log("Plugin: Using PVP Cape (Yellow)")
                    inject_joymax(0x7516, b'\x05', False)
                else:
                    log("Plugin: Wrong PVP Cape color!")
        elif msg == "ZERK":
            log("Plugin: Using Berserker mode")
            inject_joymax(0x70A7, b'\x01', False)
        elif msg == "RETURN":
            log('Plugin: Trying to use return scroll...')
            # Avoid high CPU usage with too many chars at the same time
            Timer(random.uniform(0.5, 2), use_return_scroll).start()
        elif msg.startswith("TP"):
            # deletes command header
            msg = msg[2:]
            if not msg:
                return
            # remove whatever used as separator
            msg = msg[1:]
            if not msg:
                return
            # select split char
            split = ',' if ',' in msg else ' '
            # extract arguments
            source_dest = msg.split(split)
            # needs to be at least two name points to try teleporting
            if len(source_dest) >= 2:
                inject_teleport(source_dest[0].strip(), source_dest[1].strip())
        elif msg.startswith("INJECT "):
            msgPacket = msg[7:].split()
            msgPacketLen = len(msgPacket)
            if msgPacketLen == 0:
                log("Plugin: Incorrect structure to inject packet")
                return
            # Check packet structure
            opcode = int(msgPacket[0], 16)
            data = bytearray()
            encrypted = False
            dataIndex = 1
            if msgPacketLen >= 2:
                enc = msgPacket[1].lower()
                if enc == 'true' or enc == 'false':
                    encrypted = enc == "true"
                    dataIndex += 1
            # Create packet data and inject it
            for i in range(dataIndex, msgPacketLen):
                data.append(int(msgPacket[i], 16))
            inject_joymax(opcode, data, encrypted)
            # Log the info
            log("Plugin: Injecting packet...\nOpcode: 0x" + '{:02X}'.format(opcode) + " - Encrypted: " + (
                "Yes" if encrypted else "No") + "\nData: " + (
                    ' '.join('{:02X}'.format(int(msgPacket[x], 16)) for x in range(dataIndex, msgPacketLen)) if len(
                        data) else 'None'))
        elif msg.startswith("CHAT "):
            handleChatCommand(msg[5:])
        elif msg.startswith("MOVEON"):
            if msg == "MOVEON":
                randomMovement()
            else:
                try:
                    # split and parse movement radius
                    radius = int(float(msg[6:].split()[0]))
                    # to positive
                    radius = (radius if radius > 0 else radius * -1)
                    randomMovement(radius)
                except:
                    log("Plugin: Movement maximum radius incorrect")
        elif msg.startswith("FOLLOW"):
            # default values
            charName = player
            distance = 10
            if msg != "FOLLOW":
                # Check params
                msg = msg[6:].split()
                try:
                    if len(msg) >= 1:
                        charName = msg[0]
                    if len(msg) >= 2:
                        distance = float(msg[1])
                except:
                    log("Plugin: Follow distance incorrect")
                    return
            # Start following
            if start_follow(charName, distance):
                log("Plugin: Starting to follow to [" + charName + "] using [" + str(distance) + "] as distance")
        elif msg == "NOFOLLOW":
            if stop_follow():
                log("Plugin: Following stopped")
        elif msg.startswith("PROFILE"):
            if msg == "PROFILE":
                if set_profile('Default'):
                    log("Plugin: Setting Default profile")
            else:
                msg = msg[7:]
                if set_profile(msg):
                    log("Plugin: Setting " + msg + " profile")
        elif msg == "DC":
            log("Plugin: Disconnecting...")
            disconnect()
        elif msg.startswith("MOUNT"):
            # default value
            pet = "horse"
            if msg != "MOUNT":
                msg = msg[5:].split()
                if msg:
                    pet = msg[0]
            # Try mount pet
            if MountPet(pet):
                log("Plugin: Mounting pet [" + pet + "]")
        elif msg.startswith("DISMOUNT"):
            # default value
            pet = "horse"
            if msg != "DISMOUNT":
                msg = msg[8:].split()
                if msg:
                    pet = msg[0]
            # Try dismount pet
            if DismountPet(pet):
                log("Plugin: Dismounting pet [" + pet + "]")
        elif msg == "GETOUT":
            # Check if has party
            if get_party():
                # Left it
                log("Plugin: Leaving the party..")
                inject_joymax(0x7061, b'', False)
        elif msg.startswith("RECALL "):
            msg = msg[7:]
            if msg:
                npcUID = GetNPCUniqueID(msg)
                if npcUID > 0:
                    log("Plugin: Designating recall to \"" + msg.title() + "\"...")
                    inject_joymax(0x7059, struct.pack('I', npcUID), False)


# Called every 500ms
def event_loop():
    if inGame and followActivated:
        player = near_party_player(followPlayer)
        # check if is near
        if not player:
            return
        # check distance to the player
        if followDistance > 0:
            p = get_position()
            playerDistance = round(GetDistance(p['x'], p['y'], player['x'], player['y']), 2)
            # check if has to move
            if followDistance < playerDistance:
                # generate vector unit
                x_unit = (player['x'] - p['x']) / playerDistance
                y_unit = (player['y'] - p['y']) / playerDistance
                # distance to move
                movementDistance = playerDistance - followDistance
                log("Following " + followPlayer + "...")
                move_to(movementDistance * x_unit + p['x'], movementDistance * y_unit + p['y'], 0)
        else:
            # Avoid negative numbers
            log("Following " + followPlayer + "...")
            move_to(player['x'], player['y'], 0)


# Plugin loaded
log("Plugin: " + pName + " v" + pVersion + " successfully loaded")

if os.path.exists(getPath()):
    # Adding RELOAD plugin support
    loadConfigs()
else:
    # Creating configs folder
    os.makedirs(getPath())
    log('Plugin: ' + pName + ' folder has been created')
