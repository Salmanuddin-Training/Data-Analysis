{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "#property() function\n",
    "class Student:\n",
    "    def __init__(self):\n",
    "        self.__name=''\n",
    "        \n",
    "    def setname(self,name):\n",
    "        print('setname() runs.....')\n",
    "        self.__name=name\n",
    "    \n",
    "    def getname(self):\n",
    "        print('getname() runs.....')\n",
    "        return self.__name\n",
    "    \n",
    "    def delname(self):\n",
    "        print('delname() runs.....')\n",
    "        del self.__name\n",
    "    \n",
    "    name=property(getname, setname)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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