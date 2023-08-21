import unittest
import libcplx as lc
import math

class TestSCplx(unittest.TestCase):

    def test_Suma1(self):
        # (3+2i) + (-5 + 5.2i) = -2 + 7.2i
        a = (3, 2)
        b = (-5, 5.2)
        self.assertEqual(lc.sumacplx(a, b), (-2, 7.2))


    def test_Suma2(self):

        c1 = (3, 5)
        c2 = (-2.6, 6.8)
        suma = lc.sumacplx(c1, c2)
        self.assertAlmostEqual(suma[0], 0.4)
        self.assertAlmostEqual(suma[1], 11.8)

    def test_Resta(self):
        # (3+2i) - (-5 + 5.2i) = 8 + -3.2i
        c1 = (3, 2)
        c2 = (-5, 5.2)
        resta = lc.restcplx(c1, c2)
        self.assertAlmostEqual(resta[0], 8)
        self.assertAlmostEqual(resta[1], -3.2)

    def test_Resta2(self):
        c1 = (3, 5)
        c2 = (-2.6, 6.8)
        resta = lc.restcplx(c1, c2)
        self.assertAlmostEqual(resta[0], 5.6)
        self.assertAlmostEqual(resta[1], -1.8)

    def test_multi(self):
        # (3+2i) x (-5 + 5.2i) = -25.4 + 5.6i
        c1 = (3, 2)
        c2 = (-5, 5.2)
        mult = lc.mutcplx(c1, c2)
        self.assertAlmostEqual(mult[0], -25.4)
        self.assertAlmostEqual(mult[1], 5.6)

    def test_multi2(self):
        c1 = (3, 5)
        c2 = (-2.6, 6.8)
        mult = lc.mutcplx(c1, c2)
        self.assertAlmostEqual(mult[0], -41.8)
        self.assertAlmostEqual(mult[1], 7.4)

    def test_divi(self):
        # (3+2i) / (-5 + 5.2i) = -0.08839354342813219 + -0.49192928516525747i
        c1 = (3, 2)
        c2 = (-5, 5.2)
        divi = lc.divcplx(c1, c2)
        self.assertAlmostEqual(divi[0], -0.08839354342813219)
        self.assertAlmostEqual(divi[1], -0.49192928516525747)

    def test_divi2(self):
        c1 = (3, 5)
        c2 = (-2.6, 6.8)
        divi = lc.divcplx(c1, c2)
        self.assertAlmostEqual(divi[0], 0.4943396226415095)
        self.assertAlmostEqual(divi[1], -0.6301886792452831)

    def test_modulo(self):
        # modulo = (3*3 + 2i*2i)**(0.5) = 3.605551275463989
        c1 = (3, 2)
        self.assertAlmostEqual(lc.modulcplx(c1), 3.605551275463989)

    def test_modulo2(self):
        c1 = (-2.6, 6.8)
        self.assertAlmostEqual(lc.modulcplx(c1), 7.280109889280518)

    def test_conjugado(self):
        #Conjugado = (3, 2 ) = (3 , -2)
        c1 = (3, 2)
        self.assertAlmostEqual(lc.conjucplx(c1), (3, -2))

    def test_conjugado2(self):
        c1 = (-2.6, 6.8)
        self.assertAlmostEqual(lc.conjucplx(c1), (-2.6, -6.8))

    def test_ConverPolarCart(self):
        #  a = r * cos(theta)
        #  b = r * cos(theta)
        c1 = (4.24, math.pi / 4)
        conver = lc.ConverPolarCart(c1)
        self.assertAlmostEqual(conver[0], 2.998132752230962)
        self.assertAlmostEqual(conver[1], 2.998132752230962)

    def test_ConverPolarCart2(self):
        c1 = (4.24, math.pi/6)
        conver = lc.ConverPolarCart(c1)
        self.assertAlmostEqual(conver[0], 3.67194771204602)
        self.assertAlmostEqual(conver[1], 2.1199999999999997)

    def test_ConverCartPolar(self):
        # r = (a**2 +b**2)**0.5
        # theta = artan(b/a)
        c1 = (3, 2)
        conver = lc.ConverCartPolar(c1)
        self.assertAlmostEqual(conver[0], 13)
        self.assertAlmostEqual(conver[1], 0.5880026035475675)

    def test_ConverCartPolar2(self):
        c1 = ((-2.6, 6.8))
        conver = lc.ConverCartPolar(c1)
        self.assertAlmostEqual(conver[0], 52.99999999999999)
        self.assertAlmostEqual(conver[1], 1.9359977765830696)

    def test_fase(self):
        # theta = artan(b/a)
        c1 = (3, 2)
        self.assertAlmostEqual(lc.retornarFase(c1), 0.5880026035475675)

    def test_fase2(self):
        c1 = (-2.6, 6.8)
        self.assertAlmostEqual(lc.retornarFase(c1), 1.9359977765830696)


if __name__ == '__main__':
    unittest.main()