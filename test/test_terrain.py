import unittest
import xmlrunner

from Terrain import Terrain, Case

class TestTerrain(unittest.TestCase):

    def test_chargement(self):
        t = Terrain()
        t.charger("terrains/t1.txt")

    # Le terrain doit avoir une hauteur > 0
        self.assertGreater(t.hauteur, 0)

    # Le terrain doit avoir une largeur > 0
        self.assertGreater(t.largeur, 0)

    # cases doit contenir hauteur lignes
        self.assertEqual(len(t.cases), t.hauteur)

    # chaque ligne doit avoir largeur colonnes
        for ligne in t.cases:
            self.assertEqual(len(ligne), t.largeur)

    # vérifier qu'on trouve au moins une ENTREE
        self.assertNotEqual(t.get_entree(), (-1, -1))

    # vérifier qu'il y a au moins 1 client
        clients = t.get_clients()
        self.assertGreater(len(clients), 0)

    # vérification de types : uniquement Cases
        for ligne in t.cases:
            for c in ligne:
                self.assertIsInstance(c, Case)


    def test_accesseur(self):
        t = Terrain()
        t.cases = [
                [Case.ENTREE, Case.VIDE, Case.VIDE],
                [Case.CLIENT, Case.CLIENT, Case.CLIENT],
        ]
        self.assertEqual(t[0][0], Case.ENTREE)
        self.assertEqual(t[0][1], Case.VIDE)
        self.assertEqual(t[1][2], Case.CLIENT)

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="test-reports"))