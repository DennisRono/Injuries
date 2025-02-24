def calculate_iss(ais_severity):
    sorted_severities = sorted(ais_severity, reverse=True)
    top_three = sorted_severities[:3]
    return sum(severity**2 for severity in top_three)
