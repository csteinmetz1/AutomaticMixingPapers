import csv
import operator

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
    # define section holders
    level = ""
    pan = ""
    eq = ""
    comp = ""
    verb = ""
    integ = ""

    with open(filename) as mixing:
        mixing = csv.DictReader(mixing, dialect='excel-tab')
        
        # get column labels
        f = mixing.fieldnames
        
        # initalize table for each section
        level = "## Level\n"        + "|%s|%s|%s|%s|\n" %(f[0], f[1], f[2], f[4]) + "|---|---|---|---|\n"
        pan   = "## Panning\n"      + "|%s|%s|%s|%s|\n" %(f[0], f[1], f[2], f[4]) + "|---|---|---|---|\n"
        eq    = "## Equalization\n" + "|%s|%s|%s|%s|\n" %(f[0], f[1], f[2], f[4]) + "|---|---|---|---|\n"
        comp  = "## Compression\n"  + "|%s|%s|%s|%s|\n" %(f[0], f[1], f[2], f[4]) + "|---|---|---|---|\n"
        verb  = "## Reverb\n"       + "|%s|%s|%s|%s|\n" %(f[0], f[1], f[2], f[4]) + "|---|---|---|---|\n"
        integ = "## Integrated\n"   + "|%s|%s|%s|%s|\n" %(f[0], f[1], f[2], f[4]) + "|---|---|---|---|\n"

        for entry in mixing:
            # get attributes from table
            year      = entry['Year']
            title     = entry['Title']
            authors   = entry['Authors']
            paper     = entry['Paper']
            resources = entry['Resources']
            category  = entry['Category']
            
            if category == "level":
                level += "|%s|[%s](%s)|%s|%s|\n" %(year, title, paper, authors, resources)
            elif category == "panning":
                pan   += "|%s|[%s](%s)|%s|%s|\n" %(year, title, paper, authors, resources)
            elif category == "equalization":
                eq    += "|%s|[%s](%s)|%s|%s|\n" %(year, title, paper, authors, resources)
            elif category == "compression":
                comp  += "|%s|[%s](%s)|%s|%s|\n" %(year, title, paper, authors, resources) 
            elif category == "reverb":
                verb  += "|%s|[%s](%s)|%s|%s|\n" %(year, title, paper, authors, resources)
            elif category == "integrated":
                integ += "|%s|[%s](%s)|%s|%s|\n" %(year, title, paper, authors, resources)

    with open("README.md", "w+") as readme_file, open('header.md') as header:
        readme_file.write(header.read())
        readme_file.write(level)     
        readme_file.write(pan) 
        readme_file.write(eq) 
        readme_file.write(comp) 
        readme_file.write(verb)
        readme_file.write(integ)  

    num_papers = mixing.line_num - 1
    return num_papers

def main(filename="mixingpapers.tsv"):
    #print("Compiled " + str(build_readme(filename)) + " papers")
    sort_papers_by_year(filename)

if __name__ == "__main__":
    main("mixingpapers.tsv")