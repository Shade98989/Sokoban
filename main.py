from gameengine.GameEngine import GameEngine

# game should be squared
display_width = 500
display_height = display_width
# game render rate
fps = 60

game_engine = GameEngine(display_width, display_height, fps)
game_engine.run()

quit()
