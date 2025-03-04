# Actividad 2.4 - Optimización en conjunto grande de datos
# 
# 21 de febrero de 2025
# 
#  Mónica Lizette Cardona Solís
# Fernando Mendoza Velasco 

from pulp import *


INPUT_CSV_PATH = "actividades/2_4/mochila_alumno.csv"
OUTPUT_CSV_PATH = "actividades/2_4/mochila_resultado.csv"


def knapsack_solve(weights, prices, capacity):
    """
    Parámetros
    ----------
    weights : [int]
        Una lista con el peso de cada objeto.
    prices : [int]
        Una lista con el precio de cada objeto.
    capacity : int
        El peso máximo que puede cargar la mochila.

    Regresa: 
        Un diccionario con las llaves 'best_pick', 
        'best_price', 'avg_weight', 'avg_price'.
    """
    n = len(weights)
    x = [LpVariable(f"x{i}", cat="Binary") for i in range(n)]

    problem = LpProblem(sense=LpMaximize)

    problem += prices[0] * x[0] + prices[1] * x[1] + prices[2] * x[2] + prices[3] * x[3] + prices[4] * x[4]
    
    problem += weights[0] * x[0] + weights[1] * x[1] + weights[2] * x[2] + weights[3] * x[3] + weights[4] * x[4] <= capacity
    
    status = problem.solve()

    print(LpStatus[status])

    best_picks = [int(value(x_i)) for x_i in x]

    best_price = sum(int(best_picks[i] * prices[i]) for i in range(n))

    return {
        "best_picks": best_picks,
        "best_price": best_price,
        "avg_weight": sum(weights) / len(weights),
        "avg_price": sum(prices) / len(prices),
    }


def knapsack_parse(line: str):
    """
    Parámetros
    ----------
    line : str
        Una línea del archivo .csv.

    Regresa:
        Un diccionario con las llaves 'weights', 'prices'
        'capacity'. 
    """
    line_values = line.split(",")

    weight_values = line_values[1].strip().removeprefix("[").removesuffix("]")
    weights = list(map(int, weight_values.split()))
    
    price_values = line_values[2].strip().removeprefix("[").removesuffix("]")
    prices = list(map(int, price_values.split()))

    max_capacity = int(line_values[3])

    return {
        "weights": weights,
        "prices": prices,
        "capacity": max_capacity
    }


def format_list(list, separator=" "):
    return "[" + separator.join([str(item) for item in list]) + "]"


if __name__ == "__main__":
    with open(INPUT_CSV_PATH, "r", encoding="utf-8") as input_csv:
        with open(OUTPUT_CSV_PATH, "w+", encoding="utf-8") as output_csv:
            # Leer el encabezado
            output_csv.write(f"{input_csv.readline().strip()}\n")

            for line in input_csv:
                problem_id = int(line.split(",")[0])
                inputs = knapsack_parse(line)

                solution = knapsack_solve(inputs["weights"], inputs["prices"], inputs["capacity"])

                cost_function = " + ".join([f"{inputs['prices'][i]}*x{i}" for i in range(len(solution["best_picks"]))])
                constraint = " + ".join([f"{inputs['weights'][i]}*x{i}" for i in range(len(solution["best_picks"]))]) + f" <= {inputs['capacity']}"

                output_values = [
                    problem_id,
                    format_list(inputs["weights"]),
                    format_list(inputs["prices"]),
                    inputs["capacity"],
                    format_list(solution["best_picks"]),
                    solution["best_price"],
                    solution["avg_weight"],
                    solution["avg_price"],
                    cost_function,
                    constraint,
                ]

                output_csv.write(f"{','.join(map(str, output_values))}\n")
