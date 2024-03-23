class TwoStacks:
    # Initialize the two stacks here
    def __init__(self, size):
        self.size = size
        self.stacks = ["-"] * size
        self.top1 = -1
        self.top2 = size

    # Insert Value in First Stack
    def push1(self, value):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.stacks[self.top1] = value
        else:
            print("Stack Overflow")
            return None

    # Insert Value in Second Stack
    def push2(self, value):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.stacks[self.top2] = value
        else:
            print("Stack Overflow")
            return None

    # Return and remove top Value from First Stack
    def pop1(self):
        if self.top1 >= 0:
            val = self.stacks[self.top1]
            self.top1 -= 1
            return val
        else:
            print("Stack Underflow")
            return None

    # Return and remove top Value from Second Stack
    def pop2(self):
        if self.top2 < self.size:
            val = self.stacks[self.top2]
            self.top2 += 1
            return val
        else:
            print("Stack Underflow")
            return None

    # All ops take: O(1) time
    # Size is proportional to input size


# Test
two_stacks = TwoStacks(6)

two_stacks.push1(4)
print(f"Stacks after push1(4): {two_stacks.stacks}")

two_stacks.push2(-3)
two_stacks.push2(3)
two_stacks.push2(2)
two_stacks.push2(2)
two_stacks.push2(1212)

print(f"Stacks after push2(-3): {two_stacks.stacks}")

popped_value1 = two_stacks.pop1()  # Pop from first stack
print(f"Popped from Stack 1: {popped_value1}")
print(f"Stacks after pop1(): {two_stacks.stacks}")


try:
    assert two_stacks.stacks == [4, 1212, 2, 2, 3, -3], "Test Fails"

except AssertionError as e:
    print("ERROR:", e)
else:
    print("Test 1 passed")
