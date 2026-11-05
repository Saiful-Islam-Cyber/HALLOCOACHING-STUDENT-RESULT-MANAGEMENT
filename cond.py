

def determine_pass_fail(percentage, passing_boundary=40.0):
    """Determines if a student passes or fails based on their percentage."""
    if percentage >= passing_boundary:
        return "Pass"
    else:
        return "Fail"

def calculate_grade(percentage):
    """Returns a letter grade using standard conditional branches."""
    if percentage >= 80:
        return "A+"
    elif percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "A-"
    elif percentage >= 50:
        return "B"
    elif percentage >= 40:
        return "C"
    else:
        return "F"
