class calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        product = [i*j for i, j in zip(V1, V2)]
        dotproduct = sum(product)
        print(f"Dot product is: {dotproduct}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        vector = [float(i+j) for i, j in zip(V1, V2)]
        print(f"Add vector is: {vector}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        vector = [float(i*j) for i, j in zip(V1, V2)]
        print(f"Sous vector is: {vector}")
