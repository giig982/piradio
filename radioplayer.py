"""Python Mpc interface for 3.5 TFT Touchscreen display """
import time
import subprocess
import os
#import glob
import sys
import pygame
from pygame.locals import *
os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"
pygame.init()

def on_click():
	"""define function that checks for mouse location"""
	click_pos = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
	#check to see if exit has been pressed
	if 270 <= click_pos[0] <= 320 and 10 <= click_pos[1] <= 50:
		print "You pressed exit"
		button(0)
	#now check to see if play was pressed
	if 20 <= click_pos[0] <= 70 and 80 <= click_pos[1] <= 130:
                print "You pressed button play"
                button(1)
	#now check to see if stop  was pressed
        if 80 <= click_pos[0] <= 135 and 80 <= click_pos[1] <= 130:
                print "You pressed button stop"
                button(2)
	#now check to see if refreshed  was pressed
        if 270 <= click_pos[0] <= 320 and 70 <= click_pos[1] <= 120:
                print "You pressed button refresh"
                button(3)
	#now check to see if previous  was pressed
        if 10 <= click_pos[0] <= 60 and 180 <= click_pos[1] <= 230:
                print "You pressed button previous"
                button(4)

	 #now check to see if next  was pressed
        if 70 <= click_pos[0] <= 120 and 180 <= click_pos[1] <= 230:
                print "You pressed button next"
                button(5)

	 #now check to see if volume down was pressed
        if 130 <= click_pos[0] <= 180 and 180 <= click_pos[1] <= 230:
                print "You pressed volume down"
                button(6)

	 #now check to see if button 7 was pressed
        if 190 <= click_pos[0] <= 240 and 180 <= click_pos[1] <= 230:
                print "You pressed volume up"
                button(7)

	 #now check to see if button 8 was pressed
        if 250 <= click_pos[0] <= 300 and 180 <= click_pos[1] <= 230:
                print "You pressed mute"
                button(8)

	 #now check to see if button 9 was pressed
        if 15 <= click_pos[0] <= 125 and 165 <= click_pos[1] <= 200:
                print "You pressed button 9"
                button(9)



def button(number):
	"""define action on pressing buttons"""
	print "You pressed button ", number
	if number == 0:    #specific script when exiting
		SCREEN.fill(BLACK)
		font = pygame.font.Font(None, 24)
        	label = font.render("Radioplayer will continue in background", 1, (WHITE))
        	SCREEN.blit(label, (0, 90))
		pygame.display.flip()
		time.sleep(5)
		sys.exit()

	if number == 1:
		subprocess.call("mpc play ", shell=True)
		refresh_menu_screen()

	if number == 2:
		subprocess.call("mpc stop ", shell=True)
		refresh_menu_screen()

	if number == 3:
		subprocess.call("mpc stop ", shell=True)
		subprocess.call("mpc play ", shell=True)
		refresh_menu_screen()

	if number == 4:
		subprocess.call("mpc prev ", shell=True)
		refresh_menu_screen()

	if number == 5:
		subprocess.call("mpc next ", shell=True)
		refresh_menu_screen()

	if number == 6:
		subprocess.call("mpc volume -10 ", shell=True)
		refresh_menu_screen()

	if number == 7:
		subprocess.call("mpc volume +10 ", shell=True)
		refresh_menu_screen()

	if number == 8:
		subprocess.call("mpc volume 0 ", shell=True)
		refresh_menu_screen()

def refresh_menu_screen():
	"""refresh screen and draw elements """
	#set up the fixed items on the menu
	SCREEN.fill(WHITE) #change the colours if needed
	font = pygame.font.Font(None, 24)
	title_font = pygame.font.Font(None, 34)
	station_font = pygame.font.Font(None, 20)
	label = title_font.render("MPC RADIO", 1, (BLUE))
	label2 = font.render("Streaming Internet Radio", 1, (RED))
	SCREEN.blit(label, (105, 15))
	SCREEN.blit(label2, (88, 45))

	play_pb = pygame.image.load("play.tiff")
	pause_pb = pygame.image.load("pause.tiff")
	refresh_pb = pygame.image.load("refresh.tiff")
	previous_pb = pygame.image.load("previous.tiff")
	next_pb = pygame.image.load("next.tiff")
	vol_down_pb = pygame.image.load("volume_down.tiff")
	vol_up_pb = pygame.image.load("volume_up.tiff")
	mute_pb = pygame.image.load("mute.png")
	exit_pb = pygame.image.load("exit.tiff")
	radio_icon = pygame.image.load("radio.tiff")

	# draw the main elements on the screen
	SCREEN.blit(play_pb, (20, 80))
	SCREEN.blit(pause_pb, (80, 80))
	pygame.draw.rect(SCREEN, RED, (8, 70, 304, 108), 1)
	pygame.draw.line(SCREEN, RED, (8, 142), (310, 142), 1)
	pygame.draw.rect(SCREEN, CREAM, (10, 143, 300, 33), 0)
	SCREEN.blit(refresh_pb, (270, 70))
	SCREEN.blit(previous_pb, (10, 180))
	SCREEN.blit(next_pb, (70, 180))
	SCREEN.blit(vol_down_pb, (130, 180))
	SCREEN.blit(vol_up_pb, (190, 180))
	SCREEN.blit(mute_pb, (250, 180))
	SCREEN.blit(exit_pb, (270, 5))
	SCREEN.blit(radio_icon, (2, 1))
	pygame.draw.rect(SCREEN, BLUE, (0, 0, 480, 320), 3)

	##### display the station name and split it into 2 parts :
	station = subprocess.check_output("mpc current", shell=True)
	lines = station.split(":")
	length = len(lines)
	if length == 1:
		line1 = lines[0]
		line1 = line1[:-1]
		line2 = "No additional info: "
	else:
		line1 = lines[0]
		line2 = lines[1]

	line2 = line2[:42]
	line2 = line2[:-1]
	#trap no station data
	if line1 == "":
		line2 = "Press PLAY or REFRESH"
		station_status = "stopped"
		status_font = RED
	else:
		station_status = "playing"
		status_font = GREEN
	station_name = station_font.render(line1, 1, (RED))
	additional_data = station_font.render(line2, 1, (BLUE))
	station_label = title_font.render(station_status, 1, (status_font))
	SCREEN.blit(station_label, (175, 100))
	SCREEN.blit(station_name, (13, 145))
	SCREEN.blit(additional_data, (12, 160))

	######## add volume number
	volume = subprocess.check_output("mpc volume", shell=True)
	volume = volume[8:]
	volume = volume[:-1]
	volume_tag = font.render(volume, 1, (BLACK))
	SCREEN.blit(volume_tag, (175, 75))

	####### check to see if the Radio is connected to the internet
	ip_retcode = subprocess.check_output("hostname -I", shell=True)
	ip_retcode = ip_retcode[:3]
	if ip_retcode == "192":
		network_status = "online"
		status_font = GREEN

	else:
		network_status = "offline"
		status_font = RED

	network_status_label = font.render(network_status, 1, (status_font))
	SCREEN.blit(network_status_label, (215, 75))
	pygame.display.flip()

def main():
	""" main method"""
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				print "screen pressed" #for debugging purposes
				pos = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
				print pos #for checking
				#for debugging purposes - adds a small dot where the screen is pressed
				pygame.draw.circle(SCREEN, WHITE, pos, 2, 0)
				on_click()

#ensure there is always a safe way to end the program if the touch screen fails

			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					sys.exit()
		time.sleep(0.2)
	pygame.display.update()


#################### EVERTHING HAS NOW BEEN DEFINED ###########################

#set size of the screen
SIZE = WIDTH, HEIGHT = 480, 320
SCREEN = pygame.display.set_mode(SIZE)

#define colours
BLUE = 26, 0, 255
CREAM = 254, 255, 25
BLACK = 0, 0, 0
WHITE = 255, 255, 255
YELLOW = 255, 255, 0
RED = 255, 0, 0
GREEN = 0, 255, 0

#refresh the menu interface
refresh_menu_screen()
#check for key presses and start emergency exit
main()
station_name()


