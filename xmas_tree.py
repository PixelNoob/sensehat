from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

X = [0, 100, 0] # Green
O = [0, 0, 0] # Black
W = [255, 255, 255]  # White
B = [139, 69, 19] # Brown
U = [0, 0, 128] # Blue
R = [255, 0, 0] # Red

while True:
	xmas_tree= [
	O, O, O, X, X, O, O, O,
	O, O, X, X, X, X, O, O,
	O, X, X, X, X, X, X, O,
	O, O, X, X, X, X, O, O,
	O, X, X, X, X, X, X, O,
	X, X, X, X, X, X, X, X,
	O, O, O, B, B, O, O, O,
	O, O, O, B, B, O, O, O
	]
	sense.set_pixels(xmas_tree)
	sleep(3)
	xmas_tree = [
	O, O, O, U, U, O, O, O,
	O, O, U, U, U, U, O, O,
	O, U, U, U, U, U, U, O,
	O, O, U, U, U, U, O, O,
	O, U, U, U, U, U, U, O,
	U, U, U, U, U, U, U, U,
	O, O, O, B, B, O, O, O,
	O, O, O, B, B, O, O, O
	]
	sense.set_pixels(xmas_tree)
	sleep(3)
	xmas_tree = [
	O, O, O, W, W, O, O, O,
	O, O, W, W, W, W, O, O,
	O, W, W, W, W, W, W, O,
	O, O, W, W, W, W, O, O,
	O, W, W, W, W, W, W, O,
	W, W, W, W, W, W, W, W,
	O, O, O, B, B, O, O, O,
	O, O, O, B, B, O, O, O
	]
	sense.set_pixels(xmas_tree)
	sleep(3)
	xmas_tree = [
	O, O, O, R, R, O, O, O,
	O, O, R, R, R, R, O, O,
	O, R, R, R, R, R, R, O,
	O, O, R, R, R, R, O, O,
	O, R, R, R, R, R, R, O,
	R, R, R, R, R, R, R, R,
	O, O, O, B, B, O, O, O,
	O, O, O, B, B, O, O, O
	]
	sense.set_pixels(xmas_tree)
	sleep(3)
