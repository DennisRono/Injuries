def calculate_iss(ais_severity):
    # The ISS is calculated as the sum of the squares of the highest AIS severity code
    # in each of the three most severely injured body regions
    # For simplicity, we'll assume ais_severity is a list of AIS severity codes
    sorted_severities = sorted(ais_severity, reverse=True)
    top_three = sorted_severities[:3]
    return sum(severity**2 for severity in top_three)
