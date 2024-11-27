import json
import csv


class ConverterService:
    def csv_to_json(self, csv_file_path):
        """Convierte un archivo CSV a JSON y lo guarda en la misma ubicación"""
        json_file_path = csv_file_path.replace(".csv", ".json")

        # Crear un archivo JSON vacío
        with open(json_file_path, mode="w") as json_file:
            # Crear archivo JSON vacío
            json.dump([], json_file)

        return json_file_path

    def json_to_csv(self, json_file_path):
        """Convierte un archivo JSON a CSV y lo guarda en la misma ubicación"""
        csv_file_path = json_file_path.replace(".json", ".csv")

        # Crear un archivo CSV vacío
        with open(csv_file_path, mode="w", newline="") as csv_file:
            # csv_writer espera un objeto iterable
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([])

        return csv_file_path
