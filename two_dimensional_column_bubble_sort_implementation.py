import random
from typing import List, Optional


class TDCBSI:
    """
    TDCBSI - Two Dimensional Column  Bubble Sort Implementation.
    Даний клас реалізує класичний алгоритм сортування стовпців двовимірного масиву методом обміну.
    Розмірність масиву та всі елементи генеруються за допомогою випадкових чисел.
    """
    def __init__(self,
                 matrix_dimension: Optional[List[int]] = None,
                 output_file_path: Optional[str] = None) -> None:
        """
        Створює новий об'єкт класу.

        Parameters:
        matrix_dimension (list): Розмірність матриці,
        якщо не задана, генерується випадкова розмірність від 0 до 100 (рядків та стовпців).

        output_file_path (str): Шлях до файлу, у який буде записано матрицю до і після сортування (якщо заданий).
        """
        self.dimension = [random.randint(0, 100), random.randint(0, 100)] \
            if matrix_dimension is None else matrix_dimension
        self.matrix: List[List[int]]
        self.output_file_path = output_file_path

    def _bubble_column_sort(self) -> None:
        """ Метод сортування стовпців бульбашкою двовимірного масиву (матриці). """
        # Зовнішній цикл по стовпцях.
        for col in range(self.dimension[1]):
            # Основний цикл для сортування бульбашкою по рядках.
            for row in range(self.dimension[0]):
                # Внутрішній цикл для порівняння елементів.
                for i in range(0, self.dimension[0] - row - 1):
                    # Порівняння та обмін елементів
                    if self.matrix[i][col] > self.matrix[i + 1][col]:
                        self.matrix[i][col], self.matrix[i + 1][col] = self.matrix[i + 1][col], self.matrix[i][col]

    def _fill_matrix(self) -> None:
        """ Метод заповнення двовимірного масиву (матриці) випадковими числами від 0 до 100. """
        self.matrix = [[random.randint(0, 100) for _ in range(self.dimension[1])] for _ in range(self.dimension[0])]

    def _print_matrix(self) -> None:
        """ Метод для виводу двовимірного масиву (матриці) у консоль. """
        for row in self.matrix:
            print(' '.join(f'{element:>5}' for element in row))

    def _write_to_file(self) -> None:
        """ Метод для запису матриці у файл. """
        with open(self.output_file_path, '+a') as file:
            for row in self.matrix:
                file.write(' '.join(f'{element:>5}' for element in row) + '\n')
            file.write('\n\n\n')

    def start(self) -> None:
        """ Основний метод заповнення матриці та запуску сортування. """
        # Якщо вказан шлях к файлу, відкриємо його з режимом "w" для очищення.
        if self.output_file_path is not None:
            open(self.output_file_path, "w").close()
        # Заповнимо матрицю.
        self._fill_matrix()
        print(f'Не сортована матриця {self.dimension}:')
        self._print_matrix()
        # Якщо вказан шлях к файлу, записуємо не сортовану матрицю.
        if self.output_file_path is not None:
            self._write_to_file()
        # Сортуємо матрицю.
        self._bubble_column_sort()
        print(f'Сортована матриця {self.dimension}:')
        self._print_matrix()
        # Якщо вказан шлях к файлу, записуємо сортовану матрицю.
        if self.output_file_path is not None:
            self._write_to_file()


if __name__ == '__main__':
    TDCBSI(output_file_path='./output.txt').start()
