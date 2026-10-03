"""
Custom Exceptions and Exception Hierarchies
===========================================

Define your own error types by subclassing Exception (never BaseException for
ordinary errors). A small hierarchy with one app-specific base lets callers
catch broadly (except AppError) or narrowly (except NotFoundError). Exceptions
are just classes, so they can carry context as attributes. Use `raise ... from`
to preserve the original cause.

Key idea:
    One base exception per app/library + specific subclasses. Carry useful
    context on the exception object; chain with `from` to keep the root cause.
"""


class AppError(Exception):
    """Base class for all errors raised by this application."""


class NotFoundError(AppError):
    def __init__(self, resource: str, key: str) -> None:
        # Store context so the handler can inspect it, not just read a string.
        self.resource = resource
        self.key = key
        super().__init__(f"{resource} {key!r} not found")


class ValidationError(AppError):
    def __init__(self, field: str, reason: str) -> None:
        self.field = field
        self.reason = reason
        super().__init__(f"invalid {field}: {reason}")


def load_user(user_id: str) -> dict:
    users = {"u1": {"name": "Subham"}}
    if user_id not in users:
        raise NotFoundError("user", user_id)
    return users[user_id]


def parse_port(raw: str) -> int:
    try:
        return int(raw)
    except ValueError as exc:
        # Chain: keep the underlying ValueError as the cause (__cause__).
        raise ValidationError("port", "must be an integer") from exc


if __name__ == "__main__":
    # Catch narrowly and use the attached context:
    try:
        load_user("u2")
    except NotFoundError as e:
        print(f"narrow: {e}  (resource={e.resource}, key={e.key})")

    # Catch broadly by the shared base -- subclasses are caught too:
    try:
        load_user("u3")
    except AppError as e:
        print(f"broad: {type(e).__name__} -> {e}")

    # Exception chaining preserves the root cause:
    try:
        parse_port("abc")
    except ValidationError as e:
        print(f"chained: {e}; cause={type(e.__cause__).__name__}")

    # Expected output:
    #   narrow: user 'u2' not found  (resource=user, key=u2)
    #   broad: NotFoundError -> user 'u3' not found
    #   chained: invalid port: must be an integer; cause=ValueError
