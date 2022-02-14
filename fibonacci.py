{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "24e1d8b9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import math\n",
    " \n",
    "def isPerfectSquare(num):\n",
    "   \n",
    "    s =int(math.sqrt(num))\n",
    "    return s*s == num\n",
    " \n",
    "def isFibonacciNumber(n):\n",
    "   \n",
    "    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)\n",
    " \n",
    " \n",
    "n = int(input(\"Enter the number you want to check : \"))\n",
    "if(isFibonacciNumber(n) == True):\n",
    "    print(n, \"is fibonacci number\")\n",
    "else:\n",
    "    print(n  ,\" is not a fibonacci number\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
