BOMB = 9
TRENCH = 1


def find_path(field_places):
    field = Field(field_places)

    initial_solution = SolutionPath([(0, 0)])

    valid_solutions = []

    in_progress_solutions = [initial_solution]

    while len(in_progress_solutions) > 0:
        new_solutions = []
        for solution in in_progress_solutions:
            new_solutions.extend(solution.generate_branches(field))

        in_progress_solutions = list(filter(lambda sol: not sol.has_finished(field), new_solutions))
        valid_solutions.extend(list(filter(lambda sol: sol.has_finished(field), new_solutions)))

    return valid_solutions[0]


class Field:
    places = []

    def __init__(self, places):
        self.places = places

    def get_place_value(self, place):
        try:
            x, y = place[0], place[1]
            if (x >= 0 and x <= len(self.places)
            and y >= 0 and y <= len(self.places[x])):
                return self.places[x][y]
            else:
                return None
        except:
            return None

class SolutionPath:
    path = []

    def __init__(self, path):
        self.path = path

    def has_visited_place(self, place):
        return place in self.path

    def add_place(self, place):
        self.path.append(place)
        return self

    def generate_branches(self, field):
        return list(map(
            lambda place: SolutionPath(self.path).add_place(place),
            self.get_valid_moves(field),
        ))

    def get_valid_moves(self, field):
        places = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 or j == 0: # no diagonals
                    place = (self.path[-1][0] + i, self.path[-1][1] + j)
                    place_value = field.get_place_value(place)
                    # print(place)
                    if (
                        place_value is not None
                        and (place_value == TRENCH or place_value == BOMB)
                        and not self.has_visited_place(place)
                    ):
                        places.append(place)
        # print(places)
        return places

    def has_finished(self, field):
        return field.get_place_value((self.path[-1][0], self.path[-1][1])) == BOMB

    def __str__(self):
        return str(self.path)
