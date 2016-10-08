"""
Test program for pre-processing schedule
"""
import arrow

base = arrow.now()

STARTDATE = arrow.Arrow(2016, 9, 26)

def process(raw):
    """
    Line by line processing of syllabus file.  Each line that needs
    processing is preceded by 'head: ' for some string 'head'.  Lines
    may be continued if they don't contain ':'.  If # is the first
    non-blank character on a line, it is a comment ad skipped. 
    """
    field = None
    entry = { }
    cooked = [ ]
    week = 0
    for line in raw:
        line = line.strip()
        if len(line) == 0 or line[0]=="#" :
            continue
        parts = line.split(':')
        if len(parts) == 1 and field:
            entry[field] = entry[field] + line + " "
            continue
        if len(parts) == 2: 
            field = parts[0]
            content = parts[1]
        else:
            raise ValueError("Trouble with line: '{}'\n".format(line) + 
                "Split into |{}|".format("|".join(parts)))

        if field == "begin":
            try:
                base = arrow.get(content, "MM/DD/YYYY")
                # print("Base date {}".format(base.isoformat()))
            except:
                raise ValueError("Unable to parse date {}".format(content))

        elif field == "week":
            if entry:
                cooked.append(entry)
                entry = { }
            this_monday = monday_of_week(week)
            entry['topic'] = ""
            entry['project'] = ""
            entry['month'] = int(this_monday.format("m"))
            entry['this_month'] = int(arrow.now().format("m"))
            entry['monday'] = int(this_monday.format("d"))
            entry['today'] = int(arrow.now().format("d"))
            entry['sunday'] = int(this_monday.replace(day =+ 7).format("d"))
            entry['week'] = content + "\n" +  this_monday.format("MM/DD/YYYY")
            week += 1
            

        elif field == 'topic' or field == 'project':
            entry[field] = content

        else:
            raise ValueError("Syntax error in line: {}".format(line))

    if entry:
        cooked.append(entry)

    return cooked

def monday_of_week(num):
    temp = STARTDATE.replace(days =+ (7 * num))
    return temp

def main():
    f = open("data/schedule.txt")
    parsed = process(f)
    print(parsed)

if __name__ == "__main__":
    main()

    
    
            
    
