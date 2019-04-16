#!/usr/bin/env python
# -*- coding: utf-8 -*-


class StackOverflowError(RuntimeError):
    pass


class StackIsEmptyError(RuntimeError):
    pass


class Stack:
    def __init__(self, size):
        self.storage = [0] * size
        self.head = -1

    def push(self, v):
        pass

    def pop(self):
        pass

    def __len__(self):
        pass
