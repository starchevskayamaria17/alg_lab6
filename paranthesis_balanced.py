#!/usr/bin/env python
# -*- coding: utf-8 -*-


from stack import Stack

def is_paranthesis_balanced(s):
    openBracket = ["[","{","(", "<"]
    closeBracket = ["]","}",")", ">"]
    stack = Stack(len(s))
    for i in range(len(s)):
        if s[i] in openBracket:
            stack.push(s[i])
        elif s[i] in closeBracket:
            if stack.__len__() == 0:
                return False
            else:
                del_bracket = stack.pop()
                if del_bracket == '(' and s[i] == ')':
                    continue
                elif del_bracket == '[' and s[i] == ']':
                    continue
                elif del_bracket == '{' and s[i] == '}':
                    continue
                elif del_bracket == '<' and s[i] == '>':
                    continue
                else:
                    return False 
    if stack.__len__() == 0:
        return True
            
