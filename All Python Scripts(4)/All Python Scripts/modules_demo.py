{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "directory/folder is created successfully...!\n"
     ]
    }
   ],
   "source": [
    "#Python- OS Module- operating system tasks\n",
    "#creating directory- mkdir()\n",
    "\n",
    "import os\n",
    "os.mkdir(\"e:\\python_session\")\n",
    "print(\"directory/folder is created successfully...!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Rajesh\n"
     ]
    }
   ],
   "source": [
    "#current working directory\n",
    "import os\n",
    "\n",
    "print(os.getcwd())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "e:\\python_session\n"
     ]
    }
   ],
   "source": [
    "#change current working directory\n",
    "import os\n",
    "\n",
    "\n",
    "os.chdir(\"e:\\python_session\")\n",
    "print(os.getcwd())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "C:\\\n"
     ]
    }
   ],
   "source": [
    "#removing directory\n",
    "import os\n",
    "\n",
    "os.chdir(\"c:\")\n",
    "print(os.getcwd())\n",
    "os.rmdir(\"e:\\python_session\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['first.py', 'swatimod.py', '__pycache__']"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#listing files & sub-directories\n",
    "import os\n",
    "\n",
    "os.listdir(\"e:\\pythonscripts\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.5235987755982988\n",
      "2.302585092994046\n",
      "8.0\n",
      "9.0\n",
      "3\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "#Python-Math\n",
    "import math\n",
    "\n",
    "math.pi\n",
    "print(math.radians(30))\n",
    "print(math.log(10))\n",
    "print(math.pow(2,3))\n",
    "print(math.sqrt(81))\n",
    "print(math.ceil(2.7))\n",
    "print(math.floor(2.7))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Python-statistics module\n",
    "\n",
    "import statistics\n",
    "\n",
    "print(statistics.mean([2,5,6,9]))\n",
    "print(statistics.median([1,2,3,4,8,9]))\n",
    "print(statistics.mode([2,5,3,2,8,5,6,2,8,9]))\n",
    "print(statistics.stdev([1,1.5,2,2.5,3,3.5,4,4.5,5]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.3693063937629153\n"
     ]
    }
   ],
   "source": [
    "import statistics\n",
    "\n",
    "print(statistics.stdev([1,1.5,2,2.5,3,3.5,4,4.5,5]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
