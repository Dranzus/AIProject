import numpy as np
from PIL.ImageEnhance import Color
from numpy import ndarray

import constants
from agentsearch.state import State
from agentsearch.action import Action


class WarehouseState(State[Action]):

    def __init__(self, matrix: ndarray, rows, columns):
        super().__init__()
        # TODO

        self.rows = rows
        self.columns = columns
        self.matrix = matrix
        value = constants.FORKLIFT

    # se der erro igualar a -1?? aula

    def can_move_up(self) -> bool:
        # TODO
        # pode virar se nao for a primeira linha e se nao tiver prateleira ou produto
        return self.fkLiftPositionLine != 0 and self.matrix[self.fkLiftPositionLine - 1][
            self.fkLiftPositionColumn] != constants.SHELF and self.matrix[self.fkLiftPositionLine - 1][
            self.fkLiftPositionColumn] != constants.PRODUCT

    def can_move_right(self) -> bool:
        # TODO
        # pode virar se nao for a ultima coluna e se nao tiver prateleira ou produto
        return self.fkLiftPositionColumn != self.columns - 1 and self.matrix[self.fkLiftPositionLine][self.fkLiftPositionColumn + 1] != constants.SHELF and self.matrix[self.fkLiftPositionLine][self.fkLiftPositionColumn + 1] != constants.PRODUCT
        # pass

    def can_move_down(self) -> bool:
        # TODO
        # pode virar se nao for a ultima linha e se nao tiver prateleira ou produto
        return self.fkLiftPositionLine != self.rows - 1 and self.matrix[self.fkLiftPositionLine + 1][
            self.fkLiftPositionColumn] != constants.SHELF and self.matrix[self.fkLiftPositionLine + 1][
            self.fkLiftPositionColumn] != constants.PRODUCT
        pass

    def can_move_left(self) -> bool:
        # TODO
        # pode virar se nao for a primeira coluna e se nao tiver prateleira ou produto
        return self.fkLiftPositionColumn != 0 and self.matrix[self.fkLiftPositionLine][self.fkLiftPositionColumn - 1] != constants.SHELF and self.matrix[self.fkLiftPositionLine][self.fkLiftPositionColumn - 1] != constants.PRODUCT
        pass

    def move_up(self) -> None:
        self.fkLiftPositionLine -= 1

    def move_right(self) -> None:
        self.fkLiftPositionColumn += 1

    def move_down(self) -> None:
        self.fkLiftPositionLine += 1

    def move_left(self) -> None:
        self.fkLiftPositionColumn -= 1

    def get_cell_color(self, row: int, column: int) -> Color:
        if self.matrix[row][column] == constants.EXIT:
            return constants.COLOREXIT

        if self.matrix[row][column] == constants.PRODUCT_CATCH:
            return constants.COLORSHELFPRODUCTCATCH

        if self.matrix[row][column] == constants.PRODUCT:
            return constants.COLORSHELFPRODUCT

        switcher = {
            constants.FORKLIFT: constants.COLORFORKLIFT,
            constants.SHELF: constants.COLORSHELF,
            constants.EMPTY: constants.COLOREMPTY
        }
        return switcher.get(self.matrix[row][column], constants.COLOREMPTY)

    def __str__(self):
        matrix_string = str(self.rows) + " " + str(self.columns) + "\n"
        for row in self.matrix:
            for column in row:
                matrix_string += str(column) + " "
            matrix_string += "\n"
        return matrix_string

    def __eq__(self, other):
        if isinstance(other, WarehouseState):
            return self.fkLiftPositionLine == other.fkLiftPositionLine \
                and self.fkLiftPositionColumn == other.fkLiftPositionColumn
        return NotImplemented

    def __hash__(self):
        return hash(self.matrix.tostring())
