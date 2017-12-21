import csv
import operator

def calculate_statistics(filename):
    pass

def sort_papers_by_year(filename):
    with open(filename, "r+") as mixing:
        mixing_tsv = csv.DictReader(mixing, dialect='excel-tab')
        f = mixing_tsv.fieldnames

        sorted_mixing = sorted(mixing_tsv, key=operator.itemgetter('Year'), reverse=True)
        
        mixing.seek(0)
        writer = csv.DictWriter(mixing, delimiter='\t', dialect='excel-tab', fieldnames=f)
        writer.writeheader()
        for row in sorted_mixing:
            writer.writerow(row)
        mixing.truncate()

def build_readme(filename):
    # define dict of section holders
    sections = {"Level" : "", 
                "Panning" : "",
                "Equalization" : "",
                "Compression" : "",
                "Reverb" : "",
                "Integrated" : ""}

    with open(filename) as mixing:
        mixing = csv.DictReader(mixing, dialect='excel-tab')
        
        # get column labels
        f = mixing.fieldnames
        
        # initalize table for each section
        for section in sections:
            sections[section] = "## " + section + "\n|%s|%s|%s|%s|%s|\n" %(f[0], f[1], f[2], f[6], f[4]) + "|---|---|---|---|---|\n"

        for entry in mixing:
            # get attributes from table
            year      = entry['Year']
            title     = entry['Title']
            authors   = entry['Authors']
            paper     = entry['Paper']
            resources = entry['Resources']
            category  = entry['Category']
            approach  = entry['Approach']
            
            if resources == "No":
                sections[category] += "|%s|[%s](%s)|%s|%s|%s|\n" %(year, title, paper, authors, approach, resources)
            else:
                sections[category] += "|%s|[%s](%s)|%s|%s|[Yes](%s)|\n" %(year, title, paper, authors, approach, resources)

    with open("README.md", "w+") as readme_file, open('header.md') as header:
        readme_file.write(header.read())

        for section in sections:
            readme_file.write(sections[section])
        
    num_papers = mixing.line_num - 1
    return num_papers

def main(filename="mixingpapers.tsv"):
    sort_papers_by_year(filename)   
    print("Compiled " + str(build_readme(filename)) + " papers")

if __name__ == "__main__":
    main("mixingpapers.tsv")