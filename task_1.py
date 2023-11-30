from typing import Union


class Glass:
    def __init__(self,
                 capacity_volume: Union[int, float],
                 occupied_volume: Union[int, float]):
        # types check
        if not isinstance(capacity_volume, (int, float)) or \
           not isinstance(occupied_volume, (int, float)):
            raise TypeError(
                "Both capacity_volume and occupied_volume must be int or float")

        # values check
        if capacity_volume <= 0 or occupied_volume < 0 or \
                occupied_volume > capacity_volume:
            raise ValueError(
                "Invalid values for capacity_volume or occupied_volume")

        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume


if __name__ == "__main__":
    glass1 = Glass(300, 150)
    glass2 = Glass(500, 200)

    try:
        invalid_glass1 = Glass(0, 150)  # capacity_volume must be > 0
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")

    try:
        invalid_glass2 = Glass(300, -50)  # occupied_volume must be >= 0
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")

    try:
        invalid_glass3 = Glass(300, 400)  # occupied_volume must be <= capacity_volume
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
