import json
import csv


class ConverterService:
    def csv_to_json(self, csv_file_path):
        """Convierte un archivo CSV a JSON y lo guarda en la misma ubicación"""
        json_file_path = csv_file_path.replace(".csv", ".json")

        with open(csv_file_path, mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]  # Mantener datos como strings

        # Construir el contenido JSON con saltos de línea entre los elementos
        rows = [json.dumps(row) for row in data]
        formatted_data = ",\n".join(rows)
        formatted_json = f"[{formatted_data}]"

        with open(json_file_path, mode="w") as json_file:
            json_file.write(formatted_json)

        return json_file_path

    def json_to_csv(self, json_file_path):
        """Convierte un archivo JSON a CSV y lo guarda en la misma ubicación"""
        csv_file_path = json_file_path.replace(".json", ".csv")

        # Leer datos del archivo JSON
        with open(json_file_path, mode="r") as json_file:
            data = json.load(json_file)

        # Escribir los datos en un archivo CSV
        with open(csv_file_path, mode="w", newline="") as csv_file:
            if data:
                csv_writer = csv.DictWriter(
                    csv_file, fieldnames=data[0].keys()
                )
                csv_writer.writeheader()
                csv_writer.writerows(data)

        return csv_file_path
