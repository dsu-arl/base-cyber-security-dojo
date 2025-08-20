import random, pprint

with open("./templates/index.html", "r") as f:
    template = ''.join(f.readlines())
    print(template)


spiderList = ['6 eyed crab spider', '6 eyed crab spiders', '6 eyed sand spider', '6 eyed sand spiders', '6-eyed crab spider', '6-eyed crab spiders', '6-eyed sand spider', '6-eyed sand spiders', 'Adelaide funnel-web spider', 'Algerian jumping spider', 'Alien butt spider', 'Alpine funnel-web spider', 'Amatola Asemonea Jumping Spider', 'American garden spider', 'American grass spider', 'American house spider', 'Angelina Jolie trapdoor spider', 'Anyphaenid sac spider', 'Arizona black hole spider', 'Arizona brown spider', 'Arrowhead spider', 'Assassin spider', "Attenborough's goblin spider", 'Australian jewel spider', 'Australian jewel spiders', 'Avondale spider', 'Avondale Spider', 'Banded garden spider', 'Banded tunnelweb spider', 'Banded-legged golden orb-web spider', 'Barack Obama trapdoor spider', 'Bark sac spider', 'Batik golden web spider', 'Bird dung spider', 'Black and yellow garden spider', 'Black and Yellow Garden Spider', 'Black widow spider', 'Black Widow spider', 'Black Widow Spider', 'Black wishbone spider', 'Black-striped orchard spider', 'Blunt-spined kite spider', "Bono's Joshua Tree trapdoor spider", "Bono's Joshua Tree Trapdoor Spider", 'Bowl and doily and dwarf spiders', 'Bowl-and-doily and dwarf spiders', 'Bowl-and-doily spider', 'Braken Bat Cave spider', 'Braken Bat Cave Spider', 'Brazilian wandering spider', 'Bridge spider', 'Brisbane two-tailed spider', 'Brown house spider', 'Buck spoor spiders', 'Buck-spoor spider', 'Buck-spoor spiders', 'Buckspoor spider', 'California trapdoor spider', 'California turret spider', 'Cameroon red baboon spider', 'Canadian cross spider', 'Canadian Cross Spider', 'Cane spider', 'Cane Spider', 'Cape Le Grand assassin spider', 'Carolina wolf spider', 'Carrai cave spider', 'Cave spider', 'Cellar spider', 'Cellar Spider', 'Central Highlands assassin spider', 'Christmas spider', 'Christmas spiders', 'Citrine spider', 'Cobweb spider', 'Cobweb spiders', 'Comb footed spider', 'Comb-footed spider', 'Comb-Footed Spider', 'Comb-footed spiders', 'Common American grass spider', 'Common baboon spider', 'Common crab spider', 'Common garden spider', 'Common gray house spider', 'Common house spider', 'Corinnid sac spider', 'Corn spider', 'Corn Spider', 'Crab spider', 'Crab Spider', 'Cream house spider', 'Cross spider', 'Crucifix spider', 'Cupboard spider', 'Daddy long legs spider', 'Daddy long-legs spider', 'Daddy longlegs spider', 'Dandy long-legs spider', 'Dark fishing spider', 'Dark footed ant spider', 'Dark-footed ant-spider', 'Desert bush spider', 'Desert grass spider', 'Diadem spider', 'Distinguished jumper spider', 'Dock spider', 'Drakensberg Euophrys Jumping Spider', 'Eastern mouse spider', 'Eastern parson spider', 'Enamelled spider', 'Enamelled Spider', 'Eunuch spider', 'European cave spider', 'European Cave Spider', 'European garden spider', 'European Garden Spider', 'European wolf spider', 'Eyre Peninsula funnel-web spider', 'Falklands green spider', 'Fishing spider', 'Flat huntsman spider', 'Flinders Ranges funnel-web spider', 'Florida false wolf spider', 'Flower crab spider', 'Foliage webbing spider', 'Foliate spider', 'Furrow orb spider', 'Furrow spider', 'Garden centre spider', 'Garden ghost spider', 'Garden spider', 'Garden Spider', 'Geometric button spider', 'Giant crab spider', 'Gibraltar funnel-web spider', 'Gibraltar Funnel-web Spider', 'Gladiator spider', 'Goblin spider', 'Goblin spiders', 'Golden garden spider', 'Golden orb-weaver spider', 'Golden orb-weaving spider', 'Goldenrod crab spider', 'Goldenrod spider', 'Government Canyon bat cave spider', 'Gray cross spider', 'Green crab spiders', 'Green lynx spider', 'Green Lynx Spider', 'Guatemalan long-jawed spider', 'Guiyang jumping spider', "Hasselt's spiny spider", 'Hawaiian happy-face spider', 'Hermit spider', 'Himalayan jumping spider', 'Hopper spider', 'House button spider', 'House hopper spider', 'Intertidal spider', 'Intertidal trapdoor spider', 'Invisible spider', 'Island red chelate spider', 'Jade jumping spider', 'Joro spider', 'Jorō spider', 'Karakurt spider', 'Karoo Euophrys Jumping Spider', 'Karwar burrowing spider', 'Karwar large burrowing spider', 'Kaston sac spider', 'Ladybird spider', 'Lami Beach northern jumping spider', 'Leaf curling spider', 'Leaf-curling spider', 'Lean lynx spider', 'Leopard spider', 'Lesser red-headed mouse spider', 'Lichen huntsman spider', 'Lichen Huntsman Spider', 'Liocranid sac spider', 'Lizard eating spider', 'Lizard-eating spider', 'Long-legged sac spider', 'Longbodied cellar spider', 'Magam ornamental tiger spider', 'Magam Ornamental tiger spider', 'Malmignatte spider', 'Marbled cellar spider', 'Marbled Cellar Spider', 'Marbled cobweb spider', 'Metallic crab spider', 'Mirror spider', 'Money spider', 'Mouse spiders', 'Mullamullang cave spider', 'Napoleon spider', 'Ndumo Afraflacilla Jumping Spider', 'Nelson cave spider', 'Net casting spider', 'Net-casting spider', 'Northern black widow spider', 'Northern mouse spider', 'Northern yellow sac spider', 'Odd clawed spider', 'Odd Clawed Spider', 'Odd-clawed spider', 'Odd-Clawed Spider', 'Ogre-faced spider', 'Oonopid spider', 'Orb web spider', 'Orchard spider', 'Orchard Spider', 'Oribi Gorge Asemonea Jumping Spider', 'Ornate tiger spider', 'Otway odd clawed spider', 'Otway Odd Clawed Spider', 'Otway odd-clawed spider', 'Otway Odd-Clawed Spider', 'Pantropical jumping spider', 'Paterson Evarcha Jumping Spider', 'Peacock spider', 'Pelican spider', 'Pennsylvania funnel-web spider', 'Pennsylvania grass spider', 'Philodromid crab spider', 'Pirate wolf spider', 'Plectreurid spider', "Plomley's trapdoor spider", 'Primitive hunting spider', 'Purple-gold jumping spider', 'Rain spider', 'Red and silver dewdrop spider', 'Red legged purseweb spider', 'Red tent spider', 'Red widow spider', 'Red-headed mouse spider', 'Red-legged golden orb-weaver spider', 'Red-legged golden orb-web spider', 'Red-legged Golden Orb-web Spider', 'Regal jumping spider', 'Riparian sac spider', 'Rosemary wolf spider', "Rosser's sac spider", 'Rufous net-casting spider', 'Running crab spider', 'Rustic wolf spider', 'Sand spider', 'Sand spiders', 'Santa Rosa wolf spider', 'Scorpion tailed spider', 'Scorpion-tailed spider', 'Scorpiontailed spider', 'Sheet weaver spider', 'Sheet-weaver spiders', 'Sheet-weaving spider', 'Sheetweaver spider', 'Sheetweb spider', 'Short-bodied cellar spider', 'Silver-haired trapdoor spider', 'Six eyed crab spider', 'Six eyed crab spiders', 'Six eyed sand spider', 'Six eyed sand spiders', 'Six horned spider', 'Six spined spider', 'Six-eyed crab spider', 'Six-eyed crab spiders', 'Six-eyed sand spider', 'Six-eyed sand spiders', 'Six-horned spider', 'Six-spined spiders', 'Skull spider', 'Snake-back spider', 'Snakeback spider', 'Social huntsman spider', 'Southeastern wandering spider', 'Southern Sydney funnel-web spider', 'Spanish funnel-web spider', 'Spoor spider', "St Andrew's Cross spider", 'St Andrews Cross spider', 'St Andrews Cross Spider', "St. Andrew's Cross spider", 'St. Andrews Cross spider', 'St. Andrews Cross Spider', 'Starbellied spider', 'Steppe spider', 'Stucco spider', 'Tailed spider', 'Tan jumping spider', 'Tangle web spider', 'Tangle-web spider', 'Tangle-web spiders', 'Tasmanian cave spider', 'Tasmanian funnel-web spider', 'Three-banded crab spider', 'Tingle trapdoor spider', 'Tiny house spider', 'Titanoecid spider', 'Tropical tent-web spider', 'Tropical Tent-web Spider', 'Tropical wolf spider', 'True funnel-web spider', 'Tube web spider', 'Two-spined spider', 'Unusual peacock spider', 'Wall crab spider', 'West Gippsland assassin spider', 'Western black widow spider', 'Whistling spider', 'White lady (spider)', 'White Lady (spider)', 'White Lady spider', 'White Lady Spider', 'White widow spider', 'White-banded Evarcha Jumping Spider', 'Widow spider', 'Widow Spider', 'Widow spiders', 'Widow Spiders', 'Wrap-around spider', 'Yellow crab spider', 'Yellow garden spider', 'Yellow ghost spider', 'Yellow sac spider', 'Yellow Sac spider', 'Yellow Sac Spider', 'Yellow sack spider', 'Yellow-legged zipper spider', 'Zig-zag spider', 'Zipper spider', 'Zombie spider', 'Zorocratid spider']
print(len(spiderList))
directory = []

count = 0
for i in range(2):
    name1 = f"link {i+1} :)"
    directory.append(([name1],[]))
    for j in range(2):
        name2 = f"link {i+1}_{j+1}:)"
        directory[i][1].append([[name2],[]])
        for k in range(3):
            count = count + 1
            print("doin it ", count, " listlen ", len(spiderList))
            name3 = spiderList.pop(0)
            directory[i][1][j][1].append([name3])

count = 0


pprint.pprint(directory)
# input()
for item in directory:
    # print(str(item[0]))
    # print("\n")
    for item2 in item:
        # print("\t"+str(item2[0]))
        # print("\n")
        for item3 in item2:
            print(str(item3))
            print("\n")
            count += 1




print("count", count)



