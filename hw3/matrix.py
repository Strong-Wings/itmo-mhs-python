import numpy as np
from typing import List, Union


class NDArrayOperatorsMixin:
    def __add__(self, other: 'Matrix') -> 'Matrix':
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError(f"Неверные размеры для сложения: ({self.rows}x{self.cols}) + ({other.rows}x{other.cols})")

        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)

        return Matrix(result)

    def __mul__(self, other: 'Matrix') -> 'Matrix':
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError(f"Неверные размеры для покомпонентного умножения: ({self.rows}x{self.cols}) * ({other.rows}x{other.cols})")

        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] * other.data[i][j])
            result.append(row)

        return Matrix(result)

    def matmul(self, other: 'Matrix') -> 'Matrix':
        if self.cols != other.rows:
            raise ValueError(f"Неверные размеры для матричного умножения: ({self.rows}x{self.cols}) @ ({other.rows}x{other.cols})")

        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                sum_val = 0
                for k in range(self.cols):
                    sum_val += self.data[i][k] * other.data[k][j]
                row.append(sum_val)
            result.append(row)

        return Matrix(result)


class FileWriterMixin:
    def to_file(self, filename: str):
        with open(filename, 'w') as f:
            print(self, file=f)


class StrMixin:
    def __str__(self) -> str:
        if self.rows == 0 or self.cols == 0:
            return "[]"
        result = []
        max_len = 1
        for i in range(self.rows):
            for j in range(self.cols):
                max_len = max(max_len, len(str(self.data[i][j])))
        for i in range(self.rows):
            row_str = "["
            for j in range(self.cols):
                val = self.data[i][j]
                row_str += f"{int(val):{max_len}d}"
                if j < self.cols - 1:
                    row_str += " "
            row_str += "]"
            if i < self.rows - 1:
                row_str += "\n "
            result.append(row_str)
        return "[" + "".join(result) + "]"


class PropertyMixin:
    @property
    def rows(self) -> int:
        return self._rows

    @rows.setter
    def rows(self, value: int):
        if value < 0:
            raise ValueError("Количество строк не может быть отрицательным")
        self._rows = value

    @property
    def cols(self) -> int:
        return self._cols

    @cols.setter
    def cols(self, value: int):
        if value < 0:
            raise ValueError("Количество столбцов не может быть отрицательным")
        self._cols = value

    @property
    def data(self) -> List[List[float]]:
        return self._data

    @data.setter
    def data(self, value: List[List[float]]):
        if not value:
            self._data = []
            self._rows = 0
            self._cols = 0
        else:
            self._rows = len(value)
            self._cols = len(value[0]) if self._rows > 0 else 0
            for row in value:
                if len(row) != self._cols:
                    raise ValueError("Все строки должны иметь одинаковую длину")
            self._data = value


class HashMixin:
    matmul_cache = {}

    def __hash__(self) -> int:
        if not self.data:
            return 0
        total_sum = sum(sum(row) for row in self.data)
        return total_sum % 9999997

    def __matmul__(self, other: 'Matrix') -> 'Matrix':
        cache_key = hash(self) * hash(other)
        if cache_key in self.matmul_cache:
            return self.matmul_cache[cache_key]
        result = self.matmul(other)
        self.matmul_cache[cache_key] = result
        return result

class Matrix(HashMixin, NDArrayOperatorsMixin, FileWriterMixin, StrMixin, PropertyMixin):
    def __init__(self, data: Union[List[List[float]], np.ndarray]):
        if isinstance(data, np.ndarray):
            self.data = data.tolist()
        else:
            self.data = data
