"""Work-order status transition rule used by the lab tests."""

ALLOWED_TRANSITIONS = {
    ("PENDING", "PROCESSING"),
    ("PROCESSING", "COMPLETED"),
}


def can_transition(current, target):
    """Return True only for the two allowed work-order transitions."""
    return (current, target) in ALLOWED_TRANSITIONS
