import unittest
from unittest import TestCase
from ClasePalindromo import Palindromo

class test(unittest.TestCase):
    __palindromo= None
    __palindromo2=None
    __palindromo3=None
    def setUp(self):
        self.__palindromo = Palindromo('meneM')
        self.__palindromo2 = Palindromo('ANA')
        self.__palindromo3 = Palindromo('NIsMAN')
    def test_polindromo(self):
        self.assertEqual(self.__palindromo.esPalindromo(),True)
        self.assertEqual(self.__palindromo2.esPalindromo(),True)
        self.assertEqual(self.__palindromo3.esPalindromo(),False) 
          

if __name__ == '__main__':
    unittest.main()
   