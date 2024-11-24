import pygame
import time

class Target:
    def  __init__(self, index: int, position: list[2], movement, color: list[3], speed):
        self.index = index
        self.position = position
        self.movement = movement
        self.color = color
        self.speed = speed
    def __str__(self):
        return f"Target({self.index})"

