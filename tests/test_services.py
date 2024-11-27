from converter.services import ConverterService
import pytest


class TestConverterService:

    def _generate_folder(self):
        """Generar una carpeta de archivos de prueba si no existe"""
        import os

        if not os.path.exists("tests/test_files"):
            os.makedirs("tests/test_files")

    # Método de fábrica
    def _generate_temp_csv(self, file_path="tests/test_files/test.csv"):
        """Generar un archivo CSV temporal y las carpetas necesarias"""
        self._generate_folder()
        with open("tests/test_files/test.csv", "w") as f:
            f.write("id, name, age\n")
            f.write("1, John Doe, 30\n")
            f.write("2, Jane Smith, 25\n")
            f.write("3, Alice Johnson, 35\n")

    # Método de fábrica
    def _generate_temp_json(self, file_path="tests/test_files/test.json"):
        self._generate_folder()
        """Generar un archivo JSON temporal y las carpetas necesarias"""
        with open("tests/test_files/test.json", "w") as f:
            f.write('[{"id": 1, "name": "John Doe", "age": 30},')
            f.write('{"id": 2, "name": "Jane Smith", "age": 25},')
            f.write('{"id": 3, "name": "Alice Johnson", "age": 35}]')

    # Método de fábrica
    def _clean_temp_files(self):
        """Eliminar los archivos temporales generados"""
        import os

        # Identificar los archivos en la carpeta de prueba
        folder = os.listdir("tests/test_files")

        # Eliminar los archivos CSV y JSON
        for file in folder:
            if file.endswith((".csv", ".json")):
                os.remove(f"tests/test_files/{file}")

    def test_ensure_json_file_is_generated(self):
        """Prueba que el comportamiento genere un archivo JSON
        1. Debe existir el archivo en la ruta especificada
        2. El archivo generado tiene la extensión .json
        """
        # Arrange
        self._generate_temp_csv()
        sut = ConverterService()

        # Act
        result = sut.csv_to_json("tests/test_files/test.csv")

        # Assert
        assert result == "tests/test_files/test.json"

        # Teardown
        self._clean_temp_files()

    def test_ensure_csv_file_is_generated(self):
        """Prueba que el comportamiento genere un archivo CSV
        1. Debe existir el archivo en la ruta especificada
        2. El archivo generado tiene la extensión .csv
        """
        # Arrange
        self._generate_temp_json()
        sut = ConverterService()

        # Act
        result = sut.json_to_csv("tests/test_files/test.json")

        # Assert
        assert result == "tests/test_files/test.csv"

        # Teardown
        self._clean_temp_files()

    def test_json_to_csv_content(self):
        """Prueba que el contenido del archivo JSON forme parte del archivo CSV"""
        # Arrange
        self._generate_temp_json()
        sut = ConverterService()

        # Resultado esperado
        expected_result = "id,name,age\n"
        expected_result += "1,John Doe,30\n"
        expected_result += "2,Jane Smith,25\n"
        expected_result += "3,Alice Johnson,35\n"

        # Act
        result = sut.json_to_csv("tests/test_files/test.json")

        # Assert
        with open(result, "r") as f:
            content = f.read()
            assert content == expected_result

        # Teardown
        self._clean_temp_files()

    def test_csv_to_json_content(self):
        """Prueba que el contenido del archivo CSV forme parte del archivo JSON"""
        # Arrange
        self._generate_temp_csv()
        sut = ConverterService()

        # Resultado esperado
        expected_result = (
            '[{"id": "1", " name": " John Doe", " age": " 30"},\n'
        )
        expected_result += (
            '{"id": "2", " name": " Jane Smith", " age": " 25"},\n'
        )
        expected_result += (
            '{"id": "3", " name": " Alice Johnson", " age": " 35"}]'
        )

        # Act
        result = sut.csv_to_json("tests/test_files/test.csv")

        # Assert
        with open(result, "r") as f:
            content = f.read()
            assert content == expected_result

        # Teardown
        self._clean_temp_files()
