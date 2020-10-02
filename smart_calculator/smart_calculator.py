from collections import deque


class SmartCalculator:
    def __init__(self):
        self.dic = {}

    def process_input(self, exp):
        b = []
        n = ""
        for i in exp:
            if i.isnumeric():
                n += i
            elif i.isalpha():
                n += i
            else:
                if i in ["+", "-", "*", "/", "^", "(", ")"]:
                    b.append(n)
                    n = ""
                    b.append(i)
        if n:
            b.append(n)

        lst = []
        string = ""
        run = True
        for j in b:
            if j.isdigit() or j in ["(", ")"] or j.isalpha():
                if string:
                    if "+" in string:
                        lst.append("+")
                    elif "-" in string:
                        if string.count("-") % 2 == 0:
                            lst.append("+")
                        else:
                            lst.append("-")
                    elif "*" in string or "/" in string or "^" in string:
                        if len(string) > 1:
                            # print("Invalid expression")
                            run = False

                        else:
                            lst.append(string)
                string = ""
                lst.append(j)

            elif j in ["+", "-", "*", "/", "^"]:
                string += j

        return lst if run else "Invalid expression"

    def fst_is_high_pr(self, x, y):
        if (x in ['+', '-'] and y in ["*", "/", "^"])\
                or (x in ["*", "/"] and y == "^"):

            return False

        if (x in ["*", "/", "^"] and y in ['+', '-']) \
                or (x == "^" and y in ["*", "/"]):

            return True

        if (x in ['+', '-'] and y in ['+', '-']) \
                or (x in ["*", "/"] and y in ["*", "/"]) \
                or (x == "^" and y == "^"):

            return "equal"

    def rpn(self, exp):
        stack = deque()
        result = []

        for i in exp:
            if i.isnumeric() or i.isalpha():
                result.append(i)

            elif i in ["+", "-", "/", "*", "^"]:

                if not stack or stack[-1] == "(":
                    stack.append(i)

                elif self.fst_is_high_pr(i, stack[-1]) == True:
                    stack.append(i)

                elif self.fst_is_high_pr(i, stack[-1]) in [False, "equal"]:
                    for _ in range(len(stack)):
                        if self.fst_is_high_pr(i, stack[-1]) == False or stack[-1] != "(":
                            result.append(stack.pop())
                        else:
                            break
                    stack.append(i)

            elif i == "(":
                stack.append(i)

            elif i == ")":
                for _ in range(len(stack)):
                    if stack[-1] != "(":
                        result.append(stack.pop())
                    else:
                        stack.pop()
                        break

        for _ in range(len(stack)):
            result.append(stack.pop())

        return result

    def solve_rpn(self, exp):
        machine = deque()

        for i in exp:
            if i.isdigit():
                machine.append(i)
            elif i.isalpha():
                if i in self.dic:
                    machine.append(self.dic[i])
                else:
                    return "Unknown variable"
            elif i in ["+", "-", "/", "*", "^"]:
                sec_dig = int(machine.pop())
                fst_dig = int(machine.pop())
                if i == "+":
                    result = fst_dig + sec_dig
                    machine.append(result)
                elif i == "-":
                    result = fst_dig - sec_dig
                    machine.append(result)
                elif i == "/":
                    result = fst_dig // sec_dig
                    machine.append(result)
                elif i == "*":
                    result = fst_dig * sec_dig
                    machine.append(result)
                elif i == "^":
                    result = fst_dig ** sec_dig
                    machine.append(result)
        return machine[-1]

    def assign_var(self, cmd):
        if cmd.count("=") < 2:
            left, right = cmd.split("=")
            left = left.strip()
            right = right.strip()
            if not left.isalpha():
                print("Invalid identifier")
            else:
                try:
                    right = int(right)
                    self.dic[left] = right
                except ValueError:
                    if right.isalpha():
                        if right in self.dic:
                            self.dic[left] = self.dic[right]
                        else:
                            print("Unknown variable")
                    else:
                        print("Invalid assignment")
        else:
            print("Invalid assignment")

    def check_par(self, a):
        my_stack = deque()
        run = True

        for i in a:
            if i == "(":
                my_stack.append(i)
            elif i == ")":
                if len(my_stack) > 0:
                    my_stack.pop()
                else:
                    run = False
                    break

        return False if my_stack or not run else True

    def main(self):
        while True:
            cmd = input()

            if cmd == "":
                pass
            elif cmd == "/exit":
                print("Bye!")
                break
            elif cmd == "/help":
                print("The program calculates addition and subtraction")
            elif cmd[:1] == "/" and cmd[1:] not in ["help", "exit"]:
                print("Unknown command")
            elif "=" in cmd:
                self.assign_var(cmd)
            elif cmd[:1] == "-" and cmd[1:].isnumeric():
                print(cmd)
            else:
                if self.check_par(cmd) and self.process_input(cmd) != "Invalid expression":
                    q = self.rpn((self.process_input(cmd)))
                    print(self.solve_rpn(q))
                else:
                    print("Invalid expression")


obj = SmartCalculator()
obj.main()

