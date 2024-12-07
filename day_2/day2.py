def parse_reports():
    reports = []
    with open('input.txt', 'r') as file:
        for report in file:
            reports.append(report)
    return reports

def valid_reports(reports):
    num_valid = 0
    for report in reports:
        report = [int(report) for report in report.split()]
        num_valid += 1 if check_valid(report) else 0

    return num_valid

def check_valid(report):

    # check diffs
    for i in range(len(report)-1):
        reports_diff = abs(report[i] - report[i+1])
        in_range = (reports_diff in [1, 2, 3])

        if not in_range:
            return False

    ascending = True
    descending = True
    for i in range(len(report) - 1):
        if (report[i] > report[i+1]):
            ascending = False
        if (report[i] < report[i+1]):
            descending = False

        if (not ascending and not descending):
            return False

    return True

reports = parse_reports()
valid = valid_reports(reports)
print(valid)
