
from simplex import *
import dual_problem

if __name__ == '__main__':

    print("\tПрямая задача ЛП:")
    problem = Simplex("input_data.json")
    print(problem)

    # Находим опорное решение.
    problem.reference_solution()
    # Находим оптимальное решение.
    problem.optimal_solution()

    print("\tДвойственная задача ЛП:")
    dual_p = dual_problem.DualProblem("input_data.json")

    # Находим опорное решение.
    dual_p.reference_solution()
    # Находим оптимальное решение.
    dual_p.optimal_solution()
