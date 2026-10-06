"""
Python Interfaces — an interactive tour.

Run it:
    python3 python_interfaces.py

Then type a number to run one example, 'a' to run all of them, or 'q' to quit.

Every example prints two explanations before running its code:
    TECHNICAL -> how you'd explain it in an interview / code review
    SIMPLE    -> how you'd explain it to a high school student

Python has no `interface` keyword (unlike Java/C#/TypeScript). Instead it gives
you three tools that play the same role:
    1. Duck typing              -> informal, "if it has the method, it works"
    2. Abstract Base Classes    -> `abc.ABC` + `@abstractmethod`, enforced by inheritance
    3. Protocols                -> `typing.Protocol`, enforced by shape (structural typing)
"""

from abc import ABC, abstractmethod
from collections.abc import Iterator, Sized
from typing import Protocol, runtime_checkable


# ---------------------------------------------------------------------------
# Small printing helpers so every example looks the same
# ---------------------------------------------------------------------------

def header(title: str) -> None:
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def explain(technical: str, simple: str) -> None:
    print("\n[TECHNICAL]")
    print(technical.strip())
    print("\n[SIMPLE — high school version]")
    print(simple.strip())
    print("\n[CODE OUTPUT]")


# ---------------------------------------------------------------------------
# 1. What is an interface? (the idea, using plain duck typing)
# ---------------------------------------------------------------------------

def example_1_what_is_an_interface() -> None:
    header("1. What is an interface? (duck typing)")
    explain(
        technical="""
An interface is a CONTRACT: a set of method signatures a type promises to
provide, without saying HOW they're implemented. Code that depends on the
contract (not on a concrete class) can work with any type that fulfills it.

Python's default is duck typing: there's no declared contract at all. If an
object has the method you call, it works; if not, you get an AttributeError
at RUNTIME, only when that line actually executes.
""",
        simple="""
Think of a wall socket. The socket doesn't care if you plug in a phone
charger, a lamp, or a toaster — as long as the plug has the right shape.
The "shape of the plug" is the interface.

In Python, by default nobody checks the plug shape ahead of time. You just
try to plug it in, and if it doesn't fit... sparks (an error).
""",
    )

    # Two unrelated classes. No shared parent. They just both have .speak().
    class Dog:
        def speak(self) -> str:
            return "Woof"

    class Robot:
        def speak(self) -> str:
            return "Beep boop"

    class Rock:
        pass  # no .speak() at all

    # This function relies on an *implicit* interface: "has a speak() method".
    def make_it_talk(thing) -> None:
        print(f"{type(thing).__name__:>5} says: {thing.speak()}")

    make_it_talk(Dog())
    make_it_talk(Robot())

    # The Rock breaks the contract — but we only find out when it runs.
    try:
        make_it_talk(Rock())
    except AttributeError as e:
        print(f" Rock failed at runtime -> AttributeError: {e}")

    print("\nTakeaway: duck typing is flexible, but mistakes surface late.")


# ---------------------------------------------------------------------------
# 2. Abstract Base Classes (ABC) — the "formal" interface
# ---------------------------------------------------------------------------

def example_2_abstract_base_classes() -> None:
    header("2. Abstract Base Classes (abc.ABC + @abstractmethod)")
    explain(
        technical="""
`abc.ABC` lets you declare an explicit interface. Methods marked with
`@abstractmethod` MUST be overridden by subclasses. Python enforces this at
INSTANTIATION time: if any abstract method is left unimplemented, calling
the constructor raises TypeError. This is NOMINAL typing — a class conforms
only if it explicitly inherits from the ABC.

ABCs can also contain concrete (shared) methods, so they double as a partial
base class — something a pure Java interface traditionally couldn't do.
""",
        simple="""
An ABC is like a job description with a checklist: "To be a Shape, you MUST
know how to compute your area and your perimeter."

You can't hire "a Shape" in general — that's too vague. You can only hire a
Circle or a Square that actually filled in every item on the checklist.
""",
    )

    class Shape(ABC):
        @abstractmethod
        def area(self) -> float: ...

        @abstractmethod
        def perimeter(self) -> float: ...

        # Concrete method: every Shape gets this for free, built on the contract.
        def describe(self) -> str:
            return (f"{type(self).__name__}: area={self.area():.2f}, "
                    f"perimeter={self.perimeter():.2f}")

    class Circle(Shape):
        def __init__(self, r: float) -> None:
            self.r = r

        def area(self) -> float:
            return 3.14159 * self.r ** 2

        def perimeter(self) -> float:
            return 2 * 3.14159 * self.r

    class Square(Shape):
        def __init__(self, side: float) -> None:
            self.side = side

        def area(self) -> float:
            return self.side ** 2

        def perimeter(self) -> float:
            return 4 * self.side

    # Code depends on the interface (Shape), not on Circle/Square specifically.
    shapes: list[Shape] = [Circle(1), Square(2)]
    for s in shapes:
        print(s.describe())

    # You cannot instantiate the interface itself.
    try:
        Shape()
    except TypeError as e:
        print(f"\nShape() -> TypeError: {e}")


# ---------------------------------------------------------------------------
# 3. ABCs catch mistakes early
# ---------------------------------------------------------------------------

def example_3_abc_catches_mistakes_early() -> None:
    header("3. ABCs catch a missing method EARLY")
    explain(
        technical="""
Compare with example 1: with duck typing, a missing method fails only when
it's CALLED (possibly deep in production, on a rare code path). With an ABC,
the failure moves to OBJECT CREATION — the moment you build an incomplete
class instance, you get a TypeError listing every missing abstract method.

Fail-fast = bugs found in tests/startup instead of at 3am.
""",
        simple="""
Imagine a teacher who checks your homework the moment you hand it in
("you skipped question 2!") versus one who only notices at the final exam.

ABCs are the first teacher. They yell at you right away, which is
annoying but saves you from a much bigger problem later.
""",
    )

    class Notifier(ABC):
        @abstractmethod
        def send(self, msg: str) -> None: ...

        @abstractmethod
        def name(self) -> str: ...

    # Oops: forgot to implement name()
    class BrokenEmailNotifier(Notifier):
        def send(self, msg: str) -> None:
            print(f"email: {msg}")

    print("Trying to create BrokenEmailNotifier (missing name())...")
    try:
        BrokenEmailNotifier()
    except TypeError as e:
        print(f"-> TypeError: {e}")

    print("\nNotice: we never even called .name(). Python refused to build it.")


# ---------------------------------------------------------------------------
# 4. Protocols — structural typing ("static duck typing")
# ---------------------------------------------------------------------------

def example_4_protocols() -> None:
    header("4. Protocols (typing.Protocol) — structural typing")
    explain(
        technical="""
`typing.Protocol` (PEP 544) defines an interface by SHAPE, not by ancestry.
Any class with matching methods/attributes satisfies the protocol — no
inheritance needed. This is STRUCTURAL typing, a.k.a. "static duck typing":
type checkers (mypy, pyright) verify conformance before you run anything.

By default Protocols are only for static checking. Adding
`@runtime_checkable` lets `isinstance()` work too, but it only checks that
the method NAMES exist — not their signatures or return types.

Great for: typing third-party classes you can't modify, and keeping
modules decoupled (the implementer never has to import your interface).
""",
        simple="""
An ABC is like a club with a membership card: you're only in if you
officially signed up (inherited).

A Protocol is like a "you must be this tall to ride" sign: nobody cares
what club you're in. If you're tall enough (have the right methods),
you can ride. You didn't need to sign up for anything.
""",
    )

    @runtime_checkable
    class Drawable(Protocol):
        def draw(self) -> str: ...

    # Neither class mentions Drawable. They just happen to have draw().
    class Button:
        def draw(self) -> str:
            return "[ OK ]"

    class Tree:
        def draw(self) -> str:
            return "  ^\n /|\\\n  |"

    class Sound:
        def play(self) -> str:
            return "♪"

    def render(item: Drawable) -> None:
        # A type checker would flag render(Sound()) BEFORE running the code.
        print(item.draw())

    for obj in (Button(), Tree(), Sound()):
        ok = isinstance(obj, Drawable)
        print(f"\n{type(obj).__name__:>6} is Drawable? {ok}")
        if ok:
            render(obj)

    print("\nButton and Tree never inherited from Drawable — shape was enough.")


# ---------------------------------------------------------------------------
# 5. WHY interfaces are useful: swap implementations freely
# ---------------------------------------------------------------------------

def example_5_swap_implementations() -> None:
    header("5. Why useful #1: swap implementations without touching callers")
    explain(
        technical="""
This is the Dependency Inversion Principle (the "D" in SOLID): high-level
code (Checkout) depends on an ABSTRACTION (PaymentProcessor), not on
concrete details (Stripe, PayPal). You inject the concrete implementation
from outside (dependency injection).

Result: adding a new payment provider = adding a new class. Checkout's code
never changes (Open/Closed Principle). This is exactly the shape of many
system design / OOP interview questions (parking lot, vending machine, etc).
""",
        simple="""
Your TV remote works with any brand of AA battery — Duracell, Energizer,
the cheap ones. The remote only cares that it's "an AA battery".

If the remote were hard-wired to ONLY take Duracell, you'd need a whole
new remote to switch brands. Interfaces keep things swappable.
""",
    )

    class PaymentProcessor(ABC):
        @abstractmethod
        def charge(self, amount_cents: int) -> str: ...

    class StripeProcessor(PaymentProcessor):
        def charge(self, amount_cents: int) -> str:
            return f"Stripe charged ${amount_cents / 100:.2f}"

    class PayPalProcessor(PaymentProcessor):
        def charge(self, amount_cents: int) -> str:
            return f"PayPal charged ${amount_cents / 100:.2f}"

    class CryptoProcessor(PaymentProcessor):  # added later — Checkout unchanged
        def charge(self, amount_cents: int) -> str:
            return f"Crypto wallet charged ${amount_cents / 100:.2f}"

    class Checkout:
        # Depends on the interface, receives the concrete thing from outside.
        def __init__(self, processor: PaymentProcessor) -> None:
            self.processor = processor

        def pay(self, amount_cents: int) -> None:
            print(self.processor.charge(amount_cents))

    for proc in (StripeProcessor(), PayPalProcessor(), CryptoProcessor()):
        Checkout(proc).pay(1999)


# ---------------------------------------------------------------------------
# 6. WHY interfaces are useful: easy testing with fakes
# ---------------------------------------------------------------------------

def example_6_testing_with_fakes() -> None:
    header("6. Why useful #2: testing with fakes")
    explain(
        technical="""
Because the business logic depends on an interface, tests can inject a FAKE
implementation: no network, no database, deterministic, and fast. The fake
can also RECORD calls so the test can assert on behavior.

Here we use a Protocol, so the fake doesn't even need to import or inherit
anything from production code — it just matches the shape.
""",
        simple="""
Pilots practice in a flight simulator before flying a real plane. The
simulator "looks like" a plane to the pilot (same buttons, same controls),
but nobody gets hurt if something goes wrong.

A fake in a test is a flight simulator for your code.
""",
    )

    class EmailSender(Protocol):
        def send(self, to: str, body: str) -> bool: ...

    # Production implementation (pretend this talks to a real mail server).
    class SmtpEmailSender:
        def send(self, to: str, body: str) -> bool:
            raise RuntimeError("Would hit a real SMTP server — not in tests!")

    # Test double: records what was sent instead of really sending.
    class FakeEmailSender:
        def __init__(self) -> None:
            self.sent: list[tuple[str, str]] = []

        def send(self, to: str, body: str) -> bool:
            self.sent.append((to, body))
            return True

    # The code under test.
    def welcome_new_user(email: str, sender: EmailSender) -> None:
        sender.send(email, f"Welcome aboard, {email}!")

    fake = FakeEmailSender()
    welcome_new_user("ada@example.com", fake)

    print(f"Emails recorded by fake: {fake.sent}")
    assert fake.sent == [("ada@example.com", "Welcome aboard, ada@example.com!")]
    print("Test passed ✅ — and no real email server was touched.")


# ---------------------------------------------------------------------------
# 7. Built-in interfaces: dunder protocols and collections.abc
# ---------------------------------------------------------------------------

def example_7_builtin_protocols() -> None:
    header("7. Python's built-in interfaces (dunder methods, collections.abc)")
    explain(
        technical="""
You already use interfaces constantly. Python's language features are built
on implicit protocols defined by "dunder" methods:
    len(x)        -> x.__len__()        (Sized)
    for i in x    -> x.__iter__()       (Iterable)
    x[i]          -> x.__getitem__(i)
    with x:       -> __enter__/__exit__ (context manager)

`collections.abc` provides ABCs for these. Many use `__subclasshook__`, so
`isinstance(obj, Sized)` is True for ANY class that defines `__len__`, even
without inheriting — a structural check, like a Protocol.
""",
        simple="""
Python has secret "magic words" (methods with double underscores). If your
class knows the magic word __len__, then len() works on it. If it knows
__iter__, then for-loops work on it.

It's like teaching your dog the command "sit" — once it knows the word,
anyone can use that command with it.
""",
    )

    class Playlist:
        def __init__(self, *songs: str) -> None:
            self.songs = list(songs)

        def __len__(self) -> int:           # makes len() work
            return len(self.songs)

        def __iter__(self) -> Iterator[str]:  # makes for-loops work
            return iter(self.songs)

    p = Playlist("Song A", "Song B", "Song C")

    print(f"len(p) = {len(p)}")
    for song in p:
        print(f"  playing {song}")
    print(f"'Song B' in p -> {'Song B' in p}   (works thanks to __iter__)")
    print(f"sorted(p, reverse=True) -> {sorted(p, reverse=True)}")
    print(f"\nisinstance(p, Sized)? {isinstance(p, Sized)}  "
          f"(Playlist never inherited from Sized!)")


# ---------------------------------------------------------------------------
# 8. ABC vs Protocol — which to use? (cheat sheet)
# ---------------------------------------------------------------------------

def example_8_abc_vs_protocol() -> None:
    header("8. ABC vs Protocol — which one should I use?")
    explain(
        technical="""
                     | ABC (nominal)              | Protocol (structural)
---------------------+----------------------------+-----------------------------
Conformance by       | explicit inheritance       | matching shape
Enforced when        | instantiation (runtime)    | type-check time (mypy/pyright)
isinstance() works   | yes                        | only w/ @runtime_checkable
Shared code          | yes (concrete methods)     | not really the intent
3rd-party classes    | must subclass/register     | work automatically
Coupling             | implementer imports ABC    | implementer imports nothing

Rule of thumb:
  * You OWN the hierarchy and want runtime enforcement + shared helpers -> ABC
  * You want to describe "anything with method X" / decouple modules     -> Protocol
  * Quick script, no tooling                                             -> duck typing
""",
        simple="""
ABC   = a school club. You must officially join, and the club gives you a
        uniform (shared code). The club president checks you at the door.

Protocol = a skill test. Nobody cares where you came from. If you can do
           the skill, you pass. The checker is a robot (mypy) that grades
           your code before you even run it.

Both are ways of saying "I need something that can do X."
""",
    )

    # Same interface written both ways, side by side.
    class GreeterABC(ABC):
        @abstractmethod
        def greet(self, name: str) -> str: ...

    @runtime_checkable
    class GreeterProtocol(Protocol):
        def greet(self, name: str) -> str: ...

    class FormalGreeter(GreeterABC):      # explicitly signed up
        def greet(self, name: str) -> str:
            return f"Good evening, {name}."

    class CasualGreeter:                  # never signed up for anything
        def greet(self, name: str) -> str:
            return f"yo {name}"

    for g in (FormalGreeter(), CasualGreeter()):
        print(f"{type(g).__name__:>14}: "
              f"is GreeterABC={isinstance(g, GreeterABC)!s:5}  "
              f"is GreeterProtocol={isinstance(g, GreeterProtocol)!s:5}  "
              f"-> {g.greet('Sam')}")

    print("\nCasualGreeter satisfies the Protocol but NOT the ABC.")


# ---------------------------------------------------------------------------
# Interactive menu
# ---------------------------------------------------------------------------

EXAMPLES = {
    "1": ("What is an interface? (duck typing)", example_1_what_is_an_interface),
    "2": ("Abstract Base Classes (ABC)", example_2_abstract_base_classes),
    "3": ("ABCs catch missing methods early", example_3_abc_catches_mistakes_early),
    "4": ("Protocols (structural typing)", example_4_protocols),
    "5": ("Why useful: swap implementations", example_5_swap_implementations),
    "6": ("Why useful: testing with fakes", example_6_testing_with_fakes),
    "7": ("Built-in interfaces (dunder methods)", example_7_builtin_protocols),
    "8": ("ABC vs Protocol cheat sheet", example_8_abc_vs_protocol),
}


def print_menu() -> None:
    print("\n" + "-" * 50)
    print(" Python Interfaces — pick an example")
    print("-" * 50)
    for key, (title, _) in EXAMPLES.items():
        print(f"  {key}. {title}")
    print("  a. Run all")
    print("  q. Quit")


def main() -> None:
    while True:
        print_menu()
        try:
            choice = input("\nYour choice: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            return

        if choice in ("q", "quit", "exit"):
            print("Bye!")
            return
        if choice == "a":
            for _, fn in EXAMPLES.values():
                fn()
        elif choice in EXAMPLES:
            EXAMPLES[choice][1]()
        else:
            print(f"'{choice}' is not an option. Try 1-{len(EXAMPLES)}, 'a', or 'q'.")
            continue

        try:
            input("\nPress Enter to go back to the menu...")
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            return


if __name__ == "__main__":
    main()
