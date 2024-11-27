class ClickSequenceTracker:
    def __init__(self, index, click_sequences, reset_time_limit):
        self.index = index
        self.click_sequences = click_sequences
        self.reset_time_limit = reset_time_limit
        self.current_sequence = []
        self.current_time_elapsed = 0
        self.time_elapsed = 0
        self.start_time = 0
        self.longest_sequence_length = max(len(sequence) for sequence in self.click_sequences)

    def add_click(self, click, time_elapsed):
        self.current_sequence.append(click)
        self.reset_time(time_elapsed)

    def check_completed_sequence(self):
        current_sequence = self.current_sequence
        if self.current_sequence in self.click_sequences:
            self.reset_sequence()
            return current_sequence
        return False

    def dt(self, time_elapsed):
        """ In milliseconds"""
        self.current_time_elapsed = time_elapsed - self.start_time
        return self.current_time_elapsed

    def reset_check(self, time_elapsed):
        if (self.current_time_elapsed >= self.reset_time_limit) or (len(self.current_sequence) > self.longest_sequence_length):
            self.reset_sequence()
            self.reset_time(time_elapsed)
            return True
        return False

    def reset_sequence(self):
        self.current_sequence=[]

    def reset_time(self, time_elapsed):
        self.time_elapsed = time_elapsed
        self.current_time_elapsed = 0
        self.start_time = time_elapsed