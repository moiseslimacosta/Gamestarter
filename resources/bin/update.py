#!/usr/bin/python

import os
import os.path
import xbmc
import xbmcgui
# import xbmcaddon

# addon       = xbmcaddon.Addon()
# addonversion= addon.getAddonInfo('version')


# addonID="script.gamestarter"
# addon       = xbmcaddon.Addon(id=addonID)
# addonversion= addon.getAddonInfo('version')
# addonversion="2.0.1"

#xbmcgui.Dialog().ok("Gamestarter", addonversion)

# xbmcgui.Dialog().ok("Gamestarter", "Checking for updates, please wait.")


# script_file = os.path.realpath(__file__)
# directory = os.path.dirname(script_file)


# os.system("sh  /storage/.kodi/addons/script.gamestarter/resources/bin/update.sh")
os.system("sh  https://github.com/bite-your-idols/Gamestarter-Pi/raw/master/assets/update-checker.sh")
# os.system("wget --no-check-certificate -O /storage/.kodi/addons/script.gamestarter/resources/bin/update.sh https://github.com/bite-your-idols/Gamestarter-Pi/raw/master/resources/bin/update.sh && sh /storage/.kodi/addons/script.gamestarter/resources/bin/update.sh")
# xbmcgui.Dialog().ok("Gamestarter", "Gamestarter is up to date.")


# # una vez que el sh ha hecho lo que tnga que hacer comprobamos el resultado, si esta al dia
# if os.path.isfile(directory+"/updated") == True: 
#  	xbmcgui.Dialog().ok("Gamestarter", "Gamestarter is up to date.")

# # sino
# else:
# 	xbmcgui.Dialog().ok("Gamestarter", "Please update Gamestarter. Install from zip downloaded to /storage.")
