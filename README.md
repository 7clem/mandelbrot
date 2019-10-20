# mandelbrot
the fractal - pygame

I indend to learn pygame and draw the mandelbrot set while using git and github to synchonise code between various developement machines.

The mandelbrot set lives in the complex plane between -2 < x < 2 and -2 < y < 2.
The color of each point C is determined by the number of iterations that the suite Z defined by :
<ul>
<li>Z0 = 0
<li>Zn+1 = Z*Z + C<br>
</ul>

<p>takes to diverge, or simply for it's module to exceed 2.

<ol>
  <li>Start with a brute force implementation that calculates for each point. DONE
  <li>Speed up calculation by assuming the property that if points of the perimeter of a region have the same value than all of its interior has the same value also. WORK IN PROGRESS
  <li>Have differents threads compute differents regions in parallel. TODO
</ol>
