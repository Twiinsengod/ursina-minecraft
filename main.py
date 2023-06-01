from ursina import *

def update():
    if held_keys["a"]:
        move_personagem(quadrado, -6 * time.dt)
    if held_keys["d"]:
        move_personagem(quadrado, 6 * time.dt)
    if held_keys["s"]:
        move_personagem(quadrado, 0, -6 * time.dt)
    if held_keys["w"]:
        move_personagem(quadrado, 0, 6 * time.dt)
        
    # SEGUNDO PERSONAGEM

    if held_keys["left arrow"]:
        move_personagem(quadrado2, -6 * time.dt)
    if held_keys["right arrow"]:
        move_personagem(quadrado2, 6 * time.dt)
    if held_keys["down arrow"]:
        move_personagem(quadrado2, 0, -6 * time.dt)
    if held_keys["up arrow"]:
        move_personagem(quadrado2, 0, 6 * time.dt)

app.run()
