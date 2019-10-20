# mandelbrot
the fractal - pygame

I indend to learn pygame and draw the mandelbrot set while using git and github to synchonise code between various developement machines.

The mandelbrot set lives in the complex plane between -2 < x < 2 and -2 < y < 2.
The color of each point C is determined by the number of iterations that the suite Z defined by :
{
Z0 = 0
Zn+1 = Z*Z +C
}

takes to diverge, or simply for it's module to exceed 2.

Start with a brute force implementation that calculates for each point.
