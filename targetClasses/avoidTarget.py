from target import Target


class AvoidTarget(Target):
    def __str__(self):
        return f"AvoidTarget({self.index})"
    def move(self, mousePos):
        # Finish up avoidance logic
        # should be dynamic
        pass

