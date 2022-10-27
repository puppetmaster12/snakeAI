<h2>A Snake game | Snake AI</h2>
<h3>Overview</h3>
<p>This project is part of my learning experience on machine learning and deep learning. The project is comprised of a regular snake game built with pygame. In addition an AI agent added using Deep Q Learning built using Pytorch. I wanted to learn how to use reinforcement learning in combination with a simple game like snake and improve on it to make it more robust in solving the snake game manouvering.</p>

<h3>Setup</h3>
<b>Python 3.8</b>
<p>I recommend installing <a href="https://www.anaconda.com/products/distribution" target="_blank">Anaconda</a> or venv and setting up a virtual environment before installing the packages</p>
<p><b>Requirements.txt</b>  file contains all the packages. Use pip install -r requirements.txt to install all the packages required for the project.</p>

<h3>Running</h3>
<p>Running the snakeGame.py file runs the regular Snake game. Use the directional arrow keys to play the game. The game currently terminates if you reach a game over status which is if the snake either hits the boundary of the window or hits itself.</p>
<p>Running the agent.py file starts the training of the QLearning model.</p>

<h3>Bugs</h3>
<p>The current AI agent is incapable of converging and falls into the trap of predicting the same move on a loop until it hits itself or the boundary. This maybe a problem with insufficient balance in the reward system.</p>

<h3>TODO</h3>
<ul>
  <li>Build more levels with additional boundaries and mazes for the snake to navigate before reaching the food.</li>
  <li>Improve the AI to reach the food more efficiently.</li>
  <li>Experiment with other algorithms.</li>
</ul>

<h3>Changelog</h3>
<p><b>27/10/2022</b></p>
<p>Added a penalty for 100 moves without food and terminated the frame for 200 moves without food</p>
