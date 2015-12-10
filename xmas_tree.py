from sense_hat import SenseHat

sense = SenseHat()

X = [0, 100, 0] # Green
O = [0, 0, 0] # Black
B = [139, 69, 19] # Brown

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
