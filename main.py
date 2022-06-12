from mainGame import MainGame
import subprocess
cmd="python test.py"
p=subprocess.Popen(cmd,shell=True)
game=MainGame()

game.orbpos()
