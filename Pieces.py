class Piece:

  BLACK = 'b'
  WHITE = 'w'

  def __init__(self, color):
    if (color != Piece.BLACK and color != Piece.WHITE):
      raise ValueError("color must be {} or {}".format(Piece.BLACK, Piece.WHITE))

    self.color = color

class Tour(Piece):

  def __init__(self, color):
    # appeler la classe mère

  def is_move_valid(self, board, fromCell, toCell):
    # vérification que le mouvement est possible compte tenu de la
    # disposition des pièces sur l'échiquier
    return False

class Cavalier(Piece):

  def __init__(self, color):
    # appeler la classe mère

  def is_move_valid(self, board, fromCell, toCell):
    # vérification que le mouvement est possible compte tenu de la
    # disposition des pièces sur l'échiquier
    return False

class Fou(Piece):

  def __init__(self, color):
    # appeler la classe mère

  def is_move_valid(self, board, fromCell, toCell):
    # vérification que le mouvement est possible compte tenu de la
    # disposition des pièces sur l'échiquier
    return False

class Reine(Piece):

  def __init__(self, color):
    # appeler la classe mère

  def is_move_valid(self, board, fromCell, toCell):
    # vérification que le mouvement est possible compte tenu de la
    # disposition des pièces sur l'échiquier
    return False

class Roi(Piece):

  def __init__(self, color):
    # appeler la classe mère

  def is_move_valid(self, board, fromCell, toCell):
    # vérification que le mouvement est possible compte tenu de la
    # disposition des pièces sur l'échiquier
    return False

class Pion(Piece):

  def __init__(self, color):
    # appeler la classe mère

  def is_move_valid(self, board, fromCell, toCell):
    # vérification que le mouvement est possible compte tenu de la
    # disposition des pièces sur l'échiquier
    return False

