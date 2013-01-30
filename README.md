python-coursework
=================

Python Coursework

* In order to reach a final solution for this coursework, I used the technique of top-down design. I chose this type of design method because it makes creating of a complex program easier to do by breaking the problem into smaller and smaller parts. This also represents a good way to make a program easier to test and to be understood by other programmers.<br>
* First of all, I created the main() function which represents the highest level of the program. Here I make a call to the getInputs() function which returns the validated input of the user. After that I begin to draw the patchwork using the drawPatchWork() function which makes a call to two separate functions, one for each patch design and also collects and stores into a list, important information about the drawn patches, like : patch type and patch colour which will be used for the advanced future.<br> 
* Both drawPatch1() and drawPatch2() functions make a call to the drawBackground() function before creating the actual design, in order to set the background and the outline of the designs which is also useful for the advanced future because when we will switch the patch designs we need to completly overwrite the current design.<br>
* Having to complete a little bit more complex tasks, the drawPatch2() function makes a necessary number of calls to the drawBoat() function which will draw step by step the entire design for the 2nd patch. In order to avoid the repetition of code and to make the design more clear, the drawBoat() function also calls three separate functions: drawTriangle(), drawStick(), drawTrapezoid() each of them completing the design of a single part of the mother function.<br>
* Finally, after the patchwork is designed, the switchPatches() function allows the user to switch patches by getting the information where the user has clicked using the getClick() function, then updating the patch list with the switched patch type and patch colour, and drawing the patches in their switched places using the drawNewPatch() function which re-uses the previously created functions drawPatch1() and drawPatch2().<br>

##Marks

I received 95% for this coursework.
