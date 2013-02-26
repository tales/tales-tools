#!/usr/bin/env python





# in sprites/equipment/HEAD_plate_armor_helmet.xml
# out sprites/equipment/head/plate_armor_helmet_male.xml

import sys
import os
import shutil

def replaceStringInFile(fn, fname, newpath):
    f = open(fn,'r')
    lines = f.readlines()
    f.close()

    f = open(fn,'w')
    for line in lines:
        if fname in line:
            line = line.replace(fname, newpath)
        f.write(line)
    f.close()

def movePNG(fname, newdir, newbasename=""):
    if newbasename == "":
        newbasename = fname.split(r"/")[-1]

    newfname=newdir+newbasename
    print fname, "->", newfname
    try:
        os.makedirs(newdir)
    except:
        pass
    shutil.copyfile(fname, newfname)
    os.remove(fname)
    for (dirpath, dirnames, filenames) in os.walk("sprites"):
        #print dirpath , dirnames, filenames
        for filename in filenames:
            fn = os.path.join(dirpath, filename)
            if fn.endswith('png'):
                continue
            replaceStringInFile(fn, fname[8:], newfname[8:]) # [8:] removes "sprites/"

    replaceStringInFile("AUTHORS.txt", fname[8:], newfname[8:])# [8:] removes "sprites/"

def moveXML(fname, newfname):
    f = open(fname, 'r')
    lines = f.readlines()
    f.close()

    dirs = newfname.split(r'/')
    newdir = '/'.join(dirs[:-1])
    print newdir
    try:
        os.makedirs(newdir)
    except:
        pass

    f = open(newfname, 'w')
    for line in lines:
        if line.strip().startswith('name=') :
            cmd = line.strip()
            print cmd
            exec(cmd)
        if 'src=' in line:
            exec(line.strip())
            newsrc = newfname.split('.')[0]+ "_"+name+'.png'
            basedir = r'/'.join(newsrc.split(r"/")[:-1])+r'/'

            basename = newsrc.split(r"/")[-1:][0]
            print src.split(r"/")[-1]
            if not src.split(r"/")[-1] == 'empty.png':
                try:
                    movePNG(src, basedir, basename)
                    line = ' '*8 + 'src="' + newsrc + '"\n'
                except:
                    print "\n"*3+"WARNING", src, basedir, basename
            else:
                print "skip empty!"
        f.write(line)
    f.close()
    os.remove(fname)

def moveXMLRepair(fname, newfname):
    replaceStringInFile("AUTHORS.txt", fname[8:], newfname[8:])# [8:] removes "sprites/")
    replaceStringInFile("monsters.xml", fname[8:], newfname[8:])# [8:] removes "sprites/")
    replaceStringInFile("items.xml", fname[8:], newfname[8:])# [8:] removes "sprites/")
    replaceStringInFile("npcs.xml", fname[8:], newfname[8:])# [8:] removes "sprites/")

#fname=sys.argv[1]
#newfname=sys.argv[2]
#fname="sprites/equipment/HEAD_plate_armor_helmet.xml"
#newfname="sprites/equipment/head/plate_armor_helmet_male.xml"
#moveXML(fname, newfname)

tbl=[
["sprites/equipment/male_robe.xml","sprites/equipment/torso/robe_male.xml"],
["sprites/equipment/TORSO_leather_armor_shirt_white.xml","sprites/equipment/torso/white_shirt_male.xml"],
["sprites/equipment/BEHIND_quiver.xml","sprites/equipment/misc/quiver.xml"],
["sprites/equipment/TORSO_leather_armor_torso.xml","sprites/equipment/torso/leather_armor_male.xml"],
["sprites/equipment/ghillies.xml","sprites/equipment/misc/ghillies.xml"],
["sprites/equipment/WEAPON_shield_cutout_body.xml","sprites/equipment/hand/wooden_buckler_male.xml"],
["sprites/equipment/bow.xml","sprites/equipment/hand/bow_male.xml"],
["sprites/equipment/WEAPON_shield_cutout_chain_armor_helmet.xml","sprites/equipment/misc/wooden_buckler_cutouts_male.xml"],
["sprites/equipment/HEAD_robe_hood.xml","sprites/equipment/head/leather_hood_male.xml"],
["sprites/equipment/HEAD_leather_armor_hat.xml","sprites/equipment/head/leather_hat_male.xml"],
["sprites/equipment/dress.xml","sprites/equipment/torso/green_dress_female.xml"],
["sprites/equipment/tie.xml","sprites/equipment/necklace/orange_tie_male.xml"],
["sprites/equipment/TORSO_plate_armor_arms_shoulders.xml","sprites/equipment/misc/plate_shoulder_pad_male.xml"],
["sprites/equipment/TORSO_chain_armor_torso.xml","sprites/equipment/torso/chain_armor_male.xml"],
["sprites/equipment/vest.xml","sprites/equipment/torso/green_vest_male.xml"],
["sprites/equipment/dagger.xml","sprites/equipment/hand/dagger_male.xml"],
["sprites/equipment/TORSO_leather_armor_shoulders.xml","sprites/equipment/misc/leather_shoulder_pad_male.xml"],
["sprites/equipment/HANDS_plate_armor_gloves.xml","sprites/equipment/gloves/plate_gloves_male.xml"],
["sprites/equipment/BELT_rope.xml","sprites/equipment/misc/rope_belt_male.xml"],
["sprites/equipment/TORSO_robe_shirt_brown.xml","sprites/equipment/torso/brown_shirt_male.xml"],
["sprites/equipment/FEET_plate_armor_shoes.xml","sprites/equipment/feet/plate_boots_male.xml"],
["sprites/equipment/bowtie.xml","sprites/equipment/necklace/orange_bowtie_male.xml"],
["sprites/equipment/female_robe.xml","sprites/equipment/torso/robe_female.xml"],
["sprites/equipment/HEAD_plate_armor_helmet.xml","sprites/equipment/head/plate_armor_helmet_male.xml"],
["sprites/equipment/BELT_leather.xml","sprites/equipment/misc/leather_belt_male.xml"],
["sprites/equipment/HEAD_chain_armor_hood.xml","sprites/equipment/head/chain_hood_male.xml"],
["sprites/equipment/pants.xml","sprites/equipment/legs/green_trousers_male.xml"],
["sprites/equipment/LEGS_pants_greenish.xml","sprites/equipment/legs/light_blue_trousers_male.xml"],
["sprites/equipment/TORSO_plate_armor_torso.xml","sprites/equipment/torso/plate_armor_male.xml"],
["sprites/equipment/FEET_shoes_brown.xml","sprites/equipment/feet/brown_shoes_male.xml"],
["sprites/equipment/HEAD_chain_armor_helmet.xml","sprites/equipment/head/kettle_hat_male.xml"],
["sprites/equipment/LEGS_robe_skirt.xml","sprites/equipment/legs/robe_skirt_male.xml"],
["sprites/equipment/TORSO_leather_armor_bracers.xml","sprites/equipment/misc/leather_bracers_male.xml"],
["sprites/equipment/female_dwing.xml","sprites/equipment/misc/darkwing_female.xml"],
["sprites/equipment/LEGS_plate_armor_pants.xml","sprites/equipment/legs/plate_trousers_male.xml"],
["sprites/equipment/shirt.xml","sprites/equipment/torso/white_longshirt_male.xml"],
["sprites/equipment/TORSO_chain_armor_jacket_purple.xml","sprites/equipment/misc/purple_cape_male.xml"],
["sprites/equipment/female_mage_brownbelt.xml","sprites/equipment/misc/brown_belt_female.xml"],
["sprites/equipment/female_mage_brownhair.xml","sprites/equipment/hair/brown_female.xml"],
["sprites/equipment/female_mage_lightgrayrobe.xml","sprites/equipment/torso/lightgray_robe_female.xml"],
["sprites/equipment/female_mage_whitehair.xml","sprites/equipment/hair/white_female.xml"],
["sprites/equipment/female_mage_forestrobe.xml","sprites/equipment/torso/green_robe_female.xml"],
["sprites/equipment/female_mage_ironbuckle.xml","sprites/equipment/misc/iron_buckle_female.xml"],
["sprites/equipment/female_mage_redrobe.xml","sprites/equipment/torso/red_robe_female.xml"],
["sprites/equipment/female_mage_bronzebelt.xml","sprites/equipment/misc/bronze_belt_female.xml"],
["sprites/equipment/female_mage_darkbrownrobe.xml","sprites/equipment/torso/darkbrown_robe_female.xml"],
["sprites/equipment/female_mage_silverbuckle.xml","sprites/equipment/misc/silver_buckle_female.xml"],
["sprites/equipment/female_mage_silvertiara.xml","sprites/equipment/head/silver_tiara_female.xml"],
["sprites/equipment/female_mage_irontiara.xml","sprites/equipment/head/iron_tiara_female.xml"],
["sprites/equipment/female_mage_ironbelt.xml","sprites/equipment/misc/iron_belt_female.xml"],
["sprites/equipment/female_mage_purplerobe.xml","sprites/equipment/torso/purple_robe_female.xml"],
["sprites/equipment/female_mage_grayhair.xml","sprites/equipment/hair/gray_female.xml"],
["sprites/equipment/female_mage_ironnecklace.xml","sprites/equipment/necklace/iron_necklace_female.xml"],
["sprites/equipment/female_mage_bronzenecklace.xml","sprites/equipment/necklace/bronze_necklace_female.xml"],
["sprites/equipment/female_mage_whiteslippers.xml","sprites/equipment/feet/white_slippers_female.xml"],
["sprites/equipment/female_mage_darkblondehair.xml","sprites/equipment/hair/darkblonde_female.xml"],
["sprites/equipment/female_mage_goldbelt.xml","sprites/equipment/misc/gold_belt_female.xml"],
["sprites/equipment/female_mage_silvernecklace.xml","sprites/equipment/necklace/silver_necklace_female.xml"],
["sprites/equipment/female_mage_goldtiara.xml","sprites/equipment/head/gold_tiara_female.xml"],
["sprites/equipment/female_mage_whiterobe.xml","sprites/equipment/torso/white_robe_female.xml"],
["sprites/equipment/female_mage_lightblondehair.xml","sprites/equipment/hair/lightblonde_female.xml"],
["sprites/equipment/female_mage_brownrobe.xml","sprites/equipment/torso/brown_robe_female.xml"],
["sprites/equipment/female_mage_goldbuckle.xml","sprites/equipment/misc/gold_buckle_female.xml"],
["sprites/equipment/female_mage_bronzetiara.xml","sprites/equipment/head/bronze_tiara_female.xml"],
["sprites/equipment/female_mage_bronzebuckle.xml","sprites/equipment/misc/bronze_buckle_female.xml"],
["sprites/equipment/female_mage_blackslippers.xml","sprites/equipment/feet/black_slippers_female.xml"],
["sprites/equipment/female_mage_darkgrayrobe.xml","sprites/equipment/torso/darkgray_robe_female.xml"],
["sprites/equipment/female_mage_blackhair.xml","sprites/equipment/hair/black_female.xml"],
["sprites/equipment/female_mage_bluerobe.xml","sprites/equipment/torso/blue_robe_female.xml"],
["sprites/equipment/female_mage_blackrobe.xml","sprites/equipment/torso/black_robe_female.xml"],
["sprites/equipment/female_mage_brownslippers.xml","sprites/equipment/feet/brown_slippers_female.xml"],
["sprites/equipment/female_mage_blackbelt.xml","sprites/equipment/misc/black_belt_female.xml"],
["sprites/equipment/female_mage_silverbelt.xml","sprites/equipment/misc/silver_belt_female.xml"],
["sprites/equipment/female_mage_grayslippers.xml","sprites/equipment/feet/gray_slippers_female.xml"],
["sprites/equipment/female_mage_goldnecklace.xml","sprites/equipment/necklace/gold_necklace_female.xml"]
]

for old, new in tbl:
    moveXMLRepair(old, new)











