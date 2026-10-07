def print_equations(Xi, names):
    variables = ["x", "y", "z"]

    for i, variable in enumerate(variables):
        equation = f"d{variable}/dt = "

        terms = []

        for coefficient, name in zip(Xi[:, i], names):
            if abs(coefficient) > 1e-10:
                terms.append(f"{coefficient:+.4f} {name}")

        equation += " ".join(terms)

        print(equation)
