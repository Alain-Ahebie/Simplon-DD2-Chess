from Pieces import *

class Board:

  def __init__(self):
    # initialiser les cellules de l'échiquier
    pass

  def do_move(self, fromCellStr, toCellStr):
    # déplacement d'une pièce
    # les paramètres de la méthode sont de la forme A6, H7, etc...
    
    # créer les objets Cell correspondant aux paramètres

    # vérifier que le déplacement est possible

    # effectuer le déplacement de la pièce

class Cell:

  def __init__(self, line, column):
    # line doit être un entier de 0 à 7
    # column doit être un entier de 0 à 7
    pass

  def to_string(self):
    # retourne la forme string de la cellule, exemple D7
    return None

  def from_string(cellStr):
    # crée un objet cellule à partir de la forme string d'une cellule, exemple D7
    return None

  def is_cell_str_valid(cellStr):
    # Vérifie qu'une cellule de l'échiquier sous forme de string est correct
    # Par exemple is_cell_str_valid('G8') doit renvoyer True et is_cell_str_valid('WTF') doit renvoyer False !

    return False


