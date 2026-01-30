# SET
For bonus of a project!

To download this project, make a folder and download everything. Then make sure you have pygame installed and python no older than 3.12. Then run Main.py.

How does SET work:
B1-12 = The cards
B13 = Save button
B14 = Load button
B15 = No sets button
B16 = Reveal/hint button
T1 = Time left
T2 = Total point
T3 = Computer point
T4 = Hint
Every card in the game SET has got 4 attributes. Each being able to take any value between 1 and 3. This yield 3^4 = 81 different cards. 
This gives us vectors in 4d space that tells us about the card. Each card has a number between 1 and 3, a color: red, green or purple, 
a shape: oval, diamond or squiggle and a shading: solid, striped or empty. For every attribute they all have to be the same or different. 
Thus, you could have 3 vectors, all with element x_1, y_1 and z_1 and the sum has to equal 0 in mod 3. Those are the rules of this game.  

How the program works (For codes open:
So how does the program function and what are it’s features. Here we’ll explain the program in the order of use case. To begin, 
the requirements are python 3.12 and no older. Also, you need to have the latest pygame install. Below you can see the gamewindow. 
We will now explain what everything does. Also, to launch the game, press Ctrl + Alt + N in main.py. If that yields an error, when in main, 
open a terminal in with Ctrl + Shift + ‘. In the powershell run the command: “py Main.py”. If all fails, make sure that pygame is installed 
and your python is no older than 3.12.10. 

The display show some useful information. Such as the time left. This starts at 60 seconds. When it hits zero, all cards are reset and the computer gains a point, 
unless the user finds a set or sees there are no sets, beating the computer. If the user finds a set or sees there are no sets. He gains a point if he finds a set and 
gains 10 if there are no sets. This is added to the counter T2 and T3. When the user presses the button B16, further explanation in the subsection Buttons, the revealed 
hint is displayed in T4.  

The buttons are marked with the letter B followed by a number. Let's begin with the cards itself. If you see a SET, the user is expected to click the card. It will highlight 
yellow to show it has been selected. As soon as 3 cards have been selected, they will unselect, and a point is added to T2, if it is a SET. 
Next we have the Save button (B13). When pressed, it will prompt the user to select and name the save file. The standard folder is “location_of_install\\SET\\Saves”. 
Then we have the Load button (B14). This will save the current cards that are displayed, total point, computer points and if you press the No Sets button. To load a save, 
the user is prompted to choose a file. The standard directory is the savefolder and loads the above data. We then have the gameplay related buttons. To start, we have the No Sets button. 
This is used when the users suspects there are no sets. When pressed and there are no sets, the user is awarded with 10 points, since this is super rare. Else, the computer gains a point. 
Lastly, we have a reveal button. If you are stuck, it will simply display an SET. This is useful if you are programming a game that you don’t know how to play. It will add a point to the 
computer as well. 
