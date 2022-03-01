from .base import Result, run_pyright


def test_integer_with_choices() -> None:
    results = run_pyright(
        """\
from django.db import models

class Foo(models.Model):
    integer_with_choices = models.IntegerField(
        choices=[
            (1, "First Option"),
            (2, "Second Option"),
        ],
    )

f = Foo()
reveal_type(f.integer_with_choices)
f.integer_with_choices == 2
f.integer_with_choices == 3
f.integer_with_choices = None
f.integer_with_choices = 3
f.integer_with_choices = 2
"""
    )
    assert results == [
        Result(
            type="info",
            message='Type of "f.integer_with_choices" is "int"',
            line=12,
            column=13,
        ),
        Result(
            type="error",
            message='Cannot assign member "integer_with_choices" for type "Foo" (reportGeneralTypeIssues)',
            line=15,
            column=3,
        ),
    ]


def test_integer_with_choices_nullable() -> None:
    results = run_pyright(
        """\
from django.db import models

class Foo(models.Model):
    integer_with_choices_nullable = models.IntegerField(
        choices=[
            (1, "First Option"),
            (2, "Second Option"),
        ],
        null=True,
    )

f = Foo()
reveal_type(f.integer_with_choices_nullable)
f.integer_with_choices_nullable == 2
f.integer_with_choices_nullable == 3
f.integer_with_choices_nullable = None
f.integer_with_choices_nullable = 3
f.integer_with_choices_nullable = 2
"""
    )
    assert results == [
        Result(
            type="info",
            message='Type of "f.integer_with_choices_nullable" is "int | None"',
            line=13,
            column=13,
        ),
    ]


def test_char_with_choices() -> None:
    results = run_pyright(
        """\
from django.db import models

class Foo(models.Model):
    char_with_choices = models.CharField(
        choices=[
            ("a", "A"),
            ("b", "B"),
        ],
    )

f = Foo()
reveal_type(f.char_with_choices)
f.char_with_choices == "c"
f.char_with_choices == "a"
f.char_with_choices = None
f.char_with_choices = "c"
f.char_with_choices = "b"
"""
    )
    assert results == [
        Result(
            type="info",
            message='Type of "f.char_with_choices" is "str"',
            line=12,
            column=13,
        ),
        Result(
            type="error",
            message='Cannot assign member "char_with_choices" for type "Foo" (reportGeneralTypeIssues)',
            line=15,
            column=3,
        ),
    ]


def test_char_with_choices_nullable() -> None:
    results = run_pyright(
        """\
from django.db import models

class Foo(models.Model):
    char_with_choices_nullable = models.CharField(
        choices=[
            ("a", "A"),
            ("b", "B"),
        ],
        null=True,
    )

f = Foo()
reveal_type(f.char_with_choices_nullable)
f.char_with_choices_nullable == "c"
f.char_with_choices_nullable == "a"
f.char_with_choices_nullable = None
f.char_with_choices_nullable = "c"
f.char_with_choices_nullable = "b"
"""
    )
    assert results == [
        Result(
            type="info",
            message='Type of "f.char_with_choices_nullable" is "str | None"',
            line=13,
            column=13,
        ),
    ]
