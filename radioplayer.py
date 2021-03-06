"""Python Mpc interface for 3.5 TFT Touchscreen display """
import time
import subprocess
import os
#import glob
import sys
import pygame
import datetime
from pygame.locals import *
os.environ["SDL_FBDEV"] = "/dev/fb1"
#os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDEV"] = "/dev/input/event0"
os.environ["SDL_MOUSEDRV"] = "TSLIB"
pygame.init()

def on_click():
	"""define function that checks for mouse location"""
	click_pos = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
	#check to see if exit has been pressed
	if EXIT_PB_X <= click_pos[0] <= EXIT_PB_X + 50 and \
	EXIT_PB_Y <= click_pos[1] <= EXIT_PB_Y + 50:
		print "You pressed exit"
		button(0)
	#now check to see if play was pressed
	if PLAY_PB_X <= click_pos[0] <= (PLAY_PB_X + 50) and \
	PLAY_PB_Y <= click_pos[1] <= (PLAY_PB_Y + 50):
		print "You pressed button play"
		button(1)
	#now check to see if stop  was pressed
	if PAUSE_PB_X <= click_pos[0] <= (PAUSE_PB_X + 50) and \
	PAUSE_PB_Y <= click_pos[1] <= (PAUSE_PB_Y + 50):
		print "You pressed button stop"
		button(2)
	#now check to see if refreshed  was pressed
	if REFRESH_PB_X <= click_pos[0] <= REFRESH_PB_X + 50 and \
	REFRESH_PB_Y <= click_pos[1] <= REFRESH_PB_Y + 50:
		print "You pressed button refresh"
		button(3)
	#now check to see if previous  was pressed
	if PREVIOUS_PB_X <= click_pos[0] <= PREVIOUS_PB_X + 70 and \
	PREVIOUS_PB_Y <= click_pos[1] <= PREVIOUS_PB_Y + 50:
		print "You pressed button previous"
		button(4)

	 #now check to see if next  was pressed
	if NEXT_PB_X <= click_pos[0] <= NEXT_PB_X + 50 and \
	NEXT_PB_Y <= click_pos[1] <= NEXT_PB_Y + 50:
		print "You pressed button next"
		button(5)

	 #now check to see if volume down was pressed
	if VOL_DOWN_PB_X <= click_pos[0] <= VOL_DOWN_PB_X + 50 and \
	VOL_DOWN_PB_Y <= click_pos[1] <= VOL_DOWN_PB_Y + 50:
		print "You pressed volume down"
		button(6)

	 #now check to see if button 7 was pressed
	if VOL_UP_PB_X <= click_pos[0] <= VOL_UP_PB_X + 50 and \
	VOL_UP_PB_Y <= click_pos[1] <= VOL_UP_PB_Y + 50:
		print "You pressed volume up"
		button(7)

	 #now check to see if button 8 was pressed
	if MUTE_PB_X <= click_pos[0] <= MUTE_PB_X + 50 and \
	MUTE_PB_Y <= click_pos[1] <= MUTE_PB_Y + 50:
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
		label = FONT.render("Radioplayer will continue in background", 1, (WHITE))
		SCREEN.blit(label, (30, 130))
		pygame.display.flip()
		time.sleep(3)
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
	SCREEN.fill(BCKG_COLOR) #change the colours if needed
	label = TITLE_FONT.render("MPC RADIO", 1, (BLUE))
	label2 = FONT.render("Streaming Radio", 1, (RED))
	SCREEN.blit(label, (165, 15))
	SCREEN.blit(label2, (165, 45))


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
	SCREEN.blit(play_pb, (PLAY_PB_X, PLAY_PB_Y))
	SCREEN.blit(pause_pb, (PAUSE_PB_X, PAUSE_PB_Y))

	pygame.draw.rect(SCREEN, RED, (8, 70, 464, 108), 1)
	pygame.draw.line(SCREEN, RED, (8, 142), (470, 142), 1)
	pygame.draw.rect(SCREEN, YELLOW, (10, 143, 460, 33), 0)
	SCREEN.blit(refresh_pb, (REFRESH_PB_X, REFRESH_PB_Y))

	SCREEN.blit(previous_pb, (PREVIOUS_PB_X, PREVIOUS_PB_Y))
	SCREEN.blit(next_pb, (NEXT_PB_X, NEXT_PB_Y))
	SCREEN.blit(vol_down_pb, (VOL_DOWN_PB_X, VOL_DOWN_PB_Y))
	SCREEN.blit(vol_up_pb, (VOL_UP_PB_X, VOL_UP_PB_Y))
	SCREEN.blit(mute_pb, (MUTE_PB_X, MUTE_PB_Y))

	SCREEN.blit(exit_pb, (EXIT_PB_X, EXIT_PB_Y))
	SCREEN.blit(radio_icon, (RADIO_ICON_X, RADIO_ICON_Y))
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
	station_name = STATION_FONT.render(line1, 1, (RED))
	additional_data = STATION_FONT.render(line2, 1, (BLUE))
	station_label = TITLE_FONT.render(station_status, 1, (status_font))
	SCREEN.blit(station_label, (175, 110))
	SCREEN.blit(station_name, (13, 145))
	SCREEN.blit(additional_data, (12, 160))

	######## add volume number
	volume = subprocess.check_output("mpc volume", shell=True)
	volume = volume[8:]
	volume = volume[:-1]
	volume_tag = FONT.render(volume, 1, (BLACK))
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

	network_status_label = FONT.render(network_status, 1, (status_font))
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

		_delta = datetime.timedelta(seconds=0)
		_now = datetime.datetime.today()
		_dt = str(_now - _delta)
		clock = _dt[11:16]
		fontimg = FONT_1.render(clock, 1, RED)
		SCREEN.fill(BLACK, (5, 232, 469, 85))
		pygame.display.update()
		SCREEN.blit(fontimg, (CLOCK_X, CLOCK_Y))
		pygame.display.update()

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
RED = 245, 0, 0
GREEN = 0, 255, 0
BCKG_COLOR = 128, 204, 255

#define button positions
PLAY_PB_X = 20
PLAY_PB_Y = 80
PAUSE_PB_X = 80
PAUSE_PB_Y = 80
REFRESH_PB_X = 425
REFRESH_PB_Y = 80
PREVIOUS_PB_X = 10
PREVIOUS_PB_Y = 180
NEXT_PB_X = 90
NEXT_PB_Y = 180
VOL_DOWN_PB_X = 190
VOL_DOWN_PB_Y = 180
VOL_UP_PB_X = 415
VOL_UP_PB_Y = 180
MUTE_PB_X = 300
MUTE_PB_Y = 180
EXIT_PB_X = 428
EXIT_PB_Y = 10
RADIO_ICON_X = 7
RADIO_ICON_Y = 2
CLOCK_X = 130
CLOCK_Y = 225

BCK_CLOCK = "00:00:00"
FONT = pygame.font.Font(None, 24)
FONT_1 = pygame.font.Font("fonts/font.ttf", 92)
TITLE_FONT = pygame.font.Font(None, 34)
STATION_FONT = pygame.font.Font(None, 20)
	

#refresh the menu interface
refresh_menu_screen()
#check for key presses and start emergency exit
main()
#station_name()
