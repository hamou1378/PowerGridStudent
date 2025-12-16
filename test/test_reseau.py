import unittest
import xmlrunner

from Reseau import Reseau
from Terrain import Terrain, Case

class TestReseau(unittest.TestCase):

    def test_definition_entree(self):
        r = Reseau()

        r.noeuds[1] = (0, 0)

        r.definir_entree(1)
        self.assertEqual(r.noeud_entree, 1)

        r.definir_entree(2)
        self.assertEqual(r.noeud_entree, -1)

        
    def test_ajout_noeud(self):
        r = Reseau()

    # Ajout d'un noeud avec clé >= 0
        r.ajouter_noeud(1, (0, 0))
        self.assertIn(1, r.noeuds)
        self.assertEqual(r.noeuds[1], (0, 0))

    # Ajout d'un noeud clé 0 (ton code l'accepte)
        r.ajouter_noeud(0, (1, 1))
        self.assertIn(0, r.noeuds)
        self.assertEqual(r.noeuds[0], (1, 1))

    # Ajout d'un noeud déjà existant → ton code écrase
        r.ajouter_noeud(1, (5, 5))
        self.assertEqual(r.noeuds[1], (5, 5))

    # Clé négative → ne doit rien ajouter
        r.ajouter_noeud(-10, (9, 9))
        self.assertNotIn(-10, r.noeuds)


    def test_ajout_arc(self):
        r = Reseau()

        r.noeuds[1] = (0, 0)
        r.noeuds[2] = (1, 0)

        r.ajouter_arc(2, 1)
        self.assertIn((1, 2), r.arcs)  

        r.ajouter_arc(1, 2)
        self.assertEqual(len(r.arcs), 1)

        r.ajouter_arc(1, 3)
        self.assertEqual(len(r.arcs), 1)


    def test_validation_correcte(self):
        r = Reseau()
        r.noeuds[0] = (0, 0)
        r.noeud_entree = 0

        r.noeuds[1] = (1, 0)
        r.arcs.append((0, 1))

        r.noeuds[2] = (0, 1)
        r.arcs.append((0, 2))

        r.noeuds[3] = (0, 2)
        r.arcs.append((2, 3))

        r.noeuds[4] = (1, 2)
        r.arcs.append((3, 4))

        self.assertTrue(r.valider_reseau())

    def test_validation_incorrecte(self):
        r = Reseau()
        r.noeuds[0] = (0, 0)
        r.noeud_entree = 0

        r.noeuds[1] = (1, 0)
        r.arcs.append((0, 1))

        r.noeuds[2] = (0, 1)
        r.arcs.append((0, 2))

        r.noeuds[3] = (0, 2)
        r.arcs.append((2, 3))

        r.noeuds[4] = (1, 2)

        self.assertFalse(r.valider_reseau())

    def test_distribution_correcte(self):
        r = Reseau()
        r.noeuds[0] = (0, 0)
        r.noeud_entree = 0

        r.noeuds[1] = (1, 0)
        r.arcs.append((0, 1))

        r.noeuds[2] = (0, 1)
        r.arcs.append((0, 2))

        r.noeuds[3] = (0, 2)
        r.arcs.append((2, 3))

        r.noeuds[4] = (1, 2)
        r.arcs.append((3, 4))

        t = Terrain()
        t.cases = [
                [Case.ENTREE, Case.VIDE, Case.VIDE],
                [Case.CLIENT, Case.VIDE, Case.CLIENT],
        ]

        self.assertTrue(r.valider_distribution(t))

    def test_distribution_incorrecte(self):
        r = Reseau()
        r.noeuds[0] = (0, 0)
        r.noeud_entree = 0

        r.noeuds[1] = (1, 0)
        r.arcs.append((0, 1))

        r.noeuds[2] = (0, 1)
        r.arcs.append((0, 2))

        r.noeuds[3] = (0, 2)
        r.arcs.append((2, 3))

        r.noeuds[4] = (1, 2)
        r.arcs.append((3, 4))

        t = Terrain()
        t.cases = [
                [Case.ENTREE, Case.VIDE, Case.VIDE],
                [Case.CLIENT, Case.CLIENT, Case.CLIENT],
        ]

        self.assertFalse(r.valider_distribution(t))

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="test-reports"))